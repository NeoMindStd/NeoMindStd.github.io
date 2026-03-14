---
title:  "[기타/블로그운영] GitHub Pages + Minimal Mistakes 다크모드 토글 적용기"
excerpt: "Minimal Mistakes 블로그에 시스템 테마 연동 다크모드 토글을 추가하고 색상/가독성 회귀를 정리한 구현 기록입니다."
description: "Minimal Mistakes 블로그에 시스템 테마 연동 다크모드 토글을 추가하고 색상/가독성 회귀를 정리한 구현 기록입니다."

categories:
  - 기타
tags:
  - 기타
  - 블로그운영
  - Jekyll
  - Minimal Mistakes
  - 다크모드
  - CSS

date: 2026-03-14 21:00:00 +09:00

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

# 문제/배경

기본 스킨만으로는 야간 가독성이 부족했고, 사용자 디바이스 설정(`prefers-color-scheme`)과 동기화되지 않았습니다.  
그래서 헤더 토글 버튼과 저장형 테마 스크립트를 추가해 라이트/다크 전환을 지원했습니다.

# 원인

적용 전에 확인한 문제:

1. 코드블록/목차/네비의 명암 대비가 다크 배경에서 불균형
2. 테마 상태가 새로고침 시 유지되지 않음
3. 시스템 테마 변경과 사용자 선택 간 우선순위가 불명확

# 적용 코드/설정

주요 변경 위치:

- `_includes/head.html`: 최초 렌더 전에 theme 결정
- `_includes/masthead.html`: 토글 버튼 삽입
- `_includes/footer/custom.html`: 저장/토글/시스템 동기화 스크립트
- `assets/css/main.scss`: dark mode 변수/컴포넌트 override

초기 테마 결정 로직:

```javascript
var storedTheme = localStorage.getItem("nm-theme-preference");
var prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
var resolvedTheme = (storedTheme === "light" || storedTheme === "dark")
  ? storedTheme
  : (prefersDark ? "dark" : "light");
document.documentElement.setAttribute("data-theme", resolvedTheme);
```

# 검증 결과

- 새로고침 후에도 선택한 테마가 유지됨
- 시스템 테마 변경 시 저장값이 없는 사용자에게 자동 반영됨
- 코드블록, TOC, 네비게이션 대비를 별도 보정해 읽기 흐름이 안정됨

# 체크리스트

- [ ] 초기 렌더 전 테마 적용으로 깜빡임(FOUC)이 최소화됐는가
- [ ] 토글 버튼 접근성(aria-label/title)이 현재 상태와 일치하는가
- [ ] 다크모드에서 코드블록/TOC/네비 대비가 충분한가
- [ ] 모바일/데스크톱에서 버튼 위치와 클릭 동선이 자연스러운가
- [ ] localStorage 미지원 상황에서도 기본 테마가 정상 동작하는가

# 관련 글

- [Jekyll SEO 개선기: 메타데이터, robots.txt, 구조화 데이터](/기타/jekyll-seo-metadata-robots-structured-data/)
- [Disqus 댓글 알림 자동화: GitHub Actions + Python](/기타/disqus-comment-alert-github-actions-python/)
- [연재 목록](/series/)

- - -

 - [기타](/etc)

- - -
