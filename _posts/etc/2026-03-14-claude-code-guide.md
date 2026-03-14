---
title:  "[기타/AI] Claude Code란 무엇인가? 터미널에서 움직이는 코딩 에이전트 이해하기"
excerpt: "Anthropic의 Claude Code가 단순 채팅이 아니라 터미널 중심 코딩 에이전트라는 점과, 메모리·훅·MCP 흐름까지 정리했습니다."
description: "Claude Code의 개념, 터미널 기반 작업 방식, 코드 검색·수정·테스트·커밋 흐름, 메모리와 hooks, MCP 연결 지점을 2026-03-14 기준으로 설명합니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - Claude
  - Claude Code
  - 코딩에이전트
date: 2026-03-14 14:19:00 +09:00

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

![](/assets/images/posts/etc/claude-code-guide/hero.svg)

`Claude Code`는 Anthropic이 제공하는 터미널 기반 코딩 에이전트입니다.  
핵심은 "Claude를 터미널에서 쓴다"가 아니라,  
**터미널이라는 개발자 작업 표면 위에서 코드 탐색, 수정, 테스트, 커밋 흐름을 자연스럽게 연결한다**는 점입니다.

![](/assets/images/posts/etc/claude-code-guide/claude-code-official.png)

_Anthropic Claude Code 공식 문서의 대표 이미지_

# Claude Code를 한 줄로 보면

Anthropic 공식 문서 표현을 따르면 Claude Code는 terminal-based agentic coding tool입니다.  
공식 소개에서도 아래 작업을 직접 언급합니다.

- 코드 검색
- 파일 수정
- 테스트 작성/실행
- 커밋 및 푸시

즉 단순 질답형 챗봇보다, 실제 개발 루프에 더 가까운 도구입니다.

# 왜 터미널 기반이 중요한가

개발자 워크플로우의 핵심 도구들은 대부분 터미널과 잘 맞습니다.

- `git`
- `pytest`
- `npm`
- `uv`
- `docker`

Claude Code는 바로 이 생태계 안에 들어옵니다.  
즉 IDE를 버리라는 뜻이 아니라, **기존 CLI 도구 흐름에 에이전트를 자연스럽게 얹는다**는 장점이 있습니다.

# Claude Code의 강점

## 1) 작업 단위가 선명하다

리포지토리 안에서 "이 파일을 찾고, 수정하고, 테스트를 돌리고, 결과를 알려줘" 같은 요청과 잘 맞습니다.

## 2) 문서와 코드 동시 작업이 자연스럽다

Claude 계열은 원래 긴 문맥과 문서 설명이 강점인 편이라,  
코드와 설명을 함께 다룰 때 체감이 좋은 경우가 많습니다.

## 3) 메모리와 hooks 개념이 붙는다

Anthropic 공식 문서는 `memory`와 `hooks`를 별도 개념으로 다룹니다.  
즉 단순히 답변만 생성하는 게 아니라,  
반복 작업 패턴과 사전/사후 동작까지 구조화해 갈 수 있습니다.

# Memory와 Hooks는 왜 중요한가

## Memory

프로젝트나 사용자 선호를 계속 기억하게 해 주는 축입니다.  
예를 들어:

- 이 저장소는 어떤 테스트를 먼저 돌리는가
- 어떤 응답 형식을 선호하는가

## Hooks

특정 시점에 자동으로 동작을 연결하는 장치입니다.  
예를 들어:

- 작업 전 점검
- 작업 후 포맷팅/검증
- 특정 명령 전후 로깅

즉 Claude Code는 "한 번 잘 답하는 도구"가 아니라,  
**점점 팀 작업 방식에 적응하는 에이전트 도구**로 확장되기 좋습니다.

# MCP와도 잘 맞는 이유

Claude Code 자체만으로도 강력하지만, 외부 도구를 붙여야 생산성이 확 올라갑니다.  
그래서 MCP와 잘 연결됩니다.

이 조합이 좋은 이유는 단순합니다.

1. Claude Code는 작업 오케스트레이션에 강하다
2. MCP는 외부 도구 연결 규약을 제공한다

즉 `생각하는 모델 + 실행 가능한 도구 표면`이 연결되는 구조가 됩니다.

# 어떤 사람에게 잘 맞나

추천되는 경우:

- 터미널과 Git에 익숙하다
- 긴 설명과 코드 이해를 함께 원한다
- 반복 작업을 메모리/훅으로 다듬고 싶다

다른 도구가 더 나을 수 있는 경우:

- 완전히 GUI 중심으로만 일하고 싶다
- 채팅창 하나로만 끝나는 경험을 원한다
- 세밀한 에디터 UX가 더 중요하다

# Claude Code와 다른 도구를 비교하면

간단히 느낌을 구분하면 이렇습니다.

- `Codex`: 클라우드 샌드박스 기반 작업형 경험이 강함
- `Claude Code`: 터미널 기반 협업형 코딩 감각이 강함
- `Cursor`: 에디터 중심 경험이 강함
- `Copilot`: GitHub 생태계와 조직 단위 연결이 강함

정답은 하나가 아니라, **자기 워크플로우와 어디가 가장 잘 붙는지**입니다.

# 한 줄 정리

Claude Code는 "Claude를 개발에 쓴다"보다  
**터미널 위에서 움직이는 장기 호흡형 코딩 에이전트**로 이해하는 편이 맞습니다.

# 요약

Claude Code는 터미널 위에서 코드 검색, 수정, 테스트, 메모리와 hooks까지 묶는 작업형 도구입니다. CLI 중심 개발자라면 긴 호흡의 협업 감각과 반복 작업 구조화 측면에서 특히 매력적인 선택지가 됩니다.

# 참고 자료

- [Claude Code 개요](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code 메모리](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Claude Code hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)

# 관련 글

- [MCP란 무엇인가? AI 에이전트의 USB-C를 이해하는 가장 쉬운 설명](/기타/what-is-mcp/)
- [CLI란 무엇인가? 개발자와 AI 에이전트가 터미널을 사랑하는 이유](/기타/what-is-cli/)
- [GPT Codex란 무엇인가? Codex 앱, CLI, 클라우드 샌드박스까지](/기타/gpt-codex-guide/)
- [Cursor IDE 완전정리: Rules, Background Agents, Tab 경험은 무엇이 다른가](/기타/cursor-ide-guide/)

- - -

 - [기타](/etc)

- - -
