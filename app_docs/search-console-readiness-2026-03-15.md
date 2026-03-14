# Search Console 준비 상태

## 현재 상태

- Search Console API 사용 가능: `no`
- 현재 OAuth 스코프: `https://www.googleapis.com/auth/admob.readonly, https://www.googleapis.com/auth/adsense.readonly`

현재 토큰에는 AdMob/AdSense 읽기 권한만 들어 있어, Search Console 검색어·랜딩페이지·평균순위 데이터를 직접 읽을 수 없습니다.

## 추가로 필요한 스코프

- `https://www.googleapis.com/auth/webmasters`
- `https://www.googleapis.com/auth/webmasters.readonly`

## 다음 단계

1. Google Cloud OAuth 동의 설정에서 Search Console 스코프를 추가합니다.
2. Search Console 접근 권한이 있는 계정으로 OAuth 토큰을 다시 발급합니다.
3. 사이트 속성(`https://neomindstd.github.io/`)이 Search Console에 등록되어 있는지 확인합니다.
4. 재발급 후에는 검색어, 랜딩페이지, 평균순위 데이터를 주간 리뷰에 합칩니다.

