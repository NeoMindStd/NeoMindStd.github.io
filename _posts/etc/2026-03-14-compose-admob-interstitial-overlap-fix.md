---
title:  "[기타/앱운영] Jetpack Compose + AdMob 전면 광고 겹침 문제 해결기"
excerpt: "Compose 화면 전환 시 전면 광고가 콘텐츠와 겹쳐 보이던 이슈를 레이아웃/호출 타이밍 정리로 해결한 과정을 기록했습니다."
description: "Compose 화면 전환 시 전면 광고가 콘텐츠와 겹쳐 보이던 이슈를 레이아웃/호출 타이밍 정리로 해결한 과정을 기록했습니다."

categories:
  - 기타
tags:
  - 기타
  - 앱운영
  - Android
  - Jetpack Compose
  - AdMob
  - UX

date: 2026-03-14 20:20:00 +09:00

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

# 문제/배경

Compose로 리빌드한 앱에서 전면 광고를 호출하면, 특정 타이밍에 콘텐츠가 잠깐 가려지거나 클릭 레이어가 어긋나는 현상이 있었습니다.  
특히 화면 진입 직후 즉시 광고를 띄우는 흐름에서 UX 저하가 크게 보였습니다.

# 원인

원인은 크게 두 가지였습니다.

1. 화면 상태가 안정되기 전에 광고 호출이 먼저 발생
2. 광고 콜백 이후 UI 상태 복구가 단일 경로로 정리되지 않음

결과적으로 “광고는 닫혔는데 화면 상태는 이전 값”인 순간이 생겨 겹침처럼 보이는 문제가 생겼습니다.

# 적용 코드/설정

핵심은 “광고 호출 타이밍”과 “닫힘 후 상태 복구”를 단일 흐름으로 고정하는 것입니다.

```kotlin
fun tryShowInterstitial(onClosed: () -> Unit) {
    if (interstitialAd == null) {
        onClosed()
        return
    }

    isAdShowing = true
    interstitialAd?.fullScreenContentCallback = object : FullScreenContentCallback() {
        override fun onAdDismissedFullScreenContent() {
            isAdShowing = false
            interstitialAd = null
            onClosed()
        }
    }
    interstitialAd?.show(activity)
}
```

운영 포인트:

- 전면 광고 호출 전후 상태값을 ViewModel 기준으로 단일화
- 광고 실패/미로드 시 동일 콜백으로 자연스럽게 복귀
- 광고를 콘텐츠 이벤트와 분리해 “광고 없음”도 정상 흐름으로 취급

# 검증 결과

리빌드 버전에서 광고 표출 후 화면 깜빡임/겹침 체감이 줄었고, 사용자 흐름이 끊기는 상황도 크게 감소했습니다.  
핵심은 광고 SDK 문제가 아니라 앱 내부 상태 전환 타이밍의 일관성이었습니다.

# 체크리스트

- [ ] 전면 광고 호출 전 UI 상태를 잠그는가
- [ ] 광고 dismiss/fail 경로가 동일 콜백으로 합쳐져 있는가
- [ ] 광고 미로드 상황에서도 화면 흐름이 깨지지 않는가
- [ ] Compose recomposition 시 광고 호출이 중복되지 않는가
- [ ] 운영 로그에서 광고 상태 전환 순서가 추적 가능한가

# 관련 글

- [레거시 안드로이드 앱을 Compose + MVVM으로 리빌드한 과정](/기타/legacy-android-compose-mvvm-rebuild/)
- [Google Play app-ads.txt 적용 방법과 반영 체크리스트](/기타/google-play-app-ads-txt-checklist/)
- [프로젝트: 사이렌 사운드보드](/project/siren-soundboard)

- - -

 - [기타](/etc)

- - -
