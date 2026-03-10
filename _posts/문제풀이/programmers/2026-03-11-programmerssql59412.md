---
title:  "[프로그래머스/SQL] 입양 시각 구하기(1)(59412) 풀이"
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
  - HOUR

date: 2026-03-11 00:59:10 +0900

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
 - 문제 링크: [입양 시각 구하기(1)(59412)](https://school.programmers.co.kr/learn/courses/30/lessons/59412)
 - [문제풀이 코드 GitHub 링크](https://github.com/NeoMindStd/CodingLife/tree/master/programmers/SQL/MySQL)
 - 풀이 DB: MySQL

<br>

# 풀이
## 문제

`ANIMAL_OUTS`에서
입양이 일어난 시간대(9시~19시)별 건수를 집계하는 문제입니다.

## 코드

```sql
SELECT
    HOUR(DATETIME) HOUR,
    COUNT(*) COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR BETWEEN 09 AND 19
ORDER BY HOUR
```

## 설명

`HOUR(DATETIME)`으로 시간대를 추출해 그룹화하고
각 시간의 건수를 `COUNT(*)`로 계산합니다.

`HAVING HOUR BETWEEN 09 AND 19`로 범위를 제한한 뒤
시간 오름차순으로 출력합니다.

- - -

 - [프로그래머스 문제풀이 전체 목록 보기](/programmers)

- - -

