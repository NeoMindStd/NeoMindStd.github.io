---
title:  "[기타/AI] Brave Leo 사용법: 브라우저 안 AI 비서와 BYOM, Ollama 연결까지"
excerpt: "Brave Leo를 공식 페이지와 지원 문서 기준으로 정리한 가이드입니다. 지원 플랫폼, 기본 사용 흐름, BYOM과 Ollama 연결 포인트까지 함께 설명합니다."
description: "Brave Leo 공식 소개와 지원 문서, BYOM/Ollama 안내를 기준으로 Brave 브라우저 안 AI 비서를 어떻게 쓰는지 정리한 글입니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - Brave
  - Leo
  - Browser
  - Ollama
date: 2026-03-14 23:25:00 +09:00
permalink: /기타/brave-leo-guide/
header:
  og_image: /assets/images/posts/etc/brave-leo-guide/official.png
  teaser: /assets/images/posts/etc/brave-leo-guide/official.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
# shortterm-growth-enhancement: begin
quick_takeaways:
  - "Brave Leo는 AI 브라우저 중에서도 프라이버시와 BYOM 감각이 강한 편이라, 기존 브라우저 습관을 크게 버리지 않고 확장하기 좋습니다."
  - "Perplexity Comet처럼 브라우저 경험 전체를 바꾸는 쪽과는 결이 다르니, 내 사용 습관이 어디에 가까운지 먼저 보는 편이 좋습니다."
decision_table_title: "한눈에 고르기"
decision_table_headers:
  - "상황"
  - "먼저 보기"
decision_table_rows:
  - left: "기존 브라우저에 AI를 덧대는 감각"
    right: "Brave Leo"
  - left: "검색과 리서치를 AI 브라우저로 통합"
    right: "Perplexity Comet"
  - left: "Microsoft 계정·Windows 기본 흐름"
    right: "Edge Copilot Mode"
custom_next_reads_title: "이 글과 함께 보면 좋은 글"
custom_next_reads_intro: "지금 읽은 내용을 바로 확장하거나, 실제 선택과 설치까지 이어질 만한 글들만 골랐습니다."
custom_next_reads:
  - title: "AI 브라우저 비교"
    url: "/기타/ai-browser-comparison-2026/"
    note: "세 제품을 한 번에 비교할 때"
  - title: "Perplexity Comet 설치와 사용법"
    url: "/기타/perplexity-comet-guide/"
    note: "브라우저 자체가 더 바뀌는 대안"
  - title: "Ollama 설치와 사용법"
    url: "/기타/ollama-guide/"
    note: "BYOM 감각을 로컬 모델로 이어갈 때"
# shortterm-growth-enhancement: end
---

- - -

 - [기타](/etc)

- - -

![대표 이미지](/assets/images/posts/etc/brave-leo-guide/hero.svg)

![공식 로고](/assets/images/posts/etc/brave-leo-guide/logo.png)

![공식 페이지 이미지](/assets/images/posts/etc/brave-leo-guide/official.png)

# 어떤 서비스인가

Brave Leo는 Brave 브라우저 안에 붙어 있는 AI 비서입니다. 별도 사이트로 이동하지 않고 현재 탭, PDF, 검색 흐름 안에서 바로 질문하고 요약을 받는 경험이 핵심입니다.

