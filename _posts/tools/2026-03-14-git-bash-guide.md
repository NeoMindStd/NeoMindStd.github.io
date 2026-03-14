---
title:  "[Tools] Git Bash 설치와 사용법: Git for Windows로 가장 편하게 시작하기"
excerpt: "Git Bash를 Git for Windows 공식 배포판으로 설치하고, Windows에서 Git CLI를 쓰기 좋은 환경을 만드는 방법을 정리했습니다."
description: "Git Bash와 Git for Windows 공식 사이트, 다운로드 경로, 설치 방법, 기본 Git 사용 흐름을 설명한 가이드입니다."

categories:
  - Tools
tags:
  - Tools
  - Git Bash
  - Git
  - Windows
date: 2026-03-14 18:24:00 +09:00
permalink: /tools/git-bash-guide/
header:
  og_image: /assets/images/posts/tools/git-bash-guide/social.png
  teaser: /assets/images/posts/tools/git-bash-guide/social.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [Tools](/tools)

- - -

![Git Bash 개요](/assets/images/posts/tools/git-bash-guide/hero.svg)

![Git Bash ?? ??](/assets/images/posts/tools/git-bash-guide/logo.png)

# 무엇인가

Git Bash는 Windows에서 Git CLI를 비교적 자연스럽게 쓰게 해 주는 셸 환경입니다. 실제 설치는 Git for Windows 패키지로 이뤄지고, Git Bash는 그 안에 포함된 Bash 터미널이라고 보면 이해가 쉽습니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [Git Bash](https://gitforwindows.org/)
- 다운로드: [공식 다운로드 페이지](https://git-scm.com/download/win)

# 지원 OS와 설치 방법

## Windows

공식 다운로드 페이지에서 Windows용 설치 파일이나 패키지를 내려받아 설치합니다. 설치가 끝나면 첫 실행과 버전 확인을 한 번 진행하는 편이 좋습니다. 줄바꿈 변환과 PATH 노출 범위를 설치 시점에 잘 고르면 이후 마찰이 줄어듭니다.

## macOS

현재 공식 macOS 배포를 확인하기 어렵습니다. Git Bash 자체는 Windows용 구성입니다.

## Linux

현재 공식 Linux 배포를 확인하기 어렵습니다. Git Bash 자체는 Windows용 구성입니다.

# 기본 사용법

1. Git Bash를 열고 `git --version`으로 설치 상태를 먼저 확인합니다.
2. `git config --global user.name`과 `user.email`을 설정해 작성자 정보를 넣습니다.
3. 저장소를 clone 하거나 init 한 뒤 add, commit, push 흐름을 Bash에서 익힙니다.

# 주의할 점

Windows 경로와 POSIX 경로를 섞어 쓰면 헷갈리기 쉽습니다. 특히 줄바꿈 자동 변환 옵션은 프로젝트 전체에 영향을 주니 설치 시점에 잘 정하는 편이 좋습니다.

# 요약

Git Bash는 Windows에서 Git CLI를 가장 부담 없이 시작하는 길입니다. 설치형 옵션 중 줄바꿈과 PATH 노출 범위를 잘 고르면 이후 마찰이 많이 줄어듭니다.

# 참고 자료

- [Git for Windows](https://gitforwindows.org/)
- [Git Download for Windows](https://git-scm.com/download/win)
- [Git 공식 다운로드](https://git-scm.com/downloads/)

- - -

 - [Tools](/tools)

- - -
