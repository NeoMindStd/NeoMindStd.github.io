---
title:  "[프로그래머스/SQL] 고양이와 개는 몇 마리 있을까(59040) 풀이"
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
  - GROUP BY
  - COUNT

date: 2026-03-11 00:34:10 +0900

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
 - 문제 링크: [고양이와 개는 몇 마리 있을까(59040)](https://school.programmers.co.kr/learn/courses/30/lessons/59040)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS` 테이블에서
동물 타입(`ANIMAL_TYPE`)별 개수를 구하되,
고양이(`Cat`)와 개(`Dog`)만 조회하는 문제입니다.

## 코드

```sql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) count FROM ANIMAL_INS GROUP BY ANIMAL_TYPE HAVING ANIMAL_TYPE IN ("Cat", "Dog") ORDER BY ANIMAL_TYPE
```

## 설명

`GROUP BY ANIMAL_TYPE`로 타입별 집계를 만든 뒤,
`HAVING ... IN ("Cat", "Dog")`로 필요한 타입만 남깁니다.

마지막으로 타입명 기준 정렬을 적용합니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

