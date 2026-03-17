# 중기계획 1차 실행: AI 클러스터 링크 구조 보강

## 목적

- AI 허브를 단순 목록이 아니라 `클러스터 -> 대표 글 -> 설치/비교/개념` 흐름으로 만들기
- 다음 클릭을 더 자연스럽게 만들어 허브 체류와 재순환을 높이기
- 이후 Search Console에서 AI/Tools 랜딩이 늘었을 때 클러스터 단위로 성과를 보기 쉽게 준비하기

## 이번에 손본 대표 글

### AI 브라우저·리서치

- `ai-browser-comparison-2026`
  - 클러스터 허브 링크 추가
  - Comet / Leo / Edge 설치 글 + 딥리서치 글까지 연결

### 로컬 LLM·셀프호스팅

- `local-llm-guide`
  - 클러스터 허브 링크 추가
  - Ollama / LM Studio / Open WebUI / Apple Silicon 글 연결

### 생성형 창작 AI

- `creative-ai-guide-2026`
  - 클러스터 허브 링크 추가
  - 음악 / 이미지 / 영상 비교 글과 프롬프트 가이드 연결

### 실무용 AI·워크플로우

- `gemini-workspace-guide`
  - 실무용 AI 허브 링크 추가
  - Gemini CLI / 딥리서치 / Perplexity Labs 연결
- `prompt-engineering-practical-guide`
  - 빠른 답, 한눈에 고르기, 관련 읽을거리 추가
  - workflows 허브 / coding-tools 허브 / MCP / Eval 연결

### AI 코딩 도구

- `gemini-cli-guide`
  - coding-tools 허브 링크 추가
  - workflows 허브 링크 추가
  - 프론티어 비교 / MCP / Claude Code 연결 유지

## 공통 레이아웃 변경

- `single.html`
  - AI 카테고리 글 하단 CTA를 개별 글 몇 개 위주에서
  - `AI 코딩 도구`, `AI 브라우저·리서치`, `로컬 LLM·셀프호스팅`, `생성형 창작 AI`, `실무용 AI·워크플로우`
    클러스터 허브 중심으로 변경

## 기대 효과

1. 한 글에서 끝나는 비율 감소
2. 허브 페이지 진입 후 다음 클릭률 개선
3. Search Console이 AI 허브군을 인식하기 시작했을 때 클러스터 단위 개선이 쉬워짐

## 다음 중기 작업 후보

1. 클러스터별 대표 비교 글 1개씩 더 보강
2. AI 코딩 도구 허브에 설치 난이도 / 추천 사용자 비교표 추가
3. 브라우저·리서치 허브에 `조사형 vs 작업형` 분류 표 추가
4. 로컬 LLM 허브에 메모리 / 운영체제 / UI 유무 기준 비교표 추가
