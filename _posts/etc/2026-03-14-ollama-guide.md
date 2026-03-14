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
---

- - -

 - [기타](/etc)

- - -

![대표 이미지](/assets/images/posts/etc/ollama-guide/hero.svg)

![공식 페이지 이미지](/assets/images/posts/etc/ollama-guide/official.png)

# 어떤 도구인가

Ollama의 장점은 모델 받아서 바로 돌리는 경험이 매우 짧다는 점입니다. 클라우드 API 대신 로컬에서 모델을 내려받아 채팅하거나, 로컬 OpenAI 호환 API처럼
연결하는 흐름까지 자연스럽게 이어집니다.

개념이나 비교 관점이 먼저 필요하면 [로컬 LLM 시작 가이드](/기타/local-llm-guide/)도 같이 보면 연결이 더 잘 됩니다. Ollama를 LM Studio, llama.cpp와 함께 비교해서 보고 싶다면 이 글이 연결됩니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [https://ollama.com/](https://ollama.com/)
- 다운로드/접속 경로: [https://ollama.com/download](https://ollama.com/download)
- 공식 문서: [https://ollama.com/library](https://ollama.com/library)

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

Ollama의 장점은 모델 받아서 바로 돌리는 경험이 매우 짧다는 점입니다. 클라우드 API 대신 로컬에서 모델을 내려받아 채팅하거나, 로컬 OpenAI 호환 API처럼
연결하는 흐름까지 자연스럽게 이어집니다.

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
