---
title:  "[기타/AI] RAG란 무엇인가? 검색, 파인튜닝, 메모리와 어떻게 다른가"
excerpt: "RAG는 왜 아직도 AI 실무의 중심일까? 검색 증강 생성의 개념, 왜 2026년에도 핵심인지, 파인튜닝·메모리·긴 컨텍스트와 무엇이 다른지 2026-03-14 기준 공식 자료 중심으로 정리했습니다."
description: "RAG(Retrieval-Augmented Generation)의 개념, 어떻게 동작하는지, OpenAI Retrieval/File Search와 Google Vertex AI RAG Engine 같은 현재 제품 흐름, 그리고 파인튜닝·메모리·긴 컨텍스트와의 차이를 설명한 글입니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - LLM
  - RAG
  - Retrieval
  - Vector Store
date: 2026-03-14 17:44:00 +09:00
permalink: /기타/what-is-rag/
header:
  og_image: /assets/images/posts/etc/what-is-rag/social.png
  teaser: /assets/images/posts/etc/what-is-rag/social.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
# shortterm-growth-enhancement: begin
quick_takeaways:
  - "RAG는 최신 문서나 내부 자료를 모델 바깥에서 찾아 붙여 주는 방식이라, 문서가 자주 바뀌는 서비스에 특히 잘 맞습니다."
  - "모델 자체의 말투나 사고방식을 바꾸는 파인튜닝과는 목적이 다르기 때문에 둘을 섞어 생각하지 않는 편이 좋습니다."
decision_table_title: "한눈에 고르기"
decision_table_headers:
  - "상황"
  - "먼저 보기"
decision_table_rows:
  - left: "자주 바뀌는 문서와 정책을 반영"
    right: "RAG 우선 검토"
  - left: "말투, 출력 형식, 태스크 성향을 바꾸고 싶음"
    right: "파인튜닝 또는 프롬프트 설계 검토"
  - left: "대화 맥락을 누적 관리"
    right: "메모리 구조와 세션 설계까지 같이 보기"
custom_next_reads_title: "이 글과 함께 보면 좋은 글"
custom_next_reads_intro: "지금 읽은 내용을 바로 확장하거나, 실제 선택과 설치까지 이어질 만한 글들만 골랐습니다."
custom_next_reads:
  - title: "딥리서치란 무엇인가"
    url: "/기타/what-is-deep-research/"
    note: "검색과 조사 흐름까지 넓혀 볼 때"
  - title: "AI Eval이란 무엇인가"
    url: "/기타/what-is-ai-eval/"
    note: "RAG 품질 검증까지 이어서 볼 때"
  - title: "프롬프트 엔지니어링 가이드"
    url: "/기타/prompt-engineering-practical-guide/"
    note: "검색 없이도 품질을 올릴 때"
# shortterm-growth-enhancement: end
---

- - -

 - [기타](/etc)

- - -

![](/assets/images/posts/etc/what-is-rag/hero.svg)

# 빠른 답

- 최신 정보나 사내 문서처럼 모델 밖에 있는 지식을 써야 하면 여전히 RAG가 가장 실용적인 기본 해법입니다.
- 파인튜닝은 모델 습관을 바꾸는 데 가깝고, RAG는 필요한 문서를 질문 시점에 찾아 근거로 붙이는 구조라는 점이 핵심 차이입니다.
- 그래서 자주 바뀌는 문서, 출처가 중요한 답변, 내부 지식 검색에는 RAG가 여전히 강합니다.

요즘 AI를 이야기할 때 `RAG`는 이미 너무 많이 들어서 오히려 감이 흐려진 단어가 됐습니다.  
검색을 붙인다는 건 알겠는데, 막상 실무에 들어가면 자주 이런 질문이 나옵니다.

- 그냥 긴 문서를 통째로 넣으면 안 되나?
- 그럼 웹검색이랑 뭐가 다르지?
- 파인튜닝으로 해결하면 되는 것 아닌가?
- 메모리 기능이 있으면 RAG가 필요 없지 않나?

