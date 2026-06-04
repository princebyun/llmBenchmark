
# -*- coding: utf-8 -*-
import streamlit as st

MODEL_WIKI_DATA = {
    "Meta Llama 3 시리즈 (8B, 70B)": {
        "title": "Meta Llama 3 시리즈 (8B, 70B)",
        "description": "로컬 LLM의 절대적인 기준점. 8B와 70B 두 가지 체급으로 제공되는 최고 성능의 모델입니다.",
        "developer": "Meta AI",
        "architecture": "트랜스포머 디코더, 8K 컨텍스트, Grouped Query Attention(GQA). 15조 토큰 학습.",
        "pros_cons": """**장점 (Pros):**\n- 체급 대비 압도적 지능, 훌륭한 한국어 지원, 거대한 생태계\n\n**단점 (Cons):**\n- 기본 컨텍스트 길이가 8K로 긴 문서 처리에 불리함""",
        "use_cases": "- 일상적인 챗봇, 코드 생성, 텍스트 요약",
        "benchmark": "8B: 6GB VRAM / 70B: 40GB VRAM"
    },
    "Meta Llama 2 시리즈 (7B, 13B, 70B)": {
        "title": "Meta Llama 2 시리즈 (7B, 13B, 70B)",
        "description": "오픈소스 LLM 생태계를 폭발적으로 성장시킨 전설적인 이전 세대 모델입니다.",
        "developer": "Meta AI",
        "architecture": "트랜스포머 기반, 4K 컨텍스트.",
        "pros_cons": """**장점 (Pros):**\n- 안정적이고 가장 많은 파인튜닝 레퍼런스 보유\n\n**단점 (Cons):**\n- 최신 모델 대비 떨어지는 지능 및 한국어 능력""",
        "use_cases": "- 레거시 시스템 유지보수, 파인튜닝 교육용",
        "benchmark": "7B: 5.5GB / 13B: 8.5GB / 70B: 40GB VRAM"
    },
    "CodeLlama 시리즈 (7B~70B)": {
        "title": "CodeLlama 시리즈 (7B~70B)",
        "description": "Llama 2를 기반으로 코딩 능력을 극대화한 개발자용 모델입니다.",
        "developer": "Meta AI",
        "architecture": "최대 100K 토큰 지원, 파이썬/C++ 등 특화 학습.",
        "pros_cons": """**장점 (Pros):**\n- 광범위한 언어 지원, 매우 긴 코드 컨텍스트 이해\n\n**단점 (Cons):**\n- 일반적인 대화나 한국어 질문에는 취약함""",
        "use_cases": "- 로컬 Copilot 연동, 코드 자동 완성",
        "benchmark": "체급에 따라 5.5GB ~ 40GB VRAM"
    },
    "Google Gemma 2 시리즈 (2B, 9B, 27B)": {
        "title": "Google Gemma 2 시리즈 (2B, 9B, 27B)",
        "description": "제미나이(Gemini) 기술로 빚어낸 강력하고 가벼운 최신 오픈 모델 라인업입니다.",
        "developer": "Google DeepMind",
        "architecture": "8K 컨텍스트, Sliding Window Attention 적용.",
        "pros_cons": """**장점 (Pros):**\n- Llama 3를 위협하는 강력한 벤치마크 점수 및 팩트 정확도\n\n**단점 (Cons):**\n- 특이한 파라미터 수(9B, 27B)로 인한 애매한 VRAM 요구량""",
        "use_cases": "- 학술 논문 분석, 정확한 정보 검색",
        "benchmark": "9B: 6.5GB / 27B: 18GB VRAM"
    },
    "Google Gemma 1 시리즈 (2B, 7B)": {
        "title": "Google Gemma 1 시리즈 (2B, 7B)",
        "description": "Gemma 라인업의 첫 번째 세대 모델입니다.",
        "developer": "Google DeepMind",
        "architecture": "Gemma 오리지널 아키텍처.",
        "pros_cons": """**장점 (Pros):**\n- 모바일(2B)에서도 구동 가능한 범용성\n\n**단점 (Cons):**\n- 한국어 번역투 심함, 잦은 환각(Hallucination)""",
        "use_cases": "- 저전력 디바이스(Edge) 텍스트 처리",
        "benchmark": "2B: 2.5GB / 7B: 5.5GB VRAM"
    },
    "Qwen 2 시리즈 (0.5B ~ 72B)": {
        "title": "Qwen 2 시리즈 (0.5B ~ 72B)",
        "description": "현존 오픈소스 중 최고의 다국어 처리 능력과 코딩 능력을 자랑하는 모델입니다.",
        "developer": "Alibaba Cloud",
        "architecture": "최대 128K 컨텍스트, 29개국어 사전 학습.",
        "pros_cons": """**장점 (Pros):**\n- 놀랍도록 자연스러운 한국어 구사, 수학/코딩 최상위권\n\n**단점 (Cons):**\n- 서구권 중심의 문화적/역사적 지식 부족""",
        "use_cases": "- 다국어 번역기, 논리적 수학 문제 풀이",
        "benchmark": "7B: 5.5GB / 72B: 42GB VRAM"
    },
    "Qwen 1.5 시리즈 (0.5B ~ 110B)": {
        "title": "Qwen 1.5 시리즈 (0.5B ~ 110B)",
        "description": "다양한 파라미터 선택지(14B, 32B 등)를 제공했던 훌륭한 이전 세대 모델입니다.",
        "developer": "Alibaba Cloud",
        "architecture": "32K 컨텍스트.",
        "pros_cons": """**장점 (Pros):**\n- 내 그래픽카드 VRAM에 딱 맞게 고를 수 있는 다양한 체급\n\n**단점 (Cons):**\n- Qwen 2 출시로 인한 성능 우위 상실""",
        "use_cases": "- 특정 VRAM(16GB 등) 환경에 맞춘 서버 구축",
        "benchmark": "14B: 9GB / 32B: 20GB VRAM"
    },
    "Qwen-VL / Audio": {
        "title": "Qwen-VL / Audio",
        "description": "텍스트뿐만 아니라 이미지와 소리까지 이해하는 멀티모달(Multimodal) 모델입니다.",
        "developer": "Alibaba Cloud",
        "architecture": "시각 및 청각 인코더가 결합된 아키텍처.",
        "pros_cons": """**장점 (Pros):**\n- 이미지 안의 글씨(OCR)나 상황을 정확히 인식함\n\n**단점 (Cons):**\n- 텍스트 전용 모델보다 VRAM을 훨씬 많이 차지함""",
        "use_cases": "- 이미지 캡셔닝, 시각 장애인용 사진 묘사",
        "benchmark": "최소 10GB VRAM 이상"
    },
    "Microsoft Phi-3 (Mini, Small, Medium)": {
        "title": "Microsoft Phi-3 (Mini, Small, Medium)",
        "description": "SLM(소형언어모델)의 기적. 아주 작은 크기로 GPT-3.5급 논리를 펼칩니다.",
        "developer": "Microsoft",
        "architecture": "교과서(Textbook) 수준의 정제된 고품질 데이터 집중 훈련.",
        "pros_cons": """**장점 (Pros):**\n- 극도로 적은 VRAM 소모, 압도적인 논리력\n\n**단점 (Cons):**\n- 세상의 모든 지식을 담기엔 모델 뇌가 너무 작아 환각 발생""",
        "use_cases": "- 오프라인 모바일 앱, 단순 텍스트 요약",
        "benchmark": "Mini(3.8B): 3GB / Medium(14B): 9GB VRAM"
    },
    "WizardLM 시리즈 (7B ~ 70B)": {
        "title": "WizardLM 시리즈 (7B ~ 70B)",
        "description": "지시 복잡성(Instruction Complexity)을 훈련시켜 명령 수행력을 높인 모델입니다.",
        "developer": "Microsoft/WizardLM",
        "architecture": "Evol-Instruct 기법 적용.",
        "pros_cons": """**장점 (Pros):**\n- 복잡하고 여러 단계로 꼬인 사용자의 지시를 정확히 따름\n\n**단점 (Cons):**\n- 최신 베이스 모델(Llama 3 등) 미적용 시 성능 한계""",
        "use_cases": "- 복합적인 명령을 내리는 비서",
        "benchmark": "체급별 상이 (5.5GB ~ 40GB)"
    },
    "Mistral 7B & NeMo 12B": {
        "title": "Mistral 7B & NeMo 12B",
        "description": "오픈소스 생태계를 이끌어온 미스트랄의 핵심 단일(Dense) 모델 라인업입니다.",
        "developer": "Mistral AI",
        "architecture": "GQA, SWA(Sliding Window Attention), Tekken 토크나이저.",
        "pros_cons": """**장점 (Pros):**\n- 체급을 뛰어넘는 가성비, 검열이 적은 자유로운 텍스트\n\n**단점 (Cons):**\n- 안전장치가 부족해 상용 서비스 시 필터링 주의""",
        "use_cases": "- 창의적 글쓰기, 웹소설 작성",
        "benchmark": "7B: 5.5GB / 12B: 8GB VRAM"
    },
    "Mixtral (8x7B, 8x22B)": {
        "title": "Mixtral (8x7B, 8x22B)",
        "description": "여러 명의 전문가(Expert)가 협력하는 MoE 아키텍처 모델입니다.",
        "developer": "Mistral AI",
        "architecture": "MoE(Mixture of Experts) 방식. 활성 파라미터는 전체의 약 1/4 수준.",
        "pros_cons": """**장점 (Pros):**\n- 거대한 지식량을 가졌음에도 답변 출력 속도가 매우 빠름\n\n**단점 (Cons):**\n- 메모리(VRAM) 자체는 전체 크기만큼 거대하게 다 차지함""",
        "use_cases": "- 기업용 다목적 챗봇, 종합 지식 검색",
        "benchmark": "8x7B: 26GB / 8x22B: 80GB VRAM"
    },
    "DeepSeek Coder (1.3B ~ 33B, V2)": {
        "title": "DeepSeek Coder (1.3B ~ 33B, V2)",
        "description": "전 세계 수많은 프로그래머들의 로컬 코파일럿으로 쓰이는 코딩 모델입니다.",
        "developer": "DeepSeek AI",
        "architecture": "2조 토큰 이상의 방대한 코드 및 수학 데이터 집중 학습.",
        "pros_cons": """**장점 (Pros):**\n- 어지간한 70B 범용 모델을 압도하는 정교한 코드 작성 능력\n\n**단점 (Cons):**\n- 코딩 이외의 일반 대화는 다소 부자연스러움""",
        "use_cases": "- 로컬 코드 에디터 연동, 사내 코드 리뷰",
        "benchmark": "6.7B: 5.5GB / 33B: 20GB VRAM"
    },
    "DeepSeek LLM (7B, 67B)": {
        "title": "DeepSeek LLM (7B, 67B)",
        "description": "딥시크 기술력의 기반이 되는 강력한 범용 언어 모델입니다.",
        "developer": "DeepSeek AI",
        "architecture": "중국어와 영어 중심의 대규모 사전 학습.",
        "pros_cons": """**장점 (Pros):**\n- 수학적 사고력이 훌륭하고 매우 빠른 응답성\n\n**단점 (Cons):**\n- 한국어 번역이나 대화 시 어색함이 남음""",
        "use_cases": "- 수학 논문 요약, 영-중 번역",
        "benchmark": "7B: 5.5GB / 67B: 38GB VRAM"
    },
    "Upstage Solar 10.7B": {
        "title": "Upstage Solar 10.7B",
        "description": "대한민국의 업스테이지가 만들어 글로벌 1위를 달성했던 명작 모델입니다.",
        "developer": "Upstage",
        "architecture": "Depth Up-Scaling (DUS) 기법을 통한 Llama 2 기반 확장 아키텍처.",
        "pros_cons": """**장점 (Pros):**\n- 10B 체급에서 30B를 이기는 벤치마크, 훌륭한 한국어 이해\n\n**단점 (Cons):**\n- 최신 세대 모델들의 등장으로 가성비 약간 하락""",
        "use_cases": "- 한국어 중심의 챗봇 서비스 구축",
        "benchmark": "7.5GB VRAM"
    },
    "Upstage Solar Pro": {
        "title": "Upstage Solar Pro",
        "description": "Solar 10.7B의 성공을 잇는 최신 업그레이드 버전입니다.",
        "developer": "Upstage",
        "architecture": "대폭 개선된 한국어 튜닝 및 컨텍스트 확장.",
        "pros_cons": """**장점 (Pros):**\n- 더욱 매끄러워진 한국어 문장력과 논리 추론\n\n**단점 (Cons):**\n- 해외 모델 대비 상대적으로 좁은 생태계 지원""",
        "use_cases": "- 국내 기업용 사내망 AI 엔진",
        "benchmark": "8GB VRAM"
    },
    "Falcon (7B, 40B, 180B)": {
        "title": "Falcon (7B, 40B, 180B)",
        "description": "UAE에서 막대한 자본으로 훈련시켜 상업적 무료로 푼 혁신적 모델 라인업입니다.",
        "developer": "TII",
        "architecture": "커스텀 트랜스포머 아키텍처.",
        "pros_cons": """**장점 (Pros):**\n- 상업적 제약이 전혀 없는 완전한 오픈 라이선스, 방대한 지식(180B)\n\n**단점 (Cons):**\n- 구형 아키텍처로 인한 속도 및 토큰 효율성 저하""",
        "use_cases": "- 라이선스 제약 없는 상용 서비스망 구축",
        "benchmark": "40B: 24GB / 180B: 100GB 이상"
    },
    "Yi 시리즈 (6B, 34B)": {
        "title": "Yi 시리즈 (6B, 34B)",
        "description": "중국 01.AI의 역작으로 긴 텍스트 문맥 유지에 특화된 모델입니다.",
        "developer": "01.AI",
        "architecture": "최대 200K의 압도적인 컨텍스트 길이 지원.",
        "pros_cons": """**장점 (Pros):**\n- 소설책 수십 권 분량을 한 번에 기억하는 엄청난 장기 기억력\n\n**단점 (Cons):**\n- 긴 컨텍스트 사용 시 급격히 증가하는 VRAM 소모량""",
        "use_cases": "- 장편 소설 번역, 방대한 법률/의료 문서 검토",
        "benchmark": "6B: 5GB / 34B: 22GB VRAM"
    },
    "Command R (35B)": {
        "title": "Command R (35B)",
        "description": "RAG(검색 증강 생성)와 외부 도구(API) 사용에 극도로 특화된 모델입니다.",
        "developer": "Cohere",
        "architecture": "35B 파라미터, 도구 사용(Tool Use) 특화 학습, 128K 컨텍스트.",
        "pros_cons": """**장점 (Pros):**\n- 주어진 문서를 바탕으로 가장 정확하게 답변을 뽑아냄 (환각 최소화)\n\n**단점 (Cons):**\n- 로컬 구동 시 무거운 체급""",
        "use_cases": "- 기업 사내 문서 기반 검색(RAG) 시스템",
        "benchmark": "22GB VRAM"
    },
    "Command R+ (104B)": {
        "title": "Command R+ (104B)",
        "description": "Command R의 성능을 극한으로 끌어올린 엔터프라이즈급 104B 거대 모델입니다.",
        "developer": "Cohere",
        "architecture": "104B 파라미터, 다국어 RAG 성능 최적화.",
        "pros_cons": """**장점 (Pros):**\n- 오픈소스 최고 수준의 정확도와 도구 제어 능력\n\n**단점 (Cons):**\n- 개인 장비로는 절대 불가능한 엄청난 하드웨어 요구""",
        "use_cases": "- 거대 데이터센터용 복합 에이전트 구축",
        "benchmark": "최소 60GB VRAM"
    },
    "DBRX (132B)": {
        "title": "DBRX (132B)",
        "description": "데이터브릭스가 공개한 132B 크기의 초대형 오픈소스 MoE 모델입니다.",
        "developer": "Databricks",
        "architecture": "세밀한 MoE (Fine-grained Mixture-of-Experts) 아키텍처.",
        "pros_cons": """**장점 (Pros):**\n- 빠른 속도와 강력한 코딩/수학/논리 퍼포먼스\n\n**단점 (Cons):**\n- 무거운 용량""",
        "use_cases": "- 대규모 기업용 분석 시스템",
        "benchmark": "80GB VRAM 이상"
    },
    "Grok-1 (314B)": {
        "title": "Grok-1 (314B)",
        "description": "일론 머스크의 xAI가 공개한 현존 최대 크기의 314B 오픈소스 모델입니다.",
        "developer": "xAI",
        "architecture": "MoE 아키텍처, 314B 파라미터.",
        "pros_cons": """**장점 (Pros):**\n- 상상을 초월하는 거대한 지식량과 재치 있는 답변 스타일\n\n**단점 (Cons):**\n- 슈퍼컴퓨터 급 장비가 아니면 다운로드조차 부담스러움""",
        "use_cases": "- 대규모 AI 클러스터 연구용",
        "benchmark": "최소 200GB VRAM 이상"
    },
    "Vicuna (7B, 13B, 33B)": {
        "title": "Vicuna (7B, 13B, 33B)",
        "description": "가장 오랜 기간 사랑받아 온 대화형(Chat) 튜닝의 교과서 모델입니다.",
        "developer": "LMSYS",
        "architecture": "ShareGPT의 고품질 사용자 대화 데이터로 파인튜닝.",
        "pros_cons": """**장점 (Pros):**\n- 마치 진짜 사람과 채팅하는 듯한 부드럽고 찰진 대화 톤\n\n**단점 (Cons):**\n- 최신 지식 및 다국어 지원 부족""",
        "use_cases": "- 챗봇 UI/UX 프로토타입 제작",
        "benchmark": "체급별 상이"
    },
    "Zephyr (7B, 141B)": {
        "title": "Zephyr (7B, 141B)",
        "description": "DPO(직접 선호 최적화) 기술을 널리 알린 매우 친절한 성격의 모델입니다.",
        "developer": "Hugging Face H4",
        "architecture": "미스트랄 및 Mixtral 베이스에 DPO 강화학습 적용.",
        "pros_cons": """**장점 (Pros):**\n- 사용자의 지시를 매우 긍정적이고 헌신적으로 수행함\n\n**단점 (Cons):**\n- 한국어로 물으면 영어로 대답하려는 경향""",
        "use_cases": "- 영문 기반 친절한 고객지원 봇",
        "benchmark": "7B: 5.5GB / 141B: 80GB VRAM"
    },
    "OpenChat 3.5": {
        "title": "OpenChat 3.5",
        "description": "오픈소스 데이터만으로 벤치마크 상위권을 장악했던 기적의 튜닝 모델입니다.",
        "developer": "OpenChat",
        "architecture": "C-RLFT 기법 (조건부 강화학습).",
        "pros_cons": """**장점 (Pros):**\n- 7B라는 작은 크기에서 나오는 완벽에 가까운 코딩과 일상 대화\n\n**단점 (Cons):**\n- Llama 3 등장 이후 포지션이 겹쳐 사용 빈도 감소""",
        "use_cases": "- 범용적인 로컬 비서",
        "benchmark": "5.5GB VRAM"
    },
    "TinyLlama 1.1B": {
        "title": "TinyLlama 1.1B",
        "description": "웹 브라우저에서도 돌아갈 수 있게 만든 초미니 장난감(Toy) 모델입니다.",
        "developer": "Open Source",
        "architecture": "1.1B 초소형 아키텍처, 3조 토큰 학습.",
        "pros_cons": """**장점 (Pros):**\n- 이론상 라즈베리파이나 스마트워치에서도 구동되는 극한의 가벼움\n\n**단점 (Cons):**\n- 한국어 불가, 복잡한 논리 불가""",
        "use_cases": "- LLM 원리 교육 및 구조 테스트",
        "benchmark": "1.5GB VRAM 미만"
    },
    "StarCoder 2 (3B, 7B, 15B)": {
        "title": "StarCoder 2 (3B, 7B, 15B)",
        "description": "전 세계 개발자들이 연합하여 구축한 순수 오픈소스 코드 생성기입니다.",
        "developer": "BigCode",
        "architecture": "600개 이상의 프로그래밍 언어로 훈련됨.",
        "pros_cons": """**장점 (Pros):**\n- 거의 모든 마이너한 프로그래밍 언어까지 커버하는 방대한 코드 지식\n\n**단점 (Cons):**\n- 대화형(Chat) 능력이 심각하게 결여됨""",
        "use_cases": "- VSC 백그라운드 자동완성 서버",
        "benchmark": "15B: 10GB VRAM"
    },
    "Jamba": {
        "title": "Jamba",
        "description": "전통적인 트랜스포머의 한계를 깬 혁신적인 하이브리드 모델입니다.",
        "developer": "AI21 Labs",
        "architecture": "Mamba (SSM) + Transformer 하이브리드 아키텍처.",
        "pros_cons": """**장점 (Pros):**\n- 엄청나게 긴 텍스트를 처리할 때도 VRAM과 연산량이 크게 늘지 않음\n\n**단점 (Cons):**\n- 아직 지원하는 생태계 툴(Ollama 등)이 제한적임""",
        "use_cases": "- 장편 소설 한 권 전체 분석",
        "benchmark": "12GB VRAM"
    },
    "OLMo (1B, 7B)": {
        "title": "OLMo (1B, 7B)",
        "description": "AI 연구의 투명성을 위해 학습 코드와 데이터까지 전부 공개한 100% 진정한 오픈 모델입니다.",
        "developer": "Allen AI",
        "architecture": "학습 데이터(Dolma)와 트레이닝 스크립트 완전 공개.",
        "pros_cons": """**장점 (Pros):**\n- 데이터 출처가 투명하여 라이선스 분쟁의 여지가 없음\n\n**단점 (Cons):**\n- 타 7B 모델 대비 벤치마크 퍼포먼스 자체는 낮음""",
        "use_cases": "- 기업의 자체 파인튜닝을 위한 퓨어 베이스",
        "benchmark": "5.5GB VRAM"
    },
    "Stable LM 2 (1.6B, 12B)": {
        "title": "Stable LM 2 (1.6B, 12B)",
        "description": "스테이블 디퓨전(Stable Diffusion)으로 유명한 회사에서 만든 언어 모델입니다.",
        "developer": "Stability AI",
        "architecture": "다양한 데이터셋의 최적 혼합 비율(Mix) 적용.",
        "pros_cons": """**장점 (Pros):**\n- 투명하고 뛰어난 영문 생성 품질\n\n**단점 (Cons):**\n- 타사 모델에 비해 낮은 인지도와 한글 튜닝 부재""",
        "use_cases": "- 가벼운 영문 텍스트 생성기",
        "benchmark": "1.6B: 2GB VRAM"
    },
    "LLaVA 시리즈": {
        "title": "LLaVA 시리즈",
        "description": "Llama 모델에 '눈'을 달아주어 이미지를 볼 수 있게 만든 멀티모달 선구자입니다.",
        "developer": "UW/MSR",
        "architecture": "Vision Encoder (CLIP) + 언어 모델 (Llama/Vicuna) 결합.",
        "pros_cons": """**장점 (Pros):**\n- 입력한 이미지의 내용을 텍스트로 아주 상세하고 정확하게 묘사함\n\n**단점 (Cons):**\n- 일반 텍스트만 처리할 때보다 무겁고 속도가 느림""",
        "use_cases": "- 시각 기반 질의응답(VQA)",
        "benchmark": "최소 8GB VRAM"
    },
    "Phind-CodeLlama 34B": {
        "title": "Phind-CodeLlama 34B",
        "description": "개발자 전용 검색엔진 Phind에서 튜닝한 압도적인 코딩 모델입니다.",
        "developer": "Phind",
        "architecture": "CodeLlama 34B 베이스 + 고품질 프롬프트 응답 튜닝.",
        "pros_cons": """**장점 (Pros):**\n- 복잡한 에러 코드를 던져주면 해결책을 귀신같이 찾아냄\n\n**단점 (Cons):**\n- 일반 유저가 돌리기 힘든 34B 체급의 무거움""",
        "use_cases": "- 시니어 개발자의 코드 디버깅 보조",
        "benchmark": "22GB VRAM"
    },
    "InternLM 2 (1.8B, 7B, 20B)": {
        "title": "InternLM 2 (1.8B, 7B, 20B)",
        "description": "중국 상하이 AI 연구소에서 개발한 매우 긴 텍스트 처리 전문 모델입니다.",
        "developer": "Shanghai AI Lab",
        "architecture": "최대 200K 컨텍스트, 탁월한 문서 요약력.",
        "pros_cons": """**장점 (Pros):**\n- 거대한 문서를 통째로 넣고 요약할 때 정보 누락이 적음\n\n**단점 (Cons):**\n- 중국어 편향성 존재""",
        "use_cases": "- 기업용 대규모 문서 분석기",
        "benchmark": "20B: 14GB VRAM"
    },
    "Baichuan 2 (7B, 13B)": {
        "title": "Baichuan 2 (7B, 13B)",
        "description": "중국의 AI 벤처에서 만든 상업 및 의료 특화 다국어 모델입니다.",
        "developer": "Baichuan",
        "architecture": "영어와 중국어 중심의 2.6조 토큰 학습.",
        "pros_cons": """**장점 (Pros):**\n- 중국 내 라이선스 및 상업 서비스용으로 각광\n\n**단점 (Cons):**\n- 한국어 및 서양 문화 지식 부재""",
        "use_cases": "- 중화권 타겟 서비스 엔진",
        "benchmark": "13B: 8.5GB VRAM"
    },
    "ChatGLM 3 (6B)": {
        "title": "ChatGLM 3 (6B)",
        "description": "칭화대 연구진이 만든 중국 최초의 걸작 6B 모델입니다.",
        "developer": "Tsinghua Univ",
        "architecture": "효율적인 GLM 아키텍처 도입.",
        "pros_cons": """**장점 (Pros):**\n- 낮은 VRAM 소모량 대비 탁월한 지식 검색 능력\n\n**단점 (Cons):**\n- 영-중 외의 다국어(한국어)는 사실상 불가능""",
        "use_cases": "- 연구용 레퍼런스",
        "benchmark": "5GB VRAM"
    },
    "Orion 14B": {
        "title": "Orion 14B",
        "description": "2.5조 토큰의 다국어 훈련을 받은 강력한 중형급 모델입니다.",
        "developer": "OrionStar",
        "architecture": "아시아 언어 처리에 특화된 14B 체급.",
        "pros_cons": """**장점 (Pros):**\n- 일본어, 한국어 등 다국어 처리 효율이 상당히 높음\n\n**단점 (Cons):**\n- Qwen 시리즈의 그늘에 가려진 인지도""",
        "use_cases": "- 아시아 통합 다국어 챗봇",
        "benchmark": "9GB VRAM"
    },
    "Xverse (7B, 13B, 65B)": {
        "title": "Xverse (7B, 13B, 65B)",
        "description": "대규모 다국어 말뭉치를 집중적으로 훈련받은 모델입니다.",
        "developer": "Xverse",
        "architecture": "3.2조 토큰의 거대 데이터셋 학습.",
        "pros_cons": """**장점 (Pros):**\n- 65B 모델의 경우 GPT-3.5를 압도하는 훌륭한 추론력\n\n**단점 (Cons):**\n- 마찬가지로 중국어 중심의 편향""",
        "use_cases": "- 대형 코퍼스 연구용",
        "benchmark": "65B: 38GB VRAM"
    },
    "Aya 23 (8B, 35B)": {
        "title": "Aya 23 (8B, 35B)",
        "description": "무려 23개의 언어를 원어민처럼 구사하기 위해 특별히 만들어진 다국어 최적화 모델입니다.",
        "developer": "Cohere",
        "architecture": "다국어 특별 파인튜닝, Command R 베이스.",
        "pros_cons": """**장점 (Pros):**\n- 한국어를 포함한 23개 언어를 놀랍도록 매끄럽게 번역하고 이해함\n\n**단점 (Cons):**\n- 영어 전용 모델에 비해 코딩 능력이 살짝 떨어짐""",
        "use_cases": "- 글로벌 번역기, 다국어 CS 봇",
        "benchmark": "8B: 6GB / 35B: 22GB VRAM"
    },
    "Breeze 7B (대만)": {
        "title": "Breeze 7B (대만)",
        "description": "대만의 미디어텍(MediaTek)에서 번체 중국어(Taiwanese)에 특화시켜 만든 모델입니다.",
        "developer": "MediaTek",
        "architecture": "Mistral 7B 기반 번체 튜닝.",
        "pros_cons": """**장점 (Pros):**\n- 대만의 문화와 번체 한자를 가장 완벽하게 묘사함\n\n**단점 (Cons):**\n- 한국인에게는 필요성이 매우 낮음""",
        "use_cases": "- 대만 타겟 서비스 특화 봇",
        "benchmark": "5.5GB VRAM"
    },
    "SeaLLM (7B, 13B)": {
        "title": "SeaLLM (7B, 13B)",
        "description": "동남아시아(SEA) 지역의 마이너한 언어들을 완벽하게 커버하기 위한 모델입니다.",
        "developer": "Alibaba",
        "architecture": "태국어, 베트남어, 인니어 등 소수 언어 집중 훈련.",
        "pros_cons": """**장점 (Pros):**\n- 구글 번역기도 잘 못하는 동남아 소수 언어를 찰떡같이 번역함\n\n**단점 (Cons):**\n- 일반 범용 목적으론 활용도 낮음""",
        "use_cases": "- 동남아 현지화 및 글로벌 게임 서비스",
        "benchmark": "13B: 8.5GB VRAM"
    },

}

