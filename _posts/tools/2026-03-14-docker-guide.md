---
title:  "[Tools] Docker 설치와 사용법: 공식 다운로드부터 첫 컨테이너 실행까지"
excerpt: "Docker Desktop을 공식 사이트에서 설치하고, Windows/macOS/Linux에서 첫 컨테이너와 이미지 흐름을 익히는 입문 가이드입니다."
description: "Docker와 Docker Desktop 공식 사이트, 다운로드 경로, 설치 방법, 기본 컨테이너 사용 흐름을 정리한 글입니다."

categories:
  - Tools
tags:
  - Tools
  - Docker
  - Container
  - Windows
  - macOS
  - Linux
date: 2026-03-14 18:16:00 +09:00
permalink: /tools/docker-guide/
header:
  og_image: /assets/images/posts/tools/docker-guide/social.png
  teaser: /assets/images/posts/tools/docker-guide/social.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
# shortterm-growth-enhancement: begin
quick_takeaways:
  - "로컬 개발 환경을 빠르게 맞추고 싶다면 Docker Desktop으로 시작하는 쪽이 가장 부담이 적습니다."
  - "초반에는 이미지, 컨테이너, 볼륨, 포트 매핑 순서만 이해해도 체감이 크게 좋아집니다."
decision_table_title: "한눈에 고르기"
decision_table_headers:
  - "상황"
  - "먼저 보기"
decision_table_rows:
  - left: "노트북에서 바로 개발 환경 재현"
    right: "Docker Desktop부터 시작"
  - left: "서버나 CI 같은 리눅스 환경 중심"
    right: "Engine/Compose 흐름까지 같이 보기"
  - left: "개발 툴과 API 테스트를 묶어 쓰기"
    right: "Python, Postman 글도 함께 보기"
custom_next_reads_title: "이 글과 함께 보면 좋은 글"
custom_next_reads_intro: "지금 읽은 내용을 바로 확장하거나, 실제 선택과 설치까지 이어질 만한 글들만 골랐습니다."
custom_next_reads:
  - title: "Python 설치와 사용법"
    url: "/tools/python-guide/"
    note: "개발 환경 기본 축을 같이 맞출 때"
  - title: "Postman 설치와 사용법"
    url: "/tools/postman-guide/"
    note: "컨테이너로 띄운 API를 테스트할 때"
  - title: "Open WebUI 설치와 사용법"
    url: "/기타/open-webui-guide/"
    note: "Docker 실전 예제로 이어질 때"
# shortterm-growth-enhancement: end
---

- - -

 - [Tools](/tools)

- - -

![Docker Desktop 개요](/assets/images/posts/tools/docker-guide/hero.svg)

![Docker ?? ??](/assets/images/posts/tools/docker-guide/logo.png)

![Docker Desktop 공식 이미지](/assets/images/posts/tools/docker-guide/official.png)

# 무엇인가

Docker는 애플리케이션과 실행 환경을 이미지 단위로 묶어 재현성을 높이는 컨테이너 플랫폼입니다. 로컬 개발, 테스트, 배포 흐름을 맞출 때 특히 강하고, 요즘은 프론트엔드와 데이터 도구에도 널리 쓰입니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [Docker Desktop](https://www.docker.com/)
- 다운로드: [공식 다운로드 페이지](https://www.docker.com/products/docker-desktop/)

# 지원 OS와 설치 방법

## Windows

공식 다운로드 페이지에서 Windows용 설치 파일이나 패키지를 내려받아 설치합니다. 설치가 끝나면 첫 실행과 버전 확인을 한 번 진행하는 편이 좋습니다. WSL 2 또는 Hyper-V 요구사항을 먼저 확인하는 편이 좋습니다.

## macOS

공식 다운로드 페이지에서 macOS용 패키지를 내려받아 설치합니다. Apple Silicon/Intel 구분과 보안 경고 처리 여부를 먼저 확인하는 편이 좋습니다. Apple Silicon과 Intel 빌드 구분을 먼저 확인하는 편이 좋습니다.

## Linux

공식 다운로드 페이지나 공식 문서에서 Linux용 패키지와 배포판별 설치 방식을 확인합니다. 설치 후 CLI나 첫 실행 테스트로 정상 동작을 확인합니다. Desktop과 Engine/Compose 중 어떤 구성이 필요한지 먼저 정하는 편이 좋습니다.

# 기본 사용법

1. 터미널에서 `docker run hello-world`를 실행해 엔진 연결을 확인합니다.
2. 프로젝트 루트에 Dockerfile이나 compose.yaml을 만들고 이미지를 빌드합니다.
3. Desktop UI와 CLI에서 로그, 볼륨, 포트 매핑을 함께 확인합니다.

# 주의할 점

Docker는 설치보다 시스템 요구사항 정리가 더 중요합니다. Windows는 WSL 2 메모리, macOS는 CPU 아키텍처, Linux는 Desktop과 Engine의 역할 차이를 먼저 이해해 두면 이후가 훨씬 덜 꼬입니다.

# 요약

Docker는 로컬 개발 환경을 재현 가능하게 만드는 데 가장 큰 가치가 있습니다. 공식 다운로드 페이지와 OS별 설치 문서를 기준으로 시작하고, 첫 단계는 hello-world 정도면 충분합니다.

# 참고 자료

- [Docker 공식 사이트](https://www.docker.com/)
- [Docker Desktop 다운로드](https://www.docker.com/products/docker-desktop/)
- [Install Docker Desktop on Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
- [Install Docker Desktop on Mac](https://docs.docker.com/desktop/setup/install/mac-install/)
- [Install Docker Desktop on Linux](https://docs.docker.com/desktop/setup/install/linux/)

- - -

 - [Tools](/tools)

- - -
