# 🚀 LLM Benchmark

<div align="center">

![LLM Benchmark Logo](https://img.shields.io/badge/LLM_Benchmark-4F46E5?style=for-the-badge&logo=rocket&logoColor=white)

**최적의 로컬 AI 모델을 찾기 위한 완벽한 성능 평가 대시보드**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white)](#)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)](#)
[![Local AI](https://img.shields.io/badge/Local_LLM-000000?style=flat-square&logo=probot&logoColor=white)](#)

</div>

## 📌 프로젝트 소개 (About)

**LLM Benchmark**는 로컬 환경에서 구동되는 대규모 언어 모델(LLM)들의 성능을 객관적으로 평가하고 비교 분석할 수 있는 웹 기반 애플리케이션입니다. 

단순한 텍스트 생성 속도(Tokens/s)뿐만 아니라 코딩, 번역, 수학적 논리 추론, 긴 글 요약 등 다양한 시나리오에서의 성능을 측정하며, 직관적인 대시보드를 통해 결과를 한눈에 파악할 수 있습니다. Ollama, LM Studio, vLLM 등 대표적인 로컬 AI 구동 엔진들을 모두 지원하여 사용자 환경에 맞춘 유연한 벤치마킹이 가능합니다.

---

## ✨ 주요 기능 (Key Features)

### 1. ⚡ 다각도 성능 평가 (Multi-Scenario Benchmarking)
단일 목적의 테스트가 아닌, 다양한 실사용 환경을 가정한 프롬프트를 통해 모델의 종합적인 성능을 측정합니다.
* **일반 텍스트 생성** (Basic Text Generation)
* **코드 작성 및 논리** (Code Writing & Logic)
* **다국어 번역 성능** (Translation)
* **수학 및 논리 추론** (Math/Logic Reasoning)
* **긴 텍스트 요약** (Long Text Summarization)
* **짧은 응답 반응속도** (TTFT - Time To First Token)
* **멀티턴 대화 유지력** (Multi-turn Conversation)

### 2. 🔌 다양한 로컬 LLM 엔진 완벽 연동
별도의 설정 없이 포트만 맞추면 즉시 로컬 엔진들과 통신하여 성능을 측정합니다.
* **Ollama** (Port: 11434)
* **LM Studio** (Port: 1234)
* **vLLM** (Port: 8000)

### 3. 💻 하드웨어 모니터링 및 리더보드 (Hardware & Leaderboard)
* **리소스 추적:** 벤치마크 진행 중 시스템 리소스(CPU, RAM 등)를 모니터링하여 가벼운 모델인지 무거운 모델인지 판별합니다.
* **히스토리 및 랭킹:** 과거 벤치마크 결과들을 기록하고, 모델별 성능 순위를 리더보드 형태로 제공하여 어떤 모델이 가장 우수한지 한눈에 비교할 수 있습니다.

### 4. 🌐 완벽한 다국어 및 SEO 지원 (I18n & SEO)
* 브라우저 언어를 감지하여 **한국어(Korean)** 및 **영어(English)** UI를 동적으로 제공합니다.
* 성능 평가용 프롬프트 역시 설정된 언어에 맞춰 자동으로 최적화되어 테스트됩니다.

---

## 🚀 시작하기 (Getting Started)

### 사전 요구 사항 (Prerequisites)
* Python 3.8+ 이상
* 로컬 LLM 실행 환경 (Ollama, LM Studio, vLLM 중 하나 이상 실행 중이어야 함)

### 설치 및 실행 (Installation & Run)

1. 저장소 클론 및 디렉토리 이동
```bash
git clone https://github.com/princebyun/llmBenchmark.git
cd llmBenchmark
```

2. 필수 패키지 설치
```bash
pip install -r requirements.txt
```

3. 애플리케이션 실행
```bash
streamlit run app.py
```

---

## 📬 문의 (Contact)
프로젝트에 대한 버그 리포트, 수정 및 기능 요청사항은 아래 이메일로 편하게 연락주세요.
* **Email:** [princebyun@gmail.com](mailto:princebyun@gmail.com)

<br>
<div align="center">
    Copyright ⓒ 2026 princebyun. All rights reserved.
</div>
