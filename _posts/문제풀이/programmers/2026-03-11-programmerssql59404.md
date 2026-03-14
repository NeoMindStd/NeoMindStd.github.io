---
title:  "[프로그래머스/SQL] 여러 기준으로 정렬하기(59404) 풀이"
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
  - ORDER BY
  - 정렬

date: 2026-03-11 00:52:10 +0900

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
 - 문제 링크: [여러 기준으로 정렬하기(59404)](https://school.programmers.co.kr/learn/courses/30/lessons/59404)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS`에서 `ANIMAL_ID`, `NAME`, `DATETIME`을 조회하고
이름 오름차순, 이름이 같으면 입소 시각 내림차순으로 정렬하는 문제입니다.

## 코드

```sql
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC
```

## 설명

`ORDER BY NAME, DATETIME DESC`를 사용하면
1차 기준은 이름 오름차순, 2차 기준은 날짜 내림차순이 됩니다.

문제 요구와 정렬 기준이 정확히 일치합니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

