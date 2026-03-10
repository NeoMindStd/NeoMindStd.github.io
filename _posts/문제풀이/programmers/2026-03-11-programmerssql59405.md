---
title:  "[프로그래머스/SQL] 상위 n개 레코드(59405) 풀이"
excerpt: "MySQL을 이용한 프로그래머스 SQL 문제풀이"

categories:
  - 문제풀이
tags:
  - 프로그래머스
  - Programmers
  - 문제풀이
  - PS
  - SQL
  - MySQL
  - SELECT
  - LIMIT

date: 2026-03-11 00:11:10 +0900

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

# 문제 정보
 - 문제 출처: [프로그래머스 코딩테스트 연습](https://school.programmers.co.kr/learn/challenges?order=recent&page=1)
 - 문제 링크: [상위 n개 레코드(59405)](https://school.programmers.co.kr/learn/courses/30/lessons/59405)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS` 테이블에서
가장 먼저 들어온 동물의 이름 1개를 조회하는 문제입니다.

## 코드

```sql
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1
```

## 설명

입소 시각이 가장 이른 행이 필요하므로
`DATETIME` 오름차순 정렬 후 `LIMIT 1`을 적용하면 됩니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

