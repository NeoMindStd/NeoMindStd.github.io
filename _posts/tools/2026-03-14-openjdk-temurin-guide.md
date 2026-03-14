---
title:  "[Tools] OpenJDK 설치와 사용법: Eclipse Temurin 기준으로 실용적으로 시작하기"
excerpt: "OpenJDK를 실제로 설치할 때 많이 쓰는 Eclipse Temurin 배포판을 기준으로, 공식 다운로드와 환경 변수 설정을 정리했습니다."
description: "OpenJDK 실사용 배포판인 Eclipse Temurin 공식 사이트와 다운로드 경로, 설치 방법, 기본 사용법을 설명한 가이드입니다."

categories:
  - Tools
tags:
  - Tools
  - OpenJDK
  - Temurin
  - Java
  - Windows
  - macOS
  - Linux
date: 2026-03-14 18:18:00 +09:00
permalink: /tools/openjdk-temurin-guide/
header:
  og_image: /assets/images/posts/tools/openjdk-temurin-guide/social.png
  teaser: /assets/images/posts/tools/openjdk-temurin-guide/social.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [Tools](/tools)

- - -

![OpenJDK (Eclipse Temurin) 개요](/assets/images/posts/tools/openjdk-temurin-guide/hero.svg)

![Eclipse Temurin ?? ??](/assets/images/posts/tools/openjdk-temurin-guide/logo.png)

![OpenJDK (Eclipse Temurin) 공식 이미지](/assets/images/posts/tools/openjdk-temurin-guide/official.png)

# 무엇인가

OpenJDK는 프로젝트 이름이고, 실제 사용자는 그 위에 올라간 배포판을 선택해 설치하는 경우가 많습니다. 그중 Eclipse Temurin은 가장 현실적인 출발점 중 하나입니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [OpenJDK (Eclipse Temurin)](https://adoptium.net/)
- 다운로드: [공식 다운로드 페이지](https://adoptium.net/temurin/releases/)

# 지원 OS와 설치 방법

## Windows

공식 다운로드 페이지에서 Windows용 설치 파일이나 패키지를 내려받아 설치합니다. 설치가 끝나면 첫 실행과 버전 확인을 한 번 진행하는 편이 좋습니다. Temurin 경로를 JAVA_HOME으로 잡고 기존 JDK와 충돌하지 않는지 확인하는 편이 좋습니다.

## macOS

공식 다운로드 페이지에서 macOS용 패키지를 내려받아 설치합니다. Apple Silicon/Intel 구분과 보안 경고 처리 여부를 먼저 확인하는 편이 좋습니다. 셸 프로파일에서 원하는 Java 버전이 우선되도록 정리하는 편이 좋습니다.

## Linux

공식 다운로드 페이지나 공식 문서에서 Linux용 패키지와 배포판별 설치 방식을 확인합니다. 설치 후 CLI나 첫 실행 테스트로 정상 동작을 확인합니다. 패키지 방식과 tarball 방식 중 팀 표준과 맞는 쪽을 먼저 정하는 편이 좋습니다.

# 기본 사용법

1. 설치 직후 `java -version`으로 Temurin/OpenJDK 런타임을 확인합니다.
2. 프로젝트 요구사항에 맞춰 JAVA_HOME과 IDE JDK 경로를 맞춥니다.
3. 간단한 컴파일 테스트로 빌드 툴과 연결되기 전 환경을 검증합니다.

# 주의할 점

OpenJDK는 하나처럼 보이지만 실제 설치 체험은 배포판마다 다릅니다. 팀 문서나 CI 환경이 특정 배포판을 전제로 한다면 그것과 일치하는지가 더 중요합니다.

# 요약

OpenJDK를 현실적으로 시작하려면 배포판 선택부터 정해야 합니다. Temurin은 가장 무난한 선택지 중 하나이고, 설치 후에는 버전 충돌 없이 JAVA_HOME을 관리하는 것이 핵심입니다.

# 참고 자료

- [Adoptium 공식 사이트](https://adoptium.net/)
- [Temurin Releases](https://adoptium.net/temurin/releases/)
- [Adoptium Installation](https://adoptium.net/installation/)

- - -

 - [Tools](/tools)

- - -
