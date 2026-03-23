# 중기 8차: AI 대표 글 상단 프로필 배지 도입 (2026-03-23)

## 작업 목적

- AI 글 랜딩 직후 사용자가 "이 글이 나에게 맞는지"를 즉시 판단하게 만들기
- 글 본문 전환 전에 난이도, 플랫폼, 추천 대상을 시각적으로 보여줘 이탈을 줄이기

## 반영 내용

### 공통 레이아웃

- `single` 레이아웃 헤더에 프로필 배지 영역 추가
- front matter 값이 있을 때만 노출하도록 조건부 렌더링 처리

신규 front matter 키:

- `profile_difficulty`
- `profile_platforms`
- `profile_audience`

### 스타일

- 기존 Tools 배지 스타일을 재사용
- 글 상단 배지 간격 전용 클래스(`nm-post-profile-badges`) 추가

### 적용 포스트

- `/기타/gemini-cli-guide/`
- `/기타/ollama-guide/`
- `/기타/codex-cli-guide/`
- `/기타/claude-code-setup-guide/`
- `/기타/cursor-editor-guide/`
- `/기타/github-copilot-setup-guide/`

## 기대 효과

- 설치형/비교형 AI 글에서 랜딩 초반 의사결정이 빨라짐
- 허브에서 들어온 사용자와 직접 랜딩 사용자가 같은 정보 구조를 보게 됨
- 이후 Search Console/GA에서 글 단위 이탈률과 다음 클릭률 비교가 쉬워짐
