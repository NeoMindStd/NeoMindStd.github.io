---
title:  "[기타/AI] Claude Code 설치와 사용법: Anthropic 코딩 에이전트를 터미널에 붙이는 법"
excerpt: "Claude Code를 공식 quickstart 기준으로 설치하고, macOS/Linux/Windows(WSL)에서 첫 실행과 기본 워크플로우를 정리한 가이드입니다."
description: "Claude Code 공식 quickstart, 설치 스크립트와 npm/Homebrew 경로, WSL 지원, 기본 사용 흐름을 설명한 실전 글입니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - Claude
  - Claude Code
  - Anthropic
  - CLI
  - 코딩에이전트
date: 2026-03-14 19:47:00 +09:00
permalink: /기타/claude-code-setup-guide/
header:
  og_image: /assets/images/posts/etc/claude-code-setup-guide/official.png
  teaser: /assets/images/posts/etc/claude-code-setup-guide/official.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

![대표 이미지](/assets/images/posts/etc/claude-code-setup-guide/hero.svg)

![공식 페이지 이미지](/assets/images/posts/etc/claude-code-setup-guide/official.png)

# 어떤 도구인가

Claude Code는 긴 문맥과 설명형 협업 감각이 강한 코딩 에이전트입니다. 리포지토리 맥락을 읽고, 파일을 수정하고, 테스트를 돌리고, Memory와 Hooks 같은
요소까지 붙여 팀 워크플로우에 적응시키는 방식이 핵심입니다.

개념이나 비교 관점이 먼저 필요하면 [Claude Code란 무엇인가?](/기타/claude-code-guide/)도 같이 보면 연결이 더 잘 됩니다. 도구의 포지션과 철학을 먼저 읽고 싶다면 기존 개념 글이 배경이 됩니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [Claude Code 공식 문서](https://code.claude.com/docs/en/overview)
- 다운로드/접속 경로: [Claude Code Quickstart](https://code.claude.com/docs/en/quickstart)
- 공식 문서: [Claude Code Hooks 문서](https://code.claude.com/docs/en/hooks)

# 지원 환경과 설치 방법

## Windows

공식 quickstart 기준으로 Claude Code는 Windows에서 WSL을 통한 사용을 안내합니다. 순수 PowerShell보다 WSL을 기준으로 보는 편이
안전하고, 이후 Git과 셸 도구 연동도 더 자연스럽습니다.

## macOS

macOS는 설치 스크립트, npm, Homebrew 경로를 모두 공식 문서가 다룹니다. 가장 빠른 진입은 설치 스크립트이고, 패키지 관리 흐름을 선호하면 Homebrew나
npm 경로도 괜찮습니다.

## Linux

Linux는 설치 스크립트나 npm 경로가 가장 일반적입니다. 서버나 원격 개발 환경에서도 잘 맞지만, 셸 권한과 프로젝트 권한을 먼저 점검하는 편이 좋습니다.

# 기본 사용법

Claude Code는 설치 후 바로 Hooks와 Memory를 다 붙이기보다, 대화형 작업부터 안정시키는 편이 좋습니다. 리포지토리 하나를 골라 파일 탐색과 작은 수정, 테스트 실행이 자연스럽게 이어지는지부터 확인하면 이후 설정이 훨씬 쉬워집니다.

1. 공식 quickstart의 설치 스크립트 또는 npm, Homebrew 경로로 설치합니다.
2. 리포지토리 루트에서 `claude`를 실행하고, 작업 범위와 선호하는 명령 흐름을 정리합니다.
3. 작은 수정부터 맡기고 Memory와 Hooks 설정은 이후 단계에서 붙입니다.

```bash
curl -fsSL https://claude.ai/install.sh | bash
# 또는
npm install -g @anthropic-ai/claude-code
claude
```

# 어떤 사람에게 잘 맞나

Claude Code는 설명과 코드 이해를 함께 다루고 싶거나, 터미널 안에서 장문 컨텍스트 협업을 선호하는 사람에게 잘 맞습니다. 문서와 코드가 섞인 작업에서 특히
편합니다.

# 주의할 점

WSL 여부, 셸 권한, 훅 자동화 범위가 꼬이면 처음 체감이 생각보다 무거울 수 있습니다. 처음부터 모든 자동화를 붙이기보다, 대화형 사용부터 안정시키는 편이 좋습니다.

# 요약

Claude Code는 설치보다 워크플로우 적응력이 매력인 도구입니다. 공식 quickstart의 기본 설치를 따라간 뒤, 작은 코드 수정과 설명형 협업부터 시작하면 장점이
빨리 드러납니다.

# 참고 자료

- [Claude Code Overview](https://code.claude.com/docs/en/overview)
- [Claude Code Quickstart](https://code.claude.com/docs/en/quickstart)
- [Claude Code Memory](https://code.claude.com/docs/en/memory)
- [Claude Code Hooks](https://code.claude.com/docs/en/hooks)
