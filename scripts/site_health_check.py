#!/usr/bin/env python3
"""Simple health checks for the published blog site."""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


@dataclass
class CheckResult:
    name: str
    url: str
    ok: bool
    status_code: int | None
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run published site health checks.")
    parser.add_argument(
        "--base-url",
        default="https://neomindstd.github.io",
        help="Base URL of the site.",
    )
    parser.add_argument(
        "--report-path",
        default=".cache/site-health-report.json",
        help="Path to write JSON report.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=20,
        help="Request timeout in seconds.",
    )
    return parser.parse_args()


def fetch_url(url: str, timeout_seconds: int) -> tuple[int, str]:
    req = Request(url, headers={"User-Agent": "NeoMindStd-Site-Health-Check/1.0"})
    with urlopen(req, timeout=timeout_seconds) as response:
        status_code = response.getcode()
        content = response.read().decode("utf-8", errors="replace")
    return status_code, content


def check_plain_page(name: str, url: str, timeout_seconds: int) -> CheckResult:
    try:
        status_code, _ = fetch_url(url, timeout_seconds)
        ok = status_code == 200
        return CheckResult(
            name=name,
            url=url,
            ok=ok,
            status_code=status_code,
            detail="ok" if ok else f"unexpected_status:{status_code}",
        )
    except HTTPError as exc:
        return CheckResult(
            name=name,
            url=url,
            ok=False,
            status_code=exc.code,
            detail=f"http_error:{exc.code}",
        )
    except URLError as exc:
        return CheckResult(
            name=name,
            url=url,
            ok=False,
            status_code=None,
            detail=f"url_error:{exc.reason}",
        )


def check_sitemap(url: str, base_url: str, timeout_seconds: int) -> CheckResult:
    try:
        status_code, content = fetch_url(url, timeout_seconds)
        has_urlset = "<urlset" in content
        has_base = base_url.rstrip("/") in content
        ok = status_code == 200 and has_urlset and has_base
        detail_parts = []
        if status_code != 200:
            detail_parts.append(f"unexpected_status:{status_code}")
        if not has_urlset:
            detail_parts.append("missing:urlset")
        if not has_base:
            detail_parts.append("missing:base_url")
        return CheckResult(
            name="sitemap.xml",
            url=url,
            ok=ok,
            status_code=status_code,
            detail="ok" if ok else ",".join(detail_parts),
        )
    except HTTPError as exc:
        return CheckResult("sitemap.xml", url, False, exc.code, f"http_error:{exc.code}")
    except URLError as exc:
        return CheckResult("sitemap.xml", url, False, None, f"url_error:{exc.reason}")


def check_robots(url: str, timeout_seconds: int) -> CheckResult:
    try:
        status_code, content = fetch_url(url, timeout_seconds)
        has_allow = "Allow: /" in content
        has_sitemap = "Sitemap:" in content
        ok = status_code == 200 and has_allow and has_sitemap
        detail_parts = []
        if status_code != 200:
            detail_parts.append(f"unexpected_status:{status_code}")
        if not has_allow:
            detail_parts.append("missing:allow")
        if not has_sitemap:
            detail_parts.append("missing:sitemap")
        return CheckResult(
            name="robots.txt",
            url=url,
            ok=ok,
            status_code=status_code,
            detail="ok" if ok else ",".join(detail_parts),
        )
    except HTTPError as exc:
        return CheckResult("robots.txt", url, False, exc.code, f"http_error:{exc.code}")
    except URLError as exc:
        return CheckResult("robots.txt", url, False, None, f"url_error:{exc.reason}")


def write_summary(results: list[CheckResult]) -> None:
    summary_path = Path(".cache/site-health-summary.md")
    summary_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "## Site Health Report",
        "",
        "| Check | Status | Detail |",
        "|---|---|---|",
    ]
    for result in results:
        status = "PASS" if result.ok else "FAIL"
        lines.append(f"| `{result.name}` | {status} | {result.detail} |")
    summary_text = "\n".join(lines) + "\n"
    summary_path.write_text(summary_text, encoding="utf-8")

    step_summary_path = os.getenv("GITHUB_STEP_SUMMARY", "").strip()
    if step_summary_path:
        step_summary = Path(step_summary_path)
        step_summary.parent.mkdir(parents=True, exist_ok=True)
        with step_summary.open("a", encoding="utf-8") as handle:
            handle.write(summary_text)


def main() -> int:
    args = parse_args()
    base_url = args.base_url.rstrip("/")

    page_checks = [
        ("home", "/"),
        ("boj_hub", "/boj/"),
        ("programmers_hub", "/programmers/"),
        ("projects_hub", "/projects/"),
        ("etc_hub", "/etc/"),
        ("sample_boj_post", "/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj20254/"),
        ("sample_ops_post", "/%EA%B8%B0%ED%83%80/google-play-app-ads-txt-checklist/"),
    ]

    results: list[CheckResult] = []
    for name, path in page_checks:
        results.append(check_plain_page(name, f"{base_url}{path}", args.timeout_seconds))

    results.append(check_sitemap(f"{base_url}/sitemap.xml", base_url, args.timeout_seconds))
    results.append(check_robots(f"{base_url}/robots.txt", args.timeout_seconds))

    report = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "base_url": base_url,
        "results": [asdict(result) for result in results],
    }

    report_path = Path(args.report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    write_summary(results)

    failed = [result for result in results if not result.ok]
    if failed:
        print("Site health check failed:")
        for fail in failed:
            print(f"- {fail.name}: {fail.detail} ({fail.url})")
        return 1

    print("Site health check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
