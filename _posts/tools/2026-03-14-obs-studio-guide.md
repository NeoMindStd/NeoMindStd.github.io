---
title:  "[Tools] OBS 설치와 사용법: 공식 다운로드부터 첫 녹화와 송출까지"
excerpt: "OBS Studio를 공식 사이트에서 설치하고, 씬·소스·오디오 설정을 잡아 첫 녹화나 송출을 시작하는 방법을 정리했습니다."
description: "OBS Studio 공식 사이트와 다운로드 경로, Windows/macOS/Linux 설치 방법, 기본 사용 흐름을 설명한 가이드입니다."

categories:
  - Tools
tags:
  - Tools
  - OBS
  - Streaming
  - Recording
  - Windows
  - macOS
  - Linux
date: 2026-03-14 18:28:00 +09:00
permalink: /tools/obs-studio-guide/
header:
  og_image: /assets/images/posts/tools/obs-studio-guide/social.png
  teaser: /assets/images/posts/tools/obs-studio-guide/social.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [Tools](/tools)

- - -

![OBS Studio 개요](/assets/images/posts/tools/obs-studio-guide/hero.svg)

![OBS Studio 공식 이미지](/assets/images/posts/tools/obs-studio-guide/official.png)

# 무엇인가

OBS Studio는 녹화와 라이브 송출에서 가장 널리 쓰이는 무료 오픈소스 도구 중 하나입니다. 장면 구성, 캡처 소스, 오디오 믹서, 인코더 설정을 한 번에 다루기 때문에 처음엔 복잡해 보여도 기본 흐름은 단순합니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [OBS Studio](https://obsproject.com/)
- 다운로드: [공식 다운로드 페이지](https://obsproject.com/download)

# 지원 OS와 설치 방법

## Windows

공식 다운로드 페이지에서 Windows용 설치 파일이나 패키지를 내려받아 설치합니다. 설치가 끝나면 첫 실행과 버전 확인을 한 번 진행하는 편이 좋습니다. 첫 실행 시 자동 구성 마법사를 한 번 돌려 두는 편이 좋습니다.

## macOS

공식 다운로드 페이지에서 macOS용 패키지를 내려받아 설치합니다. Apple Silicon/Intel 구분과 보안 경고 처리 여부를 먼저 확인하는 편이 좋습니다. 화면 녹화와 마이크 권한을 시스템 설정에서 먼저 허용해야 합니다.

## Linux

공식 다운로드 페이지나 공식 문서에서 Linux용 패키지와 배포판별 설치 방식을 확인합니다. 설치 후 CLI나 첫 실행 테스트로 정상 동작을 확인합니다. 배포판과 데스크톱 환경에 따라 캡처 방식 차이가 있을 수 있습니다.

# 기본 사용법

1. Scene을 만들고 Display Capture나 Audio Input Capture 같은 소스를 추가합니다.
2. 오디오 믹서에서 마이크와 시스템 사운드 레벨을 맞춥니다.
3. 짧은 테스트 녹화로 화질과 동기화를 확인한 뒤 실제 방송이나 녹화를 시작합니다.

# 주의할 점

처음부터 최고 화질을 노리면 오히려 더 빨리 꼬입니다. 먼저 짧은 테스트 녹화로 안정성을 확인하고, 그 다음에 해상도와 비트레이트를 올리는 편이 좋습니다.

# 요약

OBS는 설치보다 씬과 소스를 어떻게 쌓느냐가 더 중요합니다. 첫날에는 자동 구성 마법사와 짧은 테스트 녹화만 해도 충분히 좋은 출발이 됩니다.

# 참고 자료

- [OBS 공식 사이트](https://obsproject.com/)
- [OBS 다운로드](https://obsproject.com/download)
- [OBS Knowledge Base](https://obsproject.com/kb/)

- - -

 - [Tools](/tools)

- - -
