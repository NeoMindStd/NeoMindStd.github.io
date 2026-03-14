---
title:  "[기타/AI] OpenClaw 설치와 사용법: 개인 AI 비서를 채팅 앱에 붙이는 법"
excerpt: "OpenClaw를 공식 사이트와 문서 기준으로 설치하고, Node 기반 온보딩과 Docker 경로, 채팅 채널 연결 흐름까지 정리했습니다."
description: "OpenClaw 공식 사이트, GitHub 릴리스, Node 22 기반 설치, `openclaw onboard` 초기 설정 흐름을 설명한 글입니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - OpenClaw
  - Personal AI
  - AI Assistant
  - Clawbot
date: 2026-03-14 19:44:00 +09:00
permalink: /기타/openclaw-guide/
header:
  og_image: /assets/images/posts/etc/openclaw-guide/official.png
  teaser: /assets/images/posts/etc/openclaw-guide/official.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

![대표 이미지](/assets/images/posts/etc/openclaw-guide/hero.svg)

![공식 페이지 이미지](/assets/images/posts/etc/openclaw-guide/official.png)

# 어떤 도구인가

OpenClaw는 IDE 안의 코딩 보조보다, 여러 채팅 채널과 음성 인터페이스에 걸친 개인 비서를 만드는 쪽에 가깝습니다. 즉 내 기기에서 돌아가고, 내가 쓰는 채팅
앱에서 응답하는 비서를 원하는 사람에게 맞는 도구입니다.

개념이나 비교 관점이 먼저 필요하면 [OpenClaw란 무엇인가?](/기타/openclaw-overview/)도 같이 보면 연결이 더 잘 됩니다. 도구의 철학과 구조를 먼저 보고 싶다면 기존 개념 글도 같이 보면 좋습니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [https://openclaw.ai](https://openclaw.ai)
- 다운로드/접속 경로: [https://github.com/openclaw/openclaw/releases](https://github.com/openclaw/openclaw/releases)
- 공식 문서: [https://docs.openclaw.ai/start/getting-started](https://docs.openclaw.ai/start/getting-started)

# 지원 환경과 설치 방법

## Windows

공식 README 기준으로 Windows는 WSL2 경로가 강하게 권장됩니다. Node 22 이상을 준비한 뒤 `npm install -g openclaw@latest`로
설치하고, 온보딩 마법사를 실행하는 쪽이 가장 안정적입니다.

## macOS

macOS는 Node 22 이상만 맞춰 두면 전역 npm 설치와 `openclaw onboard --install-daemon` 흐름이 매끄럽습니다. 개인용 항상 켜진 비서
느낌을 원할 때 잘 맞습니다.

## Linux

Linux는 npm 또는 pnpm 전역 설치와 Docker 경로를 모두 공식 문서가 다룹니다. 홈서버나 개인 VPS에 올릴 생각이라면 Docker 문서도 같이 보는 편이
좋습니다.

# 기본 사용법

OpenClaw는 IDE 안의 코딩 보조보다, 여러 채팅 채널과 음성 인터페이스에 걸친 개인 비서를 만드는 쪽에 가깝습니다. 즉 내 기기에서 돌아가고, 내가 쓰는 채팅
앱에서 응답하는 비서를 원하는 사람에게 맞는 도구입니다.

1. Node 22 이상 환경에서 `npm install -g openclaw@latest`로 설치합니다.
2. `openclaw onboard --install-daemon`을 실행해 게이트웨이, 워크스페이스, 모델 공급자, 채널 연결을 순서대로 설정합니다.
3. 설정이 끝나면 자주 쓰는 채팅 채널에서 비서를 호출하고, 필요하면 Docker 문서로 배포 구조를 확장합니다.

```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon
```

# 어떤 사람에게 잘 맞나

OpenClaw는 개인용 always-on 비서를 꾸미고 싶은 사람에게 흥미로운 선택지입니다. 메신저 중심 워크플로우, 멀티 채널, 장기 실행 서비스에 관심이 있다면 특히
매력이 있습니다.

# 주의할 점

연결 채널이 많아질수록 인증 정보와 권한 관리도 복잡해집니다. 채널 연동을 넓히기 전에 모델 키, 홈 디렉터리 권한, 로그 보존 범위를 먼저 정리하는 편이 안전합니다.

# 요약

OpenClaw는 일반적인 AI 채팅 앱보다 훨씬 개인 비서 운영에 가까운 도구입니다. 공식 Getting Started와 Docker 문서를 기준으로 작은 채널 하나부터
붙여 보면서 감을 잡는 편이 좋습니다.

# 참고 자료

- [OpenClaw Website](https://openclaw.ai)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [OpenClaw Releases](https://github.com/openclaw/openclaw/releases)
- [OpenClaw Getting Started](https://docs.openclaw.ai/start/getting-started)
- [OpenClaw Docker Install](https://docs.openclaw.ai/install/docker)
