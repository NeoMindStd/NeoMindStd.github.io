---
title:  "[기타/AI] MCP란 무엇인가? AI 에이전트의 USB-C를 이해하는 가장 쉬운 설명"
excerpt: "Model Context Protocol(MCP)이 왜 갑자기 중요해졌는지, 호스트·클라이언트·서버·툴 구조를 중심으로 쉽게 정리했습니다."
description: "MCP(Model Context Protocol)의 핵심 개념, host/client/server 구조, tool/resource/prompt 구분, 그리고 Codex·Claude Code·Copilot 같은 도구에서 왜 주목받는지 설명합니다."

categories:
  - 기타
tags:
  - 기타
  - AI
  - MCP
  - 에이전트
  - Tool Use
date: 2026-03-14 14:11:00 +09:00

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

![](/assets/images/posts/etc/what-is-mcp/hero.svg)

AI 에이전트 이야기를 하다 보면 `MCP 서버 붙였어요`, `MCP로 툴 연결했어요` 같은 말을 자주 듣게 됩니다.  
처음엔 뭔가 거대한 프레임워크처럼 들리지만, 핵심만 보면 생각보다 단순합니다.

MCP는 `Model Context Protocol`의 약자입니다.  
한마디로 말하면 **모델이 외부 도구와 맥락을 표준 방식으로 연결받기 위한 인터페이스 규약**입니다.

![](/assets/images/posts/etc/what-is-mcp/architecture.svg)

# 왜 갑자기 중요해졌나

LLM은 텍스트만으로도 강력하지만, 혼자서는 할 수 없는 일이 많습니다.

- 파일을 직접 읽기
- 데이터베이스 조회
- 브라우저 열기
- 이슈 트래커 확인
- 배포 도구 실행

예전에는 각 제품이 저마다 다른 플러그인 방식이나 자체 SDK를 만들었습니다.  
그러다 보니 도구 하나를 여러 에이전트에 붙일 때 중복 작업이 많았습니다.

MCP가 주목받는 이유는 이 지점을 표준화하려 하기 때문입니다.  
쉽게 말해 **"이 에이전트도, 저 에이전트도 같은 방식으로 도구를 연결하게 하자"**는 흐름입니다.

# 가장 쉬운 비유

MCP를 `USB-C`에 비유하면 이해가 쉽습니다.

- 노트북이 호스트
- USB-C 규격이 연결 방식
- 외부 장치가 서버
- 실제 장치 기능이 tool/resource

장치 종류는 다양해도, 연결 규약이 통일되면 호환성이 크게 올라갑니다.  
MCP도 비슷하게 에이전트와 도구 사이의 공통 언어 역할을 합니다.

# 핵심 구성요소

공식 문서 관점에서 이해할 때 중요한 축은 아래 정도입니다.

| 구성 | 역할 |
|:--|:--|
| Host | MCP를 사용하는 애플리케이션. 예: IDE, 에이전트 앱 |
| Client | Host 안에서 서버와 연결을 관리하는 쪽 |
| Server | tool/resource/prompt를 제공하는 쪽 |
| Tool | 모델이 호출할 수 있는 행동 |
| Resource | 모델이 참고할 수 있는 데이터나 문맥 |
| Prompt | 작업을 시작할 때 재사용 가능한 템플릿 |

실전에서는 보통 "에이전트가 MCP 서버에 연결해서 툴을 쓴다" 정도로 말하지만, 실제로는 이 구성이 한 세트로 움직입니다.

# Tool, Resource, Prompt는 어떻게 다른가

초반에 가장 헷갈리는 부분이 바로 여기입니다.

## Tool

실행 가능한 액션입니다.

- `create_issue`
- `search_docs`
- `run_test`
- `query_database`

즉 "무언가를 한다"에 가깝습니다.

## Resource

참고할 수 있는 데이터입니다.

- 설정 파일
- 문서
- 현재 워크스페이스 상태
- 리포지토리 메타데이터

즉 "읽을 수 있다"에 가깝습니다.

## Prompt

자주 쓰는 작업 문맥 템플릿입니다.

- 코드리뷰 시작 프롬프트
- 장애 분석 프롬프트
- 문서화 템플릿

