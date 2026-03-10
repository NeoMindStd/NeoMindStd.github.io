---
title:  "[프로젝트] Always Opened Secret Rooms"
excerpt: "The Binding of Isaac: Repentance용 편의성 모드. 새 게임 시작 시 X-ray Vision을 자동 지급해 비밀방 입구를 항상 확인할 수 있게 합니다."

categories:
  - Project
tags:
  - Project
  - Game Mod
  - Steam Workshop
  - Lua
  - The Binding of Isaac

date: 2026-03-09 KST 23:30 +0900

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [프로젝트 전체 목록 보기](/projects)

- - -

# Always Opened Secret Rooms

## 실행 화면

![](/assets/images/posts/projects/always-opened-secret-rooms/thumbnail.jpg){: .align-center}

## 프로젝트 개요

`The Binding of Isaac: Repentance` 모드입니다.  
게임 시작 시 플레이어에게 `X-ray Vision`을 자동 부여해 비밀방과 슈퍼 비밀방 입구를 항상 열려 보이게 만드는 QoL(편의성) 모드입니다.

 - 저장소: [NeoMindStd/AlwaysOpenedSecretRooms](https://github.com/NeoMindStd/AlwaysOpenedSecretRooms)
 - 배포: [Steam Workshop - Always Opened Secret Rooms](https://steamcommunity.com/sharedfiles/filedetails/?id=2489944697)
 - 성과: (2026-03-10 기준) 누적 방문자 6,449명, 현재 구독자 2,724명, 현재 즐겨찾기 174명, 평점 5점(33개 평가), 댓글 11개

## 프로젝트 개발 정보

 - 개발 기간: 2021-05-17 ~ 2021-06-06
 - 출시 일자: 2021-05-17
 - 최신 업데이트: 2021-06-06 (v1.5)
 - 개발 인원: 1
 - 역할: 기획, Lua 구현, Steam Workshop 배포/운영

### 개발 내용

 - `MC_POST_PLAYER_INIT`, `MC_POST_PLAYER_RENDER`, `MC_POST_NEW_LEVEL` 콜백으로 시작 시점/재시작 시점 분기 처리
 - 캐릭터 타입(예: Lilith)과 층 진입 순서를 고려해 중복 지급 버그 방지
 - 이어하기(continue) 상황에서 아이템이 반복 지급되던 이슈 수정
 - Alt Isaac 플레이 시 의도치 않게 지급되는 이슈 수정 후 v1.5 반영

## 실행 및 개발 환경

|:----:|:----|
| **<center>플랫폼</center>** | Steam Workshop (The Binding of Isaac: Repentance) |
| **<center>개발 언어</center>** | Lua |
| **<center>모드 형태</center>** | Gameplay / QoL Tweak |
| **<center>버전</center>** | 1.5 |

## 개발 후기

짧은 코드량으로도 플레이 경험 체감을 크게 바꿀 수 있는 모드 구조를 목표로 했습니다.  
특히 캐릭터별 초기화 시점과 이어하기 동작이 달라 발생하는 예외 케이스를 분리 처리하면서,  
단순 기능이라도 안정적으로 배포/유지보수하려면 이벤트 타이밍 설계가 중요하다는 점을 확인한 프로젝트였습니다.

- - -

 - [프로젝트 전체 목록 보기](/projects)

- - -

