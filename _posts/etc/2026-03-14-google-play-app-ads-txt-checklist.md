---
title:  "[기타/앱운영] Google Play app-ads.txt 적용 방법과 반영 체크리스트"
excerpt: "Google Play 앱에 app-ads.txt를 연결할 때 실제 운영에서 확인했던 반영 포인트와 점검 순서를 정리했습니다."
description: "Google Play 앱에 app-ads.txt를 연결할 때 실제 운영에서 확인했던 반영 포인트와 점검 순서를 정리했습니다."

categories:
  - 기타
tags:
  - 기타
  - 앱운영
  - Android
  - AdMob
  - app-ads.txt
  - Google Play

date: 2026-03-14 20:10:00 +09:00

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

# 문제/배경

AdMob 수익이 집계되기 시작한 뒤, 앱 단위의 광고 신뢰성 이슈를 줄이기 위해 `app-ads.txt`를 정리했습니다.  
웹 `ads.txt`만 맞춰두면 끝나는 줄 알기 쉽지만, 앱은 Play Console의 개발자 웹사이트/앱 URL/파일 경로가 모두 맞아야 실제 반영이 안정적으로 진행됩니다.

# 원인

`app-ads.txt` 문제는 대부분 아래 세 가지에서 발생했습니다.

1. Play Console에 등록된 앱 URL과 실제 호스팅 URL 불일치
2. 파일 경로는 맞지만 내용 포맷(`publisher id`, `seller type`) 오기
3. 반영 대기 시간을 고려하지 않고 즉시 실패로 판단

# 적용 코드/설정

현재 블로그/앱 경로에서는 동일한 포맷으로 파일을 관리합니다.

```text
google.com, pub-5609154832705787, DIRECT, f08c47fec0942fa0
```

운영 중인 실제 파일 경로:

- `/app-ads.txt`
- `/project/horror-world/app-ads.txt`
- `/project/siren-soundboard/app-ads.txt`

# 검증 결과

적용 이후에는 앱 상세 페이지와 웹 경로가 연결된 상태에서 누락 경고 없이 유지되고 있습니다.  
핵심은 파일 내용보다도 “Play Console에 저장된 URL과 동일 도메인에서 파일을 서빙하는지”를 먼저 확인하는 것이었습니다.

# 체크리스트

- [ ] Play Console 앱 설정에 공개 URL이 정확히 등록되어 있는가
- [ ] `app-ads.txt`가 공개 URL 기준 루트에서 200으로 열리는가
- [ ] 파일 첫 줄 포맷이 `google.com, pub-..., DIRECT, f08c47...` 형식인가
- [ ] 앱별 하위 경로에서 중복 파일을 쓸 경우 내용이 동일한가
- [ ] 수정 직후 최소 24~48시간은 반영 지연을 감안했는가

# 관련 글

- [프로젝트: 호러 월드](/project/horror-world)
- [프로젝트: 사이렌 사운드보드](/project/siren-soundboard)
- [Jetpack Compose + AdMob 전면 광고 겹침 문제 해결기](/기타/compose-admob-interstitial-overlap-fix/)

- - -

 - [기타](/etc)

- - -
