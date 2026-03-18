#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

import requests
from google.auth.transport.requests import Request
from google.oauth2 import service_account


EXPECTED_DIMENSIONS = [
    {
        "parameterName": "ai_source",
        "displayName": "AI Source",
        "description": "AI referral source captured from ai_referral_visit",
        "scope": "EVENT",
    },
    {
        "parameterName": "ai_referrer_host",
        "displayName": "AI Referrer Host",
        "description": "Referrer host captured from ai_referral_visit",
        "scope": "EVENT",
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check GA4 custom dimensions for AI referral reporting.")
    parser.add_argument(
        "--service-account",
        type=Path,
        default=None,
        help="Path to a Google service account JSON. Falls back to GA4_SERVICE_ACCOUNT_JSON or GOOGLE_APPLICATION_CREDENTIALS.",
    )
    parser.add_argument("--property-id", default="382166604")
    parser.add_argument("--attempt-create", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    return parser.parse_args()


def resolve_service_account_path(cli_value: Path | None) -> Path:
    if cli_value is not None:
        return cli_value

    env_value = os.environ.get("GA4_SERVICE_ACCOUNT_JSON") or os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if env_value:
        return Path(env_value)

    raise SystemExit(
        "Missing service account path. Pass --service-account or set GA4_SERVICE_ACCOUNT_JSON / GOOGLE_APPLICATION_CREDENTIALS."
    )


def build_token(service_account_path: Path, scopes: list[str]) -> str:
    creds = service_account.Credentials.from_service_account_file(str(service_account_path), scopes=scopes)
    creds.refresh(Request())
    return creds.token


def request_json(method: str, url: str, token: str, *, body: dict[str, Any] | None = None) -> tuple[bool, dict[str, Any]]:
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    if body is not None:
        headers["Content-Type"] = "application/json"
    response = requests.request(method, url, headers=headers, json=body, timeout=120)
    try:
        payload = response.json()
    except Exception:
        payload = {"raw": response.text[:1000]}
    return response.ok, {"status_code": response.status_code, "response": payload}


def list_dimensions(property_id: str, token: str) -> dict[str, Any]:
    url = f"https://analyticsadmin.googleapis.com/v1beta/properties/{property_id}/customDimensions"
    ok, result = request_json("GET", url, token)
    return {"ok": ok, "api": result, "rows": result.get("response", {}).get("customDimensions", []) if ok else []}


def create_dimension(property_id: str, token: str, payload: dict[str, Any]) -> dict[str, Any]:
    url = f"https://analyticsadmin.googleapis.com/v1beta/properties/{property_id}/customDimensions"
    ok, result = request_json("POST", url, token, body=payload)
    return {"ok": ok, "api": result, "payload": payload}


def render(property_id: str, listed: dict[str, Any], create_results: list[dict[str, Any]]) -> str:
    existing = listed.get("rows", [])
    existing_by_parameter = {row.get("parameterName"): row for row in existing}
    missing = [dimension for dimension in EXPECTED_DIMENSIONS if dimension["parameterName"] not in existing_by_parameter]

    lines: list[str] = []
    lines.append("# GA4 AI 커스텀 차원 상태")
    lines.append("")
    lines.append(f"- 대상 속성: `properties/{property_id}` (`neomindstd.github.io - GA4`)")
    lines.append("")
    lines.append("## 현재 등록 상태")
    lines.append("")
    if existing:
        for row in existing:
            lines.append(f"- `{row.get('displayName')}` / `{row.get('parameterName')}` / `{row.get('scope')}`")
    else:
        lines.append("- 등록된 커스텀 차원이 없습니다.")
    lines.append("")
    lines.append("## AI 유입 측정에 필요한 차원")
    lines.append("")
    for dimension in EXPECTED_DIMENSIONS:
        exists = dimension["parameterName"] in existing_by_parameter
        lines.append(
            f"- `{dimension['displayName']}` (`{dimension['parameterName']}`, {dimension['scope']}) : `{'ready' if exists else 'missing'}`"
        )
    lines.append("")
    lines.append("## 자동 생성 시도 결과")
    lines.append("")
    if create_results:
        for result in create_results:
            payload = result["payload"]
            status_code = result["api"].get("status_code")
            if result["ok"]:
                lines.append(f"- `{payload['parameterName']}` 생성 성공 (`{status_code}`)")
            else:
                message = result["api"].get("response", {}).get("error", {}).get("message") or result["api"].get("response")
                lines.append(f"- `{payload['parameterName']}` 생성 실패 (`{status_code}`): `{message}`")
    else:
        lines.append("- 이번 실행에서는 자동 생성을 시도하지 않았습니다.")
    lines.append("")
    lines.append("## 권장 설정값")
    lines.append("")
    lines.append("1. `Admin > Data display > Custom definitions > Create custom dimension`")
    lines.append("2. 아래 2개를 이벤트 범위로 추가")
    lines.append("   - Display name: `AI Source` / Event parameter: `ai_source`")
    lines.append("   - Display name: `AI Referrer Host` / Event parameter: `ai_referrer_host`")
    lines.append("3. 저장 후 24~48시간 뒤 탐색/이벤트 보고서에서 확인")
    lines.append("")
    if missing:
        lines.append("## 메모")
        lines.append("")
        lines.append("- 현재 서비스 계정으로는 목록 조회는 되지만 생성 권한은 없습니다.")
        lines.append("- GA4 속성에서 `Editor` 이상 권한이 있는 계정으로 UI에서 한 번 등록하는 것이 가장 빠릅니다.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    service_account_path = resolve_service_account_path(args.service_account)
    readonly_token = build_token(service_account_path, ["https://www.googleapis.com/auth/analytics.readonly"])
    listed = list_dimensions(args.property_id, readonly_token)

    create_results: list[dict[str, Any]] = []
    if args.attempt_create:
        existing_by_parameter = {row.get("parameterName") for row in listed.get("rows", [])}
        edit_token = build_token(service_account_path, ["https://www.googleapis.com/auth/analytics.edit"])
        for dimension in EXPECTED_DIMENSIONS:
            if dimension["parameterName"] in existing_by_parameter:
                continue
            create_results.append(create_dimension(args.property_id, edit_token, dimension))

    text = render(args.property_id, listed, create_results)
    args.out.write_text(text + "\n", encoding="utf-8")
    print(f"Wrote status: {args.out}")


if __name__ == "__main__":
    main()
