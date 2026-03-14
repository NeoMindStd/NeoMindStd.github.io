---
title:  "[기타/프로젝트회고] 사이렌 사운드보드 UX 개선기: 반복/속도/볼륨 설계"
excerpt: "재생 앱에서 가장 자주 건드리는 제어(반복, 속도, 볼륨)를 어떻게 분리하고 저장형 UX로 설계했는지 정리했습니다."
description: "Siren Soundboard의 무한 반복, 마스터/개별 볼륨, 항목별 재생속도, 상세 메뉴 플로우를 Compose 기반으로 개선한 설계 기록입니다."

categories:
  - 기타
tags:
  - 기타
  - 프로젝트회고
  - Android
  - UX
  - Audio
  - SirenSoundboard
date: 2026-03-13 18:20:00 +09:00

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

# 문제/배경

사이렌 사운드 앱은 기능 자체보다 조작 흐름이 중요합니다.  
사용자는 빠르게 재생/중지하고, 필요할 때만 세부 설정(속도/볼륨/시스템 사운드)을 만지길 원합니다.

# 원인

기존 구조는 다음 문제가 있었습니다.

1. 자주 쓰는 제어와 상세 제어가 섞여 있어 화면 집중도가 낮음
2. 항목별 속도/볼륨 조절이 저장형으로 일관되지 않음
3. 다크/라이트/시스템 테마 전환 경험이 분리되어 있지 않음

# 적용 코드/설정

## 1) 제어 레이어 분리

- 메인: 재생, 정지, 무한 반복, 마스터 볼륨
- 상세 메뉴: 항목별 속도/볼륨, 시스템 사운드 설정

`DetailMenuDialog`, `TargetTempoDialog`, `TargetVolumeDialog`로 역할을 나눴습니다.

## 2) 저장형 설정 모델

`SirenSettingsStore`에서 반복, 마스터 볼륨, 항목별 속도/볼륨, 테마 모드를 일관 저장합니다.

```kotlin
const val KEY_INFINITE_LOOP = "infinite_loop_enabled"
const val KEY_MASTER_VOLUME = "master_volume"
const val KEY_THEME_MODE = "theme_mode"
private fun tempoKey(sirenId: SirenId): String = "tempo_${sirenId.name}"
```

## 3) 오디오 재생 안정화

`SirenAudioEngine`에서 로딩 대기/재생 시작/볼륨 변경을 분리하고, 볼륨 페이드 처리로 급격한 음량 변화를 줄였습니다.

```kotlin
fun play(sirenId: SirenId, tempo: Float, volume: Float, loop: Boolean)
fun setMasterVolume(volume: Float)
fun setSirenVolume(sirenId: SirenId, volume: Float)
```

## 4) 테마 모드 통합

`ThemeMode.SYSTEM/LIGHT/DARK`를 앱 전역에서 동일하게 처리해 화면/다이얼로그 톤을 맞췄습니다.

# 검증 결과

- 자주 쓰는 제어를 상단에 고정해 조작 횟수 감소
- 항목별 속도/볼륨 유지로 재실행 시 초기 재설정 부담 감소
- 다크/라이트 전환 시 텍스트 대비와 카드 가독성 개선

# 체크리스트

- [ ] 메인 제어와 상세 제어가 시각적으로 분리되어 있는가
- [ ] 반복/속도/볼륨/테마 값이 앱 재실행 후 복원되는가
- [ ] 항목별 최대 속도 제한이 사운드 특성에 맞게 설정되어 있는가
- [ ] 재생 시작/정지 시 급격한 볼륨 변화가 없는가
- [ ] 상세 메뉴 진입 없이도 핵심 기능(재생/정지/반복/마스터볼륨)을 처리할 수 있는가

# 관련 글

- [프로젝트 소개: 사이렌 사운드보드](/project/siren-soundboard/)
- [Firebase Analytics 이벤트 설계: 앱 운영 기준으로 다시 잡기](/기타/firebase-analytics-event-design/)
- [레거시 안드로이드 앱을 Compose + MVVM으로 리빌드한 과정](/기타/legacy-android-compose-mvvm-rebuild/)

- - -

 - [기타](/etc)

- - -
