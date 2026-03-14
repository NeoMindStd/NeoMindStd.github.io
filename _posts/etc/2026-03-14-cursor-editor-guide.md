---
title:  "[기타/AI] Cursor 설치와 사용법: AI 에디터에서 Agent, Tab, Rules 제대로 쓰기"
excerpt: "Cursor를 공식 다운로드 페이지 기준으로 설치하고, Windows/macOS/Linux에서 Agent 모드와 Rules, 자동완성 흐름을 어떻게 쓰면 좋은지 정리했습니다."
description: "Cursor 공식 사이트, 다운로드 경로, 지원 OS, Agent와 Rules 중심의 기본 사용 흐름을 설명한 가이드입니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - Cursor
  - AI Editor
  - Code Editor
  - Agent
date: 2026-03-14 19:48:00 +09:00
permalink: /기타/cursor-editor-guide/
header:
  og_image: /assets/images/posts/etc/cursor-editor-guide/official.png
  teaser: /assets/images/posts/etc/cursor-editor-guide/official.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

![대표 이미지](/assets/images/posts/etc/cursor-editor-guide/hero.svg)

![Cursor ?? ??](/assets/images/posts/etc/cursor-editor-guide/logo.png)

![공식 페이지 이미지](/assets/images/posts/etc/cursor-editor-guide/official.png)

# 빠른 답

- Cursor는 VS Code에 가까운 작업감 위에 AI 에이전트를 얹은 에디터입니다.
- 핵심은 자동완성 하나보다 Agent, Chat, Rules를 조합해 코드베이스 작업 전체를 맡기는 데 있습니다.
- IDE 안에서 오래 머무는 개발자에게 특히 잘 맞고, 터미널 중심이면 Claude Code나 Codex CLI가 더 잘 맞을 수 있습니다.

# 어떤 도구인가

Cursor의 핵심은 단순 자동완성보다 Agent와 Rules 조합입니다. Tab은 속도를 올리고, Chat과 Agent는 문맥을 넓히고, Rules는 팀 규칙과 코딩
습관을 고정하는 식으로 역할을 나누는 편이 효율적입니다.

개념이나 비교 관점이 먼저 필요하면 [Cursor IDE 완전정리](/기타/cursor-ide-guide/)도 같이 보면 연결이 더 잘 됩니다. 기능 비교와 포지션 설명이 먼저 필요하면 기존 개념 글이 이어집니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [Cursor 공식 사이트](https://cursor.com/)
- 다운로드/접속 경로: [Cursor 다운로드 페이지](https://cursor.com/download)
- 공식 문서: [Cursor Agent 문서](https://docs.cursor.com/en/chat/agent)

# 지원 환경과 설치 방법

## Windows

Windows에서는 공식 다운로드 페이지에서 설치 파일을 받아 일반 IDE처럼 설치하면 됩니다. 기존 VS Code 사용 감각이 있어도 Cursor 쪽 Rules와
Agent 모드는 따로 익히는 편이 좋습니다.

## macOS

macOS에서도 공식 앱을 받아 설치하는 방식이 가장 단순합니다. 처음 실행 시 키보드 단축키, 터미널 통합, 기존 설정 가져오기 여부를 정리해 두면 적응이 빨라집니다.

## Linux

Linux 역시 공식 다운로드 페이지에서 제공하는 패키지로 설치할 수 있습니다. 원격 개발과 SSH 흐름을 함께 쓰는 경우엔 에디터보다 백엔드 권한과 환경 구성이 더
중요합니다.

# 기본 사용법

Cursor는 처음부터 모든 AI 기능을 켜기보다, Rules와 Tab, Agent의 역할을 나눠서 익히는 편이 좋습니다. 짧은 보완은 Tab과 Inline에 맡기고, 여러 파일이 걸린 수정만 Agent에 넘기는 습관을 들이면 훨씬 덜 산만합니다.

1. 공식 다운로드 페이지에서 OS에 맞는 앱을 설치합니다.
2. 프로젝트를 연 뒤 Rules를 먼저 정리하고, 짧은 작업은 Tab과 Inline, 긴 작업은 Agent에 맡깁니다.
3. Background Agent나 Docs 연결 같은 고급 기능은 기본 흐름이 안정된 뒤 확장합니다.

# 어떤 사람에게 잘 맞나

Cursor는 IDE 안에서 AI를 가장 적극적으로 쓰고 싶다는 사람에게 잘 맞습니다. 특히 에디터를 중심으로 작업하고, 터미널 에이전트보다 GUI 감각을 선호하는
개발자에게 강합니다.

# 주의할 점

처음부터 모든 기능을 켜면 오히려 산만해질 수 있습니다. Rules 없이 Agent만 쓰면 일관성이 떨어지고, 반대로 Rules만 세게 잡으면 답답해질 수 있어서 균형이
중요합니다.

# 요약

Cursor는 좋은 자동완성 도구라기보다, 에디터 안에 에이전트 워크플로우를 심은 제품에 가깝습니다. 설치 후에는 Tab보다 Rules와 Agent 역할 분담을 먼저 잡는
편이 훨씬 효율적입니다.

# 참고 자료

- [Cursor](https://cursor.com/)
- [Cursor Download](https://cursor.com/download)
- [Cursor Agent Docs](https://docs.cursor.com/en/chat/agent)
- [Cursor Rules Docs](https://docs.cursor.com/en/context/rules)
