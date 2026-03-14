---
title:  "[기타/AI] Gemini CLI 설치와 사용법: 터미널에서 구글 Gemini 에이전트 시작하기"
excerpt: "Gemini CLI를 공식 GitHub와 문서 기준으로 설치하고, Windows/macOS/Linux에서 인증·도구 사용·MCP 연결까지 시작하는 실전 가이드입니다."
description: "Gemini CLI 공식 저장소와 문서, 설치 경로, Google 계정 또는 API 키 인증, 지원 환경, 기본 사용 흐름을 정리한 글입니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - Gemini
  - Gemini CLI
  - CLI
  - Google AI
date: 2026-03-14 19:40:00 +09:00
permalink: /기타/gemini-cli-guide/
header:
  og_image: /assets/images/posts/etc/gemini-cli-guide/official.png
  teaser: /assets/images/posts/etc/gemini-cli-guide/official.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

![대표 이미지](/assets/images/posts/etc/gemini-cli-guide/hero.svg)

![공식 페이지 이미지](/assets/images/posts/etc/gemini-cli-guide/official.png)

# 어떤 도구인가

Gemini CLI는 터미널 한복판에서 프롬프트, 파일 작업, 셸 명령, 웹 가져오기, MCP 도구 연결을 같이 다루는 타입의 에이전트입니다. 코드베이스를 훑어보게 하거나,
작은 자동화 스크립트를 같이 다듬는 데 특히 잘 맞습니다.

개념이나 비교 관점이 먼저 필요하면 [2026 프론티어 모델 비교](/기타/frontier-models-comparison-2026/)도 같이 보면 연결이 더 잘 됩니다. Gemini 모델 계열 자체가 궁금하면 이 글도 같이 보면 좋습니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- 다운로드/접속 경로: [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- 공식 문서: [https://geminicli.com/docs/](https://geminicli.com/docs/)

# 지원 환경과 설치 방법

## Windows

Windows에서는 Node.js와 npm이 준비되어 있으면 `npx @google/gemini-cli`로 바로 실행하거나 `npm install -g
@google/gemini-cli`로 전역 설치할 수 있습니다. GUI 설치 마법사보다는 Node 생태계에 얹히는 방식이라, PowerShell이나 Windows
Terminal에서 쓰는 흐름에 더 자연스럽습니다.

## macOS

macOS에서는 `npm install -g @google/gemini-cli`로 설치할 수 있고, 공식 README 기준으로 Homebrew와 MacPorts 경로도
제공됩니다. 터미널 권한과 기본 셸 설정만 정리해 두면 바로 사용할 수 있습니다.

## Linux

Linux에서는 npm 전역 설치가 가장 단순하고, Homebrew를 쓰는 배포판이라면 `brew install gemini-cli` 경로도 가능합니다. 서버나 원격 개발
환경에서도 CLI라서 설정이 비교적 가볍습니다.

# 기본 사용법

Gemini CLI는 터미널 한복판에서 프롬프트, 파일 작업, 셸 명령, 웹 가져오기, MCP 도구 연결을 같이 다루는 타입의 에이전트입니다. 코드베이스를 훑어보게 하거나,
작은 자동화 스크립트를 같이 다듬는 데 특히 잘 맞습니다.

1. `npx @google/gemini-cli` 또는 전역 설치 후 `gemini`를 실행합니다.
2. 처음 실행에서 Google 계정 로그인 또는 `GEMINI_API_KEY` 기반 인증을 마칩니다.
3. 프로젝트 폴더에서 파일을 읽게 하거나 셸 명령을 제안받고, 필요한 경우 MCP 서버를 연결해 도구 범위를 넓힙니다.

```bash
npx @google/gemini-cli
# 또는
npm install -g @google/gemini-cli
gemini
```

# 어떤 사람에게 잘 맞나

Gemini CLI는 브라우저 탭이 아니라 터미널에서 바로 에이전트를 부리고 싶다는 사람에게 잘 맞습니다. 특히 긴 컨텍스트, Google 계정 기반 접근, 검색과 셸
명령을 한 흐름으로 잇고 싶은 개발자에게 장점이 큽니다.

# 주의할 점

권한을 준 디렉터리와 셸 명령 범위는 늘 의식해야 합니다. CLI 에이전트는 편하지만, 프로젝트 루트와 인증 키 관리가 느슨하면 실수도 빠르게 커집니다.

# 요약

Gemini CLI는 설치 자체보다 인증과 작업 범위를 어떻게 설계하느냐가 더 중요합니다. 공식 저장소와 문서를 기준으로 npm 또는 Homebrew 경로를 잡고, 먼저
작은 작업부터 맡기면서 감을 익히는 편이 좋습니다.

# 참고 자료

- [Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli)
- [Gemini CLI Docs](https://geminicli.com/docs/)
- [Gemini CLI Installation](https://geminicli.com/docs/get-started/installation/)
- [Gemini CLI Authentication](https://geminicli.com/docs/get-started/authentication/)
