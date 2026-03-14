---
title:  "[프로그래머스/SQL] 중복 제거하기(59408) 풀이"
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
  - DISTINCT
  - COUNT

date: 2026-03-11 00:47:10 +0900

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
 - 문제 링크: [중복 제거하기(59408)](https://school.programmers.co.kr/learn/courses/30/lessons/59408)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS`에서 이름이 있는 동물(`NAME IS NOT NULL`)의
서로 다른 이름 개수를 구하는 문제입니다.

## 코드

```sql
SELECT COUNT(DISTINCT NAME) count FROM ANIMAL_INS WHERE NAME IS NOT NULL
```

## 설명

중복 제거된 이름 개수는 `COUNT(DISTINCT NAME)`으로 구합니다.
`NULL`은 제외해야 하므로 `WHERE NAME IS NOT NULL` 조건을 함께 사용합니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

