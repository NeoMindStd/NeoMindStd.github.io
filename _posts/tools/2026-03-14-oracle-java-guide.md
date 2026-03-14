---
title:  "[Tools] Oracle Java 설치와 사용법: 공식 JDK 다운로드부터 JAVA_HOME 설정까지"
excerpt: "Oracle Java를 공식 다운로드 페이지에서 내려받고, Windows/macOS/Linux에서 JDK 설치와 환경 변수 설정까지 정리했습니다."
description: "Oracle Java 공식 사이트와 JDK 다운로드 경로, 설치 방법, JAVA_HOME 설정과 기본 사용법을 정리한 가이드입니다."

categories:
  - Tools
tags:
  - Tools
  - Oracle Java
  - JDK
  - Windows
  - macOS
  - Linux
date: 2026-03-14 18:17:00 +09:00
permalink: /tools/oracle-java-guide/
header:
  og_image: /assets/images/posts/tools/oracle-java-guide/social.png
  teaser: /assets/images/posts/tools/oracle-java-guide/social.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [Tools](/tools)

- - -

![Oracle Java 개요](/assets/images/posts/tools/oracle-java-guide/hero.svg)

![Oracle Java ?? ??](/assets/images/posts/tools/oracle-java-guide/logo.png)

![Oracle Java 공식 이미지](/assets/images/posts/tools/oracle-java-guide/official.png)

# 무엇인가

Oracle Java는 Oracle이 배포하는 JDK/JRE 계열입니다. 기업 환경이나 특정 벤더 문서를 따라야 할 때 여전히 자주 등장하고, 설치 후 JAVA_HOME과 PATH를 제대로 잡는 것이 가장 기본입니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [Oracle Java](https://www.oracle.com/java/)
- 다운로드: [공식 다운로드 페이지](https://www.oracle.com/java/technologies/downloads/)

# 지원 OS와 설치 방법

## Windows

공식 다운로드 페이지에서 Windows용 설치 파일이나 패키지를 내려받아 설치합니다. 설치가 끝나면 첫 실행과 버전 확인을 한 번 진행하는 편이 좋습니다. 여러 JDK가 공존한다면 JAVA_HOME 우선순위를 꼭 정리하는 편이 좋습니다.

## macOS

공식 다운로드 페이지에서 macOS용 패키지를 내려받아 설치합니다. Apple Silicon/Intel 구분과 보안 경고 처리 여부를 먼저 확인하는 편이 좋습니다. Apple Silicon과 Intel 구분을 먼저 확인하면 덜 헷갈립니다.

## Linux

공식 다운로드 페이지나 공식 문서에서 Linux용 패키지와 배포판별 설치 방식을 확인합니다. 설치 후 CLI나 첫 실행 테스트로 정상 동작을 확인합니다. 패키지 관리자 설치 후 alternatives 설정을 함께 보는 편이 좋습니다.

# 기본 사용법

1. 설치 후 `java -version`과 `javac -version`으로 런타임과 컴파일러를 확인합니다.
2. 프로젝트별로 필요한 Java 버전에 맞춰 JAVA_HOME과 IDE 설정을 맞춥니다.
3. 간단한 HelloWorld.java를 컴파일하고 실행해 환경을 검증합니다.

# 주의할 점

Oracle Java는 기술 요소뿐 아니라 라이선스와 배포 정책도 함께 봐야 합니다. 팀 기준 문서가 있다면 그것을 먼저 따르는 편이 맞습니다.

# 요약

Oracle Java는 설치 자체보다 버전 관리와 환경 변수 관리가 핵심입니다. 공식 다운로드 페이지에서 필요한 버전을 고르고 JAVA_HOME을 명확히 정리해 두면 이후가 쉬워집니다.

# 참고 자료

- [Oracle Java 공식 사이트](https://www.oracle.com/java/)
- [Oracle JDK Downloads](https://www.oracle.com/java/technologies/downloads/)
- [Oracle Java Documentation](https://docs.oracle.com/en/java/)

- - -

 - [Tools](/tools)

- - -
