
# -*- coding: utf-8 -*-

MODEL_WIKI_DATA = {
    "Meta Llama 4 시리즈 (Scout, Maverick 등)": {
        "title": "Meta Llama 4 시리즈 (Scout, Maverick 등)",
        "description": "2025~2026년 기준 오픈소스 최고봉. 네이티브 멀티모달 능력과 MoE(전문가 혼합)를 도입한 완벽한 4세대 라인업입니다.",
        "developer": "Meta AI",
        "architecture": "Llama 4 Scout(109B, 활성 17B), Maverick(400B). 최대 10M(천만) 토큰 컨텍스트 지원.",
        "pros_cons": """**장점 (Pros):**\n- 압도적 추론, 이미지/비디오 네이티브 이해, 천만 토큰의 광활한 기억력\n\n**단점 (Cons):**\n- MoE 구조라 전체 VRAM 요구량이 매우 높음""",
        "use_cases": "- 기업용 대규모 AI 비서, 영상 분석 자동화",
        "benchmark": "Scout 109B: 60GB VRAM / Maverick: 200GB 이상"
    },
    "Meta Llama 3 시리즈 (8B, 70B)": {
        "title": "Meta Llama 3 시리즈 (8B, 70B)",
        "description": "로컬 LLM의 대중화를 이끈 전설적인 3세대 모델. 여전히 가성비로 널리 쓰입니다.",
        "developer": "Meta AI",
        "architecture": "트랜스포머 디코더, 8K 컨텍스트, Grouped Query Attention(GQA).",
        "pros_cons": """**장점 (Pros):**\n- 체급 대비 압도적 지능, 거대한 생태계 및 최적화 자료\n\n**단점 (Cons):**\n- Llama 4 대비 부족한 컨텍스트(8K)와 멀티모달 부재""",
        "use_cases": "- 일상적인 챗봇, 코드 생성, 텍스트 요약",
        "benchmark": "8B: 6GB VRAM / 70B: 40GB VRAM"
    },
    "CodeLlama 시리즈 (7B~70B)": {
        "title": "CodeLlama 시리즈 (7B~70B)",
        "description": "Llama 2를 기반으로 코딩 능력을 극대화한 레거시 개발자용 모델입니다.",
        "developer": "Meta AI",
        "architecture": "최대 100K 토큰 지원, 파이썬/C++ 등 특화 학습.",
        "pros_cons": """**장점 (Pros):**\n- 광범위한 언어 지원, 매우 긴 코드 컨텍스트 이해\n\n**단점 (Cons):**\n- 일반적인 대화나 한국어 질문에는 취약함""",
        "use_cases": "- 로컬 Copilot 연동, 코드 자동 완성",
        "benchmark": "체급에 따라 5.5GB ~ 40GB VRAM"
    },
    "Google Gemma 4 시리즈": {
        "title": "Google Gemma 4 시리즈",
        "description": "2026년 4월 출시된 구글의 최신작. 멀티모달(텍스트, 이미지, 오디오)과 스스로 생각하는 '추론(Thinking)' 모드를 탑재했습니다.",
        "developer": "Google DeepMind",
        "architecture": "256K 컨텍스트, 네이티브 함수 호출(Function Calling), E-시리즈(Edge용).",
        "pros_cons": """**장점 (Pros):**\n- 탁월한 한국어 및 다국어 추론, 기기 내에서 이미지/음성 동시 처리\n\n**단점 (Cons):**\n- 아직 지원되지 않는 구형 로컬 툴들 존재""",
        "use_cases": "- 학술 논문 분석, 복합 멀티모달 정보 검색",
        "benchmark": "E-series: 4GB / 대형 모델: 30GB VRAM"
    },
    "Google Gemma 2 시리즈 (2B, 9B, 27B)": {
        "title": "Google Gemma 2 시리즈 (2B, 9B, 27B)",
        "description": "제미나이(Gemini) 기술로 빚어내어 과거 Llama 3를 위협했던 고성능 2세대 라인업입니다.",
        "developer": "Google DeepMind",
        "architecture": "8K 컨텍스트, Sliding Window Attention 적용.",
        "pros_cons": """**장점 (Pros):**\n- 훌륭한 팩트 정확도와 빠른 한국어 생성\n\n**단점 (Cons):**\n- 특이한 파라미터 수(9B, 27B)로 인한 애매한 VRAM 요구량""",
        "use_cases": "- 학술 논문 분석, 정확한 정보 검색",
        "benchmark": "9B: 6.5GB / 27B: 18GB VRAM"
    },
    "Qwen 3 & 3.7 시리즈 (30B~235B)": {
        "title": "Qwen 3 & 3.7 시리즈 (30B~235B)",
        "description": "2025~2026년 출시된 알리바바의 괴물. 에이전틱(Agentic) 기능과 멀티모달로 무장했습니다.",
        "developer": "Alibaba Cloud",
        "architecture": "Qwen3-235B(MoE), Qwen3-30B(활성 3B). 2026년 5월 최신 3.7 버전 릴리즈.",
        "pros_cons": """**장점 (Pros):**\n- 현존 아시아권 최고 성능, 완벽한 한국어 번역 및 코딩 능력, 압도적 속도\n\n**단점 (Cons):**\n- 중국어 기반 지식이 너무 깊어 서구권 문화 답변 간혹 어색함""",
        "use_cases": "- 전문 다국어 번역기, 코딩 및 에이전트 봇",
        "benchmark": "30B MoE: 18GB / 235B: 120GB VRAM"
    },
    "Qwen 2 시리즈 (0.5B ~ 72B)": {
        "title": "Qwen 2 시리즈 (0.5B ~ 72B)",
        "description": "전 세계를 강타했던 Qwen 가문의 2세대 모델. 매우 강력한 수학 능력을 지녔습니다.",
        "developer": "Alibaba Cloud",
        "architecture": "최대 128K 컨텍스트, 29개국어 사전 학습.",
        "pros_cons": """**장점 (Pros):**\n- 놀랍도록 자연스러운 한국어 구사, 수학 최상위권\n\n**단점 (Cons):**\n- 구형 아키텍처로 최신 3세대에 점수 밀림""",
        "use_cases": "- 구형 인프라 다국어 서비스 유지보수",
        "benchmark": "7B: 5.5GB / 72B: 42GB VRAM"
    },
    "Qwen-VL / Audio": {
        "title": "Qwen-VL / Audio",
        "description": "텍스트뿐만 아니라 이미지와 소리까지 이해하는 멀티모달 1세대 라인업입니다.",
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
        "pros_cons": """**장점 (Pros):**\n- 극도로 적은 VRAM 소모, 압도적인 논리력\n\n**단점 (Cons):**\n- 세상의 모든 지식을 담기엔 모델 뇌가 너무 작아 환각 발생 잦음""",
        "use_cases": "- 오프라인 모바일 앱, 단순 텍스트 요약",
        "benchmark": "Mini(3.8B): 3GB / Medium(14B): 9GB VRAM"
    },
    "WizardLM 시리즈 (7B ~ 70B)": {
        "title": "WizardLM 시리즈 (7B ~ 70B)",
        "description": "지시 복잡성(Instruction Complexity)을 훈련시켜 명령 수행력을 높인 모델입니다.",
        "developer": "Microsoft/WizardLM",
        "architecture": "Evol-Instruct 기법 적용.",
        "pros_cons": """**장점 (Pros):**\n- 복잡하고 여러 단계로 꼬인 사용자의 지시를 정확히 따름\n\n**단점 (Cons):**\n- 최신 베이스 모델(Llama 4 등) 미적용 시 한계""",
        "use_cases": "- 복합적인 명령을 내리는 비서",
        "benchmark": "체급별 상이 (5.5GB ~ 40GB)"
    },
    "DeepSeek V2 & Coder V2 (236B)": {
        "title": "DeepSeek V2 & Coder V2 (236B)",
        "description": "2024~2025년을 지배한 미친 가성비의 혁신적 MoE 라인업입니다.",
        "developer": "DeepSeek AI",
        "architecture": "236B MoE (활성 21B), Multi-Head Latent Attention(MLA) 신기술.",
        "pros_cons": """**장점 (Pros):**\n- 동급 최고의 속도와 코딩 능력 대비 극히 적은 VRAM 점유(MLA 덕분)\n\n**단점 (Cons):**\n- 설치 및 구동(vLLM 등) 최적화에 난이도 있음""",
        "use_cases": "- 로컬 최고급 코딩 보조, 복합 챗봇",
        "benchmark": "활성 21B 기준 24GB VRAM 구동 가능"
    },
    "DeepSeek LLM (7B, 67B)": {
        "title": "DeepSeek LLM (7B, 67B)",
        "description": "딥시크 기술력의 기반이 되는 강력한 초기 범용 언어 모델입니다.",
        "developer": "DeepSeek AI",
        "architecture": "중국어와 영어 중심의 대규모 사전 학습.",
        "pros_cons": """**장점 (Pros):**\n- 수학적 사고력이 훌륭하고 매우 빠른 응답성\n\n**단점 (Cons):**\n- 한국어 번역이나 대화 시 어색함이 남음""",
        "use_cases": "- 수학 논문 요약, 영-중 번역",
        "benchmark": "7B: 5.5GB / 67B: 38GB VRAM"
    },
    "Mistral v0.3 & NeMo 12B": {
        "title": "Mistral v0.3 & NeMo 12B",
        "description": "오픈소스 생태계를 이끌어온 미스트랄의 강력한 단일(Dense) 최신 모델들입니다.",
        "developer": "Mistral AI",
        "architecture": "함수 호출(Function Calling) 지원, Tekken 토크나이저.",
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
        "pros_cons": """**장점 (Pros):**\n- 가장 완벽하고 자연스러운 한국어 문장력과 논리 추론\n\n**단점 (Cons):**\n- 해외 모델 대비 상대적으로 좁은 생태계 지원""",
        "use_cases": "- 국내 기업용 사내망 AI 엔진",
        "benchmark": "8GB VRAM"
    },
    "Command R+ (104B)": {
        "title": "Command R+ (104B)",
        "description": "RAG(검색 증강 생성) 성능을 극한으로 끌어올린 엔터프라이즈급 거대 모델입니다.",
        "developer": "Cohere",
        "architecture": "104B 파라미터, 도구 사용(Tool Use) 특화, 128K 컨텍스트.",
        "pros_cons": """**장점 (Pros):**\n- 오픈소스 최고 수준의 정확도와 환각(Hallucination) 억제 능력\n\n**단점 (Cons):**\n- 개인 장비로는 구동하기 힘든 무거운 체급""",
        "use_cases": "- 기업 사내 문서 기반 검색(RAG) 시스템",
        "benchmark": "최소 60GB VRAM"
    },
    "Command R (35B)": {
        "title": "Command R (35B)",
        "description": "Command R+의 동생 격으로, 3090/4090 환경에서 최적의 RAG 효율을 냅니다.",
        "developer": "Cohere",
        "architecture": "35B 파라미터.",
        "pros_cons": """**장점 (Pros):**\n- 주어진 문서를 바탕으로 가장 정확하게 답변을 뽑아냄\n\n**단점 (Cons):**\n- 범용적인 챗봇 대화로는 매력이 다소 떨어짐""",
        "use_cases": "- 학술 논문/법률 문서 팩트체크",
        "benchmark": "22GB VRAM"
    },
    "Grok-1.5 (초거대 MoE)": {
        "title": "Grok-1.5 (초거대 MoE)",
        "description": "일론 머스크의 xAI가 공개한 그록 시리즈. 오픈소스 생태계에 큰 충격을 주었습니다.",
        "developer": "xAI",
        "architecture": "거대한 파라미터의 MoE 아키텍처, 128K 긴 컨텍스트.",
        "pros_cons": """**장점 (Pros):**\n- 방대한 글로벌 상식, 유머러스하고 제한 없는 재치 있는 답변 스타일\n\n**단점 (Cons):**\n- 일반 데스크탑에서는 구동 불가능한 무시무시한 용량""",
        "use_cases": "- 대규모 AI 클러스터 및 슈퍼컴퓨터 연구용",
        "benchmark": "최소 200GB VRAM 이상"
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
    "Falcon (7B, 40B, 180B)": {
        "title": "Falcon (7B, 40B, 180B)",
        "description": "UAE에서 막대한 자본으로 훈련시켜 상업용 완전 무료로 푼 혁신적 라인업입니다.",
        "developer": "TII",
        "architecture": "커스텀 트랜스포머 아키텍처.",
        "pros_cons": """**장점 (Pros):**\n- 상업적 제약이 전혀 없는 완전한 오픈 라이선스\n\n**단점 (Cons):**\n- 구형 아키텍처로 인한 속도 및 최신 모델 대비 토큰 효율성 저하""",
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
    "Jamba 1.5": {
        "title": "Jamba 1.5",
        "description": "전통적인 트랜스포머의 한계를 깬 혁신적인 하이브리드 최신 모델입니다.",
        "developer": "AI21 Labs",
        "architecture": "Mamba 2 (SSM) + Transformer 하이브리드 아키텍처.",
        "pros_cons": """**장점 (Pros):**\n- 엄청나게 긴 텍스트를 처리할 때도 VRAM과 연산량이 크게 늘지 않음\n\n**단점 (Cons):**\n- 아직 지원하는 생태계 툴(Ollama 등)이 일부 제한적임""",
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
    "InternLM 2.5 (1.8B, 7B, 20B)": {
        "title": "InternLM 2.5 (1.8B, 7B, 20B)",
        "description": "중국 상하이 AI 연구소에서 개발한 매우 긴 텍스트 처리 전문 최신 모델입니다.",
        "developer": "Shanghai AI Lab",
        "architecture": "최대 1000K 컨텍스트, 탁월한 문서 요약력.",
        "pros_cons": """**장점 (Pros):**\n- 거대한 문서를 통째로 넣고 요약할 때 정보 누락이 가장 적음\n\n**단점 (Cons):**\n- 중국어 편향성 존재""",
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
    "ChatGLM 4": {
        "title": "ChatGLM 4",
        "description": "칭화대 연구진이 만든 고성능 최신 4세대 GLM 아키텍처 모델입니다.",
        "developer": "Tsinghua Univ",
        "architecture": "128K 지원 효율적인 GLM 아키텍처 도입.",
        "pros_cons": """**장점 (Pros):**\n- 낮은 VRAM 소모량 대비 탁월한 지식 검색과 다국어 능력\n\n**단점 (Cons):**\n- 구동 환경 세팅의 번거로움""",
        "use_cases": "- 연구용 다국어 챗봇",
        "benchmark": "9GB VRAM"
    },
    "Orion 14B": {
        "title": "Orion 14B",
        "description": "2.5조 토큰의 다국어 훈련을 받은 강력한 중형급 모델입니다.",
        "developer": "OrionStar",
        "architecture": "아시아 언어 처리에 특화된 14B 체급.",
        "pros_cons": """**장점 (Pros):**\n- 일본어, 한국어 등 다국어 처리 효율이 상당히 높음\n\n**단점 (Cons):**\n- Qwen 3의 등장으로 가려진 인지도""",
        "use_cases": "- 아시아 통합 다국어 챗봇",
        "benchmark": "9GB VRAM"
    },
    "Xverse (7B, 13B, 65B)": {
        "title": "Xverse (7B, 13B, 65B)",
        "description": "대규모 다국어 말뭉치를 집중적으로 훈련받은 모델입니다.",
        "developer": "Xverse",
        "architecture": "3.2조 토큰의 거대 데이터셋 학습.",
        "pros_cons": """**장점 (Pros):**\n- 65B 모델의 경우 거대한 추론력을 자랑\n\n**단점 (Cons):**\n- 마찬가지로 중국어 중심의 편향""",
        "use_cases": "- 대형 코퍼스 연구용",
        "benchmark": "65B: 38GB VRAM"
    },
    "Aya 23 (8B, 35B)": {
        "title": "Aya 23 (8B, 35B)",
        "description": "무려 23개의 언어를 원어민처럼 구사하기 위해 특별히 만들어진 다국어 튜닝 모델입니다.",
        "developer": "Cohere",
        "architecture": "다국어 특별 파인튜닝, Command R 베이스.",
        "pros_cons": """**장점 (Pros):**\n- 한국어를 포함한 23개 언어를 놀랍도록 매끄럽게 번역하고 이해함\n\n**단점 (Cons):**\n- 코딩 성능은 최신 모델 대비 살짝 아쉬움""",
        "use_cases": "- 글로벌 번역기, 다국어 CS 봇",
        "benchmark": "8B: 6GB / 35B: 22GB VRAM"
    },
    "SeaLLM 3": {
        "title": "SeaLLM 3",
        "description": "동남아시아(SEA) 지역의 마이너한 언어들을 완벽하게 커버하기 위한 특화 모델입니다.",
        "developer": "Alibaba",
        "architecture": "태국어, 베트남어, 인니어 등 소수 언어 집중 훈련.",
        "pros_cons": """**장점 (Pros):**\n- 구글 번역기도 잘 못하는 동남아 소수 언어를 찰떡같이 번역함\n\n**단점 (Cons):**\n- 일반 범용 목적으론 활용도 낮음""",
        "use_cases": "- 동남아 현지화 및 글로벌 게임 서비스",
        "benchmark": "8GB VRAM"
    },
    "OpenHermes 2.5": {
        "title": "OpenHermes 2.5",
        "description": "수많은 데이터셋을 기가 막히게 배합하여 만든 역대 최고의 7B 튜닝 모델입니다.",
        "developer": "Teknium",
        "architecture": "Mistral 7B 베이스, 엄청난 양의 커스텀 데이터셋 조합.",
        "pros_cons": """**장점 (Pros):**\n- 마치 실제 사람 비서처럼 코딩부터 일상 대화까지 센스 있게 대답함\n\n**단점 (Cons):**\n- 베이스가 구형이라 최신 Llama 4에 스펙은 밀림""",
        "use_cases": "- 로컬 챗봇의 훌륭한 UI/UX 레퍼런스",
        "benchmark": "5.5GB VRAM"
    },

}

MODEL_WIKI_DATA_EN = {
    "Meta Llama 4 시리즈 (Scout, Maverick 등)": {
        "title": "Meta Llama 4 Series (Scout, Maverick, etc.)",
        "description": "The pinnacle of open-source as of 2025~2026. A perfect 4th-generation lineup introducing native multimodal capabilities and MoE (Mixture of Experts).",
        "developer": "Meta AI",
        "architecture": "Llama 4 Scout (109B, 17B active), Maverick (400B). Supports up to 10M token context.",
        "pros_cons": "**Pros:**\n- Overwhelming reasoning, native image/video understanding, vast 10M token memory\n\n**Cons:**\n- Extremely high VRAM requirement due to MoE structure",
        "use_cases": "- Enterprise large-scale AI assistant, automated video analysis",
        "benchmark": "Scout 109B: 60GB VRAM / Maverick: 200GB+ VRAM"
    },
    "Meta Llama 3 시리즈 (8B, 70B)": {
        "title": "Meta Llama 3 Series (8B, 70B)",
        "description": "The legendary 3rd-generation model that popularized local LLMs. Still widely used for its cost-effectiveness.",
        "developer": "Meta AI",
        "architecture": "Transformer decoder, 8K context, Grouped Query Attention (GQA).",
        "pros_cons": "**Pros:**\n- Overwhelming intelligence for its size, massive ecosystem and optimization resources\n\n**Cons:**\n- Limited context (8K) and lack of multimodal features compared to Llama 4",
        "use_cases": "- Daily chatbot, code generation, text summarization",
        "benchmark": "8B: 6GB VRAM / 70B: 40GB VRAM"
    },
    "CodeLlama 시리즈 (7B~70B)": {
        "title": "CodeLlama Series (7B~70B)",
        "description": "A legacy developer model maximizing coding capabilities based on Llama 2.",
        "developer": "Meta AI",
        "architecture": "Up to 100K token support, specialized training in Python/C++.",
        "pros_cons": "**Pros:**\n- Extensive language support, deep understanding of long code contexts\n\n**Cons:**\n- Weak in general conversation or non-English queries",
        "use_cases": "- Local Copilot integration, code auto-completion",
        "benchmark": "5.5GB ~ 40GB VRAM depending on size"
    },
    "Google Gemma 4 시리즈": {
        "title": "Google Gemma 4 Series",
        "description": "Google's latest release from April 2026. Equipped with multimodal (text, image, audio) and a self-reflecting 'Thinking' mode.",
        "developer": "Google DeepMind",
        "architecture": "256K context, native Function Calling, E-series (for Edge).",
        "pros_cons": "**Pros:**\n- Excellent reasoning, processes image/audio simultaneously on-device\n\n**Cons:**\n- Some older local tools do not support it yet",
        "use_cases": "- Academic paper analysis, complex multimodal information retrieval",
        "benchmark": "E-series: 4GB / Large models: 30GB VRAM"
    },
    "Google Gemma 2 시리즈 (2B, 9B, 27B)": {
        "title": "Google Gemma 2 Series (2B, 9B, 27B)",
        "description": "High-performance 2nd-generation lineup built with Gemini technology that threatened Llama 3.",
        "developer": "Google DeepMind",
        "architecture": "8K context, Sliding Window Attention applied.",
        "pros_cons": "**Pros:**\n- Great factual accuracy and fast generation\n\n**Cons:**\n- Awkward VRAM requirements due to unusual parameter counts (9B, 27B)",
        "use_cases": "- Academic paper analysis, accurate info search",
        "benchmark": "9B: 6.5GB / 27B: 18GB VRAM"
    },
    "Qwen 3 & 3.7 시리즈 (30B~235B)": {
        "title": "Qwen 3 & 3.7 Series (30B~235B)",
        "description": "Alibaba's monster released in 2025~2026. Armed with Agentic features and multimodal.",
        "developer": "Alibaba Cloud",
        "architecture": "Qwen3-235B (MoE), Qwen3-30B (3B active). Latest 3.7 version released May 2026.",
        "pros_cons": "**Pros:**\n- Best performance in Asia, perfect multi-language translation & coding, overwhelming speed\n\n**Cons:**\n- Deep Chinese knowledge sometimes makes Western cultural answers awkward",
        "use_cases": "- Pro multi-language translator, coding & agent bots",
        "benchmark": "30B MoE: 18GB / 235B: 120GB VRAM"
    },
    "Qwen 2 시리즈 (0.5B ~ 72B)": {
        "title": "Qwen 2 Series (0.5B ~ 72B)",
        "description": "The 2nd-generation model from the Qwen family that took the world by storm. Extremely strong in math.",
        "developer": "Alibaba Cloud",
        "architecture": "Up to 128K context, pre-trained on 29 languages.",
        "pros_cons": "**Pros:**\n- Incredibly natural multi-language speaking, top-tier math skills\n\n**Cons:**\n- Outperformed by the latest 3rd-generation architecture",
        "use_cases": "- Maintenance of legacy multi-language services",
        "benchmark": "7B: 5.5GB / 72B: 42GB VRAM"
    },
    "Qwen-VL / Audio": {
        "title": "Qwen-VL / Audio",
        "description": "The 1st-generation multimodal lineup understanding images and sound alongside text.",
        "developer": "Alibaba Cloud",
        "architecture": "Architecture combining visual and audio encoders.",
        "pros_cons": "**Pros:**\n- Accurately recognizes text in images (OCR) and situations\n\n**Cons:**\n- Consumes much more VRAM than text-only models",
        "use_cases": "- Image captioning, photo description for the visually impaired",
        "benchmark": "Minimum 10GB VRAM"
    },
    "Microsoft Phi-3 (Mini, Small, Medium)": {
        "title": "Microsoft Phi-3 (Mini, Small, Medium)",
        "description": "The miracle of SLM (Small Language Models). Unfolds GPT-3.5 level logic with a tiny footprint.",
        "developer": "Microsoft",
        "architecture": "Intensively trained on highly refined, Textbook-quality data.",
        "pros_cons": "**Pros:**\n- Extremely low VRAM consumption, overwhelming logic\n\n**Cons:**\n- The model's brain is too small to hold all worldly knowledge, causing frequent hallucinations",
        "use_cases": "- Offline mobile apps, simple text summarization",
        "benchmark": "Mini(3.8B): 3GB / Medium(14B): 9GB VRAM"
    },
    "WizardLM 시리즈 (7B ~ 70B)": {
        "title": "WizardLM Series (7B ~ 70B)",
        "description": "A model trained on Instruction Complexity to enhance command execution capabilities.",
        "developer": "Microsoft/WizardLM",
        "architecture": "Evol-Instruct technique applied.",
        "pros_cons": "**Pros:**\n- Accurately follows complex and multi-step user instructions\n\n**Cons:**\n- Limited if not applied to the latest base models (like Llama 4)",
        "use_cases": "- Assistant for executing complex commands",
        "benchmark": "Varies by size (5.5GB ~ 40GB)"
    },
    "DeepSeek V2 & Coder V2 (236B)": {
        "title": "DeepSeek V2 & Coder V2 (236B)",
        "description": "The revolutionary MoE lineup with insane cost-effectiveness that dominated 2024~2025.",
        "developer": "DeepSeek AI",
        "architecture": "236B MoE (21B active), Multi-Head Latent Attention (MLA) technology.",
        "pros_cons": "**Pros:**\n- Extremely low VRAM usage for its top-tier speed and coding ability (thanks to MLA)\n\n**Cons:**\n- Difficult to setup and optimize (vLLM, etc.)",
        "use_cases": "- Top-tier local coding assistant, complex chatbot",
        "benchmark": "Can run on 24GB VRAM based on 21B active"
    },
    "DeepSeek LLM (7B, 67B)": {
        "title": "DeepSeek LLM (7B, 67B)",
        "description": "A strong early general language model serving as the foundation of DeepSeek's tech.",
        "developer": "DeepSeek AI",
        "architecture": "Large-scale pre-training focused on Chinese and English.",
        "pros_cons": "**Pros:**\n- Excellent mathematical reasoning and very fast responsiveness\n\n**Cons:**\n- Awkwardness remains in translation and conversation for other languages",
        "use_cases": "- Math paper summarization, EN-CN translation",
        "benchmark": "7B: 5.5GB / 67B: 38GB VRAM"
    },
    "Mistral v0.3 & NeMo 12B": {
        "title": "Mistral v0.3 & NeMo 12B",
        "description": "Mistral's powerful latest dense models leading the open-source ecosystem.",
        "developer": "Mistral AI",
        "architecture": "Supports Function Calling, Tekken tokenizer.",
        "pros_cons": "**Pros:**\n- Cost-effectiveness exceeding its class, free text generation with little censorship\n\n**Cons:**\n- Lack of safety rails requires careful filtering for commercial use",
        "use_cases": "- Creative writing, web novel generation",
        "benchmark": "7B: 5.5GB / 12B: 8GB VRAM"
    },
    "Mixtral (8x7B, 8x22B)": {
        "title": "Mixtral (8x7B, 8x22B)",
        "description": "An MoE architecture model where multiple experts collaborate.",
        "developer": "Mistral AI",
        "architecture": "MoE (Mixture of Experts). Active parameters are about 1/4 of the total.",
        "pros_cons": "**Pros:**\n- Very fast output speed despite having massive knowledge\n\n**Cons:**\n- Memory (VRAM) usage still takes up the entire massive size",
        "use_cases": "- Enterprise multipurpose chatbot, comprehensive knowledge search",
        "benchmark": "8x7B: 26GB / 8x22B: 80GB VRAM"
    },
    "Upstage Solar 10.7B": {
        "title": "Upstage Solar 10.7B",
        "description": "A masterpiece model created by Upstage (Korea) that reached global #1.",
        "developer": "Upstage",
        "architecture": "Extended architecture based on Llama 2 via Depth Up-Scaling (DUS).",
        "pros_cons": "**Pros:**\n- Benchmark performance beating 30B models at a 10B size, excellent Korean understanding\n\n**Cons:**\n- Cost-effectiveness slightly dropped due to newer generation models",
        "use_cases": "- Building Korean-centric chatbot services",
        "benchmark": "7.5GB VRAM"
    },
    "Upstage Solar Pro": {
        "title": "Upstage Solar Pro",
        "description": "The latest upgraded version succeeding Solar 10.7B.",
        "developer": "Upstage",
        "architecture": "Significantly improved Korean tuning and context expansion.",
        "pros_cons": "**Pros:**\n- The most perfect and natural Korean sentences and logical reasoning\n\n**Cons:**\n- Relatively narrow ecosystem support compared to overseas models",
        "use_cases": "- Intranet AI engine for Korean enterprises",
        "benchmark": "8GB VRAM"
    },
    "Command R+ (104B)": {
        "title": "Command R+ (104B)",
        "description": "An enterprise-grade massive model pushing RAG (Retrieval-Augmented Generation) performance to the limit.",
        "developer": "Cohere",
        "architecture": "104B parameters, specialized in Tool Use, 128K context.",
        "pros_cons": "**Pros:**\n- Top open-source accuracy and hallucination suppression\n\n**Cons:**\n- Too heavy to run on personal equipment",
        "use_cases": "- Corporate internal document search (RAG) systems",
        "benchmark": "Minimum 60GB VRAM"
    },
    "Command R (35B)": {
        "title": "Command R (35B)",
        "description": "The smaller sibling of Command R+, offering optimal RAG efficiency on 3090/4090 setups.",
        "developer": "Cohere",
        "architecture": "35B parameters.",
        "pros_cons": "**Pros:**\n- Extracts answers most accurately based on provided documents\n\n**Cons:**\n- Somewhat lacks appeal as a general-purpose conversational chatbot",
        "use_cases": "- Academic paper / Legal document fact-checking",
        "benchmark": "22GB VRAM"
    },
    "Grok-1.5 (초거대 MoE)": {
        "title": "Grok-1.5 (Massive MoE)",
        "description": "The Grok series released by Elon Musk's xAI. Shocked the open-source ecosystem.",
        "developer": "xAI",
        "architecture": "Massive parameter MoE architecture, 128K long context.",
        "pros_cons": "**Pros:**\n- Vast global knowledge, humorous and unrestricted witty answer style\n\n**Cons:**\n- Terrifying size impossible to run on regular desktops",
        "use_cases": "- Large-scale AI clusters and supercomputer research",
        "benchmark": "Minimum 200GB VRAM+"
    },
    "DBRX (132B)": {
        "title": "DBRX (132B)",
        "description": "An ultra-large open-source MoE model of 132B released by Databricks.",
        "developer": "Databricks",
        "architecture": "Fine-grained Mixture-of-Experts architecture.",
        "pros_cons": "**Pros:**\n- Fast speed and strong coding/math/logic performance\n\n**Cons:**\n- Heavy footprint",
        "use_cases": "- Large-scale enterprise analytics systems",
        "benchmark": "80GB VRAM+"
    },
    "Falcon (7B, 40B, 180B)": {
        "title": "Falcon (7B, 40B, 180B)",
        "description": "An innovative lineup trained with massive UAE capital and released completely free for commercial use.",
        "developer": "TII",
        "architecture": "Custom Transformer architecture.",
        "pros_cons": "**Pros:**\n- Completely open license with zero commercial restrictions\n\n**Cons:**\n- Lower speed and token efficiency compared to newer models due to older architecture",
        "use_cases": "- Building commercial services without license limits",
        "benchmark": "40B: 24GB / 180B: 100GB+"
    },
    "Yi 시리즈 (6B, 34B)": {
        "title": "Yi Series (6B, 34B)",
        "description": "A masterpiece from China's 01.AI specialized in maintaining long text contexts.",
        "developer": "01.AI",
        "architecture": "Supports an overwhelming context length up to 200K.",
        "pros_cons": "**Pros:**\n- Incredible long-term memory to remember dozens of novels at once\n\n**Cons:**\n- Rapidly increasing VRAM consumption when using long contexts",
        "use_cases": "- Translating full novels, reviewing massive legal/medical docs",
        "benchmark": "6B: 5GB / 34B: 22GB VRAM"
    },
    "Vicuna (7B, 13B, 33B)": {
        "title": "Vicuna (7B, 13B, 33B)",
        "description": "The textbook model for Chat tuning that has been loved for the longest time.",
        "developer": "LMSYS",
        "architecture": "Fine-tuned with high-quality user conversation data from ShareGPT.",
        "pros_cons": "**Pros:**\n- Smooth and engaging conversational tone, like chatting with a real person\n\n**Cons:**\n- Lacks recent knowledge and multi-language support",
        "use_cases": "- Chatbot UI/UX prototyping",
        "benchmark": "Varies by size"
    },
    "Zephyr (7B, 141B)": {
        "title": "Zephyr (7B, 141B)",
        "description": "A very friendly model that popularized DPO (Direct Preference Optimization).",
        "developer": "Hugging Face H4",
        "architecture": "Applied DPO reinforcement learning on Mistral and Mixtral bases.",
        "pros_cons": "**Pros:**\n- Executes user instructions with extreme dedication and positivity\n\n**Cons:**\n- Tends to answer in English even if asked in other languages",
        "use_cases": "- Friendly English-based customer support bot",
        "benchmark": "7B: 5.5GB / 141B: 80GB VRAM"
    },
    "OpenChat 3.5": {
        "title": "OpenChat 3.5",
        "description": "A miracle tuned model that dominated benchmarks using only open-source data.",
        "developer": "OpenChat",
        "architecture": "C-RLFT technique (Conditioned Reinforcement Learning).",
        "pros_cons": "**Pros:**\n- Near-perfect coding and daily conversation from a small 7B size\n\n**Cons:**\n- Usage declined due to overlapping position after Llama 3's release",
        "use_cases": "- General-purpose local assistant",
        "benchmark": "5.5GB VRAM"
    },
    "TinyLlama 1.1B": {
        "title": "TinyLlama 1.1B",
        "description": "A micro toy model designed to run even in web browsers.",
        "developer": "Open Source",
        "architecture": "1.1B micro architecture, trained on 3T tokens.",
        "pros_cons": "**Pros:**\n- Extreme lightness, theoretically runnable on Raspberry Pi or smartwatches\n\n**Cons:**\n- Cannot handle complex logic or multi-language well",
        "use_cases": "- LLM education and structural testing",
        "benchmark": "Under 1.5GB VRAM"
    },
    "StarCoder 2 (3B, 7B, 15B)": {
        "title": "StarCoder 2 (3B, 7B, 15B)",
        "description": "A pure open-source code generator built by a coalition of developers worldwide.",
        "developer": "BigCode",
        "architecture": "Trained on over 600 programming languages.",
        "pros_cons": "**Pros:**\n- Vast code knowledge covering almost all minor programming languages\n\n**Cons:**\n- Severely lacks general conversational (Chat) abilities",
        "use_cases": "- VSC background auto-completion server",
        "benchmark": "15B: 10GB VRAM"
    },
    "Jamba 1.5": {
        "title": "Jamba 1.5",
        "description": "An innovative hybrid model breaking the limits of traditional Transformers.",
        "developer": "AI21 Labs",
        "architecture": "Mamba 2 (SSM) + Transformer Hybrid architecture.",
        "pros_cons": "**Pros:**\n- VRAM and computation barely increase even when processing extremely long texts\n\n**Cons:**\n- Ecosystem tools support (like Ollama) is still somewhat limited",
        "use_cases": "- Analyzing an entire novel at once",
        "benchmark": "12GB VRAM"
    },
    "OLMo (1B, 7B)": {
        "title": "OLMo (1B, 7B)",
        "description": "A 100% truly open model that released training code and data for AI research transparency.",
        "developer": "Allen AI",
        "architecture": "Training data (Dolma) and scripts fully open.",
        "pros_cons": "**Pros:**\n- Transparent data origins leave no room for license disputes\n\n**Cons:**\n- Benchmark performance itself is lower compared to other 7B models",
        "use_cases": "- Pure base for corporate fine-tuning",
        "benchmark": "5.5GB VRAM"
    },
    "Stable LM 2 (1.6B, 12B)": {
        "title": "Stable LM 2 (1.6B, 12B)",
        "description": "A language model created by the company famous for Stable Diffusion.",
        "developer": "Stability AI",
        "architecture": "Optimal mix ratio of various datasets applied.",
        "pros_cons": "**Pros:**\n- Transparent and excellent English generation quality\n\n**Cons:**\n- Lower awareness and lacks multi-language tuning compared to competitors",
        "use_cases": "- Lightweight English text generator",
        "benchmark": "1.6B: 2GB VRAM"
    },
    "LLaVA 시리즈": {
        "title": "LLaVA Series",
        "description": "The multimodal pioneer that gave 'eyes' to Llama models to see images.",
        "developer": "UW/MSR",
        "architecture": "Vision Encoder (CLIP) + Language Model (Llama/Vicuna) combined.",
        "pros_cons": "**Pros:**\n- Describes input images extremely detailed and accurately in text\n\n**Cons:**\n- Heavier and slower than processing only plain text",
        "use_cases": "- Vision-based Question Answering (VQA)",
        "benchmark": "Minimum 8GB VRAM"
    },
    "Phind-CodeLlama 34B": {
        "title": "Phind-CodeLlama 34B",
        "description": "An overwhelming coding model tuned by the developer search engine Phind.",
        "developer": "Phind",
        "architecture": "CodeLlama 34B base + High-quality prompt response tuning.",
        "pros_cons": "**Pros:**\n- Magically finds solutions when thrown complex error codes\n\n**Cons:**\n- The 34B weight makes it hard for average users to run",
        "use_cases": "- Code debugging assistant for senior developers",
        "benchmark": "22GB VRAM"
    },
    "InternLM 2.5 (1.8B, 7B, 20B)": {
        "title": "InternLM 2.5 (1.8B, 7B, 20B)",
        "description": "A recent model specialized in very long text processing developed by Shanghai AI Lab.",
        "developer": "Shanghai AI Lab",
        "architecture": "Up to 1000K context, exceptional document summarization.",
        "pros_cons": "**Pros:**\n- Minimal info loss when swallowing and summarizing massive documents\n\n**Cons:**\n- Contains Chinese language bias",
        "use_cases": "- Large-scale document analyzer for enterprises",
        "benchmark": "20B: 14GB VRAM"
    },
    "Baichuan 2 (7B, 13B)": {
        "title": "Baichuan 2 (7B, 13B)",
        "description": "A multi-language model specialized for commerce and medicine from a Chinese AI startup.",
        "developer": "Baichuan",
        "architecture": "Trained on 2.6T tokens focused on English and Chinese.",
        "pros_cons": "**Pros:**\n- Popular for licenses and commercial services within China\n\n**Cons:**\n- Lacks Korean and Western cultural knowledge",
        "use_cases": "- Service engine targeted at the Greater China region",
        "benchmark": "13B: 8.5GB VRAM"
    },
    "ChatGLM 4": {
        "title": "ChatGLM 4",
        "description": "The high-performance 4th-generation GLM architecture model by Tsinghua Univ researchers.",
        "developer": "Tsinghua Univ",
        "architecture": "Efficient GLM architecture supporting 128K.",
        "pros_cons": "**Pros:**\n- Exceptional knowledge search and multi-language ability relative to its low VRAM usage\n\n**Cons:**\n- Cumbersome environment setup",
        "use_cases": "- Multi-language chatbot for research",
        "benchmark": "9GB VRAM"
    },
    "Orion 14B": {
        "title": "Orion 14B",
        "description": "A strong mid-sized model trained on 2.5T tokens of multi-language data.",
        "developer": "OrionStar",
        "architecture": "14B class specialized in Asian language processing.",
        "pros_cons": "**Pros:**\n- High efficiency in processing Asian languages like Japanese and Korean\n\n**Cons:**\n- Overshadowed by the release of Qwen 3",
        "use_cases": "- Unified Asian multi-language chatbot",
        "benchmark": "9GB VRAM"
    },
    "Xverse (7B, 13B, 65B)": {
        "title": "Xverse (7B, 13B, 65B)",
        "description": "A model intensively trained on large-scale multi-language corpora.",
        "developer": "Xverse",
        "architecture": "Trained on a massive dataset of 3.2T tokens.",
        "pros_cons": "**Pros:**\n- The 65B model boasts massive reasoning power\n\n**Cons:**\n- Bias toward Chinese content",
        "use_cases": "- Large corpus research",
        "benchmark": "65B: 38GB VRAM"
    },
    "Aya 23 (8B, 35B)": {
        "title": "Aya 23 (8B, 35B)",
        "description": "A multi-language tuned model specifically made to speak 23 languages like a native.",
        "developer": "Cohere",
        "architecture": "Special multi-language fine-tuning, based on Command R.",
        "pros_cons": "**Pros:**\n- Incredibly smooth translation and understanding of 23 languages including Korean\n\n**Cons:**\n- Coding performance is slightly lacking compared to the newest models",
        "use_cases": "- Global translator, multi-language CS bot",
        "benchmark": "8B: 6GB / 35B: 22GB VRAM"
    },
    "SeaLLM 3": {
        "title": "SeaLLM 3",
        "description": "A specialized model to perfectly cover minor languages in the Southeast Asia (SEA) region.",
        "developer": "Alibaba",
        "architecture": "Intensively trained on minority languages like Thai, Vietnamese, and Indonesian.",
        "pros_cons": "**Pros:**\n- Flawlessly translates Southeast Asian minority languages that even Google Translate struggles with\n\n**Cons:**\n- Low utility for general-purpose tasks",
        "use_cases": "- SEA localization and global game services",
        "benchmark": "8GB VRAM"
    },
    "OpenHermes 2.5": {
        "title": "OpenHermes 2.5",
        "description": "The best 7B tuned model ever made by masterfully mixing numerous datasets.",
        "developer": "Teknium",
        "architecture": "Mistral 7B base, combined with a massive amount of custom datasets.",
        "pros_cons": "**Pros:**\n- Sensibly answers everything from coding to daily chat, like a real human assistant\n\n**Cons:**\n- Base is older, so specs fall behind the latest Llama 4",
        "use_cases": "- Excellent UI/UX reference for local chatbots",
        "benchmark": "5.5GB VRAM"
    }
}
