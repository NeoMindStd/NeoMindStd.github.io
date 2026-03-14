---
title:  "[기타/블로그운영] Disqus API 403 대응: RSS 폴백 설계와 운영 포인트"
excerpt: "GitHub Actions 환경에서 Disqus API가 403으로 실패할 때, RSS 폴백으로 알림 자동화를 끊기지 않게 만든 운영 패턴을 정리했습니다."
description: "Disqus 댓글 알림 자동화에서 API 403 오류를 RSS 폴백으로 우회한 구조, 상태관리(state), bootstrap 동작, 검증 포인트를 정리했습니다."

categories:
  - 기타
tags:
  - 기타
  - 블로그운영
  - Disqus
  - GitHub Actions
  - Python
  - 자동화
date: 2026-03-14 13:03:00 +09:00

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

# 문제/배경

Disqus 댓글 알림 자동화는 기본적으로 API(`forums/listPosts`)를 사용합니다.  
하지만 GitHub Actions 러너 환경에서는 간헐적으로 `HTTP 403 FORBIDDEN`이 발생해 알림이 중단될 수 있었습니다.

# 원인

1. 외부 러너 IP/환경에 따른 API 접근 차단 가능성
2. API 단일 경로에만 의존한 구조
3. 첫 실행 시 과거 댓글까지 한 번에 알림이 날아갈 위험

# 적용 코드/설정

## 1) 소스 모드: `api`, `rss`, `auto`

`auto` 모드에서 API 실패 시 RSS로 자동 전환되도록 구성했습니다.

```python
parser.add_argument(
    "--source",
    choices=["auto", "api", "rss"],
    default="auto",
    help="Comment source mode: api, rss, or auto(api->rss fallback).",
)
```

## 2) API 실패 시 RSS 폴백

API 호출에서 예외가 나면 경고를 출력하고 `latest.rss`를 읽습니다.

```python
except RuntimeError as exc:
    if args.source == "api":
        raise
    print(f"Disqus API failed ({exc}). Falling back to RSS feed.", file=sys.stderr)
```

## 3) 상태 파일과 부트스트랩

첫 실행은 과거 댓글을 기준 상태로만 저장하고 메일 전송을 건너뜁니다.

```python
bootstrap_run = len(known_comment_ids) == 0 and args.bootstrap_if_empty
if bootstrap_run:
    write_state(state_path, next_known_ids)
```

# 검증 결과

- API 정상 시 `source_used=api`, 장애 시 `source_used=rss`로 연속 운영 가능
- 최초 실행 대량 알림 폭주 없이 baseline 구축
- 이후 신규 댓글만 선별되어 메일 알림 전송

# 체크리스트

- [ ] `--source auto` 또는 환경변수 기본값이 auto로 설정되어 있는가
- [ ] 상태 파일(`.cache/disqus-comment-alert/state.json`)이 유지되는가
- [ ] 첫 실행 bootstrap 시 메일 미발송이 의도대로 동작하는가
- [ ] RSS 파싱 실패 시 로그로 원인 추적이 가능한가
- [ ] GitHub Actions 출력값(`source_used`, `new_comments_count`)이 남는가

# 관련 글

- [Disqus 댓글 알림 자동화: GitHub Actions + Python](/기타/disqus-comment-alert-github-actions-python/)
- [Jekyll SEO 개선기: 메타데이터, robots.txt, 구조화 데이터](/기타/jekyll-seo-metadata-robots-structured-data/)

- - -

 - [기타](/etc)

- - -
