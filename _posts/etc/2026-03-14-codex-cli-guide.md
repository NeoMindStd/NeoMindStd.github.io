---
title:  "[기타/AI] Codex CLI 설치와 사용법: 터미널에서 OpenAI 코딩 에이전트 시작하기"
excerpt: "Codex CLI를 공식 OpenAI 문서 기준으로 설치하고, macOS/Linux/Windows에서 인증과 첫 작업까지 이어지는 실전 가이드입니다."
description: "Codex CLI 공식 문서, npm 설치, ChatGPT 로그인 또는 API 키 인증, 기본 사용 흐름을 정리한 글입니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - OpenAI
  - Codex CLI
  - CLI
  - 코딩에이전트
date: 2026-03-14 19:46:00 +09:00
permalink: /기타/codex-cli-guide/
header:
  og_image: /assets/images/posts/etc/codex-cli-guide/official.png
  teaser: /assets/images/posts/etc/codex-cli-guide/official.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

![대표 이미지](/assets/images/posts/etc/codex-cli-guide/hero.svg)

![Codex CLI ?? ??](/assets/images/posts/etc/codex-cli-guide/logo.png)

![공식 페이지 이미지](/assets/images/posts/etc/codex-cli-guide/official.png)

# 어떤 도구인가

Codex CLI는 터미널에서 바로 코딩 에이전트를 부른다는 감각이 핵심입니다. OpenAI 공식 문서 기준으로 ChatGPT 계정 로그인 또는
`OPENAI_API_KEY` 인증을 택할 수 있고, 저장소 안에서 수정·테스트·요약 흐름을 이어갈 수 있습니다.

개념이나 비교 관점이 먼저 필요하면 [GPT Codex 앱 사용 가이드](/기타/codex-app-guide/)도 같이 보면 연결이 더 잘 됩니다. 브라우저와 IDE 표면, CLI 표면을 같이 비교하고 싶다면 이 글을 이어서 보면 좋습니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [Codex CLI 공식 문서](https://developers.openai.com/codex/cli)
- 다운로드/접속 경로: [Codex 개요 문서](https://developers.openai.com/codex)
- 공식 문서: [Codex 앱 문서](https://developers.openai.com/codex/app)

# 지원 환경과 설치 방법

## Windows

Windows도 공식 문서에서 지원 대상으로 다뤄집니다. Node와 npm이 준비되어 있으면 `npm i -g @openai/codex`로 설치하고, PowerShell이나
Windows Terminal에서 실행할 수 있습니다.

## macOS

macOS에서는 npm 전역 설치 후 바로 쓸 수 있습니다. 터미널, Git, 테스트 명령과 붙여 쓰는 흐름이 자연스러워서 로컬 개발용으로 진입하기 좋습니다.

## Linux

Linux 역시 npm 전역 설치가 기본 경로입니다. 원격 개발 환경이나 컨테이너 안에서도 비교적 가볍게 올릴 수 있어 CLI형 코딩 에이전트와 잘 맞습니다.

# 기본 사용법

Codex CLI는 설치 직후 큰 리팩터링보다 작은 수정 요청으로 시작하는 편이 안전합니다. 로그인이나 API 키 인증이 끝나면, 우선 테스트 가능한 간단한 수정 과제를 맡기고 diff와 로그를 읽는 감각부터 익히는 게 좋습니다.

1. `npm i -g @openai/codex`로 CLI를 설치합니다.
2. `codex`를 실행하고 ChatGPT 로그인 또는 API 키 인증을 마칩니다.
3. 프로젝트 폴더에서 수정 요청, 테스트 실행, diff 검토를 반복합니다.

```bash
npm i -g @openai/codex
codex
```

# 어떤 사람에게 잘 맞나

Codex CLI는 브라우저보다 터미널이 편하고, Git과 테스트 명령까지 한 흐름으로 엮고 싶은 개발자에게 잘 맞습니다. 기존 CLI 습관을 크게 바꾸지 않으면서
에이전트를 얹는 감각이 강합니다.

# 주의할 점

권한을 준 저장소에서 실제 명령이 돌아가는 만큼, 민감 파일과 실행 범위를 늘 체크해야 합니다. 특히 API 키 인증을 쓸 때는 로컬 셸 히스토리와 환경 변수 관리가
중요합니다.

# 요약

Codex CLI는 설치 자체는 간단하지만, 인증 방식과 작업 범위 설정이 사용성을 좌우합니다. 공식 CLI 문서 그대로 `npm 설치 -> 로그인 -> 작은 작업부터`
순서로 접근하면 시행착오가 적습니다.

# 참고 자료

- [Codex CLI](https://developers.openai.com/codex/cli)
- [Codex Overview](https://developers.openai.com/codex)
- [Codex App Docs](https://developers.openai.com/codex/app)
