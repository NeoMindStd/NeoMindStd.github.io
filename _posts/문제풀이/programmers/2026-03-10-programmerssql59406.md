---
title:  "[프로그래머스/SQL] 동물 수 구하기(59406) 풀이"
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
  - COUNT
  - 집계함수

date: 2026-03-10 23:38:10 +0900

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
 - 문제 링크: [동물 수 구하기(59406)](https://school.programmers.co.kr/learn/courses/30/lessons/59406)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS` 테이블에 있는 동물의 총 개수를 구하는 문제입니다.

## 코드

```sql
SELECT COUNT(*) count FROM ANIMAL_INS
```

## 설명

`COUNT(*)`로 전체 행 수를 집계하면 됩니다.
결과 컬럼명은 `count`로 지정했습니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

