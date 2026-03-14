---
title:  "[프로그래머스/SQL] DATETIME에서 DATE로 형 변환(59414) 풀이"
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
  - DATE_FORMAT
  - SELECT

date: 2026-03-11 00:45:10 +0900

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
 - 문제 링크: [DATETIME에서 DATE로 형 변환(59414)](https://school.programmers.co.kr/learn/courses/30/lessons/59414)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS` 테이블의 `DATETIME`을
`YYYY-MM-DD` 형식의 날짜 문자열로 변환해 출력하는 문제입니다.

## 코드

```sql
SELECT
    ANIMAL_ID,
    NAME,
    DATE_FORMAT(DATETIME, '%Y-%m-%d')날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

## 설명

`DATE_FORMAT` 함수를 사용해
`DATETIME` 값을 날짜 형식(`%Y-%m-%d`)으로 변환합니다.

요구 컬럼을 출력하고 `ANIMAL_ID` 오름차순으로 정렬하면 됩니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