[로컬 LLM 시작 가이드](/기타/local-llm-guide/)를 봤다면 알겠지만, Leo가 흥미로운 이유는 브라우저 안 AI이면서도 일부 흐름에서는 BYOM(Bring Your Own Model)과 Ollama 연결을 공식적으로 다룬다는 점입니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [Brave Leo](https://brave.com/leo/)
- 다운로드 경로: [Brave Browser 다운로드](https://brave.com/download/)
- 공식 문서: [What is Leo?](https://support.brave.com/hc/en-us/articles/18850147976461-What-is-Leo)
- BYOM/Ollama 문서: [How do I use Leo?](https://support.brave.com/hc/en-us/articles/4418164128269-How-do-I-use-Leo-Brave-s-integrated-AI-assistant-in-the-Brave-browser)

# 지원 환경과 시작 방법

공식 지원 문서 기준으로 Leo는 모든 데스크톱용 Brave 브라우저와 Android용 Brave, iOS 1.63 이상 Brave에서 사용할 수 있습니다. 다만 Ollama를 연결하는 BYOM 흐름은 데스크톱 Brave 1.82 이상과 Ollama 0.9 이상을 전제로 안내됩니다.

## Windows / macOS / Linux

데스크톱에서는 Brave 브라우저를 설치한 뒤 바로 Leo를 켤 수 있습니다. 웹페이지 요약과 PDF 질의응답, BYOM까지 포함하면 데스크톱이 가장 기능 폭이 넓습니다.

1. [Brave Browser](https://brave.com/download/)를 설치합니다.
2. 브라우저 우측 상단 또는 사이드 패널에서 Leo를 엽니다.
3. 현재 탭 요약, 질의응답, 번역 같은 기본 기능부터 써봅니다.
4. 더 깊게 쓰려면 Leo 설정에서 BYOM과 Ollama 연결을 검토합니다.

## Android

Android용 Brave에서도 Leo를 사용할 수 있습니다. 모바일에서는 빠른 요약과 검색형 질문에 특히 잘 맞습니다.

## iOS

공식 문서 기준으로 iOS에서는 Brave 1.63 이상에서 Leo 지원이 안내됩니다. 다만 데스크톱과 기능 폭이 완전히 같다고 기대하기보다, 모바일 친화적인 요약/질문 흐름 위주로 보는 편이 좋습니다.

# 기본 사용법

Leo는 "검색하려고 브라우저를 떠나는" 흐름을 줄이는 데 강합니다. 현재 열어 둔 페이지를 기준으로 바로 질문을 이어갈 수 있다는 점이 핵심입니다.

1. 웹페이지나 PDF를 연 상태에서 Leo를 엽니다.
2. 현재 페이지를 요약해 달라고 하거나, 핵심 포인트만 뽑아 달라고 요청합니다.
3. 필요한 경우 Leo Premium 모델이나 BYOM/Ollama를 연결해 응답 스타일을 조정합니다.

# 어떤 사람에게 잘 맞나

Leo는 브라우저를 바꾸는 부담은 적게 가져가고 싶지만, 웹페이지 요약과 질문은 자주 쓰는 사람에게 잘 맞습니다. 특히 프라이버시를 중요하게 보고, 로컬 모델 연결까지 탐색하고 싶다면 Perplexity Comet보다 Leo가 더 편할 수 있습니다.

# 주의할 점

BYOM과 Ollama 연결은 데스크톱 전용 안내에 가깝고, 기능도 브라우저 버전에 영향을 받습니다. 그래서 "모바일에서도 똑같이 되겠지"라고 보기보다, 기기별 기능 차이를 공식 지원 문서 기준으로 확인하는 편이 좋습니다.

# 요약

Brave Leo는 브라우저 안 AI 비서 중에서도 접근 장벽이 낮고, 프라이버시와 BYOM 확장성을 같이 챙길 수 있는 제품입니다. 그냥 AI 채팅창 하나가 아니라, 현재 페이지 문맥을 읽고 이어서 묻는 경험을 원한다면 특히 잘 맞습니다.

# 참고 자료

- [Brave Leo](https://brave.com/leo/)
- [Brave Download](https://brave.com/download/)
- [What is Leo?](https://support.brave.com/hc/en-us/articles/18850147976461-What-is-Leo)
- [Using Leo and BYOM](https://support.brave.com/hc/en-us/articles/4418164128269-How-do-I-use-Leo-Brave-s-integrated-AI-assistant-in-the-Brave-browser)
