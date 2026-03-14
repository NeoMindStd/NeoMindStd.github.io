---
title:  "[기타/프로젝트회고] 호러 월드 리빌드 회고: 오래된 앱을 다시 살릴 때 체크한 것들"
excerpt: "2015년에 만든 콘텐츠 앱을 2026년에 다시 운영 가능한 상태로 되살리며 체크한 구조/정책/UX 포인트를 정리했습니다."
description: "Horror World 리빌드 과정에서 Compose+MVVM 전환, 광고 동의 플로우, 읽기 UX 개선, 운영 체크리스트를 중심으로 회고합니다."

categories:
  - 기타
tags:
  - 기타
  - 프로젝트회고
  - Android
  - Jetpack Compose
  - MVVM
  - HorrorWorld
date: 2026-03-14 13:04:00 +09:00

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

# 문제/배경

호러 월드는 오래전에 출시한 앱이라, 최신 Android 정책/SDK/UX 기준으로는 유지보수 난도가 높았습니다.  
핵심 목표는 "새 앱 개발"이 아니라 **기존 사용자 경험을 보존하면서 운영 가능한 구조로 리빌드**하는 것이었습니다.

# 원인

리빌드가 필요했던 이유는 아래와 같습니다.

1. 레거시 UI/구조에서 기능 확장 비용이 큼
2. 광고 동의/정책 대응(UMP) 체계 부재
3. 읽기 중심 콘텐츠 앱인데 사용자 설정(텍스트 크기/배경 등) 제어가 약함

# 적용 코드/설정

## 1) 구조 전환: Compose + MVVM

UI와 상태를 분리해 화면 추가/개선 시 영향 범위를 줄였습니다.

## 2) 광고 동의와 초기화 분리

`AdsConsentManager`에서 동의 상태를 먼저 확정하고, 광고 SDK는 그 이후에만 초기화합니다.

```kotlin
_canRequestAds.value = consentInformation.canRequestAds()
if (!_canRequestAds.value) return
MobileAds.initialize(context) {}
```

## 3) 전면 광고는 선로딩 후 조건 노출

`GalleryInterstitialAdManager`를 두어 선로딩(`preload`)과 실제 표시(`showIfAvailable`)를 분리했습니다.

```kotlin
if (canRequestAds) interstitialManager?.preload()
val shown = interstitialManager?.showIfAvailable(activity) { /* continue */ } ?: false
```

## 4) 읽기 경험 개선

스토리 읽기 화면의 설정(글자 크기/줄간격/배경 어둡기)을 저장형 UX로 정비해 재방문 시 피로를 줄였습니다.

# 검증 결과

- 광고/정책/콘텐츠 흐름이 충돌하지 않는 운영 구조 확보
- 읽기 중심 UX 개선으로 장문 콘텐츠 소비 안정화
- 이벤트 로그와 설정 저장이 분리되어 추적/수정이 쉬워짐

# 체크리스트

- [ ] 구조 전환 시 도메인 상태와 UI 상태를 분리했는가
- [ ] 광고 동의 플로우가 앱 시작 경로에서 일관되게 호출되는가
- [ ] 광고 노출 타이밍이 콘텐츠 흐름을 깨지 않는가
- [ ] 사용자 설정(텍스트/테마/음소거 등)이 재실행 후 유지되는가
- [ ] 정책 문서(개인정보처리방침, app-ads.txt) 링크가 공개 URL로 연결되는가

# 관련 글

- [프로젝트 소개: 호러 월드](/project/horror-world/)
- [AdMob 수익 최적화를 위한 배너/전면/리워드 배치 회고](/기타/admob-placement-retrospective/)
- [Firebase Analytics 이벤트 설계: 앱 운영 기준으로 다시 잡기](/기타/firebase-analytics-event-design/)

- - -

 - [기타](/etc)

- - -
