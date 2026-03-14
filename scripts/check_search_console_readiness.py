#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
from pathlib import Path


SEARCH_SCOPES = {
    "https://www.googleapis.com/auth/webmasters",
    "https://www.googleapis.com/auth/webmasters.readonly",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check whether the current Google OAuth token is ready for Search Console.")
    parser.add_argument("--token", type=Path, default=Path(r"D:\WorkSpace\secrets\oauth-token.json"))
    parser.add_argument("--out", type=Path, required=True)
    return parser.parse_args()


def render(token_json: dict) -> str:
    scopes = token_json.get("scopes", [])
    missing = sorted(SEARCH_SCOPES.difference(scopes))
    has_ready_scope = not missing

    lines = []
    lines.append("# Search Console 준비 상태")
    lines.append("")
    lines.append("## 현재 상태")
    lines.append("")
    lines.append(f"- Search Console API 사용 가능: `{'yes' if has_ready_scope else 'no'}`")
    lines.append(f"- 현재 OAuth 스코프: `{', '.join(scopes) if scopes else 'none'}`")
    lines.append("")
    if has_ready_scope:
        lines.append("현재 토큰에는 Search Console 조회에 필요한 스코프가 포함되어 있습니다.")
    else:
        lines.append("현재 토큰에는 AdMob/AdSense 읽기 권한만 들어 있어, Search Console 검색어·랜딩페이지·평균순위 데이터를 직접 읽을 수 없습니다.")
        lines.append("")
        lines.append("## 추가로 필요한 스코프")
        lines.append("")
        for scope in missing:
            lines.append(f"- `{scope}`")
        lines.append("")
        lines.append("## 다음 단계")
        lines.append("")
        lines.append("1. Google Cloud OAuth 동의 설정에서 Search Console 스코프를 추가합니다.")
        lines.append("2. Search Console 접근 권한이 있는 계정으로 OAuth 토큰을 다시 발급합니다.")
        lines.append("3. 사이트 속성(`https://neomindstd.github.io/`)이 Search Console에 등록되어 있는지 확인합니다.")
        lines.append("4. 재발급 후에는 검색어, 랜딩페이지, 평균순위 데이터를 주간 리뷰에 합칩니다.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    token_json = json.loads(args.token.read_text(encoding="utf-8"))
    text = render(token_json)
    args.out.write_text(text + "\n", encoding="utf-8")
    print(f"Wrote readiness report: {args.out}")


if __name__ == "__main__":
    main()
