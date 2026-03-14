---
title:  "[Tools] Python 설치와 사용법: 공식 다운로드부터 가상환경까지"
excerpt: "Python을 공식 사이트에서 설치하고, PATH 설정, pip, venv까지 처음 세팅할 때 필요한 핵심만 정리했습니다."
description: "Python 공식 다운로드 경로, Windows/macOS/Linux 설치 방법, pip와 venv 사용법을 정리한 가이드입니다."

categories:
  - Tools
tags:
  - Tools
  - Python
  - Windows
  - macOS
  - Linux
  - pip
date: 2026-03-14 18:19:00 +09:00
permalink: /tools/python-guide/
header:
  og_image: /assets/images/posts/tools/python-guide/social.png
  teaser: /assets/images/posts/tools/python-guide/social.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [Tools](/tools)

- - -

![Python 개요](/assets/images/posts/tools/python-guide/hero.svg)

![Python ?? ??](/assets/images/posts/tools/python-guide/logo.png)

![Python 공식 이미지](/assets/images/posts/tools/python-guide/official.png)

# 무엇인가

Python은 범용성이 매우 높은 언어라서 설치 직후 무엇을 하느냐가 사람마다 다릅니다. 그래도 공통적으로 중요한 건 공식 배포판 설치, PATH 정리, 패키지 관리, 가상환경 분리입니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [Python](https://www.python.org/)
- 다운로드: [공식 다운로드 페이지](https://www.python.org/downloads/)

# 지원 OS와 설치 방법

## Windows

공식 다운로드 페이지에서 Windows용 설치 파일이나 패키지를 내려받아 설치합니다. 설치가 끝나면 첫 실행과 버전 확인을 한 번 진행하는 편이 좋습니다. 설치 시작 화면에서 Add Python to PATH를 먼저 확인하는 편이 좋습니다.

## macOS

공식 다운로드 페이지에서 macOS용 패키지를 내려받아 설치합니다. Apple Silicon/Intel 구분과 보안 경고 처리 여부를 먼저 확인하는 편이 좋습니다. 시스템 기본 Python과 혼동하지 않도록 python3 기준으로 확인하는 편이 좋습니다.

## Linux

공식 다운로드 페이지나 공식 문서에서 Linux용 패키지와 배포판별 설치 방식을 확인합니다. 설치 후 CLI나 첫 실행 테스트로 정상 동작을 확인합니다. 패키지 관리자 설치와 별도 버전 관리 도구 중 어떤 흐름을 쓸지 먼저 정하는 편이 좋습니다.

# 기본 사용법

1. 터미널에서 버전을 확인한 뒤 `python -m venv .venv`로 가상환경을 만듭니다.
2. 가상환경을 활성화하고 pip install로 필요한 패키지를 설치합니다.
3. 간단한 스크립트를 실행해 인터프리터와 패키지 연동을 확인합니다.

# 주의할 점

Python은 설치보다 버전 충돌과 패키지 관리에서 더 자주 막힙니다. 시스템 전역 인터프리터를 여러 도구가 공유할수록 꼬이기 쉬우므로, 프로젝트마다 가상환경을 분리하는 습관이 중요합니다.

# 요약

Python은 공식 설치판 자체는 어렵지 않지만, 이후 운영은 pip와 venv가 사실상 핵심입니다. 첫날부터 가상환경을 기준으로 쓰면 훨씬 덜 헤맵니다.

# 참고 자료

- [Python 공식 사이트](https://www.python.org/)
- [Python Downloads](https://www.python.org/downloads/)
- [Using Python](https://docs.python.org/3/using/index.html)

- - -

 - [Tools](/tools)

- - -
