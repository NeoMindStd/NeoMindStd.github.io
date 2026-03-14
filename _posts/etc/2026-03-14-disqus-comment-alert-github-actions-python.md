---
title:  "[기타/블로그운영] Disqus 댓글 알림 자동화: GitHub Actions + Python"
excerpt: "Disqus 댓글이 달리면 게시글 링크와 함께 메일 알림을 받도록 GitHub Actions와 Python 스크립트로 자동화한 구성입니다."
description: "Disqus 댓글이 달리면 게시글 링크와 함께 메일 알림을 받도록 GitHub Actions와 Python 스크립트로 자동화한 구성입니다."

categories:
  - 기타
tags:
  - 기타
  - 블로그운영
  - Disqus
  - GitHub Actions
  - Python
  - 자동화

date: 2026-03-14 20:30:00 +09:00

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

# 문제/배경

블로그 댓글을 놓치지 않으려면 Disqus 관리자 화면을 수시로 확인해야 했습니다.  
운영 피로도를 줄이기 위해 “신규 댓글이 생기면 메일로 게시글 링크까지 자동 전송”하도록 구성했습니다.

# 원인

수동 확인 방식은 다음 문제가 있었습니다.

1. 댓글 확인이 늦어짐
2. 어떤 글에 달렸는지 빠르게 파악하기 어려움
3. 운영자가 부재 중일 때 대응 누락

# 적용 코드/설정

구성 요소는 2개입니다.

1. 워크플로우: `.github/workflows/disqus-comment-notify.yml`
2. 감지 스크립트: `scripts/disqus_comment_notifier.py`

워크플로우는 10분 주기로 실행되며, 신규 댓글이 있을 때만 메일을 발송합니다.

```yaml
on:
  schedule:
    - cron: "*/10 * * * *"
  workflow_dispatch:
```

Disqus API가 막힐 때를 대비해 RSS 폴백도 같이 넣었습니다.

```python
parser.add_argument(
    "--source",
    choices=["auto", "api", "rss"],
    default="auto",
    help="Comment source mode: api, rss, or auto(api->rss fallback).",
)
```

# 검증 결과

- 신규 댓글 발생 시 게시글 링크, 작성자, 댓글 요약이 메일로 전달됨
- 첫 실행은 과거 댓글 대량 발송을 막기 위해 baseline만 저장하고 스킵
- API 403 상황에서도 RSS 폴백으로 감지가 계속됨

# 체크리스트

- [ ] `DISQUS_API_KEY`, `SMTP_USERNAME`, `SMTP_PASSWORD` 시크릿이 등록됐는가
- [ ] 첫 실행에서 baseline 초기화가 정상 완료됐는가
- [ ] 수동 실행(`workflow_dispatch`) 시 감지 결과 출력이 정상인가
- [ ] 신규 댓글 작성 후 메일 본문에 게시글 링크가 포함되는가
- [ ] API 실패 시 RSS 폴백 로그가 남는가

# 관련 글

- [Disqus 댓글 알림 문서 (GitHub)](https://github.com/NeoMindStd/NeoMindStd.github.io/blob/master/app_docs/disqus-comment-notify.md)
- [Jekyll SEO 개선기: 메타데이터, robots.txt, 구조화 데이터](/기타/jekyll-seo-metadata-robots-structured-data/)

- - -

 - [기타](/etc)

- - -
