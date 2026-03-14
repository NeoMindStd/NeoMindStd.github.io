---
title:  "[기타/AI] Open WebUI 설치와 사용법: Docker와 pip로 셀프호스팅 AI 워크스페이스 만들기"
excerpt: "Open WebUI를 공식 사이트와 문서 기준으로 설치하고, Docker·pip·uvx 경로와 Ollama/OpenAI 호환 연결 흐름을 정리한 가이드입니다."
description: "Open WebUI 공식 사이트, 빠른 설치 경로, 지원 환경, 첫 로그인 이후 모델 백엔드 연결 흐름을 설명한 글입니다."

categories:
  - 기타
  - AI
tags:
  - 기타
  - AI
  - Open WebUI
  - Self-hosted AI
  - Docker
  - Ollama
date: 2026-03-14 19:43:00 +09:00
permalink: /기타/open-webui-guide/
header:
  og_image: /assets/images/posts/etc/open-webui-guide/official.png
  teaser: /assets/images/posts/etc/open-webui-guide/official.png

toc: true
toc_sticky: true
toc_label: "목차"

published: true
---

- - -

 - [기타](/etc)

- - -

![대표 이미지](/assets/images/posts/etc/open-webui-guide/hero.svg)

![공식 페이지 이미지](/assets/images/posts/etc/open-webui-guide/official.png)

# 어떤 도구인가

Open WebUI는 단순한 채팅 UI가 아니라, Ollama나 OpenAI 호환 API를 붙여 팀용 혹은 개인용 AI 워크스페이스를 꾸리는 데 초점을 둔 도구입니다. 로컬
모델과 클라우드 모델을 한 인터페이스로 묶을 때 특히 편합니다.

개념이나 비교 관점이 먼저 필요하면 [Ollama 설치와 사용법](/기타/ollama-guide/)도 같이 보면 연결이 더 잘 됩니다. Open WebUI와 가장 자주 같이 붙는 로컬 백엔드는 Ollama라서 이 글과 같이 보는 편이 좋습니다.

# 공식 사이트와 다운로드 경로

- 공식 사이트: [Open WebUI 공식 사이트](https://openwebui.com/)
- 다운로드/접속 경로: [Open WebUI Quick Start](https://docs.openwebui.com/getting-started/quick-start/)
- 공식 문서: [Open WebUI 공식 문서](https://docs.openwebui.com/)

# 지원 환경과 설치 방법

## Windows

Windows에서는 Docker Desktop을 이미 쓰고 있다면 Docker 경로가 가장 편합니다. 로컬에서 Python 환경을 관리할 자신이 있다면 `pip` 설치도
가능하지만, 업데이트와 데이터 볼륨 관리까지 생각하면 Docker가 더 무난합니다.

## macOS

macOS 역시 Docker 경로가 가장 단순합니다. Homebrew로 Python 환경을 잘 관리하는 편이라면 `pip install -U open-webui` 또는
`uvx --python 3.11 open-webui` 경로도 선택할 수 있습니다.

## Linux

Linux 서버나 NAS 계열 환경에서는 Docker가 거의 표준 경로에 가깝습니다. 직접 Python으로 올리는 방식도 가능하지만, 서비스 재시작과 데이터 보존까지
생각하면 컨테이너 방식이 더 관리하기 쉽습니다.

# 기본 사용법

Open WebUI는 화면을 먼저 꾸미기보다, 어떤 백엔드를 붙일지부터 정하는 편이 좋습니다. 처음에는 Ollama나 OpenAI 호환 엔드포인트 하나만 연결해서 로그인, 대화, 파일 업로드 흐름이 자연스럽게 도는지만 확인해도 충분합니다.

1. 공식 Quick Start의 Docker 또는 Python 경로로 Open WebUI를 실행합니다.
2. 브라우저에서 초기 계정을 만들고, Settings에서 Ollama 또는 OpenAI 호환 백엔드를 연결합니다.
3. 워크스페이스, 프롬프트, 파일 업로드 흐름을 정리해 개인 또는 팀용 UI로 씁니다.

```bash
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
# 또는
pip install -U open-webui
```

# 어떤 사람에게 잘 맞나

Open WebUI는 Ollama 같은 로컬 백엔드는 있는데, 사람들이 쓰기 쉬운 브라우저 화면이 필요하다는 상황에 잘 맞습니다. 셀프호스팅과 협업용 UI 사이의 균형을
잡기 좋습니다.

# 주의할 점

셀프호스팅 UI이기 때문에 계정, 외부 접속, 저장 데이터, 연결 백엔드의 키 관리가 곧 보안 이슈가 됩니다. 외부에 열어둘 계획이라면 리버스 프록시와 인증 정책을 먼저
생각하는 편이 좋습니다.

# 요약

Open WebUI는 로컬 LLM과 클라우드 API를 사람 친화적인 화면으로 묶어 주는 도구입니다. 공식 Quick Start의 Docker 경로만 익혀도 체감이 빠르고,
이후에 Python 설치나 고급 설정으로 확장하면 됩니다.

# 참고 자료

- [Open WebUI](https://openwebui.com/)
- [Open WebUI Docs](https://docs.openwebui.com/)
- [Open WebUI Quick Start](https://docs.openwebui.com/getting-started/quick-start/)
- [Open WebUI Features](https://docs.openwebui.com/features/)
