---
title:  "[프로젝트] 사이렌 사운드보드"
excerpt: "각종 사이렌, 경보, 알람 사운드를 다양한 속도로 재생할 수 있는 앱입니다."
description: "사이렌 사운드보드는 여러 종류의 경보음을 빠르게 재생하고 세밀하게 조절할 수 있는 사운드보드 앱입니다."

categories:
  - Project
tags:
  - Project
  - Android
  - Java
  - Kotlin
  - Jetpack Compose
  - MVVM

date: 2020-02-14 KST 00:36 +0900

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [프로젝트 전체 목록 보기](/projects)

- - -

# 사이렌 사운드보드

## 실행 화면

![](/assets/images/posts/projects/siren-soundboard/screen-main-ko-20260313.jpg){: width="240px"}
![](/assets/images/posts/projects/siren-soundboard/screen-detail-ko-20260313.jpg){: width="240px"}
![](/assets/images/posts/projects/siren-soundboard/screen-main-en-20260313.jpg){: width="240px"}
![](/assets/images/posts/projects/siren-soundboard/screen-detail-en-20260313.jpg){: width="240px"}

한국어/영어 메인 화면과 상세 메뉴 화면(2026-03-13 캡처)입니다.

## 프로젝트 개요

사이렌 사운드보드는 여러 종류의 경보음을 빠르게 재생하고 세밀하게 조절할 수 있는 사운드보드 앱입니다.

 - 배포: [플레이 스토어](https://play.google.com/store/apps/details?id=std.neomind.sirenpackage)
 - 최신 버전: `4.0.4 (45)` (2026-03-13 기준)
 - 성과: (2020-02-14 기준) 2,780회 이상 설치, 평점 4.429/5.0 (21명 참여)
 - 운영: Firebase Analytics + AdMob 적용
 - 개인정보 처리방침: [보기](/project/siren-soundboard/PRIVACY_POLICY.html)

## 주요 기능

 - 탭 한 번으로 재생/정지
 - 무한 반복 토글
 - 마스터 볼륨 및 항목별 볼륨 조절
 - 항목별 재생 속도 조절
 - 상세 메뉴에서 시스템 사운드(알람/알림/벨소리/SMS) 설정 지원
 - 테마 모드(시스템/라이트/다크) 지원
 - 다국어 지원(ko/en/ja/zh-CN/zh-TW/pt/es)

## 프로젝트 개발 정보

 - 개발 기간: 2014.02.01. ~ 2014.02.27. (초기 개발), 2026.03 리빌드/유지보수
 - 출시 일자: 2014.02.27.
 - 개발 인원: 1
 - 역할: 설계 및 구현

### f7b07f1(3.2.0) 이후 업데이트 이력

 - Jetpack Compose + MVVM 구조로 전환
 - 반응형 그리드 레이아웃, 상단 제어/상태 UI 재정비
 - 롱클릭 상세 메뉴를 섹션화하고 재생/볼륨/속도 제어 흐름 개선
 - 시스템 사운드 설정(알람/알림/벨소리/SMS) 기능 강화
 - 무한 반복 토글, 마스터/개별 볼륨 저장형 제어 추가
 - SoundPool 로드 대기/페이드 인아웃으로 재생 안정성 개선
 - 테마 모드(시스템/라이트/다크) 전환 적용
 - 다국어 리소스 확장 및 항목 명칭 정리
 - Firebase Analytics 재생 세션 추적 연동
 - 앱 내 개인정보 처리방침 웹뷰 진입 추가

## 실행 및 개발 환경

|:----:|:----|
| **<center>개발 O/S</center>** | Windows 8.1 → Windows 10 |
| **<center>실행 O/S</center>** | Android |
| **<center>프레임워크</center>** | Android SDK, Jetpack Compose |
| **<center>아키텍처</center>** | MVVM |
| **<center>개발 언어</center>** | JAVA → Kotlin |
| **<center>에디터 / IDE</center>** | Eclipse → Android Studio |

## 개발 후기

고등학교 시절 안드로이드 학습용으로 시작한 앱을 장기간 운영하면서, 단순 사운드 재생 앱이라도 UX/성능/정책 대응이 계속 필요하다는 점을 체감한 프로젝트입니다.

2026년 리빌드에서는 구조 전환(Compose + MVVM), 재생 제어 안정화, 접근성과 다국어 개선, 개인정보 고지 및 분석 체계까지 정비해 실제 운영 품질을 끌어올렸습니다.

처음 만든 앱을 최신 스택으로 다시 다듬는 과정 자체가, 오래 유지보수 가능한 소프트웨어를 만드는 연습이 되었습니다.

- - -

 - [프로젝트 전체 목록 보기](/projects)

- - -
