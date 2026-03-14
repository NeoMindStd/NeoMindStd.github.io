#!/usr/bin/env python3
"""Normalize post front matter metadata for SEO consistency."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

FRONT_MATTER_RE = re.compile(r"\A---\r?\n(?P<front>.*?)\r?\n---\r?\n", re.DOTALL)
DESCRIPTION_LINE_RE = re.compile(r"(?m)^description\s*:\s*.*$")
EXCERPT_LINE_RE = re.compile(r"(?m)^(excerpt\s*:[^\n]*\n)")


@dataclass
class ProcessResult:
    path: Path
    updated: bool
    reason: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fill missing post descriptions from excerpts."
    )
    parser.add_argument(
        "--root",
        default="_posts",
        help="Root directory that contains post markdown files.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Apply changes to files. Without this flag, run in dry-run mode.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print file-level processing logs.",
    )
    return parser.parse_args()


def build_description_line(description: str) -> str:
    return f"description: {json.dumps(description, ensure_ascii=False)}"


def update_front_matter(front_matter: str, description: str) -> tuple[str, bool]:
    description_line = build_description_line(description)

    if DESCRIPTION_LINE_RE.search(front_matter):
        new_front = DESCRIPTION_LINE_RE.sub(description_line, front_matter, count=1)
        return new_front, new_front != front_matter

    excerpt_match = EXCERPT_LINE_RE.search(front_matter)
    if excerpt_match:
        insertion_point = excerpt_match.end()
        new_front = (
            front_matter[:insertion_point]
            + description_line
            + "\n"
            + front_matter[insertion_point:]
        )
        return new_front, True

    lines = front_matter.splitlines()
    if lines:
        lines.insert(1, description_line)
    else:
        lines = [description_line]
    return "\n".join(lines), True


def process_file(path: Path, *, write: bool) -> ProcessResult:
    original_text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(original_text)
    if not match:
        return ProcessResult(path=path, updated=False, reason="skip:no_front_matter")

    front_matter = match.group("front")
    body = original_text[match.end() :]

    try:
        meta = yaml.safe_load(front_matter) or {}
    except yaml.YAMLError:
        return ProcessResult(path=path, updated=False, reason="skip:yaml_parse_error")

    excerpt_value = meta.get("excerpt", "")
    description_value = meta.get("description", "")
    excerpt = "" if excerpt_value is None else str(excerpt_value).strip()
    description = "" if description_value is None else str(description_value).strip()

    if description:
        return ProcessResult(path=path, updated=False, reason="skip:already_has_description")
    if not excerpt:
        return ProcessResult(path=path, updated=False, reason="skip:missing_excerpt")

    normalized_front, changed = update_front_matter(front_matter, excerpt)
    if not changed:
        return ProcessResult(path=path, updated=False, reason="skip:no_change")

    newline = "\r\n" if "\r\n" in original_text else "\n"
    normalized_text = f"---{newline}{normalized_front}{newline}---{newline}{body}"

    if write:
        path.write_text(normalized_text, encoding="utf-8", newline="")

    return ProcessResult(path=path, updated=True, reason="updated")


def iter_post_files(root: Path) -> list[Path]:
    extensions = {".md", ".markdown", ".mkd", ".mkdn", ".mkdown"}
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in extensions
    )


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()

    if not root.exists():
        raise SystemExit(f"Root path not found: {root}")

    stats: dict[str, int] = {
        "total": 0,
        "applied": 0,
        "skip:already_has_description": 0,
        "skip:missing_excerpt": 0,
        "skip:no_front_matter": 0,
        "skip:yaml_parse_error": 0,
        "skip:no_change": 0,
        "updated": 0,
    }

    for file_path in iter_post_files(root):
        result = process_file(file_path, write=args.write)
        stats["total"] += 1
        stats[result.reason] = stats.get(result.reason, 0) + 1
        if result.updated:
            stats["applied"] += 1
        if args.verbose:
            print(f"{result.reason}: {result.path}")

    mode = "write" if args.write else "dry-run"
    print(f"mode={mode}")
    print(f"root={root}")
    print(f"total={stats['total']}")
    print(f"updated={stats['applied']}")
    print(f"skip:already_has_description={stats['skip:already_has_description']}")
    print(f"skip:missing_excerpt={stats['skip:missing_excerpt']}")
    print(f"skip:no_front_matter={stats['skip:no_front_matter']}")
    print(f"skip:yaml_parse_error={stats['skip:yaml_parse_error']}")
    print(f"skip:no_change={stats['skip:no_change']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
