---
title:  "[프로그래머스/SQL] 동명 동물 수 찾기(59041) 풀이"
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
  - GROUP BY
  - HAVING

date: 2026-03-11 00:35:10 +0900

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
 - 문제 링크: [동명 동물 수 찾기(59041)](https://school.programmers.co.kr/learn/courses/30/lessons/59041)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS` 테이블에서
같은 이름을 2번 이상 가진 동물 이름과 개수를 조회하는 문제입니다.

## 코드

```sql
SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) > 1 ORDER BY NAME
```

## 설명

이름별로 그룹화(`GROUP BY NAME`)한 뒤
개수가 2 이상인 그룹만 `HAVING COUNT(NAME) > 1`로 필터링합니다.

정렬은 이름 오름차순(`ORDER BY NAME`)입니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

