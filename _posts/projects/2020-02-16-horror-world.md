---
title:  "[프로젝트] 호러 월드"
excerpt: "호러 테마파크를 주제로 한 괴담, 공포 사진 제공 어플리케이션"
description: "호러 월드(Horror World) 안드로이드 앱 프로젝트 소개. 공포 테마파크 컨셉의 괴담/사진 콘텐츠 앱과 2026 리빌드 개선 내역을 정리했습니다."

categories:
  - Project
tags:
  - Project
  - Android
  - Java
  - Kotlin
  - Jetpack Compose
  - MVVM

date: 2020-02-17 KST 02:53 +0900

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [프로젝트 전체 목록 보기](/projects)

- - -

# 호러 월드

## 실행 화면

![](/assets/images/posts/projects/horror-world/splash.png){: width="250px"}
![](/assets/images/posts/projects/horror-world/main.png){: width="250px"}
![](/assets/images/posts/projects/horror-world/list.png){: width="250px"}
![](/assets/images/posts/projects/horror-world/text.png){: width="250px"}
![](/assets/images/posts/projects/horror-world/image.png){: width="250px"}

## 프로젝트 개요

호러 테마파크를 주제로 한 괴담/공포 사진 콘텐츠 앱.
초기 공개(2015) 이후 2026년에 전체 구조와 UX를 현대화해 재정비했습니다.

 - 배포: [플레이 스토어](https://play.google.com/store/apps/details?id=std.neomind.horrorworld)
 - 성과: (2026-03-10 기준) Google Play 5K+ 다운로드, 12세 이용가, 광고 포함
 - 최근 스토어 업데이트: 2026-03-10

## 프로젝트 개발 정보

 - 개발 기간: 2015.07.01. ~ 2015.08.15. (초기 개발), 2026.03 유지보수/리빌드
 - 출시 일자: 2015.08.07.
 - 개발 인원: 1
 - 역할: 설계 및 구현

### 개발 내용

 - '이해하면 무서운 사진'과 '무서운 이야기' 모음을 콘텐츠로 제공
 - '무서운 이야기' 콘텐츠는 읽기 쉽도록 어디까지 읽었었는지를 가시적으로 표시
 - 앱의 이름과 어울리게 유령의 집 같은 테마로 제작

### 2026 리빌드/개선 내역

 - 레거시 UI를 Jetpack Compose + MVVM 구조로 전환
 - 빌드/배포 체계 현대화(dev/debug/release 트랙 정리, 릴리즈 최적화 및 난독화 정비)
 - targetSdk 36 기준 대응 및 릴리즈 안정성 보강
 - 스토리 읽기 UX 개선(스와이프 페이징, 글자 크기/줄간격/배경 어둡기 설정 저장)
 - 스토리 목록 필터 UX 개선 및 헤더/리스트 가독성 개선
 - 배너/전면 광고 위치 및 로딩 타이밍 문제 수정(콘텐츠/네비게이션 가림 이슈 해소)
 - UMP 기반 광고 동의 플로우 적용, 동의 상태 기반 광고 로딩
 - Firebase Analytics 이벤트/화면 추적 정비
 - 다국어/로케일 로딩 확장(스토리 자산 및 UI), 원격 콘텐츠 파이프라인 추가

## 실행 및 개발 환경

|:----:|:----|
| **<center>개발 O/S</center>** | Windows 8.1 → Windows 10 |
| **<center>실행 O/S</center>** | Android |
| **<center>프레임워크</center>** | Android SDK, Jetpack Compose |
| **<center>아키텍처</center>** | MVVM |
| **<center>개발 언어</center>** | JAVA → Kotlin |
| **<center>에디터 / IDE</center>** | Eclipse → Android Studio |

## 개발 후기

사이렌 사운드보드와 마찬가지로, 안드로이드 공부용으로 개발한 앱입니다.

리소스를 직접 구해 편집, 생산한 덕분에 컨텐츠 제공형 프로그램에 있어 리소스가 얼마나 중요한지 알 수 있었습니다.

초기에는 버려진 흉가와 같은 곳을 탐험하는 컨셉으로 잡았지만, 미술이나 그림, 편집 프로그램에 깊이 공부해본 적이 없었고 저작권에서 자유로운 리소스의 수집에 한계가 있어 방향을 변경해 현재의 모습으로 완성되었습니다.

또한, 여러 목록을 나열하는 방법을 배우는 과정에서 객체지향 디자인 패턴 중 어댑터 패턴을 배울 수 있었습니다.

안드로이드 SDK에서 리스트뷰, 갤러리뷰 등의 여러 아이템을 보여주는 뷰는 데이터와 인터페이스, 뷰 클라이언트를 분리시키기 위해 어댑터 패턴을 사용합니다.

데이터를 담은 부모 뷰가 자식 뷰를 요청할 때, 인터페이스의 getView()메소드가 Iterable 객체의 아이템을 get 하여 자식 뷰를 구성 후 반환하도록 구현했습니다.

- - -

 - [프로젝트 전체 목록 보기](/projects)

- - -