이 질문들이 자주 나오는 이유는,  
RAG가 단순히 "검색 기능 하나"가 아니라 **모델이 외부 지식을 다루는 전체 방식**과 맞물려 있기 때문입니다.

# RAG를 가장 짧게 설명하면

RAG는 `Retrieval-Augmented Generation`, 한국어로는 `검색 증강 생성`입니다.  
이름 그대로 **필요한 정보를 먼저 찾아서(retrieval), 그 정보를 바탕으로 답을 생성(generation)하는 방식**입니다.

핵심은 모델이 이미 알고 있는 것만으로 답하지 않고,  
**질문 시점에 외부 지식 베이스에서 관련 문서를 꺼내와서 근거로 삼는다**는 점입니다.

Lewis 외 연구진의 `2020-05-22` 논문은 이를 `parametric memory`와 `non-parametric memory`를 결합하는 방식으로 설명했습니다.  
요즘 실무에서는 이 개념이 더 단순화되어,  
"모델 바깥 문서를 찾아서 컨텍스트에 넣고 답하게 하는 구조"로 이해하는 편이 좋습니다.

![](/assets/images/posts/etc/what-is-rag/pipeline.svg)

# 왜 2026년에도 여전히 핵심인가

RAG는 새로운 유행어라기보다, 오히려 너무 오래 살아남아서 핵심이 된 개념에 가깝습니다.  
그 이유는 아주 현실적입니다.

- 회사 문서는 모델 학습 데이터에 없을 수 있다
- 최신 정보는 모델 파라미터에 바로 들어가지 않는다
- 출처가 필요한 답변은 근거 문서를 함께 봐야 한다
- 파인튜닝만으로는 자주 바뀌는 지식을 관리하기 어렵다

`2026-03-14` 기준으로도 주요 플랫폼은 모두 RAG 계열 기능을 별도 제품 축으로 두고 있습니다.

## OpenAI

OpenAI는 공식 Retrieval 가이드와 File Search 문서에서,  
벡터 스토어를 만들고 파일을 업로드하면 파일이 자동으로 `chunking`, `embedding`, `indexing`되어 검색 가능한 지식 베이스가 된다고 설명합니다.

즉 OpenAI도 RAG를 "직접 다 구현해야 하는 패턴"이 아니라,  
**플랫폼 차원에서 제공하는 기본 워크플로우**로 보고 있습니다.

## Google

Google Cloud는 `Vertex AI RAG Engine`을 별도 제품 이름으로 운영합니다.  
이건 단순 예제가 아니라, Google이 RAG를 엔터프라이즈급 워크로드에서 중요한 계층으로 보고 있다는 신호입니다.

## Anthropic

Anthropic Glossary는 RAG를 외부 지식 베이스나 문서를 컨텍스트 윈도우에 주입해  
응답을 근거에 더 가깝게 만드는 기법으로 설명합니다.  
Anthropic 문서에서 특히 중요한 포인트는, **RAG는 런타임에 데이터를 가져온다**는 점입니다.

즉 RAG는 아직도 "대체되기 전 기술"이 아니라,  
현재 AI 제품 구조에서 **지식을 연결하는 가장 현실적인 기본기**에 가깝습니다.

<p>
  <img src="/assets/images/posts/etc/frontier-models-comparison-2026/openai-official.png" width="220px" alt="OpenAI official image"/>
  <img src="/assets/images/posts/etc/frontier-models-comparison-2026/gemini-official.png" width="220px" alt="Google Gemini official image"/>
  <img src="/assets/images/posts/etc/claude-code-guide/claude-code-official.png" width="220px" alt="Anthropic Claude official image"/>
</p>

_RAG는 특정 벤더만의 패턴이 아니라 주요 AI 플랫폼이 공통으로 밀고 있는 연결 방식이다_

# RAG는 실제로 어떻게 동작하나

실무에서는 보통 이 순서로 생각하면 됩니다.

1. 문서를 잘게 나눈다
2. 각 조각을 임베딩한다
3. 벡터 스토어나 검색 인덱스에 저장한다
4. 질문이 들어오면 관련 조각을 검색한다
5. 찾은 조각을 프롬프트에 넣는다
6. 모델이 그 근거를 바탕으로 답한다

