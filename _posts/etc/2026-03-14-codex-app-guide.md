---
title:  "[기타/AI] GPT Codex 앱 사용 가이드: 브라우저, Windows 앱, IDE 확장까지"
excerpt: "OpenAI Codex를 브라우저와 Windows 앱, IDE 확장 관점에서 정리한 실전 가이드입니다. 설치가 필요한 곳과 접속만 하면 되는 곳을 구분해서 설명합니다."
description: "OpenAI Codex 앱의 공식 접속 경로, Windows 앱 가이드, VS Code와 JetBrains 확장 문서, 기본 작업 흐름을 정리한 글입니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - OpenAI
  - Codex
  - GPT Codex
  - Browser Agent
  - IDE
date: 2026-03-14 19:45:00 +09:00
permalink: /기타/codex-app-guide/
header:
  og_image: /assets/images/posts/etc/codex-app-guide/official.png
  teaser: /assets/images/posts/etc/codex-app-guide/official.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

![대표 이미지](/assets/images/posts/etc/codex-app-guide/hero.svg)

![공식 페이지 이미지](/assets/images/posts/etc/codex-app-guide/official.png)

# 어떤 도구인가

Codex 앱은 단순 채팅창보다 작업 단위 위임에 가까운 UI입니다. 이슈를 주고, 저장소 문맥을 읽게 하고, 결과와 diff를 검토한 뒤 IDE나 로컬 워크플로우로
이어받는 방식이 핵심입니다.

개념이나 비교 관점이 먼저 필요하면 [GPT Codex란 무엇인가?](/기타/gpt-codex-guide/)도 같이 보면 연결이 더 잘 됩니다. Codex의 제품 포지션과 CLI, 샌드박스 개념이 먼저 궁금하면 기존 글이 배경이 됩니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [Codex 앱 공식 문서](https://developers.openai.com/codex/app)
- 다운로드/접속 경로: [Codex 접속 경로](https://chatgpt.com/codex)
- 공식 문서: [Codex IDE 문서](https://developers.openai.com/codex/ide)

# 지원 환경과 설치 방법

## Windows

Windows에서는 공식 문서가 Codex app on Windows 가이드를 제공합니다. 브라우저 접속은 가장 빠른 경로이고, 앱 가이드를 따르면 Windows용 전용
흐름과 WSL2 연동까지 정리할 수 있습니다.

## macOS

macOS에서는 브라우저 접속이나 데스크톱 앱 경로를 통해 진입하는 방식이 자연스럽습니다. 로컬 에디터와 연결하려면 Codex IDE 문서를 같이 보는 편이 좋습니다.

## Linux

Linux는 브라우저 접속이 기본 경로입니다. 로컬 IDE와의 연결이 필요하면 VS Code나 JetBrains 쪽 공식 문서를 참고해 확장 기반으로 접근하는 편이
좋습니다.

# 기본 사용법

Codex 앱은 채팅창처럼 묻고 답하기보다 작업 단위를 맡기고 결과를 검토하는 흐름이 더 잘 맞습니다. 처음에는 리포지토리 전체 작업보다 작은 수정 한두 개를 태스크로 넘겨 보면서 결과 형식을 익히는 편이 좋습니다.

1. 브라우저에서 `chatgpt.com/codex`에 접속하거나 공식 문서의 앱 가이드를 따라 진입합니다.
2. 작업할 저장소나 환경을 연결하고, 할 일을 태스크 단위로 설명합니다.
3. 결과 diff와 로그를 검토한 뒤 IDE 확장이나 CLI로 이어 받아 후속 수정을 진행합니다.

# 어떤 사람에게 잘 맞나

Codex 앱은 로컬 터미널보다 브라우저나 IDE 중심으로 코딩 에이전트를 쓰고 싶다는 사람에게 맞습니다. 특히 작업 위임과 결과 검토 흐름을 분리하고 싶은 팀에 잘
맞습니다.

# 주의할 점

클라우드 측 작업 환경에 저장소 문맥과 권한을 넘기는 구조라서, 어떤 저장소를 연결하고 무엇을 읽게 하는지 항상 체크해야 합니다. 브라우저형 에이전트일수록 연결 권한과
데이터 흐름을 더 의식하는 편이 좋습니다.

# 요약

Codex 앱은 설치형 프로그램이라기보다 브라우저와 IDE를 잇는 작업형 코딩 에이전트 경험에 가깝습니다. 공식 앱, Windows, IDE 문서를 같이 보면 어떤 표면에서
써야 할지 감이 빨리 잡힙니다.

# 참고 자료

- [Codex App Docs](https://developers.openai.com/codex/app)
- [Codex on Windows](https://developers.openai.com/codex/app/windows)
- [Codex in IDEs](https://developers.openai.com/codex/ide)
- [Codex Access](https://chatgpt.com/codex)
