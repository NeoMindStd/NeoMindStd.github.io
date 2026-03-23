---
title: "로컬 LLM·셀프호스팅 허브"
permalink: /ai/local-llm/
layout: single
excerpt: "Ollama, LM Studio, Open WebUI, OpenClaw, Apple Silicon 메모리 구조처럼 로컬 LLM과 셀프호스팅 흐름을 모아둔 허브입니다."
description: "로컬 LLM 설치, 셀프호스팅 워크스페이스, Apple Silicon 메모리 구조까지 한 번에 볼 수 있는 NeoMind 허브 페이지입니다."
---

- - -

 - [AI 허브 전체 보기](/ai/)

- - -

# 로컬 LLM·셀프호스팅 허브

직접 모델을 내려받아 돌리거나, 개인 AI 워크스페이스를 셀프호스팅하는 흐름을 중심으로 정리했습니다.

### 빠른 선택 카드

<div class="nm-hub-pick-grid">
  <article class="nm-hub-pick-card">
    <h4><a href="/기타/ollama-guide/">터미널 중심으로 빠르게 시작</a></h4>
    <p>로컬 LLM을 가장 빠르게 체험하려면 Ollama부터 시작하는 편이 쉽고, API 기반 실험까지 바로 이어집니다.</p>
    <p class="nm-tools-badges">
      <span class="nm-tools-badge">난이도: 입문</span>
      <span class="nm-tools-badge">환경: Win/macOS/Linux</span>
      <span class="nm-tools-badge">추천: 개발자</span>
    </p>
  </article>
  <article class="nm-hub-pick-card">
    <h4><a href="/기타/lm-studio-guide/">GUI 중심으로 모델 바꿔보기</a></h4>
    <p>터미널보다 화면 기반 사용이 편하면 LM Studio가 진입 장벽이 낮고, 모델 교체와 성능 비교도 직관적입니다.</p>
    <p class="nm-tools-badges">
      <span class="nm-tools-badge">난이도: 입문</span>
      <span class="nm-tools-badge">환경: 데스크톱 앱</span>
      <span class="nm-tools-badge">추천: 일반 사용자</span>
    </p>
  </article>
  <article class="nm-hub-pick-card">
    <h4><a href="/기타/open-webui-guide/">셀프호스팅 워크스페이스 확장</a></h4>
    <p>개인/팀 단위로 여러 모델을 하나의 웹 UI에서 관리하고 싶다면 Open WebUI 흐름으로 확장하는 것이 좋습니다.</p>
    <p class="nm-tools-badges">
      <span class="nm-tools-badge">난이도: 중급</span>
      <span class="nm-tools-badge">환경: Docker/pip</span>
      <span class="nm-tools-badge">추천: 운영 사용자</span>
    </p>
  </article>
  <article class="nm-hub-pick-card">
    <h4><a href="/기타/apple-silicon-unified-memory-local-llm/">장비 한계부터 이해하기</a></h4>
    <p>맥 사용자라면 설치 전에 통합 메모리 구조와 모델 크기별 체감을 먼저 이해하면 시행착오를 줄일 수 있습니다.</p>
    <p class="nm-tools-badges">
      <span class="nm-tools-badge">난이도: 입문</span>
      <span class="nm-tools-badge">형식: 하드웨어 이해</span>
      <span class="nm-tools-badge">추천: macOS 사용자</span>
    </p>
  </article>
</div>

### 환경별 빠른 선택표

| 도구 | UI | 잘 맞는 환경 | 메모리/장비 감각 | 대표 글 |
|:--|:--|:--|:--|:--|
| Ollama | CLI | Windows / macOS / Linux | 터미널 중심, 빠른 시작 | [Ollama 설치와 사용법](/기타/ollama-guide/) |
| LM Studio | GUI | Windows / macOS / Linux | 데스크톱에서 모델을 쉽게 바꿔보는 용도 | [LM Studio 설치와 사용법](/기타/lm-studio-guide/) |
| Open WebUI | 웹 UI | Docker / pip 가능한 환경 | 여러 모델과 워크스페이스를 브라우저로 묶을 때 | [Open WebUI 설치와 사용법](/기타/open-webui-guide/) |
| OpenClaw | 채팅형 UI | 개인 AI 비서 흐름 | 채팅 앱 중심 자동화 감각 | [OpenClaw 설치와 사용법](/기타/openclaw-guide/) |
| Apple Silicon 맥 | 장비 관점 | macOS | 통합 메모리로 로컬 LLM 체감이 갈림 | [Apple Silicon 통합 메모리 글](/기타/apple-silicon-unified-memory-local-llm/) |

### 추천 순서

1. 처음 로컬 LLM을 맛보려면 `Ollama` 또는 `LM Studio` 중 하나만 먼저 고릅니다.
2. `CLI/API 중심`이면 Ollama, `GUI 중심`이면 LM Studio가 더 편합니다.
3. 모델을 여러 명이 같이 쓰거나 개인 워크스페이스처럼 운영하려면 Open WebUI까지 확장합니다.
4. 맥 사용자라면 설치보다 먼저 `Apple Silicon 통합 메모리` 글을 보고 내 장비 한계를 이해하는 편이 훨씬 덜 헤맵니다.

### 먼저 비교할 글

 - [로컬 LLM 시작 가이드: Ollama, LM Studio, llama.cpp를 어떻게 고를까](/기타/local-llm-guide/)
 - [Apple Silicon 통합 메모리는 왜 로컬 LLM에 유리할까? VRAM 관점으로 이해하기](/기타/apple-silicon-unified-memory-local-llm/)
 - [램·SSD·M4 Mac mini는 왜 비싸게 느껴질까? AI 시대 메모리 가격의 이유](/기타/ai-memory-pricing-m4-mac-mini/)

### 설치와 운영 가이드

 - [Ollama 설치와 사용법: Windows, macOS, Linux에서 로컬 LLM 바로 돌리기](/기타/ollama-guide/)
 - [LM Studio 설치와 사용법: 데스크톱에서 로컬 AI 모델을 가장 쉽게 다루는 법](/기타/lm-studio-guide/)
 - [Open WebUI 설치와 사용법: Docker와 pip로 셀프호스팅 AI 워크스페이스 만들기](/기타/open-webui-guide/)
 - [OpenClaw 설치와 사용법: 개인 AI 비서를 채팅 앱에 붙이는 법](/기타/openclaw-guide/)

### 같이 보면 좋은 개념 글

 - [RAG란 무엇인가? 검색, 파인튜닝, 메모리와 어떻게 다른가](/기타/what-is-rag/)
 - [MCP란 무엇인가? AI 에이전트의 USB-C를 이해하는 가장 쉬운 설명](/기타/what-is-mcp/)
 - [CLI란 무엇인가? 개발자와 AI 에이전트가 터미널을 사랑하는 이유](/기타/what-is-cli/)

- - -

 - [AI 허브 전체 보기](/ai/)

- - -