여기서 중요한 건 "모델이 검색을 이해한다"보다,  
**검색 품질이 답변 품질을 크게 좌우한다**는 점입니다.

그래서 RAG는 모델만 바꾸는 문제라기보다,

- chunking을 어떻게 할지
- metadata를 어떻게 붙일지
- 어떤 검색 전략을 쓸지
- 몇 개 문서를 넣을지
- 근거 인용을 어떻게 할지

같은 설계 문제가 함께 따라옵니다.

# 웹검색, 파인튜닝, 메모리와는 무엇이 다른가

이 부분이 제일 많이 헷갈립니다.

![](/assets/images/posts/etc/what-is-rag/compare.svg)

| 개념 | 무엇을 하는가 | 잘 맞는 문제 | 잘 안 맞는 문제 |
|:--|:--|:--|:--|
| RAG | 외부 문서를 런타임에 검색해 컨텍스트로 넣음 | 최신 지식, 사내 문서, 출처 기반 답변 | 모델 행동 자체를 바꾸는 일 |
| 웹검색 | 공개 웹에서 최신 정보를 찾아옴 | 최신 뉴스, 공개 정보 탐색 | 사내 문서, 비공개 지식 |
| 파인튜닝 | 모델 자체의 패턴과 행동을 추가 학습 | 말투, 형식, 특정 태스크 적응 | 자주 바뀌는 사실 업데이트 |
| 메모리 | 사용자/세션 정보를 지속적으로 유지 | 개인화, 장기 선호 기억 | 문서 지식 베이스 검색 |
| 긴 컨텍스트 | 한 번에 더 많은 텍스트를 읽음 | 문서 통째 요약, 짧은 기간의 큰 입력 | 반복 검색과 선택적 검색 |

즉 이들을 한 줄로 정리하면 대략 이렇습니다.

- `RAG`는 지식을 가져오는 방식
- `파인튜닝`은 모델 행동을 바꾸는 방식
- `메모리`는 사용자나 대화 이력을 유지하는 방식
- `긴 컨텍스트`는 한 번에 많이 읽는 방식

그래서 "메모리가 있으니 RAG가 필요 없다"거나  
"긴 컨텍스트가 크니 RAG는 끝났다"는 식의 말은 보통 과장입니다.

# 그럼 긴 컨텍스트가 커지면 RAG는 필요 없어지나

이 질문도 정말 자주 나옵니다.  
결론부터 말하면, **덜 필요해지는 영역은 있어도 완전히 사라지진 않습니다.**

긴 컨텍스트가 좋아하는 작업은 이런 것입니다.

- 문서 한두 개를 통째로 넣고 읽게 하기
- 긴 회의록, 긴 코드 파일 요약
- 이미 후보 문서가 정해진 상황에서 큰 입력 처리

반대로 RAG가 더 강한 작업은 이런 것입니다.

- 문서가 수천, 수만 개일 때
- 필요한 조각만 골라와야 할 때
- 자주 바뀌는 문서를 계속 반영해야 할 때
- 검색 결과를 메타데이터로 필터링해야 할 때

즉 긴 컨텍스트는 "한 번에 많이 읽는 능력"이고,  
RAG는 "많은 자료 중 필요한 걸 찾아오는 능력"입니다.  
둘은 경쟁자라기보다 자주 같이 씁니다.

# RAG가 잘 맞는 문제

RAG는 특히 아래에서 강합니다.

## 사내 문서 기반 QA

- 정책 문서
- 제품 매뉴얼
- 운영 위키
- 고객지원 FAQ

이런 건 모델이 원래 외우고 있길 기대하기보다,  
질문 시점에 근거 문서를 찾아 넣는 편이 훨씬 안전합니다.

## 최신성 중요한 답변

가격, 정책, 제품 사양처럼 자주 바뀌는 정보는  
파인튜닝보다 RAG가 관리하기 쉽습니다.

## 출처가 필요한 답변

어디서 왔는지 보여줘야 하는 시스템에서는  
RAG가 근거 문서를 함께 다루기 좋습니다.

## 특정 도메인 지식 연결

