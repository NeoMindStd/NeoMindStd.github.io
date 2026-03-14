---
title:  "[프로그래머스/SQL] 최솟값 구하기(59038) 풀이"
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
  - MIN
  - 집계함수

date: 2026-03-11 00:41:10 +0900

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
 - 문제 링크: [최솟값 구하기(59038)](https://school.programmers.co.kr/learn/courses/30/lessons/59038)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS` 테이블에서
가장 오래된 `DATETIME` 값을 조회하는 문제입니다.

## 코드

```sql
SELECT MIN(DATETIME) 시간 FROM ANIMAL_INS
```

## 설명

최솟값 집계 함수 `MIN`을 사용해
`DATETIME` 컬럼의 가장 작은 값을 구합니다.

출력 컬럼 별칭은 `시간`으로 지정했습니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

