---
title:  "[프로젝트] 쿠폰 매니저"
excerpt: "OCR 기술을 응용하여 바코드와 글자를 자동 인식 후 분류, 다량의 기프티콘을 효율적으로 관리할 수 있게 도와주는 iOS, 안드로이드 어플리케이션"

categories:
  - Project
tags:
  - Project
  - Android
  - Java
  - iOS
  - Swift
  - Flutter
  - Dart
  - SQLite

date: 2020-02-23 KST 21:10 +0900

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [프로젝트 전체 목록 보기](/projects)

- - -

# 쿠폰 매니저

## 실행 화면

![](/assets/images/posts/projects/coupon-manager/view_coupon.jpg){:width="30%"}&nbsp;&nbsp;
![](/assets/images/posts/projects/coupon-manager/view_coupon_details.jpg){:width="30%"}&nbsp;&nbsp;
![](/assets/images/posts/projects/coupon-manager/setting.jpg){:width="30%"}

## 프로젝트 개요

OCR 기술을 응용하여 바코드와 글자를 자동 인식 후 분류, 다량의 기프티콘을 효율적으로 관리할 수 있게 도와주는 iOS, 안드로이드 어플리케이션

 - 배포: [플레이 스토어](https://play.google.com/store/apps/details?id=com.in74mz.couponmanager), [앱스토어](https://apps.apple.com/us/app/%EC%BF%A0%ED%8F%B0-%EB%A7%A4%EB%8B%88%EC%A0%80-%EA%B0%84%ED%8E%B8%ED%95%9C-%EC%BF%A0%ED%8F%B0-%EA%B4%80%EB%A6%AC/id1475508479)
 - 플레이스토어 성과: (2020-02-23 기준) 1,000 ~ 5,000회 설치, 평점 4.3/5.0 (32명 참여)
 - 앱스토어 성과: (2020-02-23 기준) 평점 4.3/5.0 (12명 참여)

## 프로젝트 개발 정보

 - 개발 기간: 2019.01.19. ~ 2019.10.19.
 - 출시 일자: 2019.03.20.
 - 개발 인원: 3 → 2
 - 역할: UI 및 로직, DB 구현

### 개발 내용

 - (네이티브) 메인화면, 정렬기능, DB, 쿠폰보기 화면 UI 및 로직 구현
 - (플러터) 네이티브 앱을 플러터 앱으로 포팅
 - (플러터) 설정화면과 쿠폰보기 화면의 UI 및 로직 구현, 카테고리 관리 로직 구현

## 실행 및 개발 환경

|:----:|:----|
| **<center>개발 O/S</center>** | Windows 10 → Windows 10, mac OS Mojave |
| **<center>실행 O/S</center>** | Android → Android, iOS |
| **<center>프레임워크</center>** | Android SDK → Flutter SDK |
| **<center>개발 언어</center>** | JAVA, SQLite → Dart, JAVA, Swift, SQLite |
| **<center>에디터 / IDE</center>** | Android Studio |

## 개발 후기

Git 관리전략과 Pull-Request등 Git을 본격적으로 배운 프로젝트입니다.

우선 Android SDK를 이용하여 네이티브 앱으로 개발 후, Flutter SDK를 이용하여 크로스플랫폼으로 다시 개발하였습니다. 

Dart와 Flutter라는 처음 접하는 언어와 프레임워크를 다루었지만, 학부에서 ‘프로그래밍 언어론’ 강의를 이수했던 터라 쉽게 익힐 수 있었습니다.

Dart와 1.8 버전의 JAVA를 다루며 익명 함수(람다식)와 함수형 프로그래밍을 배우고, 코드의 가독성을 높이기 위해 사용했습니다.

또, 디자인 패턴 중 MVC, MVVM, BLoC 패턴을 배워 실제 프로젝트에 응용했습니다.

- - -

 - [프로젝트 전체 목록 보기](/projects)

- - -