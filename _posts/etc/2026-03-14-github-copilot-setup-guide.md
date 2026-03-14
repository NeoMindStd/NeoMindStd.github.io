---
title:  "[기타/AI] GitHub Copilot 설치와 사용법: VS Code, JetBrains, 웹에서 바로 쓰기"
excerpt: "GitHub Copilot을 공식 문서 기준으로 설치하고, VS Code·JetBrains·Visual Studio·Xcode·Neovim 환경에서 어떻게 시작하면 좋은지 정리했습니다."
description: "GitHub Copilot 공식 문서, 설치 가능한 개발 환경, 브라우저와 에디터 사용 흐름, 기본 활용법을 설명한 가이드입니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - GitHub Copilot
  - VS Code
  - JetBrains
  - AI Coding
date: 2026-03-14 19:49:00 +09:00
permalink: /기타/github-copilot-setup-guide/
header:
  og_image: /assets/images/posts/etc/github-copilot-setup-guide/official.png
  teaser: /assets/images/posts/etc/github-copilot-setup-guide/official.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

![대표 이미지](/assets/images/posts/etc/github-copilot-setup-guide/hero.svg)

![공식 페이지 이미지](/assets/images/posts/etc/github-copilot-setup-guide/official.png)

# 어떤 도구인가

Copilot은 가장 넓은 툴 호환성이 강점입니다. 팀마다 에디터가 달라도 같은 서비스 계정과 정책으로 묶기 쉽고, 자동완성, 채팅, 요즘의 에이전트형 기능까지 하나의
축으로 이어집니다.

개념이나 비교 관점이 먼저 필요하면 [GitHub Copilot 완전정리](/기타/github-copilot-guide/)도 같이 보면 연결이 더 잘 됩니다. 제품 개념과 포지션을 먼저 읽고 싶다면 기존 글이 배경이 됩니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [GitHub Copilot 공식 페이지](https://github.com/features/copilot)
- 다운로드/접속 경로: [Copilot 확장 설치 문서](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension)
- 공식 문서: [GitHub Copilot 소개 문서](https://docs.github.com/en/copilot/get-started/what-is-github-copilot)

# 지원 환경과 설치 방법

## Windows

Windows에서는 VS Code, Visual Studio, JetBrains 계열 IDE에서 Copilot을 가장 자연스럽게 설치할 수 있습니다. 공식 문서는 환경별
확장 설치 경로를 따로 제공하니, 쓰는 IDE 기준으로 진입하는 편이 좋습니다.

대표적인 설치법 두 가지만 꼽으면 VS Code 확장 설치와 JetBrains 플러그인 설치입니다. VS Code에서는 확장 탭에서 `GitHub Copilot`을 설치하고, JetBrains에서는 Marketplace에서 같은 이름의 플러그인을 설치한 뒤 GitHub 로그인까지 마치면 됩니다.

## macOS

macOS에서는 VS Code, JetBrains뿐 아니라 Xcode와 Neovim 경로도 공식 문서가 안내합니다. 브라우저에서 GitHub Copilot Chat을 쓰는
방식과 로컬 IDE 확장을 같이 조합할 수도 있습니다.

가장 많이 쓰는 경로는 VS Code 확장 설치와 JetBrains Marketplace 플러그인 설치입니다. Xcode나 Neovim까지 바로 넓히기보다, 먼저 주력 에디터 하나에 붙이는 편이 훨씬 덜 헷갈립니다.

## Linux

Linux는 VS Code, JetBrains, Neovim 같은 교차 플랫폼 편집기 쪽이 핵심입니다. 서버 개발 환경이 많다면 브라우저 채팅보다 로컬 IDE 확장 중심으로
접근하는 편이 안정적입니다.

대표적으로는 VS Code 확장 설치와 Neovim 플러그인 설치를 많이 씁니다. GUI 편집기를 쓴다면 VS Code, 터미널 중심이면 `github/copilot.vim` 쪽부터 시작하는 편이 무난합니다.

# 기본 사용법

Copilot은 처음부터 여러 IDE에 동시에 붙이기보다, 가장 오래 쓰는 편집기 하나에서 먼저 익히는 편이 좋습니다. 자동완성과 Chat이 각각 어떤 상황에서 유용한지 감이 잡힌 뒤에 다른 에디터로 넓히는 쪽이 훨씬 덜 헷갈립니다.

1. 공식 설치 문서에서 자신의 IDE를 고른 뒤 확장을 설치합니다.
2. GitHub 계정으로 로그인하고, 자동완성과 Copilot Chat이 정상적으로 뜨는지 확인합니다.
3. 짧은 인라인 제안과 긴 대화형 요청을 구분해서 사용합니다.

# 어떤 사람에게 잘 맞나

Copilot은 특정 IDE에 올인하기보다 여러 편집기와 팀 표준을 함께 가져가야 하는 조직에 잘 맞습니다. 이미 GitHub 생태계를 쓰고 있다면 도입 장벽도 낮은
편입니다.

# 주의할 점

편집기별 기능 차이와 조직 정책 차이를 같이 봐야 합니다. 같은 Copilot이라도 VS Code, JetBrains, Visual Studio, Xcode 경험이 완전히
똑같지는 않기 때문에 기대치를 맞추는 편이 좋습니다.

# 요약

GitHub Copilot의 가장 큰 장점은 넓은 지원 환경입니다. 공식 설치 문서에서 자신의 IDE를 고르고, 자동완성과 채팅을 분리해서 익히면 훨씬 덜 헷갈립니다.

# 참고 자료

- [GitHub Copilot](https://github.com/features/copilot)
- [What is GitHub Copilot?](https://docs.github.com/en/copilot/get-started/what-is-github-copilot)
- [Install the GitHub Copilot extension](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension)
- [About Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)
