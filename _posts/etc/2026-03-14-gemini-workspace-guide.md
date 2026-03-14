---
title:  "[기타/AI] Gemini in Docs, Sheets, Slides, Drive 사용법: Google Workspace AI를 어디까지 쓸 수 있나"
excerpt: "Google Workspace용 Gemini를 공식 블로그와 지원 문서 기준으로 정리한 가이드입니다. Docs, Sheets, Slides, Drive에서 무엇이 달라졌는지와 접근 경로를 함께 설명합니다."
description: "Google Workspace용 Gemini의 공식 업데이트와 지원 문서를 바탕으로 Docs, Sheets, Slides, Drive에서의 접근 경로와 활용 범위를 정리한 글입니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - Gemini
  - Google Workspace
  - Docs
  - Sheets
  - Slides
  - Drive
date: 2026-03-14 23:27:00 +09:00
permalink: /기타/gemini-workspace-guide/
header:
  og_image: /assets/images/posts/etc/gemini-workspace-guide/official.png
  teaser: /assets/images/posts/etc/gemini-workspace-guide/official.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
# shortterm-growth-enhancement: begin
quick_takeaways:
  - "문서 작성, 시트 정리, 슬라이드 초안이 많은 사람이라면 Gemini Workspace가 코딩 도구보다 훨씬 바로 체감되는 AI입니다."
  - "반대로 코드 수정이나 리포지토리 작업이 중심이라면 Gemini CLI나 Cursor 같은 도구가 더 직접적입니다."
decision_table_title: "한눈에 고르기"
decision_table_headers:
  - "상황"
  - "먼저 보기"
decision_table_rows:
  - left: "Docs, Sheets, Slides를 매일 씀"
    right: "Gemini Workspace 우선"
  - left: "터미널·리포지토리 작업이 더 많음"
    right: "Gemini CLI나 Cursor 검토"
  - left: "조사와 자료 수집 비중이 큼"
    right: "딥리서치나 AI 브라우저 흐름도 같이 보기"
custom_next_reads_title: "이 글과 함께 보면 좋은 글"
custom_next_reads_intro: "지금 읽은 내용을 바로 확장하거나, 실제 선택과 설치까지 이어질 만한 글들만 골랐습니다."
custom_next_reads:
  - title: "Gemini CLI 설치와 사용법"
    url: "/기타/gemini-cli-guide/"
    note: "개발자 워크플로까지 확장할 때"
  - title: "딥리서치란 무엇인가"
    url: "/기타/what-is-deep-research/"
    note: "문서 초안 이전 조사 단계"
  - title: "생성형 창작 AI 입문"
    url: "/기타/creative-ai-guide-2026/"
    note: "텍스트 밖 창작 도구까지 넓혀 볼 때"
# shortterm-growth-enhancement: end
---

- - -

 - [기타](/etc)

- - -

![대표 이미지](/assets/images/posts/etc/gemini-workspace-guide/hero.svg)

![공식 페이지 이미지](/assets/images/posts/etc/gemini-workspace-guide/official.png)

# 어떤 서비스인가

Gemini in Docs, Sheets, Slides, Drive는 별도 AI 앱이라기보다 Google Workspace 안에 스며든 보조 레이어에 가깝습니다. 문서 초안, 표 정리, 슬라이드 구성, Drive 파일 질의응답을 같은 생태계 안에서 이어 가는 게 핵심입니다.

2026년 3월 10일 Google 공식 블로그 업데이트도 이 네 표면을 중심으로 기능 확장을 설명합니다.

# 공식 사이트와 접속 경로

- 공식 사이트: [Google Workspace with Gemini](https://workspace.google.com/products/gemini/)
- 공식 업데이트: [Gemini updates to Docs, Sheets, Slides and Drive](https://blog.google/products-and-platforms/products/workspace/gemini-workspace-updates-march-2026/)
- Docs 지원 문서: [Gemini in Google Docs editors](https://support.google.com/docs/answer/14355406)
- Drive 지원 문서: [Use Gemini in Google Drive](https://support.google.com/drive/answer/14206169)

# 지원 환경과 접근 방식

이 제품은 설치형 앱이라기보다 Google Workspace 표면에서 활성화되는 기능에 가깝습니다. 그래서 접근 방법은 운영체제보다 계정과 구독, 그리고 사용하는 앱 표면이 더 중요합니다.

## Windows / macOS / Linux

데스크톱에서는 Chrome, Edge, Safari 같은 최신 브라우저에서 Docs, Sheets, Slides, Drive에 로그인해 사용하는 흐름이 기본입니다. 계정이 기능 롤아웃 대상이거나 플랜이 맞으면 패널 형태로 Gemini 기능을 바로 볼 수 있습니다.

## Android / iOS

모바일에서는 Google Docs, Sheets, Slides, Drive, Gmail 앱에서 일부 Gemini 기능이 순차적으로 보이는 구조입니다. 기능 폭은 데스크톱이 더 넓지만, 모바일은 빠른 요약과 후속 수정에 강합니다.

# 기본 사용법

처음부터 "모든 문서를 AI로 처리하겠다"보다, 반복되는 문서 작업 한두 가지를 줄이는 쪽이 체감이 큽니다.

1. Docs에서 초안 생성이나 문장 다듬기를 시도합니다.
2. Sheets에서 표 구조나 요약 포인트 정리를 맡깁니다.
3. Slides에서 발표 골격과 문장 흐름을 다듬습니다.
4. Drive에서 관련 파일을 찾아 문맥 질문을 던집니다.

# 어떤 사람에게 잘 맞나

Google Docs, Drive 중심으로 일하는 사람, 팀 문서와 자료가 이미 Google 생태계에 많은 사람에게 특히 잘 맞습니다. 반대로 로컬 도구나 데스크톱 IDE 중심 작업이 많다면 [Brave Leo](/기타/brave-leo-guide/)나 [Claude Code](/기타/claude-code-setup-guide/) 같은 도구가 더 직접적일 수 있습니다.

# 주의할 점

기능 사용 가능 여부는 계정, 요금제, 조직 정책에 따라 차이가 큽니다. 그래서 "블로그에서 봤는데 왜 안 보이지"보다, 내 Google 계정이 어느 플랜에 속하는지와 관리자가 어떤 기능을 열어 둔 상태인지 먼저 확인하는 편이 좋습니다.

# 요약

Gemini in Workspace는 별도 AI 앱을 추가하는 경험보다, 이미 쓰던 Docs/Sheets/Slides/Drive에 AI를 덧입히는 경험에 가깝습니다. 문서, 표, 슬라이드, 파일 검색이 모두 Google 쪽에 모여 있다면 가장 체감이 큰 생산성 AI 중 하나입니다.

# 참고 자료

- [Google Workspace with Gemini](https://workspace.google.com/products/gemini/)
- [Gemini updates to Docs, Sheets, Slides and Drive](https://blog.google/products-and-platforms/products/workspace/gemini-workspace-updates-march-2026/)
- [Use Gemini in Google Docs](https://support.google.com/docs/answer/14355406)
- [Use Gemini in Google Drive](https://support.google.com/drive/answer/14206169)
