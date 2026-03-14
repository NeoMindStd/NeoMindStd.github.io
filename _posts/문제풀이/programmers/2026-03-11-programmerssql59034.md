---
title:  "[프로그래머스/SQL] 모든 레코드 조회하기(59034) 풀이"
excerpt: "MySQL을 이용한 프로그래머스 SQL 문제풀이"
description: "MySQL을 이용한 프로그래머스 SQL 문제풀이"

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
  - ORDER BY

date: 2026-03-11 00:05:10 +0900

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
 - 문제 링크: [모든 레코드 조회하기(59034)](https://school.programmers.co.kr/learn/courses/30/lessons/59034)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS` 테이블의 모든 컬럼을 조회하고,
`ANIMAL_ID` 기준 오름차순으로 정렬하는 문제입니다.

## 코드

```sql
SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID
```

## 설명

모든 컬럼 조회이므로 `SELECT *`를 사용하고,
정렬 조건은 `ORDER BY ANIMAL_ID`를 적용하면 됩니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

