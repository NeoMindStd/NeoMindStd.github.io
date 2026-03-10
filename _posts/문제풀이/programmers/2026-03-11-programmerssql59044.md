---
title:  "[프로그래머스/SQL] 오랜 기간 보호한 동물(1)(59044) 풀이"
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
  - JOIN
  - ORDER BY

date: 2026-03-11 00:57:10 +0900

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
 - 문제 링크: [오랜 기간 보호한 동물(1)(59044)](https://school.programmers.co.kr/learn/courses/30/lessons/59044)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

입양 기록이 없는 동물 중
가장 오래 보호소에 있었던 동물 3마리의
이름과 입소 날짜를 조회하는 문제입니다.

## 코드

```sql
SELECT
    INS.NAME,
    INS.DATETIME
FROM ANIMAL_OUTS AS OUTS
    RIGHT OUTER JOIN ANIMAL_INS AS INS
        ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID IS NULL
ORDER BY INS.DATETIME
    LIMIT 3;
```

## 설명

`ANIMAL_INS` 기준으로 입양이 없는 동물을 찾기 위해
`OUTS`를 조인하고 `OUTS.ANIMAL_ID IS NULL` 조건을 사용합니다.

입소 시각 오름차순 정렬 후 `LIMIT 3`으로 상위 3건을 조회합니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

