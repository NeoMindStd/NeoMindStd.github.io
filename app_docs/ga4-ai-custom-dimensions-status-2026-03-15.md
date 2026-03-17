# GA4 AI 커스텀 차원 상태

- 대상 속성: `properties/382166604` (`neomindstd.github.io - GA4`)

## 현재 등록 상태

- `Event Category` / `event_category` / `EVENT`
- `Event Label` / `event_label` / `EVENT`
- `AI Source` / `ai_source` / `EVENT`
- `AI Referrer Host` / `ai_referrer_host` / `EVENT`

## AI 유입 측정에 필요한 차원

- `AI Source` (`ai_source`, EVENT) : `ready`
- `AI Referrer Host` (`ai_referrer_host`, EVENT) : `ready`

## 자동 생성 시도 결과

- 이번 실행에서는 자동 생성을 시도하지 않았습니다.

## 권장 설정값

1. `Admin > Data display > Custom definitions > Create custom dimension`
2. 아래 2개를 이벤트 범위로 추가
   - Display name: `AI Source` / Event parameter: `ai_source`
   - Display name: `AI Referrer Host` / Event parameter: `ai_referrer_host`
3. 저장 후 24~48시간 뒤 탐색/이벤트 보고서에서 확인