의료, 법률, 기업 내부 업무처럼  
특정 문서 집합에 기반해야 하는 답변은 RAG와 잘 맞습니다.

# 흔한 실패 이유

RAG를 붙였는데도 품질이 별로라는 팀은 꽤 많습니다.  
대개 문제는 "RAG를 썼다"가 아니라, **RAG 설계를 대충 했다**는 쪽에 가깝습니다.

## 문서 조각이 너무 크거나 너무 작다

chunk가 너무 크면 검색이 거칠어지고,  
너무 작으면 문맥이 끊깁니다.

## 검색이 맞는데 답변이 헛소리를 한다

검색 결과가 들어갔어도, 프롬프트가 약하면 모델이 근거보다 상상에 기대는 일이 생깁니다.

## 근거 문서가 좋은데 ranking이 나쁘다

좋은 문서가 저장돼 있어도, 항상 위에 올라오지 않으면 체감 품질이 나빠집니다.

## 최신 문서 업데이트가 늦다

업로드와 인덱싱 프로세스가 느리면  
RAG를 붙여도 오래된 답을 하게 됩니다.

## 평가를 안 한다

RAG는 "붙이면 좋아진다"가 아닙니다.  
검색 정확도, groundedness, citation quality, latency를 계속 봐야 합니다.

이 지점은 앞서 쓴 `AI Eval` 글과도 정확히 연결됩니다.

# 내 기준으로 가장 중요한 한 줄

RAG는 모델을 더 똑똑하게 만드는 기술이라기보다,  
**모델이 필요한 정보를 제때 찾아와서 헛소리 확률을 낮추는 운영 방식**에 가깝습니다.

그래서 RAG의 본질은 모델 교체보다도,

- 어떤 문서를 넣을지
- 어떻게 쪼갤지
- 무엇을 검색할지
- 어떻게 근거를 강제할지

를 설계하는 쪽에 있습니다.

이 관점으로 보면 RAG는 유행어가 아니라  
AI를 현실 데이터에 붙일 때 거의 반드시 부딪히는 기본기처럼 느껴집니다.

# 요약

RAG는 외부 문서를 런타임에 검색해 모델의 컨텍스트에 넣고 답하게 하는 방식입니다.  
`2020-05-22` 원 논문 이후 개념은 오래됐지만, `2026-03-14` 기준으로도 OpenAI Retrieval/File Search, Google Vertex AI RAG Engine, Anthropic 공식 문서가 모두 이를 핵심 패턴으로 다루고 있다는 점에서 여전히 실무 중심 기술입니다.

RAG는 웹검색, 파인튜닝, 메모리, 긴 컨텍스트와 비슷해 보이지만 역할이 다릅니다.  
최신 정보, 사내 문서, 출처 기반 답변에는 특히 강하고, 반대로 모델 행동 자체를 바꾸거나 개인화만 해결하는 용도로 쓰기엔 맞지 않습니다.  
결국 좋은 RAG는 모델보다도 검색 설계와 평가 체계가 좌우한다고 보는 편이 맞습니다.

# 참고 자료

- [OpenAI API: Retrieval](https://platform.openai.com/docs/guides/retrieval)
- [OpenAI API: File search](https://platform.openai.com/docs/guides/tools-file-search/)
- [Google Cloud: Vertex AI RAG Engine overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview)
- [Anthropic Glossary: RAG / Fine-tuning / Context window](https://docs.anthropic.com/en/docs/about-claude/glossary)
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)

# 관련 글

- [딥리서치란 무엇인가? AI가 답변을 넘어 조사하는 방식](/기타/what-is-deep-research/)
- [AI Eval이란 무엇인가? 벤치마크보다 중요한 실전 검증](/기타/what-is-ai-eval/)
- [프롬프트를 어떻게 써야 AI가 잘 일할까? 실전 프롬프트 엔지니어링 가이드](/기타/prompt-engineering-practical-guide/)
- [A2A란 무엇인가? MCP 다음에 이해해야 할 에이전트 간 통신 표준](/기타/what-is-a2a/)

- - -

 - [기타](/etc)

- - -
