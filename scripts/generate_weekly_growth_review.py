#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import urllib.parse
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a weekly-friendly blog growth review from the unified snapshot.")
    parser.add_argument("--input", type=Path, required=True, help="Path to growth snapshot JSON")
    parser.add_argument("--out", type=Path, required=True, help="Markdown output path")
    return parser.parse_args()


def pct_delta(current: float, previous: float) -> str:
    if previous == 0:
        return "new"
    return f"{((current - previous) / previous) * 100:.1f}%"


def blog_property(snapshot: dict[str, Any]) -> dict[str, Any]:
    for prop in snapshot.get("ga4", {}).get("properties", []):
        if prop.get("display_name") == "neomindstd.github.io - GA4":
            return prop
    raise KeyError("blog GA4 property not found")


def blog_adsense(snapshot: dict[str, Any]) -> dict[str, Any]:
    for report in snapshot.get("adsense", {}).get("reports", []):
        last_rows = report.get("last_period", {}).get("rows", [])
        prev_rows = report.get("prev_period", {}).get("rows", [])
        last = next((row for row in last_rows if row.get("domain") == "neomindstd.github.io"), None)
        prev = next((row for row in prev_rows if row.get("domain") == "neomindstd.github.io"), None)
        if last and prev:
            return {"last_period": enrich_adsense_row(last), "prev_period": enrich_adsense_row(prev)}
    raise KeyError("blog AdSense domain report not found")


def enrich_adsense_row(row: dict[str, Any]) -> dict[str, Any]:
    page_views = float(row.get("page_views", 0) or 0)
    earnings = float(row.get("earnings_usd", 0) or 0)
    impressions = float(row.get("impressions", 0) or 0)
    clicks = float(row.get("clicks", 0) or 0)
    ctr = (clicks / impressions * 100) if impressions else 0.0
    page_rpm = (earnings / page_views * 1000) if page_views else 0.0
    enriched = dict(row)
    enriched["ctr"] = ctr
    enriched["page_rpm"] = page_rpm
    return enriched


def normalize_path(raw_path: str) -> str:
    if raw_path.startswith("http://") or raw_path.startswith("https://"):
        parsed = urllib.parse.urlparse(raw_path)
        raw_path = parsed.path or raw_path
    return urllib.parse.unquote(raw_path)


def extract_top_pages(prop: dict[str, Any], limit: int = 8) -> list[dict[str, Any]]:
    rows = []
    for row in prop.get("top_content", {}).get("rows", []):
        dimension = row.get("dimension", "")
        if not dimension:
            continue
        rows.append({"path": normalize_path(dimension), "views": row.get("views", 0)})
    return rows[:limit]


