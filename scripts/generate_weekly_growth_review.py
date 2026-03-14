#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a weekly-friendly blog growth review from the unified snapshot.")
    parser.add_argument("--input", type=Path, required=True, help="Path to growth snapshot JSON")
    parser.add_argument("--out", type=Path, required=True, help="Markdown output path")
    return parser.parse_args()


def pct_delta(current: float, previous: float) -> str:
    if previous == 0:
        return "new"
    return f"{((current - previous) / previous) * 100:.1f}%"


def blog_property(snapshot: dict) -> dict:
    for prop in snapshot["ga4"]["properties"]:
        if prop["display_name"] == "neomindstd.github.io - GA4":
            return prop
    raise KeyError("blog GA4 property not found")


def blog_adsense(snapshot: dict) -> dict:
    for report in snapshot["adsense"].get("reports", []):
        last_rows = report.get("last_period", {}).get("rows", [])
        prev_rows = report.get("prev_period", {}).get("rows", [])
        last = next((row for row in last_rows if row.get("domain") == "neomindstd.github.io"), None)
        prev = next((row for row in prev_rows if row.get("domain") == "neomindstd.github.io"), None)
        if last and prev:
            return {"last_period": enrich_adsense_row(last), "prev_period": enrich_adsense_row(prev)}
    for account in snapshot["adsense"].get("accounts", []):
        for report in account.get("reports", []):
            if report.get("domain") == "neomindstd.github.io":
                return {
                    "last_period": enrich_adsense_row(report["last_period"]),
                    "prev_period": enrich_adsense_row(report["prev_period"]),
                }
    raise KeyError("blog AdSense domain report not found")


def enrich_adsense_row(row: dict) -> dict:
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


def extract_top_pages(prop: dict, limit: int = 8) -> list[dict]:
    rows = []
    for row in prop.get("top_content", {}).get("rows", []):
        dimension = row.get("dimension", "")
        if not dimension:
            continue
        rows.append({"path": dimension, "views": row.get("views", 0)})
    return rows[:limit]


def extract_ai_tools_pages(rows: list[dict]) -> list[dict]:
    interesting = []
    for row in rows:
        path = row["path"]
        if path.startswith("/기타/") or path.startswith("/tools/") or path.startswith("/ai/"):
            interesting.append(row)
    return interesting


def render(snapshot: dict) -> str:
    config = snapshot["config"]
    prop = blog_property(snapshot)
    adsense = blog_adsense(snapshot)

    ga_last = prop["last_period"]["values"]
    ga_prev = prop["prev_period"]["values"]
    ads_last = adsense["last_period"]
    ads_prev = adsense["prev_period"]
    top_pages = extract_top_pages(prop)
    ai_pages = extract_ai_tools_pages(top_pages)

    lines = []
    lines.append("# 블로그 주간 성장 리뷰")
    lines.append("")
    lines.append(f"- 기준 구간: `{config['windows']['last']['start']}` ~ `{config['windows']['last']['end']}`")
    lines.append(f"- 비교 구간: `{config['windows']['prev']['start']}` ~ `{config['windows']['prev']['end']}`")
    lines.append("")
    lines.append("## 이번 구간 핵심")
    lines.append("")
    lines.append(f"- 활성 사용자: `{int(ga_last['activeUsers'])}`명 (`{pct_delta(ga_last['activeUsers'], ga_prev['activeUsers'])}`)")
    lines.append(f"- 세션: `{int(ga_last['sessions'])}` (`{pct_delta(ga_last['sessions'], ga_prev['sessions'])}`)")
    lines.append(f"- 페이지뷰: `{int(ga_last['screenPageViews'])}` (`{pct_delta(ga_last['screenPageViews'], ga_prev['screenPageViews'])}`)")
    lines.append(f"- AdSense 수익: `${ads_last['earnings_usd']:.2f}` (`{pct_delta(ads_last['earnings_usd'], ads_prev['earnings_usd'])}`)")
    lines.append(f"- AdSense CTR: `{ads_last['ctr']:.2f}%` (이전 `{ads_prev['ctr']:.2f}%`)")
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
    lines.append("")
    lines.append("## 상위 랜딩 페이지")
    lines.append("")
    for row in top_pages:
        lines.append(f"- `{row['path']}` : `{int(row['views'])}`뷰")
    lines.append("")
    lines.append("## AI/Tools 유입 체크")
    lines.append("")
    if ai_pages:
        for row in ai_pages:
            lines.append(f"- `{row['path']}` : `{int(row['views'])}`뷰")
    else:
        lines.append("- 이번 스냅샷 상위 랜딩에는 AI/Tools 페이지가 두드러지지 않았습니다.")
    lines.append("- `ai_referral_visit` 이벤트는 이미 사이트 코드에 들어가 있으므로, 다음 주부터는 GA4 커스텀 차원 등록 여부를 함께 체크합니다.")
    lines.append("")
    lines.append("## 광고/수익 체크")
    lines.append("")
    lines.append(f"- CTR은 `{ads_last['ctr']:.2f}%`로 유지 중이지만, Page RPM이 `{ads_last['page_rpm']:.3f}` 수준이라 절대 유입량을 먼저 키우는 편이 낫습니다.")
    lines.append(f"- 광고 기준 페이지뷰는 `{int(ads_last['page_views'])}`로 아직 작아서, 광고 배치보다 상위 랜딩 확대와 다음 클릭 개선이 우선입니다.")
    lines.append("")
    lines.append("## 다음 액션")
    lines.append("")
    lines.append("1. 이번에 보강한 AI/Tools 상위 글 20개의 랜딩 변화를 다음 주 스냅샷에서 우선 확인합니다.")
    lines.append("2. Search Console 권한을 추가한 뒤 검색어·평균순위 데이터를 리포트에 합칩니다.")
    lines.append("3. 상위 랜딩 중 AI/Tools 글에 들어온 사용자가 다른 글로 얼마나 이동하는지 내부 링크 클릭 흐름을 함께 점검합니다.")
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
