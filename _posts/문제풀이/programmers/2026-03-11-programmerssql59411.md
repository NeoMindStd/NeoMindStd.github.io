---
title:  "[프로그래머스/SQL] 오랜 기간 보호한 동물(2)(59411) 풀이"
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

date: 2026-03-11 01:05:10 +0900

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
 - 문제 링크: [오랜 기간 보호한 동물(2)(59411)](https://school.programmers.co.kr/learn/courses/30/lessons/59411)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

입소(`ANIMAL_INS`)와 입양(`ANIMAL_OUTS`) 기록이 모두 있는 동물 중
보호 기간이 가장 긴 동물 2마리의 아이디와 이름을 조회하는 문제입니다.

## 코드

```sql
SELECT
    OUTS.ANIMAL_ID,
    OUTS.NAME
FROM
    ANIMAL_INS AS INS,
    ANIMAL_OUTS AS OUTS
WHERE INS.ANIMAL_ID = OUTS.ANIMAL_ID
ORDER BY 
    OUTS.DATETIME - INS.DATETIME DESC
    LIMIT 2;
```

## 설명

입소/입양 테이블을 `ANIMAL_ID`로 조인한 뒤,
`OUTS.DATETIME - INS.DATETIME` 차이를 기준으로 내림차순 정렬합니다.

가장 오래 보호된 2건만 필요하므로 `LIMIT 2`를 적용합니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