def extract_ai_tools_pages(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    interesting = []
    for row in rows:
        path = row["path"]
        if path.startswith("/기타/") or path.startswith("/tools/") or path.startswith("/ai/"):
            interesting.append(row)
    return interesting


def extract_search_console_section(snapshot: dict[str, Any]) -> dict[str, Any] | None:
    report = snapshot.get("search_console", {}).get("report")
    if not report:
        return None
    last_totals = report.get("last_period", {}).get("totals", {}).get("totals", {})
    prev_totals = report.get("prev_period", {}).get("totals", {}).get("totals", {})
    top_queries = report.get("last_period", {}).get("top_queries", {}).get("rows", [])
    top_pages = report.get("last_period", {}).get("top_pages", {}).get("rows", [])
    return {
        "last_totals": last_totals,
        "prev_totals": prev_totals,
        "top_queries": top_queries,
        "top_pages": top_pages,
    }


def render(snapshot: dict[str, Any]) -> str:
    config = snapshot["config"]
    prop = blog_property(snapshot)
    adsense = blog_adsense(snapshot)
    search_console = extract_search_console_section(snapshot)

    ga_last = prop["last_period"]["values"]
    ga_prev = prop["prev_period"]["values"]
    ads_last = adsense["last_period"]
    ads_prev = adsense["prev_period"]
    top_pages = extract_top_pages(prop)
    ai_pages = extract_ai_tools_pages(top_pages)

    lines: list[str] = []
    lines.append("# 블로그 주간 성장 리뷰")
    lines.append("")
    lines.append(f"- 기준 구간: `{config['windows']['last']['start']}` ~ `{config['windows']['last']['end']}`")
    lines.append(f"- 비교 구간: `{config['windows']['prev']['start']}` ~ `{config['windows']['prev']['end']}`")
    lines.append("")
    lines.append("## 이번 구간 요약")
    lines.append("")
    lines.append(f"- 활성 사용자: `{int(ga_last['activeUsers'])}`명 (`{pct_delta(ga_last['activeUsers'], ga_prev['activeUsers'])}`)")
    lines.append(f"- 세션: `{int(ga_last['sessions'])}` (`{pct_delta(ga_last['sessions'], ga_prev['sessions'])}`)")
    lines.append(f"- 페이지뷰: `{int(ga_last['screenPageViews'])}` (`{pct_delta(ga_last['screenPageViews'], ga_prev['screenPageViews'])}`)")
    lines.append(f"- AdSense 수익: `${ads_last['earnings_usd']:.2f}` (`{pct_delta(ads_last['earnings_usd'], ads_prev['earnings_usd'])}`)")
    lines.append(f"- AdSense CTR: `{ads_last['ctr']:.2f}%` (이전 `{ads_prev['ctr']:.2f}%`)")
    if search_console:
        last_totals = search_console["last_totals"]
        prev_totals = search_console["prev_totals"]
        lines.append(f"- Search Console 클릭: `{int(last_totals.get('clicks', 0))}` (`{pct_delta(float(last_totals.get('clicks', 0)), float(prev_totals.get('clicks', 0)))}`)")
        lines.append(
            f"- Search Console 노출: `{int(last_totals.get('impressions', 0))}` (`{pct_delta(float(last_totals.get('impressions', 0)), float(prev_totals.get('impressions', 0)))}`)"
        )
    lines.append("")
    lines.append("## 블로그 KPI")
    lines.append("")
    lines.append("| 항목 | 최근 | 이전 | 변화 |")
    lines.append("|:--|--:|--:|:--|")
    lines.append(f"| 활성 사용자 | {int(ga_last['activeUsers'])} | {int(ga_prev['activeUsers'])} | {pct_delta(ga_last['activeUsers'], ga_prev['activeUsers'])} |")
    lines.append(f"| 세션 | {int(ga_last['sessions'])} | {int(ga_prev['sessions'])} | {pct_delta(ga_last['sessions'], ga_prev['sessions'])} |")
    lines.append(f"| 페이지뷰 | {int(ga_last['screenPageViews'])} | {int(ga_prev['screenPageViews'])} | {pct_delta(ga_last['screenPageViews'], ga_prev['screenPageViews'])} |")
    lines.append(f"| 참여 세션 | {int(ga_last['engagedSessions'])} | {int(ga_prev['engagedSessions'])} | {pct_delta(ga_last['engagedSessions'], ga_prev['engagedSessions'])} |")
    lines.append(f"| 참여율 | {ga_last['engagementRate']:.3f} | {ga_prev['engagementRate']:.3f} | {pct_delta(ga_last['engagementRate'], ga_prev['engagementRate'])} |")
    lines.append(f"| AdSense 수익(USD) | {ads_last['earnings_usd']:.2f} | {ads_prev['earnings_usd']:.2f} | {pct_delta(ads_last['earnings_usd'], ads_prev['earnings_usd'])} |")
    lines.append(f"| AdSense 페이지뷰 | {int(ads_last['page_views'])} | {int(ads_prev['page_views'])} | {pct_delta(ads_last['page_views'], ads_prev['page_views'])} |")
    lines.append(f"| AdSense 노출 | {int(ads_last['impressions'])} | {int(ads_prev['impressions'])} | {pct_delta(ads_last['impressions'], ads_prev['impressions'])} |")
    lines.append(f"| AdSense 클릭 | {int(ads_last['clicks'])} | {int(ads_prev['clicks'])} | {pct_delta(ads_last['clicks'], ads_prev['clicks'])} |")
    lines.append(f"| Page RPM | {ads_last['page_rpm']:.3f} | {ads_prev['page_rpm']:.3f} | {pct_delta(ads_last['page_rpm'], ads_prev['page_rpm'])} |")
    if search_console:
        last_totals = search_console["last_totals"]
        prev_totals = search_console["prev_totals"]
        lines.append(f"| Search Console 클릭 | {int(last_totals.get('clicks', 0))} | {int(prev_totals.get('clicks', 0))} | {pct_delta(float(last_totals.get('clicks', 0)), float(prev_totals.get('clicks', 0)))} |")
        lines.append(f"| Search Console 노출 | {int(last_totals.get('impressions', 0))} | {int(prev_totals.get('impressions', 0))} | {pct_delta(float(last_totals.get('impressions', 0)), float(prev_totals.get('impressions', 0)))} |")
        lines.append(f"| Search Console CTR | {float(last_totals.get('ctr', 0)):.2%} | {float(prev_totals.get('ctr', 0)):.2%} | {pct_delta(float(last_totals.get('ctr', 0)), float(prev_totals.get('ctr', 0)))} |")
        lines.append(f"| 평균 순위 | {float(last_totals.get('position', 0)):.2f} | {float(prev_totals.get('position', 0)):.2f} | {pct_delta(float(prev_totals.get('position', 0)), float(last_totals.get('position', 0)))} |")
    lines.append("")
    lines.append("## 상위 랜딩 페이지")
    lines.append("")
    for row in top_pages:
        lines.append(f"- `{row['path']}` : `{int(row['views'])}`뷰")
    lines.append("")
    if search_console:
        lines.append("## Search Console 기회")
        lines.append("")
        query_rows = search_console["top_queries"][:5]
        page_rows = search_console["top_pages"][:5]
        if not query_rows and not page_rows and float(search_console["last_totals"].get("impressions", 0)) == 0:
            lines.append("- 속성 연결은 끝났지만 아직 Search Console 행 데이터가 비어 있습니다. 새로 만든 URL-prefix 속성이라면 하루 정도 뒤 다시 확인하는 편이 좋습니다.")
            lines.append("")
        if query_rows:
            lines.append("### 상위 검색어")
            for row in query_rows:
                key = (row.get("keys") or ["(query 없음)"])[0]
                lines.append(
                    f"- `{key}` : 클릭 `{int(row.get('clicks', 0))}`, 노출 `{int(row.get('impressions', 0))}`, CTR `{float(row.get('ctr', 0)):.2%}`, 평균 순위 `{float(row.get('position', 0)):.1f}`"
                )
        if page_rows:
            lines.append("")
            lines.append("### 상위 검색 랜딩 페이지")
            for row in page_rows:
                key = normalize_path((row.get("keys") or ["(page 없음)"])[0])
                lines.append(
                    f"- `{key}` : 클릭 `{int(row.get('clicks', 0))}`, 노출 `{int(row.get('impressions', 0))}`, CTR `{float(row.get('ctr', 0)):.2%}`, 평균 순위 `{float(row.get('position', 0)):.1f}`"
                )
        lines.append("")
    lines.append("## AI/Tools 유입 체크")
    lines.append("")
    if ai_pages:
        for row in ai_pages:
            lines.append(f"- `{row['path']}` : `{int(row['views'])}`뷰")
    else:
        lines.append("- 이번 주 상위 랜딩에는 AI/Tools 페이지가 아직 크게 올라오지 않았습니다.")
    lines.append("- `ai_referral_visit` 이벤트는 이미 사이트 코드에 들어가 있으므로, 다음 주에는 GA4 커스텀 차원 등록 여부를 함께 확인합니다.")
    lines.append("")
    lines.append("## 광고/수익 체크")
    lines.append("")
    lines.append(f"- CTR은 `{ads_last['ctr']:.2f}%`로 버티고 있지만, Page RPM은 `{ads_last['page_rpm']:.3f}` 수준이라 현재는 광고 배치보다 유입 확대가 더 중요합니다.")
    lines.append(f"- 광고 기준 페이지뷰는 `{int(ads_last['page_views'])}`로 아직 작아서, 상위 랜딩 페이지의 다음 클릭과 검색 노출 확대를 먼저 보는 편이 낫습니다.")
    lines.append("")
    lines.append("## 다음 액션")
    lines.append("")
    lines.append("1. 이번에 보강한 AI/Tools 상위 글 20개의 Search Console 노출·CTR 변화를 다음 주 리뷰에서 우선 확인합니다.")
    lines.append("2. Search Console 상위 검색어 중 노출 대비 CTR이 낮은 글은 제목·설명·첫 문단 훅을 우선 다듬습니다.")
    lines.append("3. Search Console 상위 랜딩 페이지에 허브 링크와 비교 글 연결을 더 촘촘하게 넣어 다음 클릭을 올립니다.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    snapshot = json.loads(args.input.read_text(encoding="utf-8"))
    output = render(snapshot)
    args.out.write_text(output + "\n", encoding="utf-8")
    print(f"Wrote review: {args.out}")


if __name__ == "__main__":
    main()
