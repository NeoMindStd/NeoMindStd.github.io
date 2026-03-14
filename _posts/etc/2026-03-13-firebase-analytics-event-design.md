---
title:  "[기타/앱운영] Firebase Analytics 이벤트 설계: 앱 운영 기준으로 다시 잡기"
excerpt: "화면 수집만으로는 운영에 필요한 판단이 어렵습니다. 실제 앱 운영 관점에서 이벤트/파라미터 구조를 다시 설계한 기준을 정리했습니다."
description: "HorrorWorld와 Siren Soundboard 코드 기반으로 Firebase Analytics 이벤트 네이밍, 파라미터 정규화, 운영 지표 연결 방법을 정리했습니다."

categories:
  - 기타
tags:
  - 기타
  - 앱운영
  - Android
  - Firebase
  - Analytics
  - 데이터분석
date: 2026-03-13 18:05:00 +09:00

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

# 문제/배경

초기에는 `screen_view`만 쌓아두고 있었고, 실제 운영 의사결정(어떤 기능을 개선할지, 어디서 이탈하는지)에 바로 쓰기 어려웠습니다.  
그래서 이벤트 이름과 파라미터를 **기능 단위**로 재설계했습니다.

# 원인

분석이 약했던 이유는 아래와 같았습니다.

1. 이벤트 명명 규칙이 불명확함
2. 파라미터 단위/형식이 이벤트마다 제각각
3. 화면 이벤트와 행동 이벤트가 분리되지 않음

# 적용 코드/설정

## 1) 앱별 접두/도메인 기반 이벤트 네이밍

`HorrorWorld`는 `hw_` 접두를 사용해 도메인 이벤트를 분리했습니다.

```kotlin
logCustomEvent(name = "hw_story_open", params = mapOf(...))
logCustomEvent(name = "hw_gallery_select", params = mapOf(...))
```

## 2) 파라미터 정규화

`sirenpackage`는 템포/볼륨처럼 실수형 값이 많은데, 쿼리와 집계를 위해 정수 파라미터로 정규화했습니다.

```kotlin
putInt(PARAM_TEMPO_X10, (tempo * 10f).roundToInt())
putInt(PARAM_VOLUME_PCT, (volume * 100f).roundToInt())
```

## 3) 운영 지표와 바로 연결되는 이벤트 세트

`siren_play_start`, `siren_play_end`, `theme_mode_change` 같이  
"진입-실행-종료" 흐름을 한 세트로 묶어 실제 사용 패턴을 추적했습니다.

```kotlin
const val EVENT_PLAYBACK_START = "siren_play_start"
const val EVENT_PLAYBACK_END = "siren_play_end"
const val EVENT_THEME_MODE_CHANGE = "theme_mode_change"
```

# 검증 결과

- 어떤 화면이 아니라 "어떤 기능이 실제로 쓰였는지" 기준으로 분석 가능
- 템포/볼륨/재생모드 분포를 이벤트 파라미터에서 바로 집계 가능
- 기능 개선 우선순위를 감각이 아니라 로그 근거로 정할 수 있게 됨

# 체크리스트

- [ ] 이벤트 이름이 도메인/기능 기준으로 일관적인가
- [ ] 파라미터 타입(문자/정수/실수)이 문서화되어 있는가
- [ ] `screen_view`와 행동 이벤트를 분리해서 수집하는가
- [ ] 시작/종료 이벤트가 짝을 이루어 체류/완료 분석이 가능한가
- [ ] 값 정규화(예: tempo_x10, volume_pct)로 분석 쿼리가 단순해졌는가

# 관련 글

- [레거시 안드로이드 앱을 Compose + MVVM으로 리빌드한 과정](/기타/legacy-android-compose-mvvm-rebuild/)
- [사이렌 사운드보드 UX 개선기: 반복/속도/볼륨 설계](/기타/siren-soundboard-ux-design/)
- [호러 월드 리빌드 회고: 오래된 앱을 다시 살릴 때 체크한 것들](/기타/horror-world-rebuild-retrospective/)

- - -

 - [기타](/etc)

- - -
