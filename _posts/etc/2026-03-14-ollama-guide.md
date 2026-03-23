---
title:  "[기타/AI] Ollama 설치와 사용법: Windows, macOS, Linux에서 로컬 LLM 바로 돌리기"
excerpt: "Ollama를 공식 사이트 기준으로 설치하고, Windows/macOS/Linux에서 첫 모델 다운로드와 실행까지 이어지는 로컬 LLM 입문 가이드입니다."
description: "Ollama 공식 사이트와 다운로드 경로, 지원 OS, 첫 모델 pull/run 흐름, 로컬 API 사용 감각을 정리한 글입니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - Ollama
  - Local LLM
  - LLM Runner
  - macOS
  - Windows
  - Linux
date: 2026-03-14 19:41:00 +09:00
permalink: /기타/ollama-guide/
header:
  og_image: /assets/images/posts/etc/ollama-guide/official.png
  teaser: /assets/images/posts/etc/ollama-guide/official.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
profile_difficulty: "입문"
profile_platforms:
  - Windows
  - macOS
  - Linux
profile_audience:
  - 로컬 LLM 입문자
  - 프라이버시 중시 사용자
# shortterm-growth-enhancement: begin
decision_table_title: "한눈에 고르기"
decision_table_headers:
  - "상황"
  - "먼저 보기"
decision_table_rows:
  - left: "CLI로 빠르게 로컬 모델 실행"
    right: "Ollama가 가장 쉬운 편"
  - left: "GUI에서 모델을 고르고 테스트"
    right: "LM Studio도 함께 보기"
  - left: "웹 UI와 공유 환경까지 필요"
    right: "Open WebUI 조합 검토"
custom_next_reads_title: "이 글과 함께 보면 좋은 글"
custom_next_reads_intro: "지금 읽은 내용을 바로 확장하거나, 실제 선택과 설치까지 이어질 만한 글들만 골랐습니다."
custom_next_reads:
  - title: "로컬 LLM 시작 가이드"
    url: "/기타/local-llm-guide/"
    note: "전체 러너 비교를 먼저 볼 때"
  - title: "Open WebUI 설치와 사용법"
    url: "/기타/open-webui-guide/"
    note: "웹 인터페이스까지 붙이고 싶을 때"
  - title: "Apple Silicon과 로컬 LLM"
    url: "/기타/apple-silicon-unified-memory-local-llm/"
    note: "맥에서 성능 감을 잡을 때"
# shortterm-growth-enhancement: end
---

- - -

 - [기타](/etc)

- - -

![대표 이미지](/assets/images/posts/etc/ollama-guide/hero.svg)

![Ollama ?? ??](/assets/images/posts/etc/ollama-guide/logo.png)

![공식 페이지 이미지](/assets/images/posts/etc/ollama-guide/official.png)

# 빠른 답

- Ollama는 로컬 LLM을 가장 쉽게 시작하는 러너 중 하나입니다.
- 설치 후 `ollama run`만으로 바로 모델을 받아 체험할 수 있어서 입문 장벽이 낮습니다.
- 프라이버시와 오프라인 테스트에는 좋지만, 실제 속도와 모델 선택 폭은 PC 메모리와 GPU 사양 영향을 크게 받습니다.

# 어떤 도구인가

Ollama의 장점은 모델 받아서 바로 돌리는 경험이 매우 짧다는 점입니다. 클라우드 API 대신 로컬에서 모델을 내려받아 채팅하거나, 로컬 OpenAI 호환 API처럼
연결하는 흐름까지 자연스럽게 이어집니다.

개념이나 비교 관점이 먼저 필요하면 [로컬 LLM 시작 가이드](/기타/local-llm-guide/)도 같이 보면 연결이 더 잘 됩니다. Ollama를 LM Studio, llama.cpp와 함께 비교해서 보고 싶다면 이 글이 연결됩니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [Ollama 공식 사이트](https://ollama.com/)
- 다운로드/접속 경로: [Ollama 다운로드 페이지](https://ollama.com/download)
- 공식 문서: [Ollama 모델 라이브러리](https://ollama.com/library)

# 지원 환경과 설치 방법

## Windows

Windows에서는 공식 다운로드 페이지에서 설치 파일을 받아 Desktop 앱처럼 설치하면 됩니다. 설치 후 백그라운드 서비스가 뜨면 `ollama` 명령과 모델
다운로드가 바로 이어집니다.

## macOS

macOS에서는 공식 `.dmg` 또는 패키지 경로로 설치하는 방식이 가장 간단합니다. Apple Silicon 환경에서는 로컬 추론 체감이 좋아서 입문용으로 특히 많이
쓰입니다.

## Linux

Linux는 공식 설치 스크립트인 `curl -fsSL https://ollama.com/install.sh | sh` 경로가 가장 빠릅니다. 서버 환경이라면 서비스 등록
여부와 GPU 드라이버 상태를 먼저 확인하는 편이 좋습니다.

# 기본 사용법

Ollama는 처음부터 큰 모델을 욕심내기보다, 작은 모델 하나를 내려받아 속도와 메모리 체감을 보는 쪽이 훨씬 실전적입니다. `pull`과 `run` 두 명령만 익혀도 로컬 러너로서의 성격이 금방 보입니다.

1. 설치가 끝나면 `ollama pull`로 원하는 모델을 먼저 내려받습니다.
2. `ollama run`으로 바로 대화하거나 테스트 프롬프트를 실행합니다.
3. 필요하면 로컬 API 엔드포인트를 다른 앱이나 WebUI, 에디터와 연결합니다.

```bash
ollama pull llama3.1
ollama run llama3.1
```

# 어떤 사람에게 잘 맞나

Ollama는 로컬 LLM을 최대한 적은 설정으로 돌리고 싶다는 사람에게 가장 먼저 추천할 만한 러너입니다. 코드 에디터, WebUI, 사내 실험 환경의 연결점으로도 많이
쓰입니다.

# 주의할 점

모델 크기에 비해 RAM, VRAM, 저장공간이 부족하면 첫인상이 나빠지기 쉽습니다. 특히 Windows 노트북이나 저용량 SSD 환경에서는 모델 크기를 보수적으로 고르는
편이 좋습니다.

# 요약

Ollama는 로컬 LLM 러너 중에서 가장 진입이 빠른 축에 속합니다. 공식 다운로드 페이지에서 설치한 뒤 `pull -> run` 두 단계만 익혀도 로컬 AI
워크플로우의 절반은 감이 잡힙니다.

# 참고 자료

- [Ollama](https://ollama.com/)
- [Download Ollama](https://ollama.com/download)
- [Install Ollama on Linux](https://ollama.com/download/linux)
- [Ollama Library](https://ollama.com/library)
