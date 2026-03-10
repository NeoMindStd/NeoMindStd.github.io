---
title:  "[프로그래머스/SQL] 이름에 el이 들어가는 동물 찾기(59047) 풀이"
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
  - LIKE
  - LOWER

date: 2026-03-11 00:58:10 +0900

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
 - 문제 링크: [이름에 el이 들어가는 동물 찾기(59047)](https://school.programmers.co.kr/learn/courses/30/lessons/59047)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS`에서 동물 타입이 개(`Dog`)이고
이름에 `"el"`이 들어가는 동물의 아이디와 이름을 조회하는 문제입니다.

## 코드

```sql
SELECT
    ANIMAL_ID,
    NAME
FROM ANIMAL_INS
WHERE 
    ANIMAL_TYPE = "Dog" AND 
    LOWER(NAME) LIKE "%El%"
ORDER BY NAME
```

## 설명

대소문자 구분 없이 `"el"` 포함 여부를 확인하기 위해
`LOWER(NAME)`와 `LIKE` 조건을 조합했습니다.

개(`Dog`) 조건을 함께 걸고 이름 기준 오름차순 정렬합니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

