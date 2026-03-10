---
title:  "[프로그래머스/SQL] 역순 정렬하기(59035) 풀이"
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
  - ORDER BY
  - SELECT

date: 2026-03-11 00:17:10 +0900

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
 - 문제 링크: [역순 정렬하기(59035)](https://school.programmers.co.kr/learn/courses/30/lessons/59035)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS` 테이블에서
`NAME`, `DATETIME`을 조회하고
`ANIMAL_ID` 기준 내림차순으로 정렬하는 문제입니다.

## 코드

```sql
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC
```

## 설명

출력 컬럼을 선택한 뒤,
정렬 조건을 `ORDER BY ANIMAL_ID DESC`로 주면 요구사항을 만족합니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

