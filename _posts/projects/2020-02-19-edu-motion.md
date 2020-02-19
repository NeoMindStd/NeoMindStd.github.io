---
title:  "[프로젝트] 애니북 놀이터"
excerpt: "크로마키, 프레임별 편집 기능을 제공하고 여러 장의 사진을 찍어 StopMotion 영상으로 변환 및 재생하는 안드로이드 어플리케이션"

categories:
  - Project
tags:
  - Project
  - Android
  - Java
  - C++

date: 2020-02-19 KST 23:02 +0900

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [프로젝트 전체 목록 보기](/projects)

- - -

# 방공무기 교전통제 프로그램

## 실행 화면

![](/assets/images/posts/projects/edu-motion/splash.png){: .align-center}

<p align="center">
  <img src="/assets/images/posts/projects/edu-motion/project.png"/>
  <img src="/assets/images/posts/projects/edu-motion/detail.png"/>
</p>

<p align="center">
  <img src="/assets/images/posts/projects/edu-motion/manage.png"/>
  <img src="/assets/images/posts/projects/edu-motion/camera.png"/>
</p>

## 프로젝트 개요

초등생 교육에 사용되는 외주 프로젝트로서, 크로마키와 프레임별 편집 기능을 제공하고 여러 장의 사진을 찍어 StopMotion 영상으로 변환 및 재생하는 안드로이드 어플리케이션 

 - 배포: [플레이 스토어](https://play.google.com/store/apps/details?id=in74mz.edumotion) <sup id="tupleH">[1](#tupleT)</sup>
 - 성과: (2020-02-19 기준) 50회 이상 설치

## 프로젝트 개발 정보

 - 개발 기간: 2018.05.01 ~ 2018.07.15
 - 출시 일자: 2015.10.17
 - 개발 인원: 3
 - 역할: UI 및 로직 구현

### 개발 내용

 - 사용자의 스톱모션 프로젝트 저장·관리·공유하기 기능
 - 카메라의 촬영, 촬영 설정 기능 및 기존에 있던 사진을 불러오는 기능
 - 사용자의 음성을 녹음 및 저장하는 기능
 - 사용자가 등록한 프레임의 사진과 음성을 디코딩 하여 Media MUX를 이용해 사용자의 설정대로 Animated GIF 포맷이나 MP4 포맷으로 변환하여 저장하는 기능

## 실행 및 개발 환경

|:----:|:----|
| **<center>개발 O/S</center>** | Windows 10 |
| **<center>실행 O/S</center>** | Android |
| **<center>프레임워크</center>** | Android SDK |
| **<center>개발 언어</center>** | JAVA, C++ |
| **<center>에디터 / IDE</center>** | Android Studio |

## 개발 후기

이 프로젝트는 리소스 분야가 아닌 프로그래밍 분야까지도 다른 팀원과 함께 제작해본 첫 프로젝트입니다. 

이 프로젝트를 통해 기본적으로 Git이라는 형상관리도구로 협업하는 법을 배웠고, 코드 스타일을 표준을 지키고 깔끔하게 관리하는 법, 서로의 모듈 간에 데이터를 교환하는 인터페이스 등 저 혼자 코딩할 때에는 배우지 못했던 많은 것들을 배울 수 있었습니다. 

또한, 프로젝트를 개발하며 처음으로 NDK사용과 영상처리를 사용해 본 프로젝트로, 안드로이드 커널부와의 통신구조, 안드로이드가 앱과 자원을 관리하는 법, 기본적인 영상처리의 원리 등 기술적인 부분에서도 많은 것을 배울 수 있었던 앱입니다.

- - - 

<b id="tupleT">[1](#tupleH)</b> 이 프로젝트는 일회성으로, 현재는 리소스 서버를 구동하지 않아 실행이 불가능합니다

- - -

 - [프로젝트 전체 목록 보기](/projects)

- - -