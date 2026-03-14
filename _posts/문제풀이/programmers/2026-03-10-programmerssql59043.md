---
title:  "[프로그래머스/SQL] 있었는데요 없었습니다(59043) 풀이"
excerpt: "MySQL을 이용한 프로그래머스 SQL 고득점 Kit 문제풀이"
description: "MySQL을 이용한 프로그래머스 SQL 고득점 Kit 문제풀이"

categories:
  - 문제풀이
tags:
  - 프로그래머스
  - Programmers
  - 문제풀이
  - SQL
  - MySQL
  - JOIN
date: 2026-03-10 21:46:56 +0900

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

# 문제 정보
 - 문제 출처: [프로그래머스 SQL 고득점 Kit](https://school.programmers.co.kr/learn/challenges?order=recent&page=1)
 - 문제 링크: [있었는데요 없었습니다 (59043)](https://school.programmers.co.kr/learn/courses/30/lessons/59043)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이

## 문제

보호 시작(`ANIMAL_INS`) 시간보다
입양(`ANIMAL_OUTS`) 시간이 더 빠른, 즉 데이터상 앞뒤가 뒤바뀐 동물을 찾는 문제입니다.

출력 컬럼은 `ANIMAL_ID`, `NAME`이며
보호 시작 시간 오름차순으로 정렬해야 합니다.

## 코드

```sql
SELECT 
    INS.ANIMAL_ID,
    INS.NAME
FROM 
    ANIMAL_INS AS INS,
    ANIMAL_OUTS AS OUTS
WHERE
    INS.ANIMAL_ID = OUTS.ANIMAL_ID
    AND
    INS.DATETIME > OUTS.DATETIME
ORDER BY INS.DATETIME;
```

## 설명

핵심은 두 테이블을 `ANIMAL_ID`로 조인한 뒤,
시간 조건으로 필터링하는 것입니다.

 - `INS.ANIMAL_ID = OUTS.ANIMAL_ID`로 동일 동물 매칭
 - `INS.DATETIME > OUTS.DATETIME`만 추출
 - 정렬은 `INS.DATETIME` 오름차순

이 조건을 만족하는 레코드가
"보호소에 있었는데, 기록상 더 먼저 나간 것처럼 보이는" 데이터입니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -
