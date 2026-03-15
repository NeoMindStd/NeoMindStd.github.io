# GA4 AI 커스텀 차원 상태

- 대상 속성: `properties/382166604` (`neomindstd.github.io - GA4`)

## 현재 등록 상태

- `Event Category` / `event_category` / `EVENT`
- `Event Label` / `event_label` / `EVENT`

## AI 유입 측정에 필요한 차원

- `AI Source` (`ai_source`, EVENT) : `missing`
- `AI Referrer Host` (`ai_referrer_host`, EVENT) : `missing`

## 자동 생성 시도 결과

- `ai_source` 생성 실패 (`403`): `The caller does not have permission`
- `ai_referrer_host` 생성 실패 (`403`): `The caller does not have permission`

## 권장 설정값

1. `Admin > Data display > Custom definitions > Create custom dimension`
2. 아래 2개를 이벤트 범위로 추가
   - Display name: `AI Source` / Event parameter: `ai_source`
   - Display name: `AI Referrer Host` / Event parameter: `ai_referrer_host`
3. 저장 후 24~48시간 뒤 탐색/이벤트 보고서에서 확인

## 메모

- 현재 서비스 계정으로는 목록 조회는 되지만 생성 권한은 없습니다.
- GA4 속성에서 `Editor` 이상 권한이 있는 계정으로 UI에서 한 번 등록하는 것이 가장 빠릅니다.

