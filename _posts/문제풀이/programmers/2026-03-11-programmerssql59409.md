---
title:  "[프로그래머스/SQL] 중성화 여부 파악하기(59409) 풀이"
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
  - CASE
  - 문자열

date: 2026-03-11 00:53:10 +0900

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
 - 문제 링크: [중성화 여부 파악하기(59409)](https://school.programmers.co.kr/learn/courses/30/lessons/59409)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_INS`의 `SEX_UPON_INTAKE` 값을 기준으로
중성화(Neutered/Spayed) 여부를 `O`, `X`로 출력하는 문제입니다.

## 코드

```sql
SELECT
    ANIMAL_ID,
    NAME,
    CASE 
        WHEN SEX_UPON_INTAKE LIKE "%Neutered%" OR SEX_UPON_INTAKE LIKE "%Spayed%" 
        THEN "O" 
        ELSE "X" 
    END 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

## 설명

`CASE WHEN`으로 문자열 패턴을 판별해
중성화 여부를 가공 컬럼으로 출력합니다.

`Neutered` 또는 `Spayed`가 포함되면 `O`, 아니면 `X`를 반환합니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

