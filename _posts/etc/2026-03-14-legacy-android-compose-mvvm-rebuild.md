---
title:  "[기타/앱개발] 레거시 안드로이드 앱을 Jetpack Compose + MVVM으로 리빌드한 과정"
excerpt: "오래된 Android 앱을 Compose + MVVM 구조로 전환하면서 UI, 상태관리, 배포 체계를 다시 설계한 실전 리빌드 기록입니다."
description: "오래된 Android 앱을 Compose + MVVM 구조로 전환하면서 UI, 상태관리, 배포 체계를 다시 설계한 실전 리빌드 기록입니다."

categories:
  - 기타
tags:
  - 기타
  - 앱개발
  - Android
  - Jetpack Compose
  - MVVM
  - 리빌드

date: 2026-03-14 12:50:00 +09:00

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

# 문제/배경

초기 안드로이드 프로젝트는 오래된 UI/상태 관리 방식과 빌드 설정으로 유지보수가 어려웠습니다.  
단순 기능 추가보다 “장기 운영 가능한 구조”로 재정비하는 것이 우선이어서 Compose + MVVM 리빌드를 진행했습니다.

# 원인

레거시 구조에서 반복적으로 부딪힌 문제는 다음과 같았습니다.

1. 화면 로직과 상태 로직이 강하게 결합되어 수정 비용이 큼
2. 광고/분석/권한 처리 같은 운영 코드가 화면 코드에 흩어짐
3. 릴리즈 빌드/타깃 SDK 업데이트 시 영향 범위 추적이 어려움

# 적용 코드/설정

리빌드 기준:

- UI: XML 중심 화면을 Compose 컴포저블로 전환
- 상태: 화면 상태와 이벤트를 ViewModel로 이동
- 운영: 광고/분석/권한/테마를 공통 진입점에서 제어

```kotlin
@Composable
fun AppRoot(viewModel: MainViewModel) {
    val uiState by viewModel.uiState.collectAsState()
    MainScreen(
        uiState = uiState,
        onAction = viewModel::onAction
    )
}
```

프로젝트별 적용:

- [호러 월드](/project/horror-world)
- [사이렌 사운드보드](/project/siren-soundboard)

# 검증 결과

- 기능 추가 시 화면/로직 수정 범위가 분리되어 변경 속도가 빨라짐
- 광고/분석 이벤트 흐름을 단일 ViewModel 액션에서 추적 가능
- 테마/다국어/상태 복원 같은 운영 요구사항을 재사용하기 쉬워짐

# 체크리스트

- [ ] 화면 상태를 단일 source of truth(ViewModel)로 관리하는가
- [ ] 광고/분석/권한 처리가 화면 컴포저블 밖에서 제어되는가
- [ ] 테마/로케일 변경 시 UI 재구성이 안전한가
- [ ] 릴리즈 빌드에서 난독화/리소스 축소가 정상 동작하는가
- [ ] 회귀 테스트 기준 화면과 로그 포인트가 정의되어 있는가

# 관련 글

- [Jetpack Compose + AdMob 전면 광고 겹침 문제 해결기](/기타/compose-admob-interstitial-overlap-fix/)
- [Minimal Mistakes 다크모드 토글 적용기](/기타/minimal-mistakes-dark-mode-toggle/)
- [프로젝트 목록](/projects/)

- - -

 - [기타](/etc)

- - -
