---
title:  "[기타/블로그운영] Jekyll SEO 개선기: 메타데이터, robots.txt, 구조화 데이터"
excerpt: "GitHub Pages + Minimal Mistakes 블로그에서 검색 노출 품질을 높이기 위해 메타데이터와 robots/sitemap, JSON-LD를 정리한 과정입니다."
description: "GitHub Pages + Minimal Mistakes 블로그에서 검색 노출 품질을 높이기 위해 메타데이터와 robots/sitemap, JSON-LD를 정리한 과정입니다."

categories:
  - 기타
tags:
  - 기타
  - 블로그운영
  - Jekyll
  - SEO
  - Schema
  - GitHub Pages

date: 2026-03-14 12:40:00 +09:00

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

# 문제/배경

포스트 수는 충분했지만, 검색엔진에서 요약 문구/구조화 데이터가 들쭉날쭉해 유입 효율이 낮았습니다.  
그래서 Jekyll 템플릿 레벨에서 SEO 신호를 일관되게 정리했습니다.

# 원인

문제는 개별 포스트 내용보다 템플릿의 일관성 부족이었습니다.

1. 일부 포스트는 `description` 누락
2. JSON-LD가 Person 중심이라 포스트 단위 Article 정보가 약함
3. robots/sitemap/허브 페이지 설명이 운영 의도와 완전히 맞지 않음

# 적용 코드/설정

핵심 수정 포인트:

- `_includes/seo.html`: Article JSON-LD 강화
- `robots.txt`: sitemap 위치 명시
- 허브 페이지(`index`, `series`, `etc`, `projects`, `boj`, `programmers`) 소개문 검색형으로 정리

예시(JSON-LD):

```html
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "...",
  "description": "...",
  "datePublished": "...",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "..." }
}
```

# 검증 결과

- 포스트 HTML에서 `@type: Article`이 일관되게 생성됨
- robots와 sitemap 경로 확인이 단순해져 배포 검증 자동화에 유리해짐
- 허브 문구를 통해 문제풀이 외 운영 글도 탐색 동선에 노출됨

# 체크리스트

- [ ] 모든 포스트에 `title/excerpt/description`이 존재하는가
- [ ] 포스트 HTML에서 canonical + Article JSON-LD가 동시에 노출되는가
- [ ] robots.txt에 sitemap URL이 선언되어 있는가
- [ ] sitemap.xml이 배포 후 200으로 열리는가
- [ ] 허브 페이지 소개문이 실제 콘텐츠 축과 일치하는가

# 관련 글

- [Disqus 댓글 알림 자동화: GitHub Actions + Python](/기타/disqus-comment-alert-github-actions-python/)
- [Minimal Mistakes 다크모드 토글 적용기](/기타/minimal-mistakes-dark-mode-toggle/)
- [연재 목록](/series/)

- - -

 - [기타](/etc)

- - -
