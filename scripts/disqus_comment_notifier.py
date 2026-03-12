#!/usr/bin/env python3
"""Detect new Disqus comments and prepare email payloads for GitHub Actions."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from html import escape, unescape
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

DISQUS_LIST_POSTS_URL = "https://disqus.com/api/3.0/forums/listPosts.json"
DEFAULT_STATE_MAX_IDS = 500
TAG_RE = re.compile(r"<[^>]+>")
WHITESPACE_RE = re.compile(r"\s+")


@dataclass(frozen=True)
class CommentItem:
    comment_id: str
    created_at: str
    author_name: str
    message: str
    thread_title: str
    thread_link: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Poll Disqus comments and produce email notification payload."
    )
    parser.add_argument("--forum", default=os.getenv("DISQUS_FORUM", ""))
    parser.add_argument("--api-key", default=os.getenv("DISQUS_API_KEY", ""))
    parser.add_argument(
        "--site-url", default=os.getenv("BLOG_SITE_URL", "https://neomindstd.github.io")
    )
    parser.add_argument(
        "--state-path", default=".cache/disqus-comment-alert/state.json"
    )
    parser.add_argument(
        "--text-output", default=".cache/disqus-comment-alert/email.txt"
    )
    parser.add_argument(
        "--html-output", default=".cache/disqus-comment-alert/email.html"
    )
    parser.add_argument("--max-pages", type=int, default=5)
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--timeout-seconds", type=int, default=20)
    parser.add_argument("--state-max-ids", type=int, default=DEFAULT_STATE_MAX_IDS)
    parser.add_argument("--email-item-limit", type=int, default=20)
    parser.add_argument(
        "--bootstrap-if-empty",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="If true, first run stores baseline state and skips sending alert.",
    )
    parser.add_argument("--github-output", default=os.getenv("GITHUB_OUTPUT", ""))
    return parser.parse_args()


def strip_html_tags(value: str) -> str:
    without_tags = TAG_RE.sub("", value or "")
    without_entities = unescape(without_tags)
    return WHITESPACE_RE.sub(" ", without_entities).strip()


def to_epoch_seconds(iso_time: str) -> float:
    if not iso_time:
        return 0.0
    try:
        return datetime.fromisoformat(iso_time.replace("Z", "+00:00")).timestamp()
    except ValueError:
        return 0.0


def fallback_thread_link(thread: dict[str, Any], site_url: str) -> str:
    normalized_site = site_url.rstrip("/")
    link = thread.get("link")
    if isinstance(link, str) and link.strip():
        return link.strip()

    identifiers = thread.get("identifiers")
    if isinstance(identifiers, list):
        for ident in identifiers:
            if not isinstance(ident, str):
                continue
            cleaned = ident.strip()
            if not cleaned:
                continue
            if cleaned.startswith("http://") or cleaned.startswith("https://"):
                return cleaned
            return f"{normalized_site}/{cleaned.lstrip('/')}"

    slug = thread.get("slug")
    if isinstance(slug, str) and slug.strip():
        return f"{normalized_site}/{slug.strip().lstrip('/')}/"

    return normalized_site


def normalize_comment(raw: dict[str, Any], site_url: str) -> CommentItem | None:
    comment_id = str(raw.get("id", "")).strip()
    if not comment_id:
        return None

    author = raw.get("author") if isinstance(raw.get("author"), dict) else {}
    author_name = str(
        author.get("name")
        or author.get("username")
        or raw.get("authorName")
        or "Anonymous"
    ).strip()

    message = str(raw.get("message") or raw.get("raw_message") or "").strip()
    message_text = strip_html_tags(message)

    thread = raw.get("thread") if isinstance(raw.get("thread"), dict) else {}
    thread_title = str(thread.get("title") or "Untitled thread").strip()
    thread_link = fallback_thread_link(thread, site_url)

    return CommentItem(
        comment_id=comment_id,
        created_at=str(raw.get("createdAt") or ""),
        author_name=author_name or "Anonymous",
        message=message_text,
        thread_title=thread_title or "Untitled thread",
        thread_link=thread_link,
    )


def fetch_disqus_posts(
    *,
    forum: str,
    api_key: str,
    limit: int,
    max_pages: int,
    timeout_seconds: int,
) -> list[dict[str, Any]]:
    if limit < 1 or limit > 100:
        raise ValueError("--limit must be between 1 and 100")
    if max_pages < 1:
        raise ValueError("--max-pages must be >= 1")

    all_posts: list[dict[str, Any]] = []
    cursor: str | None = None

    for _ in range(max_pages):
        params = {
            "api_key": api_key,
            "forum": forum,
            "limit": str(limit),
            "include": "approved",
            "related": "thread",
            "order": "desc",
        }
        if cursor:
            params["cursor"] = cursor

        request_url = f"{DISQUS_LIST_POSTS_URL}?{urlencode(params)}"
        request = Request(
            request_url,
            headers={"User-Agent": "NeoMindStd-Disqus-Comment-Notifier/1.0"},
        )

        try:
            with urlopen(request, timeout=timeout_seconds) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            raise RuntimeError(
                f"Disqus API request failed with status {exc.code}: {exc.reason}"
            ) from exc
        except URLError as exc:
            raise RuntimeError(f"Disqus API request failed: {exc.reason}") from exc

        if payload.get("code") != 0:
            raise RuntimeError(
                f"Disqus API error code {payload.get('code')}: {payload.get('response')}"
            )

        posts = payload.get("response")
        if isinstance(posts, list):
            all_posts.extend(post for post in posts if isinstance(post, dict))

        cursor_info = payload.get("cursor") if isinstance(payload.get("cursor"), dict) else {}
        has_next = bool(cursor_info.get("hasNext"))
        next_cursor = cursor_info.get("next")
        if not has_next or not isinstance(next_cursor, str) or not next_cursor:
            break
        cursor = next_cursor

    return all_posts


def unique_preserve_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def select_new_comments(
    comments: list[CommentItem], known_comment_ids: set[str]
) -> list[CommentItem]:
    only_new = [item for item in comments if item.comment_id not in known_comment_ids]
    return sorted(only_new, key=lambda item: to_epoch_seconds(item.created_at))


def build_next_known_ids(
    latest_comments: list[CommentItem], known_comment_ids: list[str], max_ids: int
) -> list[str]:
    latest_ids = [item.comment_id for item in latest_comments]
    merged = unique_preserve_order(latest_ids + known_comment_ids)
    if max_ids <= 0:
        return merged
    return merged[:max_ids]


def truncate_text(value: str, limit: int = 280) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."


def render_text_email(forum: str, comments: list[CommentItem], generated_at_utc: str) -> str:
    lines: list[str] = [
        f"New Disqus comments detected: {len(comments)}",
        f"Forum: {forum}",
        f"Generated at (UTC): {generated_at_utc}",
        "",
    ]
    for index, item in enumerate(comments, start=1):
        lines.extend(
            [
                f"{index}. {item.thread_title}",
                f"   Link: {item.thread_link}",
                f"   Author: {item.author_name}",
                f"   Created at: {item.created_at or 'unknown'}",
                f"   Comment: {truncate_text(item.message or '(empty)')}",
                "",
            ]
        )

    lines.append(f"Moderation: https://{forum}.disqus.com/admin/moderate/")
    return "\n".join(lines).strip() + "\n"


def render_html_email(forum: str, comments: list[CommentItem], generated_at_utc: str) -> str:
    rows: list[str] = []
    for index, item in enumerate(comments, start=1):
        rows.append(
            (
                "<li>"
                f"<p><strong>{index}. {escape(item.thread_title)}</strong></p>"
                f"<p>Link: <a href=\"{escape(item.thread_link)}\">{escape(item.thread_link)}</a></p>"
                f"<p>Author: {escape(item.author_name)}</p>"
                f"<p>Created at: {escape(item.created_at or 'unknown')}</p>"
                f"<p>Comment: {escape(truncate_text(item.message or '(empty)'))}</p>"
                "</li>"
            )
        )

    rows_html = "\n".join(rows)
    moderation_link = f"https://{forum}.disqus.com/admin/moderate/"
    return (
        "<!doctype html>"
        "<html><body>"
        f"<p><strong>New Disqus comments detected: {len(comments)}</strong></p>"
        f"<p>Forum: {escape(forum)}<br/>Generated at (UTC): {escape(generated_at_utc)}</p>"
        f"<ol>{rows_html}</ol>"
        f"<p>Moderation: <a href=\"{escape(moderation_link)}\">{escape(moderation_link)}</a></p>"
        "</body></html>"
    )


def read_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"known_comment_ids": []}
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"known_comment_ids": []}

    known = parsed.get("known_comment_ids")
    if not isinstance(known, list):
        known = []
    return {"known_comment_ids": [str(item) for item in known if str(item).strip()]}


def write_state(path: Path, known_comment_ids: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "known_comment_ids": known_comment_ids,
        "updated_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")


def append_github_outputs(output_path: str, values: dict[str, str]) -> None:
    if not output_path:
        return
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        for key, value in values.items():
            one_line = str(value).replace("\r", " ").replace("\n", " ").strip()
            file.write(f"{key}={one_line}\n")


def write_email_files(text_path: Path, html_path: Path, text_body: str, html_body: str) -> None:
    text_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.parent.mkdir(parents=True, exist_ok=True)
    text_path.write_text(text_body, encoding="utf-8")
    html_path.write_text(html_body, encoding="utf-8")


def main() -> int:
    args = parse_args()
    if not args.forum:
        print("DISQUS forum is required via --forum or DISQUS_FORUM.", file=sys.stderr)
        return 2
    if not args.api_key:
        print("DISQUS API key is required via --api-key or DISQUS_API_KEY.", file=sys.stderr)
        return 2

    state_path = Path(args.state_path)
    state = read_state(state_path)
    known_comment_ids = state.get("known_comment_ids", [])
    known_comment_id_set = set(known_comment_ids)

    raw_posts = fetch_disqus_posts(
        forum=args.forum,
        api_key=args.api_key,
        limit=args.limit,
        max_pages=args.max_pages,
        timeout_seconds=args.timeout_seconds,
    )

    normalized: list[CommentItem] = []
    for raw_post in raw_posts:
        normalized_comment = normalize_comment(raw_post, args.site_url)
        if normalized_comment is not None:
            normalized.append(normalized_comment)

    new_comments = select_new_comments(normalized, known_comment_id_set)
    next_known_ids = build_next_known_ids(
        latest_comments=normalized,
        known_comment_ids=known_comment_ids,
        max_ids=args.state_max_ids,
    )

    bootstrap_run = len(known_comment_ids) == 0 and args.bootstrap_if_empty
    if bootstrap_run:
        write_state(state_path, next_known_ids)
        append_github_outputs(
            args.github_output,
            {
                "has_new_comments": "false",
                "new_comments_count": "0",
                "email_subject": "",
                "email_text_path": "",
                "email_html_path": "",
                "bootstrap_run": "true",
            },
        )
        print(
            f"Bootstrap complete. Stored {len(next_known_ids)} known comment ids without sending email."
        )
        return 0

    write_state(state_path, next_known_ids)
    generated_at_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    has_new = len(new_comments) > 0
    text_path = Path(args.text_output)
    html_path = Path(args.html_output)
    email_subject = ""

    if has_new:
        email_comments = new_comments[: args.email_item_limit]
        email_subject = f"[{args.forum}] New comments: {len(new_comments)}"
        text_body = render_text_email(args.forum, email_comments, generated_at_utc)
        html_body = render_html_email(args.forum, email_comments, generated_at_utc)
        write_email_files(text_path, html_path, text_body, html_body)

    append_github_outputs(
        args.github_output,
        {
            "has_new_comments": str(has_new).lower(),
            "new_comments_count": str(len(new_comments)),
            "email_subject": email_subject,
            "email_text_path": str(text_path),
            "email_html_path": str(html_path),
            "bootstrap_run": "false",
        },
    )

    print(
        f"Fetched={len(normalized)} Known(before)={len(known_comment_ids)} New={len(new_comments)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