def render():
    st.title("📖 모델 사전 (LLM Model Wiki)")
    st.markdown('''
    이 페이지에서는 글로벌 리더보드를 장악하고 있는 **세계 최고 수준의 오픈소스 로컬 LLM 40종**에 대한 깊이 있는 정보를 제공합니다. 
    파라미터 체급별 중복 모델을 통합하여, 서로 다른 아키텍처와 특성을 가진 40개의 거대한 모델 가문(Family)을 소개합니다.
    로컬 환경(내 PC)에 모델을 다운로드하기 전에, 아래 사전을 참고하여 내 PC 사양과 사용 목적에 딱 맞는 모델을 찾아보세요!
    ''')
    st.divider()
    
    # ---------------------------------------------------------
    # 검색 기능
    # ---------------------------------------------------------
    search_query = st.text_input("🔍 모델명 검색 (예: Llama, Qwen, Coder)", placeholder="검색어를 입력하세요...")
    all_models = list(MODEL_WIKI_DATA.keys())
    if search_query:
        models_list = [m for m in all_models if search_query.lower() in m.lower()]
    else:
        models_list = all_models
        
    # ---------------------------------------------------------
    # 페이지네이션(Pagination) 로직
    # ---------------------------------------------------------
    ITEMS_PER_PAGE = 10
    total_pages = max(1, (len(models_list) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE)
    
    if 'wiki_page' not in st.session_state:
        st.session_state['wiki_page'] = 1
        
    if st.session_state['wiki_page'] > total_pages:
        st.session_state['wiki_page'] = 1
        
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("⬅️ 이전 페이지", disabled=(st.session_state['wiki_page'] <= 1), use_container_width=True):
            st.session_state['wiki_page'] -= 1
            st.rerun()
            
    with col2:
        st.markdown(f"<h4 style='text-align: center;'>페이지 {st.session_state['wiki_page']} / {total_pages}</h4>", unsafe_allow_html=True)
        
    with col3:
        if st.button("다음 페이지 ➡️", disabled=(st.session_state['wiki_page'] >= total_pages), use_container_width=True):
            st.session_state['wiki_page'] += 1
            st.rerun()
            
    st.divider()
    
    # ---------------------------------------------------------
    # 1번안: 현재 페이지의 10개 모델을 st.expander로 렌더링
    # ---------------------------------------------------------
    current_page = st.session_state['wiki_page']
    start_idx = (current_page - 1) * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE
    
    page_models = models_list[start_idx:end_idx]
    
    if not page_models:
        st.warning("검색 결과가 없습니다.")
    
    for i, model_name in enumerate(page_models):
        data = MODEL_WIKI_DATA[model_name]
        
        with st.expander(f"📦 **{start_idx + i + 1}. {data['title']}**"):
            st.caption(f"**개발사:** {data['developer']}")
            st.markdown(f"**요약:** {data['description']}")
            
            st.subheader("🧬 아키텍처 및 기술적 특징")
            st.markdown(data["architecture"])
            
            st.subheader("⚖️ 장단점 분석 (Pros & Cons)")
            st.markdown(data["pros_cons"])
            
            st.subheader("💡 추천 활용 시나리오")
            st.markdown(data["use_cases"])
            
            st.subheader("📊 벤치마크 퍼포먼스 및 요구사항")
            st.info(data["benchmark"])
            
    # 하단 네비게이션 복제
    st.divider()
    b_col1, b_col2, b_col3 = st.columns([1, 2, 1])
    with b_col1:
        if st.button("⬅️ 이전 페이지 (하단)", disabled=(st.session_state['wiki_page'] <= 1), use_container_width=True, key="bottom_prev"):
            st.session_state['wiki_page'] -= 1
            st.rerun()
    with b_col3:
        if st.button("다음 페이지 ➡️ (하단)", disabled=(st.session_state['wiki_page'] >= total_pages), use_container_width=True, key="bottom_next"):
            st.session_state['wiki_page'] += 1
            st.rerun()

