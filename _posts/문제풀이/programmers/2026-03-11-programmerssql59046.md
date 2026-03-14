---
title:  "[프로그래머스/SQL] 루시와 엘라 찾기(59046) 풀이"
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
  - WHERE
  - IN

date: 2026-03-11 00:51:10 +0900

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
 - 문제 링크: [루시와 엘라 찾기(59046)](https://school.programmers.co.kr/learn/courses/30/lessons/59046)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS` 테이블에서
이름이 특정 목록(`Lucy`, `Ella`, `Pickle`, `Rogan`, `Sabrina`, `Mitty`)에 포함되는 동물 정보를 조회하는 문제입니다.

## 코드

```sql
SELECT
    ANIMAL_ID,
    NAME,
    SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty")
ORDER BY ANIMAL_ID
```

## 설명

여러 문자열 조건 매칭은 `IN (...)`으로 간단히 처리합니다.
조건에 맞는 행을 `ANIMAL_ID` 오름차순으로 출력하면 됩니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

