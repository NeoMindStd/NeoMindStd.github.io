---
title:  "[프로그래머스/SQL] NULL 처리하기(59410) 풀이"
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
  - IS NULL
  - IFNULL

date: 2026-03-10 23:25:10 +0900

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
 - 문제 링크: [NULL 처리하기(59410)](https://school.programmers.co.kr/learn/courses/30/lessons/59410)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS` 테이블에서

 - `ANIMAL_TYPE`
 - `NAME` (`NULL`이면 `"No name"`으로 출력)
 - `SEX_UPON_INTAKE`

를 `ANIMAL_ID` 오름차순으로 조회하면 됩니다.

## 코드

```sql
SELECT 
    ANIMAL_TYPE, 
    IFNULL(NAME, "No name") NAME,
    SEX_UPON_INTAKE 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

## 설명

 - `IFNULL(NAME, "No name")`으로 `NAME`이 `NULL`인 경우를 대체합니다.
 - 정렬 조건은 `ORDER BY ANIMAL_ID`입니다.
 - 요구 컬럼만 선택해 출력 형식을 맞춥니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

