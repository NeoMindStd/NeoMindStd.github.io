---
title:  "[기타/AI] LM Studio 설치와 사용법: 데스크톱에서 로컬 AI 모델을 가장 쉽게 다루는 법"
excerpt: "LM Studio를 공식 다운로드 페이지 기준으로 설치하고, Windows/macOS/Linux에서 모델 탐색·다운로드·채팅·로컬 서버까지 이어지는 흐름을 정리했습니다."
description: "LM Studio 공식 사이트, 다운로드 경로, 지원 OS, 모델 카탈로그와 로컬 서버 사용 흐름을 설명한 실전 가이드입니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - LM Studio
  - Local LLM
  - Desktop AI
  - Windows
  - macOS
  - Linux
date: 2026-03-14 19:42:00 +09:00
permalink: /기타/lm-studio-guide/
header:
  og_image: /assets/images/posts/etc/lm-studio-guide/official.png
  teaser: /assets/images/posts/etc/lm-studio-guide/official.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

![대표 이미지](/assets/images/posts/etc/lm-studio-guide/hero.svg)

![공식 페이지 이미지](/assets/images/posts/etc/lm-studio-guide/official.png)

# 어떤 도구인가

LM Studio는 CLI보다 GUI가 익숙한 사람에게 가장 편한 로컬 AI 앱입니다. 모델 카탈로그를 둘러보고, GGUF 계열 모델을 내려받고, 바로 채팅하거나 로컬 서버
모드로 다른 앱과 연결하는 흐름이 한 화면 안에서 정리됩니다.

개념이나 비교 관점이 먼저 필요하면 [Apple Silicon 통합 메모리와 로컬 LLM](/기타/apple-silicon-unified-memory-local-llm/)도 같이 보면 연결이 더 잘 됩니다. 맥에서 로컬 모델 체감이 왜 괜찮은지 궁금하면 이 글이 이어집니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [LM Studio 공식 사이트](https://lmstudio.ai/)
- 다운로드/접속 경로: [LM Studio 다운로드 페이지](https://lmstudio.ai/download)
- 공식 문서: [LM Studio 앱 문서](https://lmstudio.ai/docs/app)

# 지원 환경과 설치 방법

## Windows

Windows에서는 공식 다운로드 페이지에서 설치 프로그램을 내려받아 일반 데스크톱 앱처럼 설치하면 됩니다. GPU 설정과 저장 경로를 초기에 정리해 두면 이후 모델 관리가
훨씬 편해집니다.

## macOS

macOS에서도 공식 다운로드 페이지에서 Apple Silicon 또는 Intel용 앱을 내려받아 설치합니다. Apple Silicon 환경은 로컬 모델 체감이 좋아서 LM
Studio와 궁합이 좋은 편입니다.

## Linux

Linux는 공식 다운로드 페이지에서 AppImage나 배포 형식에 맞는 패키지를 받아 실행합니다. 데스크톱 중심 앱이라 원격 서버보다는 개인 워크스테이션에 더 잘
맞습니다.

# 기본 사용법

LM Studio는 Model Catalog, Chat, Local Server 세 화면만 익혀도 핵심 사용 흐름이 거의 끝납니다. 처음에는 모델 하나만 내려받아 채팅으로 성격을 보고, 그다음 필요할 때만 로컬 서버를 켜는 편이 덜 복잡합니다.

1. 앱을 설치한 뒤 Model Catalog에서 원하는 모델을 찾고 내려받습니다.
2. Chat 탭에서 바로 테스트하거나, Developers 메뉴의 로컬 서버 기능을 켭니다.
3. 필요하면 OpenAI 호환 엔드포인트 형태로 다른 앱과 연결합니다.

# 어떤 사람에게 잘 맞나

LM Studio는 터미널보다 데스크톱 앱이 편하고, 로컬 모델을 눈으로 보면서 관리하고 싶다는 사람에게 잘 맞습니다. 입문자도 모델, 메모리, 컨텍스트 길이 개념을
체감하기 쉽습니다.

# 주의할 점

GUI가 편하다고 해서 하드웨어 제약이 사라지지는 않습니다. 모델 파일 용량, 컨텍스트 길이, GPU와 메모리 사용량을 같이 보지 않으면 다운로드는 쉬워도 실행 체감이
나빠질 수 있습니다.

# 요약

LM Studio는 로컬 LLM 입문에서 가장 설명이 적게 필요한 도구 중 하나입니다. 공식 다운로드 페이지에서 앱을 설치하고, 모델 카탈로그와 로컬 서버 두 기능만 익혀도
활용 범위가 크게 넓어집니다.

# 참고 자료

- [LM Studio](https://lmstudio.ai/)
- [Download LM Studio](https://lmstudio.ai/download)
- [LM Studio App Docs](https://lmstudio.ai/docs/app)
- [LM Studio Local Server](https://lmstudio.ai/docs/app/api/local-server)
