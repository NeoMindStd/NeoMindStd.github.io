---
title:  "[프로그래머스/SQL] 이름이 없는 동물의 아이디(59039) 풀이"
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
  - ORDER BY

date: 2026-03-11 00:33:10 +0900

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
 - 문제 링크: [이름이 없는 동물의 아이디(59039)](https://school.programmers.co.kr/learn/courses/30/lessons/59039)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS` 테이블에서
이름(`NAME`)이 `NULL`인 동물의 `ANIMAL_ID`를
오름차순으로 조회하는 문제입니다.

## 코드

```sql
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NULL ORDER BY ANIMAL_ID
```

## 설명

`NULL` 비교는 `=`가 아니라 `IS NULL`을 사용해야 합니다.
조건을 적용한 뒤 `ANIMAL_ID` 기준으로 정렬하면 됩니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

