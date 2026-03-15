# GA4 AI 유입 측정 기준

## 목적

이 문서는 ChatGPT, Claude, Perplexity, Gemini, Copilot 같은 AI 서비스에서 실제 사람이 클릭해 들어온 유입을 GA4에서 분리해 보는 기준을 정리한 문서입니다.

핵심은 "AI 크롤러 접근"과 "AI 답변이나 검색 결과를 보고 사용자가 직접 클릭한 방문"을 구분하는 것입니다. 광고 수익이나 콘텐츠 성과와 더 직접 연결되는 쪽은 후자입니다.

## 사이트 코드에서 보내는 이벤트

사이트에는 AI referrer가 감지되면 아래 이벤트를 보내는 로직을 넣었습니다.

- 이벤트 이름: `ai_referral_visit`
- 이벤트 파라미터:
  - `ai_source`
  - `ai_referrer_host`

현재 감지 대상은 아래 기준입니다.

- ChatGPT: `utm_source=chatgpt.com`, `chatgpt.com`, `chat.openai.com`, `openai.com`
- Claude: `claude.ai`
- Perplexity: `perplexity.ai`
- Gemini: `gemini.google.com`, `gemini.googleusercontent.com`
- Copilot: `copilot.microsoft.com`
- Grok: `grok.com`, `x.com`

## GA4에서 먼저 만들어둘 것

GA4 관리 화면에서 아래 사용자 정의 측정기준을 이벤트 범위로 추가합니다.

1. `ai_source`
2. `ai_referrer_host`

둘 다 이벤트 범위로 잡아 두면 탐색 보고서와 이벤트 리포트에서 소스별 분리가 쉬워집니다.

### 정확한 메뉴 경로

- `Admin`
- `Data display`
- `Custom definitions`
- `Create custom dimension`

입력값은 아래처럼 맞추면 됩니다.

1. `AI Source`
   - Scope: `Event`
   - Event parameter: `ai_source`
   - Description: `AI referral source captured from ai_referral_visit`
2. `AI Referrer Host`
   - Scope: `Event`
   - Event parameter: `ai_referrer_host`
   - Description: `Referrer host captured from ai_referral_visit`

### 현재 상태

- 현재 속성 `properties/382166604`에는 `Event Category`, `Event Label`만 등록돼 있습니다.
- 서비스 계정으로 자동 생성을 시도했지만 `PERMISSION_DENIED`가 반환됐습니다.
- 즉 현재는 `조회 권한`은 있지만 `커스텀 차원 생성 권한`은 없는 상태입니다.
- 그래서 실제 생성은 GA4 속성에서 `Editor` 이상 권한이 있는 계정으로 한 번 등록해야 합니다.

## 가장 먼저 볼 보고서

### 1. 이벤트 보고서

- 이벤트 이름: `ai_referral_visit`
- 보조 측정기준:
  - `ai_source`
  - `ai_referrer_host`

이렇게 보면 어떤 AI 서비스가 실제 클릭 유입을 만들어내는지 빠르게 볼 수 있습니다.

### 2. 트래픽 획득 보고서

트래픽 획득 보고서에서 아래 source나 referrer를 같이 봅니다.

- `chatgpt.com`
- `claude.ai`
- `perplexity.ai`
- `gemini.google.com`
- `copilot.microsoft.com`
- `x.com`
- `grok.com`

OpenAI 쪽은 일부 링크에 `utm_source=chatgpt.com`이 붙을 수 있으니, 세션 source/medium과 이벤트 둘 다 같이 보는 편이 좋습니다.

### 3. 랜딩 페이지 보고서

`Landing page + query string`이나 `Pages and screens`에서 AI 유입이 실제로 어느 글로 들어오는지 확인합니다.

이때 특히 잘 볼 항목은 아래입니다.

- AI 카테고리 글
- 설치형 도구 글
- 비교형 글
- 오류 해결형 글

## 추천 커스텀 채널 그룹

GA4에서 커스텀 채널 그룹을 쓸 수 있다면 `AI Assistants` 같은 채널을 하나 만들어 두는 편이 좋습니다.

추천 규칙 예시는 아래와 같습니다.

- Source contains `chatgpt.com`
- Source contains `claude.ai`
- Source contains `perplexity.ai`
- Source contains `gemini.google.com`
- Source contains `copilot.microsoft.com`
- Source contains `grok.com`
- Source contains `x.com`

이렇게 해 두면 일반 검색과 AI 유입을 대시보드에서 따로 볼 수 있습니다.

## 해석할 때 주의할 점

- AI 크롤러 접근량이 늘었다고 광고 수익이 같이 늘지는 않습니다.
- 실제 광고 수익과 연결되는 건 사람이 클릭해 들어온 방문입니다.
- Perplexity나 Claude는 referrer가 항상 안정적으로 남지 않을 수 있어서 이벤트 값과 세션 source를 같이 보는 편이 안전합니다.
- 같은 AI 유입이라도 블로그형 설명 글보다 설치형, 비교형, 오류 해결형 글이 클릭 의도가 더 강한 경우가 많습니다.

## 지금 블로그에서 특히 볼만한 지표

1. `ai_referral_visit` 이벤트 수
2. `ai_source`별 유입 비중
3. AI 유입 랜딩 페이지 상위 10개
4. AI 유입 세션의 평균 참여 시간
5. AI 유입 세션의 AdSense 성과 변화

## 요약

이 블로그에서 AI 유입 측정의 핵심은 "AI가 읽었는가"가 아니라 "AI가 사람을 데려왔는가"를 보는 것입니다.

그래서 GA4에서는 `ai_referral_visit` 이벤트, `ai_source`와 `ai_referrer_host` 사용자 정의 측정기준, 그리고 AI 전용 채널 그룹을 같이 보는 구성이 가장 실용적입니다.