즉 "이 일을 어떤 방식으로 시작할지"를 재사용하게 해 줍니다.

# 실제로 어디에 쓰이나

2026년 기준으로 MCP는 여러 에이전트 도구와 잘 맞는 개념이 됐습니다.

- GitHub Copilot은 로컬/원격 MCP 서버의 tool/resource를 연결하는 흐름을 공식 문서에서 다룹니다.
- OpenAI의 Apps SDK도 MCP 기반 도구 노출 개념을 사용합니다.
- Claude Code 역시 MCP 서버를 통해 외부 도구를 붙이는 흐름이 자연스럽습니다.

즉 MCP 자체가 모델은 아니지만, **에이전트 생태계를 묶는 접점**이 되고 있습니다.

# MCP가 해 주는 것과 안 해 주는 것

MCP를 처음 보면 "그럼 이걸 쓰면 에이전트가 똑똑해지는 건가?"라는 기대를 하게 됩니다.  
정확히 말하면 그렇지는 않습니다.

MCP가 해 주는 것:

- 도구 연결 표준화
- 문맥 주입 경로 정리
- 여러 도구 간 재사용성 향상

MCP가 자동으로 해결하지 않는 것:

- 인증/권한 설계 자체
- 보안 정책 자체
- 모델 품질 자체
- 잘못 만든 툴의 품질 문제

즉 MCP는 **배선 규약**이지, 모든 운영 문제를 해결하는 마법 지팡이는 아닙니다.

# 보안 관점에서 꼭 봐야 할 것

MCP를 붙인다는 것은 곧 모델이 외부 기능에 손을 뻗는다는 뜻입니다.  
그래서 아래 항목이 중요합니다.

1. 어떤 tool이 정말 필요한가
2. 읽기 전용과 쓰기 권한을 분리했는가
3. shell 실행이나 네트워크 호출 범위를 제한했는가
4. 민감 데이터가 resource로 과하게 노출되지 않는가
5. 감사 로그를 남길 수 있는가

도구를 많이 붙이는 것보다 **권한 경계를 잘 자르는 것**이 훨씬 중요합니다.

# 언제 도입하면 좋은가

아래 조건이면 MCP 도입 가치가 높습니다.

- 같은 도구를 여러 에이전트/IDE에서 재사용하고 싶다
- 내부 문서, 이슈 트래커, 배포 툴을 한데 엮고 싶다
- agent workflow를 플러그인 의존이 아니라 표준 인터페이스로 정리하고 싶다

반대로 툴이 하나뿐이고, 외부 연결도 거의 없다면 굳이 초기에 크게 도입하지 않아도 됩니다.

# 한 줄 정리

MCP는 "모델이 외부 세계와 연결되는 방식을 표준화하는 규약"입니다.  
에이전트 시대가 깊어질수록, 모델 성능만큼이나 **도구 연결 방식의 표준화**가 중요해지고 있습니다.

# 요약

MCP는 모델을 외부 도구와 표준 방식으로 연결하는 규약입니다. Host, Client, Server, Tool, Resource 구조와 권한 경계를 함께 이해하면 에이전트 확장성을 훨씬 안정적으로 가져갈 수 있습니다.

# 참고 자료

- [Model Context Protocol 공식 문서](https://modelcontextprotocol.io/docs/getting-started/intro)
- [MCP Architecture 공식 문서](https://modelcontextprotocol.io/docs/learn/architecture)
- [GitHub Copilot MCP 공식 문서](https://docs.github.com/en/copilot/how-tos/context/model-context-protocol)
- [OpenAI Apps SDK 소개](https://developers.openai.com/apps-sdk)

# 관련 글

- [CLI란 무엇인가? 개발자와 AI 에이전트가 터미널을 사랑하는 이유](/기타/what-is-cli/)
- [AI 에이전트의 Skill이란 무엇인가? 프롬프트 묶음이 아니라 실행 가능한 작업 단위](/기타/ai-agent-skills/)
- [GPT Codex란 무엇인가? Codex 앱, CLI, 클라우드 샌드박스까지](/기타/gpt-codex-guide/)
- [GitHub Copilot 완전정리: 인라인 완성에서 코딩 에이전트까지](/기타/github-copilot-guide/)

- - -

 - [기타](/etc)

- - -
