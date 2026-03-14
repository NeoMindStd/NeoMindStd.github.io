#!/usr/bin/env python
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(r"D:\WorkSpace\NeoMindStd.github.io")
START_MARKER = "# shortterm-growth-enhancement: begin"
END_MARKER = "# shortterm-growth-enhancement: end"


ENHANCEMENTS = {
    "_posts/etc/2026-03-14-frontier-models-comparison-2026.md": {
        "quick_takeaways": [
            "코드 작업과 에이전트형 수정은 OpenAI Codex나 Claude Code 계열이, 긴 문맥과 구글 생태계는 Gemini 쪽이 더 잘 맞습니다.",
            "실시간 웹 탐색과 브라우저 흐름까지 같이 보고 싶다면 Grok이나 AI 브라우저 계열도 함께 비교하는 편이 좋습니다.",
        ],
        "decision_table_rows": [
            {"left": "코드 수정과 에이전트형 작업", "right": "Codex CLI, Claude Code 계열부터 비교"},
            {"left": "긴 문맥과 구글 생태계", "right": "Gemini 3.1 Pro와 Gemini Workspace 흐름 확인"},
            {"left": "실시간 웹 탐색과 리서치", "right": "Grok과 AI 브라우저 계열을 같이 보기"},
        ],
        "custom_next_reads": [
            {"title": "Gemini CLI 설치와 사용법", "url": "/기타/gemini-cli-guide/", "note": "구글 계열을 바로 써보고 싶을 때"},
            {"title": "Claude Code 설치와 사용법", "url": "/기타/claude-code-setup-guide/", "note": "코딩 에이전트 비교를 이어서 볼 때"},
            {"title": "AI 브라우저 비교", "url": "/기타/ai-browser-comparison-2026/", "note": "검색·리서치 흐름까지 넓혀 볼 때"},
        ],
    },
    "_posts/etc/2026-03-14-local-llm-guide.md": {
        "quick_takeaways": [
            "빠르게 시작하려면 Ollama, 데스크톱 GUI가 좋으면 LM Studio, 세밀한 튜닝과 임베딩 파이프라인은 llama.cpp 계열이 잘 맞습니다.",
            "로컬 LLM은 설치법보다 메모리와 모델 크기 선택이 체감 품질을 더 크게 좌우합니다.",
        ],
        "decision_table_rows": [
            {"left": "터미널에서 가장 빨리 시작", "right": "Ollama"},
            {"left": "GUI로 모델을 고르고 테스트", "right": "LM Studio"},
            {"left": "직접 최적화하고 파이프라인 구성", "right": "llama.cpp 계열"},
        ],
        "custom_next_reads": [
            {"title": "Ollama 설치와 사용법", "url": "/기타/ollama-guide/", "note": "가장 쉬운 로컬 LLM 입문"},
            {"title": "LM Studio 설치와 사용법", "url": "/기타/lm-studio-guide/", "note": "GUI 중심으로 시작할 때"},
            {"title": "Apple Silicon과 로컬 LLM", "url": "/기타/apple-silicon-unified-memory-local-llm/", "note": "맥 메모리 구조가 궁금할 때"},
        ],
    },
    "_posts/etc/2026-03-14-what-is-mcp.md": {
        "quick_takeaways": [
            "MCP는 모델을 외부 도구와 데이터에 연결하는 표준이라서, 요즘 AI 에디터와 CLI 에이전트 흐름을 이해할 때 거의 필수 개념입니다.",
            "툴 연결은 MCP, 여러 에이전트끼리 역할을 나누는 쪽은 A2A라고 보면 큰 흐름을 잡기 쉽습니다.",
        ],
        "decision_table_rows": [
            {"left": "파일, DB, API 같은 도구를 모델에 연결", "right": "MCP부터 이해하기"},
            {"left": "여러 에이전트가 협업하는 구조", "right": "A2A와 오케스트레이션 구조까지 같이 보기"},
            {"left": "터미널·IDE 에이전트를 실제로 써보기", "right": "Claude Code, Gemini CLI, Codex CLI 가이드로 이어가기"},
        ],
        "custom_next_reads": [
            {"title": "A2A란 무엇인가", "url": "/기타/what-is-a2a/", "note": "MCP 다음 개념을 이어서 볼 때"},
            {"title": "Claude Code 설치와 사용법", "url": "/기타/claude-code-setup-guide/", "note": "MCP 감각이 실제로 보이는 도구"},
            {"title": "Gemini CLI 설치와 사용법", "url": "/기타/gemini-cli-guide/", "note": "CLI 에이전트 흐름을 함께 볼 때"},
        ],
    },
    "_posts/etc/2026-03-14-what-is-rag.md": {
        "quick_takeaways": [
            "RAG는 최신 문서나 내부 자료를 모델 바깥에서 찾아 붙여 주는 방식이라, 문서가 자주 바뀌는 서비스에 특히 잘 맞습니다.",
            "모델 자체의 말투나 사고방식을 바꾸는 파인튜닝과는 목적이 다르기 때문에 둘을 섞어 생각하지 않는 편이 좋습니다.",
        ],
        "decision_table_rows": [
            {"left": "자주 바뀌는 문서와 정책을 반영", "right": "RAG 우선 검토"},
            {"left": "말투, 출력 형식, 태스크 성향을 바꾸고 싶음", "right": "파인튜닝 또는 프롬프트 설계 검토"},
            {"left": "대화 맥락을 누적 관리", "right": "메모리 구조와 세션 설계까지 같이 보기"},
        ],
        "custom_next_reads": [
            {"title": "딥리서치란 무엇인가", "url": "/기타/what-is-deep-research/", "note": "검색과 조사 흐름까지 넓혀 볼 때"},
            {"title": "AI Eval이란 무엇인가", "url": "/기타/what-is-ai-eval/", "note": "RAG 품질 검증까지 이어서 볼 때"},
            {"title": "프롬프트 엔지니어링 가이드", "url": "/기타/prompt-engineering-practical-guide/", "note": "검색 없이도 품질을 올릴 때"},
        ],
    },
    "_posts/etc/2026-03-14-gemini-cli-guide.md": {
        "decision_table_rows": [
            {"left": "한 번만 빠르게 체험", "right": "`npx @google/gemini-cli`로 시작"},
            {"left": "계속 쓸 CLI를 찾는 중", "right": "npm 전역 설치나 Homebrew로 고정"},
            {"left": "브라우저보다 터미널 작업 비중이 높음", "right": "Gemini CLI, Claude Code, Codex CLI를 같이 비교"},
        ],
        "custom_next_reads": [
            {"title": "2026 프론티어 모델 비교", "url": "/기타/frontier-models-comparison-2026/", "note": "Gemini가 어디에 강한지 먼저 볼 때"},
            {"title": "MCP란 무엇인가", "url": "/기타/what-is-mcp/", "note": "도구 연결 개념까지 같이 잡고 싶을 때"},
            {"title": "Claude Code 설치와 사용법", "url": "/기타/claude-code-setup-guide/", "note": "다른 CLI 에이전트와 비교할 때"},
        ],
    },
    "_posts/etc/2026-03-14-claude-code-setup-guide.md": {
        "decision_table_rows": [
            {"left": "공식 권장 흐름으로 빠르게 설치", "right": "설치 스크립트 중심으로 시작"},
            {"left": "패키지 매니저로 관리하고 싶음", "right": "Homebrew 경로 검토"},
            {"left": "Codex, Cursor와 비교해서 고를 예정", "right": "터미널 중심인지 IDE 중심인지부터 구분"},
        ],
        "custom_next_reads": [
            {"title": "Codex CLI 설치와 사용법", "url": "/기타/codex-cli-guide/", "note": "OpenAI 계열 CLI와 비교할 때"},
            {"title": "Cursor 설치와 사용법", "url": "/기타/cursor-editor-guide/", "note": "IDE 기반 에이전트와 비교할 때"},
            {"title": "MCP란 무엇인가", "url": "/기타/what-is-mcp/", "note": "도구 연결 구조까지 이해하고 싶을 때"},
        ],
    },
    "_posts/etc/2026-03-14-codex-cli-guide.md": {
        "decision_table_rows": [
            {"left": "OpenAI 계열 워크플로를 터미널에서 쓰고 싶음", "right": "Codex CLI 우선"},
            {"left": "IDE 안에서 긴 세션으로 작업", "right": "Cursor나 Copilot도 함께 비교"},
            {"left": "문서·설명 비중이 큰 협업형 수정", "right": "Claude Code 계열과 비교"},
        ],
        "custom_next_reads": [
            {"title": "GPT Codex란 무엇인가", "url": "/기타/gpt-codex-guide/", "note": "Codex 제품군 전체 그림을 볼 때"},
            {"title": "Cursor 설치와 사용법", "url": "/기타/cursor-editor-guide/", "note": "IDE 기반 대안까지 비교할 때"},
            {"title": "2026 프론티어 모델 비교", "url": "/기타/frontier-models-comparison-2026/", "note": "모델 성향까지 같이 볼 때"},
        ],
    },
    "_posts/etc/2026-03-14-cursor-editor-guide.md": {
        "decision_table_rows": [
            {"left": "IDE 안에서 에이전트와 오래 협업", "right": "Cursor가 가장 자연스러운 편"},
            {"left": "터미널에서 작은 수정과 테스트를 자주 반복", "right": "Codex CLI나 Claude Code 검토"},
            {"left": "자동완성과 PR 보조가 중심", "right": "Copilot과도 함께 비교"},
        ],
        "custom_next_reads": [
            {"title": "GitHub Copilot 설치와 사용법", "url": "/기타/github-copilot-setup-guide/", "note": "가벼운 대안을 같이 볼 때"},
            {"title": "Codex CLI 설치와 사용법", "url": "/기타/codex-cli-guide/", "note": "터미널 기반 흐름과 비교할 때"},
            {"title": "Claude Code 설치와 사용법", "url": "/기타/claude-code-setup-guide/", "note": "다른 코딩 에이전트와 비교할 때"},
        ],
    },
    "_posts/etc/2026-03-14-ollama-guide.md": {
        "decision_table_rows": [
            {"left": "CLI로 빠르게 로컬 모델 실행", "right": "Ollama가 가장 쉬운 편"},
            {"left": "GUI에서 모델을 고르고 테스트", "right": "LM Studio도 함께 보기"},
            {"left": "웹 UI와 공유 환경까지 필요", "right": "Open WebUI 조합 검토"},
        ],
        "custom_next_reads": [
            {"title": "로컬 LLM 시작 가이드", "url": "/기타/local-llm-guide/", "note": "전체 러너 비교를 먼저 볼 때"},
            {"title": "Open WebUI 설치와 사용법", "url": "/기타/open-webui-guide/", "note": "웹 인터페이스까지 붙이고 싶을 때"},
            {"title": "Apple Silicon과 로컬 LLM", "url": "/기타/apple-silicon-unified-memory-local-llm/", "note": "맥에서 성능 감을 잡을 때"},
        ],
    },
    "_posts/etc/2026-03-14-open-webui-guide.md": {
        "decision_table_rows": [
            {"left": "가장 안정적으로 빠르게 띄우기", "right": "Docker 경로 우선"},
            {"left": "파이썬 환경에 직접 붙이기", "right": "pip 설치 경로 검토"},
            {"left": "웹 UI와 로컬 모델을 같이 쓰기", "right": "Ollama와 조합하기"},
        ],
        "custom_next_reads": [
            {"title": "Ollama 설치와 사용법", "url": "/기타/ollama-guide/", "note": "Open WebUI와 가장 많이 묶이는 러너"},
            {"title": "로컬 LLM 시작 가이드", "url": "/기타/local-llm-guide/", "note": "러너 전체 비교를 볼 때"},
            {"title": "OpenClaw 설치와 사용법", "url": "/기타/openclaw-guide/", "note": "셀프호스팅 워크스페이스를 더 넓게 볼 때"},
        ],
    },
    "_posts/etc/2026-03-14-perplexity-comet-guide.md": {
        "quick_takeaways": [
            "탭을 많이 열고 조사·비교 검색을 자주 하는 사람에게는 Comet이 일반 브라우저보다 훨씬 직관적으로 느껴질 수 있습니다.",
            "반대로 기존 브라우저를 유지한 채 AI만 얹고 싶다면 Brave Leo나 Edge Copilot Mode 쪽이 더 부담이 적습니다.",
        ],
        "decision_table_rows": [
            {"left": "브라우저 자체를 AI 중심으로 바꾸고 싶음", "right": "Perplexity Comet"},
            {"left": "프라이버시와 로컬/BYOM 감각을 중요하게 봄", "right": "Brave Leo"},
            {"left": "Windows 기본 흐름과 코파일럿 연동", "right": "Edge Copilot Mode"},
        ],
        "custom_next_reads": [
            {"title": "AI 브라우저 비교", "url": "/기타/ai-browser-comparison-2026/", "note": "Comet의 위치를 한 번에 볼 때"},
            {"title": "Brave Leo 사용법", "url": "/기타/brave-leo-guide/", "note": "BYOM과 프라이버시 흐름이 궁금할 때"},
            {"title": "딥리서치란 무엇인가", "url": "/기타/what-is-deep-research/", "note": "브라우저 너머 조사 모드까지 볼 때"},
        ],
    },
    "_posts/etc/2026-03-14-brave-leo-guide.md": {
        "quick_takeaways": [
            "Brave Leo는 AI 브라우저 중에서도 프라이버시와 BYOM 감각이 강한 편이라, 기존 브라우저 습관을 크게 버리지 않고 확장하기 좋습니다.",
            "Perplexity Comet처럼 브라우저 경험 전체를 바꾸는 쪽과는 결이 다르니, 내 사용 습관이 어디에 가까운지 먼저 보는 편이 좋습니다.",
        ],
        "decision_table_rows": [
            {"left": "기존 브라우저에 AI를 덧대는 감각", "right": "Brave Leo"},
            {"left": "검색과 리서치를 AI 브라우저로 통합", "right": "Perplexity Comet"},
            {"left": "Microsoft 계정·Windows 기본 흐름", "right": "Edge Copilot Mode"},
        ],
        "custom_next_reads": [
            {"title": "AI 브라우저 비교", "url": "/기타/ai-browser-comparison-2026/", "note": "세 제품을 한 번에 비교할 때"},
            {"title": "Perplexity Comet 설치와 사용법", "url": "/기타/perplexity-comet-guide/", "note": "브라우저 자체가 더 바뀌는 대안"},
            {"title": "Ollama 설치와 사용법", "url": "/기타/ollama-guide/", "note": "BYOM 감각을 로컬 모델로 이어갈 때"},
        ],
    },
    "_posts/etc/2026-03-14-ai-browser-comparison-2026.md": {
        "quick_takeaways": [
            "조사와 비교 중심이면 Comet, 프라이버시와 BYOM은 Leo, Windows 기본 흐름과 Copilot 연동은 Edge 쪽이 더 자연스럽습니다.",
            "브라우저 선택은 모델 성능보다 탭 관리, 기본 브라우저 전환, 데이터 처리 감각 같은 사용 습관이 더 크게 작용합니다.",
        ],
        "decision_table_rows": [
            {"left": "연구·쇼핑·탭 정리가 많은 사람", "right": "Perplexity Comet"},
            {"left": "Brave 생태계와 BYOM 선호", "right": "Brave Leo"},
            {"left": "Windows와 Microsoft 생태계 중심", "right": "Copilot Mode in Edge"},
        ],
        "custom_next_reads": [
            {"title": "Perplexity Comet 설치와 사용법", "url": "/기타/perplexity-comet-guide/", "note": "리서치 중심 브라우저 흐름"},
            {"title": "Brave Leo 사용법", "url": "/기타/brave-leo-guide/", "note": "프라이버시 중심 대안"},
            {"title": "Copilot Mode in Edge 사용법", "url": "/기타/edge-copilot-mode-guide/", "note": "Windows 사용자 기준 대안"},
        ],
    },
    "_posts/etc/2026-03-14-gemini-workspace-guide.md": {
        "quick_takeaways": [
            "문서 작성, 시트 정리, 슬라이드 초안이 많은 사람이라면 Gemini Workspace가 코딩 도구보다 훨씬 바로 체감되는 AI입니다.",
            "반대로 코드 수정이나 리포지토리 작업이 중심이라면 Gemini CLI나 Cursor 같은 도구가 더 직접적입니다.",
        ],
        "decision_table_rows": [
            {"left": "Docs, Sheets, Slides를 매일 씀", "right": "Gemini Workspace 우선"},
            {"left": "터미널·리포지토리 작업이 더 많음", "right": "Gemini CLI나 Cursor 검토"},
            {"left": "조사와 자료 수집 비중이 큼", "right": "딥리서치나 AI 브라우저 흐름도 같이 보기"},
        ],
        "custom_next_reads": [
            {"title": "Gemini CLI 설치와 사용법", "url": "/기타/gemini-cli-guide/", "note": "개발자 워크플로까지 확장할 때"},
            {"title": "딥리서치란 무엇인가", "url": "/기타/what-is-deep-research/", "note": "문서 초안 이전 조사 단계"},
            {"title": "생성형 창작 AI 입문", "url": "/기타/creative-ai-guide-2026/", "note": "텍스트 밖 창작 도구까지 넓혀 볼 때"},
        ],
    },
    "_posts/etc/2026-03-15-creative-ai-guide-2026.md": {
        "quick_takeaways": [
            "음악은 Suno/Udio, 이미지·사진은 ChatGPT 이미지·Midjourney·Firefly, 영상은 Sora·Veo·Runway처럼 매체별로 먼저 나눠 보는 편이 훨씬 쉽습니다.",
            "창작형 AI는 품질 자체보다 저작권, 상업 이용 범위, 편집 워크플로까지 같이 비교해야 실제로 쓸 도구를 고르기 편합니다.",
        ],
        "decision_table_rows": [
            {"left": "노래를 빠르게 만들고 공유", "right": "음악 생성 AI부터 보기"},
            {"left": "썸네일·일러스트·사진 편집", "right": "이미지 생성 AI 비교부터 보기"},
            {"left": "짧은 영상 콘셉트와 컷 생성", "right": "영상 생성 AI 비교부터 보기"},
        ],
        "custom_next_reads": [
            {"title": "음악 생성 AI 비교와 사용법", "url": "/기타/ai-music-generation-guide-2026/", "note": "창팝·밈 문화까지 같이 볼 때"},
            {"title": "그림·사진 생성 AI 비교", "url": "/기타/ai-image-photo-generation-guide-2026/", "note": "썸네일·이미지 제작 도구를 고를 때"},
            {"title": "영상 생성 AI 비교", "url": "/기타/ai-video-generation-guide-2026/", "note": "Sora, Veo, Runway 흐름을 볼 때"},
        ],
    },
    "_posts/etc/2026-03-15-ai-image-photo-generation-guide-2026.md": {
        "quick_takeaways": [
            "가장 쉽게 시작하려면 ChatGPT 이미지, 스타일과 커뮤니티 감각은 Midjourney, Adobe 작업 흐름은 Firefly가 강점이 뚜렷합니다.",
            "이미지 AI는 결과물 한 장보다 편집 반복과 상업 이용 정책이 실제 만족도를 크게 좌우합니다.",
        ],
        "decision_table_rows": [
            {"left": "대화형으로 빠르게 결과 보기", "right": "ChatGPT 이미지"},
            {"left": "스타일 중심 일러스트와 커뮤니티 레퍼런스", "right": "Midjourney"},
            {"left": "Photoshop·디자인 실무와 연결", "right": "Adobe Firefly"},
        ],
        "custom_next_reads": [
            {"title": "생성형 창작 AI 입문", "url": "/기타/creative-ai-guide-2026/", "note": "음악·영상까지 한 번에 볼 때"},
            {"title": "영상 생성 AI 비교", "url": "/기타/ai-video-generation-guide-2026/", "note": "이미지 다음 단계로 넘어갈 때"},
            {"title": "프롬프트 엔지니어링 가이드", "url": "/기타/prompt-engineering-practical-guide/", "note": "결과물 품질을 더 끌어올릴 때"},
        ],
    },
    "_posts/etc/2026-03-15-ai-music-generation-guide-2026.md": {
        "quick_takeaways": [
            "짧은 시간에 완성곡 감각을 보고 싶다면 Suno, 대안 비교와 스타일 실험을 넓히고 싶다면 Udio를 같이 보는 편이 좋습니다.",
            "밈·커뮤니티 문화와 잘 붙는 장르라서, 기술 비교와 함께 창팝 같은 활용 문화를 같이 보면 이해가 더 빠릅니다.",
        ],
        "decision_table_rows": [
            {"left": "가사부터 곡까지 빠르게 완성", "right": "Suno 중심으로 보기"},
            {"left": "다른 스타일과 대안을 비교", "right": "Udio까지 같이 보기"},
            {"left": "밈·커뮤니티형 활용 감각이 궁금함", "right": "창팝/신창섭 문화 맥락까지 같이 보기"},
        ],
        "custom_next_reads": [
            {"title": "생성형 창작 AI 입문", "url": "/기타/creative-ai-guide-2026/", "note": "다른 매체 생성 AI까지 확장할 때"},
            {"title": "영상 생성 AI 비교", "url": "/기타/ai-video-generation-guide-2026/", "note": "음악에 영상을 붙이는 단계"},
            {"title": "프롬프트 엔지니어링 가이드", "url": "/기타/prompt-engineering-practical-guide/", "note": "가사·스타일 프롬프트를 다듬을 때"},
        ],
    },
    "_posts/etc/2026-03-15-ai-video-generation-guide-2026.md": {
        "quick_takeaways": [
            "영상 AI는 한 번에 긴 결과물을 기대하기보다, 짧은 컷과 콘셉트 시퀀스를 먼저 뽑고 편집으로 이어가는 감각이 더 실용적입니다.",
            "Sora, Veo, Runway는 품질뿐 아니라 접근성, 편집 흐름, 공개 범위 차이까지 같이 봐야 선택이 쉬워집니다.",
        ],
        "decision_table_rows": [
            {"left": "콘셉트 영상과 장면 실험", "right": "Sora, Veo 계열 먼저 비교"},
            {"left": "편집 워크플로와 후반 작업", "right": "Runway까지 같이 보기"},
            {"left": "이미지에서 영상으로 확장", "right": "이미지 생성 AI와 묶어서 보기"},
        ],
        "custom_next_reads": [
            {"title": "생성형 창작 AI 입문", "url": "/기타/creative-ai-guide-2026/", "note": "음악·이미지까지 함께 비교할 때"},
            {"title": "그림·사진 생성 AI 비교", "url": "/기타/ai-image-photo-generation-guide-2026/", "note": "스토리보드용 이미지부터 만들 때"},
            {"title": "프롬프트 엔지니어링 가이드", "url": "/기타/prompt-engineering-practical-guide/", "note": "장면 지시문을 더 잘 쓰고 싶을 때"},
        ],
    },
    "_posts/tools/2026-03-14-docker-guide.md": {
        "quick_takeaways": [
            "로컬 개발 환경을 빠르게 맞추고 싶다면 Docker Desktop으로 시작하는 쪽이 가장 부담이 적습니다.",
            "초반에는 이미지, 컨테이너, 볼륨, 포트 매핑 순서만 이해해도 체감이 크게 좋아집니다.",
        ],
        "decision_table_rows": [
            {"left": "노트북에서 바로 개발 환경 재현", "right": "Docker Desktop부터 시작"},
            {"left": "서버나 CI 같은 리눅스 환경 중심", "right": "Engine/Compose 흐름까지 같이 보기"},
            {"left": "개발 툴과 API 테스트를 묶어 쓰기", "right": "Python, Postman 글도 함께 보기"},
        ],
        "custom_next_reads": [
            {"title": "Python 설치와 사용법", "url": "/tools/python-guide/", "note": "개발 환경 기본 축을 같이 맞출 때"},
            {"title": "Postman 설치와 사용법", "url": "/tools/postman-guide/", "note": "컨테이너로 띄운 API를 테스트할 때"},
            {"title": "Open WebUI 설치와 사용법", "url": "/기타/open-webui-guide/", "note": "Docker 실전 예제로 이어질 때"},
        ],
    },
    "_posts/tools/2026-03-14-python-guide.md": {
        "quick_takeaways": [
            "파이썬은 설치 자체보다 `python --version`, `pip`, `venv`까지 한 번에 익혀 두는 편이 훨씬 실용적입니다.",
            "윈도우에서는 py 런처와 PATH 설정, 맥·리눅스에서는 기본 파이썬과 별도 설치본을 구분하는 감각이 중요합니다.",
        ],
        "decision_table_rows": [
            {"left": "스크립트와 자동화를 빠르게 시작", "right": "공식 설치본 + venv부터 익히기"},
            {"left": "AI·데이터 툴도 함께 쓸 예정", "right": "패키지 관리와 가상환경까지 같이 정리"},
            {"left": "컨테이너 환경과도 함께 쓸 예정", "right": "Docker 글까지 이어서 보기"},
        ],
        "custom_next_reads": [
            {"title": "Docker 설치와 사용법", "url": "/tools/docker-guide/", "note": "파이썬 환경을 컨테이너로 옮길 때"},
            {"title": "Postman 설치와 사용법", "url": "/tools/postman-guide/", "note": "파이썬 API를 테스트할 때"},
            {"title": "Open WebUI 설치와 사용법", "url": "/기타/open-webui-guide/", "note": "파이썬 기반 AI 앱 예제로 이어질 때"},
        ],
    },
}


def quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def build_lines(data: dict) -> list[str]:
    lines = [START_MARKER]

    if data.get("quick_takeaways"):
        lines.append("quick_takeaways:")
        for item in data["quick_takeaways"]:
            lines.append(f"  - {quote(item)}")

    lines.append("decision_table_title: " + quote("한눈에 고르기"))
    lines.append("decision_table_headers:")
    lines.append(f"  - {quote('상황')}")
    lines.append(f"  - {quote('먼저 보기')}")
    lines.append("decision_table_rows:")
    for row in data["decision_table_rows"]:
        lines.append(f"  - left: {quote(row['left'])}")
        lines.append(f"    right: {quote(row['right'])}")

    lines.append("custom_next_reads_title: " + quote("이 글과 함께 보면 좋은 글"))
    lines.append("custom_next_reads_intro: " + quote("지금 읽은 내용을 바로 확장하거나, 실제 선택과 설치까지 이어질 만한 글들만 골랐습니다."))
    lines.append("custom_next_reads:")
    for row in data["custom_next_reads"]:
        lines.append(f"  - title: {quote(row['title'])}")
        lines.append(f"    url: {quote(row['url'])}")
        if row.get("note"):
            lines.append(f"    note: {quote(row['note'])}")

    lines.append(END_MARKER)
    return lines


def replace_or_insert_block(text: str, lines: list[str]) -> str:
    block = "\n".join(lines) + "\n"
    if START_MARKER in text and END_MARKER in text:
        start = text.index(START_MARKER)
        end = text.index(END_MARKER) + len(END_MARKER)
        return text[:start] + block + text[end:]

    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("front matter not found")

    prefix, front_matter, body = parts[0], parts[1], parts[2]
    front_matter = front_matter.rstrip() + "\n" + block
    return "---".join([prefix, front_matter, body])


def main() -> None:
    updated = 0
    for relative_path, data in ENHANCEMENTS.items():
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        new_text = replace_or_insert_block(text, build_lines(data))
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
            print(f"updated {relative_path}")
    print(f"done: {updated} files")


if __name__ == "__main__":
    main()
