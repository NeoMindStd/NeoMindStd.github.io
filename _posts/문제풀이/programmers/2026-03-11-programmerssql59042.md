---
title:  "[프로그래머스/SQL] 없어진 기록 찾기(59042) 풀이"
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
  - LEFT JOIN

date: 2026-03-11 00:46:10 +0900

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
 - 문제 링크: [없어진 기록 찾기(59042)](https://school.programmers.co.kr/learn/courses/30/lessons/59042)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

입양 정보(`ANIMAL_OUTS`)는 있는데
보호소 입소 정보(`ANIMAL_INS`)는 없는 동물의
`ANIMAL_ID`, `NAME`을 조회하는 문제입니다.

## 코드

```sql
SELECT 
	OUTS.ANIMAL_ID, 
	OUTS.NAME 
FROM ANIMAL_OUTS AS OUTS 
    LEFT OUTER JOIN ANIMAL_INS AS INS
        ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL
ORDER BY OUTS.ANIMAL_ID;
```

## 설명

`ANIMAL_OUTS`를 기준으로 `LEFT JOIN`하면
`ANIMAL_INS`에 없는 레코드는 `INS.*`가 `NULL`이 됩니다.

따라서 `WHERE INS.ANIMAL_ID IS NULL` 조건으로
입소 기록이 없는 입양 기록만 필터링할 수 있습니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

