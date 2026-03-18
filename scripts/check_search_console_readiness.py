#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import os
import urllib.parse
from pathlib import Path

import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


SEARCH_SCOPES = [
    "https://www.googleapis.com/auth/webmasters.readonly",
    "https://www.googleapis.com/auth/webmasters",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check whether the current Google OAuth token is ready for Search Console.")
    parser.add_argument(
        "--token",
        type=Path,
        default=None,
        help="Path to an OAuth authorized-user JSON. Falls back to SEARCH_CONSOLE_TOKEN_JSON or GOOGLE_OAUTH_TOKEN_JSON.",
    )
    parser.add_argument("--site-url", default="https://neomindstd.github.io/")
    parser.add_argument("--out", type=Path, required=True)
    return parser.parse_args()


def resolve_token_path(cli_value: Path | None) -> Path:
    if cli_value is not None:
        return cli_value

    env_value = os.environ.get("SEARCH_CONSOLE_TOKEN_JSON") or os.environ.get("GOOGLE_OAUTH_TOKEN_JSON")
    if env_value:
        return Path(env_value)

    raise SystemExit(
        "Missing OAuth token path. Pass --token or set SEARCH_CONSOLE_TOKEN_JSON / GOOGLE_OAUTH_TOKEN_JSON."
    )


def detect_scope(scopes: list[str]) -> str | None:
    for scope in SEARCH_SCOPES:
        if scope in scopes:
            return scope
    return None


def check_site_access(token_path: Path, site_url: str) -> tuple[bool, str]:
    creds = Credentials.from_authorized_user_file(str(token_path))
    creds.refresh(Request())
    quoted = urllib.parse.quote(site_url, safe="")
    url = f"https://www.googleapis.com/webmasters/v3/sites/{quoted}"
    response = requests.get(
        url,
        headers={"Authorization": f"Bearer {creds.token}", "Accept": "application/json"},
        timeout=120,
    )
    if response.ok:
        return True, "verified"
    try:
        payload = response.json()
        message = payload.get("error", {}).get("message", response.text[:500])
    except Exception:
        message = response.text[:500]
    return False, message


def render(token_json: dict, token_path: Path, site_url: str) -> str:
    scopes = token_json.get("scopes", [])
    active_scope = detect_scope(scopes)
    has_ready_scope = active_scope is not None
    site_verified = False
    site_message = ""
    if has_ready_scope:
        site_verified, site_message = check_site_access(token_path, site_url)

    lines = []
    lines.append("# Search Console 준비 상태")
    lines.append("")
    lines.append("## 현재 상태")
    lines.append("")
    lines.append(f"- Search Console OAuth 스코프 준비: `{'yes' if has_ready_scope else 'no'}`")
    lines.append(f"- Search Console 속성 접근 가능: `{'yes' if site_verified else 'no'}`")
    lines.append(f"- 현재 OAuth 스코프: `{', '.join(scopes) if scopes else 'none'}`")
    lines.append("")

    if has_ready_scope:
        lines.append(f"현재 토큰에는 Search Console 조회에 필요한 스코프가 포함되어 있습니다. 사용 중인 스코프: `{active_scope}`")
        lines.append("")
        if site_verified:
            lines.append(f"`{site_url}` 속성은 현재 계정에서 정상적으로 읽히고 있습니다.")
        else:
            lines.append(f"`{site_url}` 속성은 현재 계정에서 아직 읽히지 않습니다.")
            lines.append(f"- API 응답: `{site_message}`")
    else:
        lines.append("현재 토큰에는 AdMob/AdSense 읽기 권한만 들어 있어 Search Console 검색어·랜딩페이지·평균순위 데이터를 직접 읽을 수 없습니다.")
        lines.append("")
        lines.append("## 추가로 필요한 스코프")
        lines.append("")
        lines.append("- `https://www.googleapis.com/auth/webmasters.readonly` 또는 `https://www.googleapis.com/auth/webmasters`")

    if not has_ready_scope:
        lines.append("")
        lines.append("## 다음 단계")
        lines.append("")
        lines.append("1. Google Cloud OAuth 동의 설정에서 Search Console 스코프를 추가합니다.")
        lines.append("2. Search Console 접근 권한이 있는 계정으로 OAuth 토큰을 다시 발급합니다.")
        lines.append("3. 사이트 속성(`https://neomindstd.github.io/`)이 Search Console에 등록되어 있는지 확인합니다.")
        lines.append("4. 이후 검색어, 랜딩페이지, 평균순위 데이터를 주간 리뷰에 합칩니다.")
    elif not site_verified:
        lines.append("")
        lines.append("## 다음 단계")
        lines.append("")
        lines.append("1. Search Console에서 `https://neomindstd.github.io/` 속성을 현재 계정에 추가하거나 기존 속성 사용자로 초대합니다.")
        lines.append("2. URL 접두어 속성이라면 소유권 확인을 완료합니다.")
        lines.append("3. 확인이 끝나면 Search Console API에서 검색어·랜딩페이지·평균순위를 읽을 수 있습니다.")
    else:
        lines.append("")
        lines.append("## 다음 단계")
        lines.append("")
        lines.append("1. Search Console 데이터를 성장 감사 스크립트와 주간 리뷰에 연결합니다.")
        lines.append("2. 상위 검색어와 랜딩페이지를 기준으로 AI/Tools 글 우선순위를 다시 정합니다.")
        lines.append("3. CTR이 낮고 노출이 높은 글부터 제목, 설명, 첫 문단 훅을 손봅니다.")

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    token_path = resolve_token_path(args.token)
    token_json = json.loads(token_path.read_text(encoding="utf-8"))
    text = render(token_json, token_path, args.site_url)
    args.out.write_text(text + "\n", encoding="utf-8")
    print(f"Wrote readiness report: {args.out}")


if __name__ == "__main__":
    main()
