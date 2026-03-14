---
title:  "[Tools] SourceTree 설치와 사용법: 공식 다운로드부터 GUI Git 흐름까지"
excerpt: "SourceTree를 공식 사이트에서 설치하고, clone·stage·commit·push까지 기본 Git GUI 흐름을 정리했습니다."
description: "SourceTree 공식 사이트와 다운로드 경로, Windows/macOS 설치 방법, 기본 사용법을 정리한 글입니다."

categories:
  - Tools
tags:
  - Tools
  - SourceTree
  - Git
  - Windows
  - macOS
date: 2026-03-14 18:26:00 +09:00
permalink: /tools/sourcetree-guide/
header:
  og_image: /assets/images/posts/tools/sourcetree-guide/social.png
  teaser: /assets/images/posts/tools/sourcetree-guide/social.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [Tools](/tools)

- - -

![SourceTree 개요](/assets/images/posts/tools/sourcetree-guide/hero.svg)

![Sourcetree ?? ??](/assets/images/posts/tools/sourcetree-guide/logo.png)

![SourceTree 공식 이미지](/assets/images/posts/tools/sourcetree-guide/official.png)

# 무엇인가

SourceTree는 Atlassian 계열의 Git GUI 도구로, 커밋 그래프와 스테이징 흐름을 눈으로 확인하기 좋습니다. Git 초보자에게는 터미널보다 진입 장벽이 낮고, 숙련자에게도 병합 상태를 시각적으로 읽기 편합니다.

# 공식 사이트와 다운로드 경로

- 공식 홈페이지 & 다운로드: [SourceTree](https://www.sourcetreeapp.com/)

# 지원 OS와 설치 방법

## Windows

공식 다운로드 페이지에서 Windows용 설치 파일이나 패키지를 내려받아 설치합니다. 설치가 끝나면 첫 실행과 버전 확인을 한 번 진행하는 편이 좋습니다. 내장 Git 사용 여부와 계정 연결 방식을 처음에 정리하면 이후가 편합니다.

## macOS

공식 다운로드 페이지에서 macOS용 패키지를 내려받아 설치합니다. Apple Silicon/Intel 구분과 보안 경고 처리 여부를 먼저 확인하는 편이 좋습니다. 키체인과 SSH 키 연동을 초기에 정리해 두면 좋습니다.

# 기본 사용법

1. 저장소를 Clone 하거나 로컬 폴더를 Add 해서 파일 변경 목록을 확인합니다.
2. 변경 파일을 Stage 한 뒤 커밋 메시지를 작성하고 로컬 커밋을 만듭니다.
3. 브랜치를 전환하거나 Pull/Push/Fetch를 실행하며 원격 저장소와 상태를 맞춥니다.

# 주의할 점

SourceTree도 Git 개념을 모르고 쓰면 실수는 그대로 납니다. reset, discard, rebase 같은 작업은 GUI 버튼이 친절해 보여도 결과는 되돌리기 어려울 수 있습니다.

# 요약

SourceTree는 Git을 시각적으로 다루는 데 강한 GUI 도구입니다. Clone, Stage, Commit, Push 흐름부터 익히고, 위험한 히스토리 수정 작업은 의미를 이해한 뒤 쓰는 것이 맞습니다.

# 참고 자료

- [SourceTree 공식 사이트](https://www.sourcetreeapp.com/)
- [SourceTree Support](https://support.atlassian.com/sourcetree/)

- - -

 - [Tools](/tools)

- - -
