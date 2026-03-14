---
title:  "[기타/앱운영] AdMob 수익 최적화를 위한 배너/전면/리워드 배치 회고"
excerpt: "배너와 전면 광고의 노출 위치를 사용자 흐름 기준으로 재배치하고, 리워드 광고는 미도입 조건을 명확히 정리한 운영 회고입니다."
description: "Horror World와 Siren Soundboard 운영 경험을 바탕으로 AdMob 배너/전면 배치 원칙, 동의 기반 로딩, 리워드 도입 기준을 정리한 회고입니다."

categories:
  - 기타
tags:
  - 기타
  - 앱운영
  - Android
  - AdMob
  - 광고
  - 수익화
date: 2026-03-14 13:01:00 +09:00

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

# 문제/배경

앱 운영에서 광고 수익을 높이려다가 사용성(콘텐츠 가림, 흐름 끊김)이 먼저 망가지는 경우가 자주 생겼습니다.  
실제로 `HorrorWorld`와 `sirenpackage`를 정비하면서, 광고를 많이 넣는 것보다 **언제/어디에/어떤 조건으로 노출하느냐**가 성과를 좌우했습니다.

# 원인

기존 이슈는 크게 세 가지였습니다.

1. 콘텐츠와 광고 레이어 충돌(특히 코드/본문/상세 UI 영역)
2. 준비되지 않은 전면 광고 호출(빈 화면 전환, 체감 끊김)
3. 동의 상태와 무관한 광고 초기화 시도

# 적용 코드/설정

## 1) 동의 상태 기반 광고 로딩

`HorrorWorld`는 UMP 동의 결과를 기준으로 `canRequestAds`를 관리하고, true일 때만 모바일 광고 SDK를 초기화하도록 정리했습니다.

```kotlin
if (!_canRequestAds.value) return
if (!isMobileAdsInitialized.compareAndSet(false, true)) return
MobileAds.initialize(context) {}
```

## 2) 전면 광고는 "게이트 지점"에서만 호출

`GalleryInterstitialAdManager`로 선로딩(`preload`) 후, 실제 노출은 콘텐츠 흐름이 끊기지 않는 지점에서만 `showIfAvailable`를 호출합니다.

```kotlin
val shown = interstitialManager?.showIfAvailable(activity) {
    // 광고 종료 후 다음 동작 진행
} ?: false
```

## 3) 배너는 하단 고정 + 생명주기 연동

`sirenpackage`는 배너를 화면 하단으로 고정하고, `resume/pause/destroy`를 명시해 회전/백그라운드 전환 시 누수를 줄였습니다.

```kotlin
Lifecycle.Event.ON_RESUME -> adView.resume()
Lifecycle.Event.ON_PAUSE -> adView.pause()
Lifecycle.Event.ON_DESTROY -> adView.destroy()
```

## 4) 리워드 광고는 "미도입 기준"을 먼저 정의

리워드 광고는 당장 붙이지 않고, 아래 조건 충족 시에만 도입하도록 정책화했습니다.

- 보상 가치가 명확한 화면(예: 힌트/프리미엄 기능 해제)
- 강제 시청이 아닌 명시적 선택 진입
- 핵심 사용 흐름과 분리된 위치

# 검증 결과

- 콘텐츠/네비게이션을 가리는 광고 이슈가 줄어 UX 불만 포인트가 감소
- 전면 광고 노출 타이밍이 안정되어 "갑작스러운 튐" 체감이 완화
- 동의 상태 기반 로딩으로 정책 대응 및 디버깅 경로가 단순화

# 체크리스트

- [ ] 광고 SDK 초기화가 동의 상태 이후에만 실행되는가
- [ ] 전면 광고는 선로딩 + 게이트 지점 호출로 분리되어 있는가
- [ ] 배너가 콘텐츠 핵심 영역을 가리지 않는가
- [ ] 배너 `resume/pause/destroy`가 화면 생명주기와 동기화되는가
- [ ] 리워드 광고는 "도입 이유/보상/진입 조건"이 문서화되어 있는가

# 관련 글

- [Jetpack Compose + AdMob 전면 광고 겹침 문제 해결기](/기타/compose-admob-interstitial-overlap-fix/)
- [Google Play app-ads.txt 적용 방법과 반영 체크리스트](/기타/google-play-app-ads-txt-checklist/)
- [호러 월드 리빌드 회고: 오래된 앱을 다시 살릴 때 체크한 것들](/기타/horror-world-rebuild-retrospective/)

- - -

 - [기타](/etc)

- - -
