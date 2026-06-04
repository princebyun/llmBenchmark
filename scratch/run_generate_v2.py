import os

# Consolidated and expanded models data (40 unique model families)
models_data = [
    # Meta
    ("Meta Llama 3 시리즈 (8B, 70B)", "Meta AI", "로컬 LLM의 절대적인 기준점. 8B와 70B 두 가지 체급으로 제공되는 최고 성능의 모델입니다.", "트랜스포머 디코더, 8K 컨텍스트, Grouped Query Attention(GQA). 15조 토큰 학습.", "체급 대비 압도적 지능, 훌륭한 한국어 지원, 거대한 생태계", "기본 컨텍스트 길이가 8K로 긴 문서 처리에 불리함", "일상적인 챗봇, 코드 생성, 텍스트 요약", "8B: 6GB VRAM / 70B: 40GB VRAM"),
    ("Meta Llama 2 시리즈 (7B, 13B, 70B)", "Meta AI", "오픈소스 LLM 생태계를 폭발적으로 성장시킨 전설적인 이전 세대 모델입니다.", "트랜스포머 기반, 4K 컨텍스트.", "안정적이고 가장 많은 파인튜닝 레퍼런스 보유", "최신 모델 대비 떨어지는 지능 및 한국어 능력", "레거시 시스템 유지보수, 파인튜닝 교육용", "7B: 5.5GB / 13B: 8.5GB / 70B: 40GB VRAM"),
    ("CodeLlama 시리즈 (7B~70B)", "Meta AI", "Llama 2를 기반으로 코딩 능력을 극대화한 개발자용 모델입니다.", "최대 100K 토큰 지원, 파이썬/C++ 등 특화 학습.", "광범위한 언어 지원, 매우 긴 코드 컨텍스트 이해", "일반적인 대화나 한국어 질문에는 취약함", "로컬 Copilot 연동, 코드 자동 완성", "체급에 따라 5.5GB ~ 40GB VRAM"),
    
    # Google
    ("Google Gemma 2 시리즈 (2B, 9B, 27B)", "Google DeepMind", "제미나이(Gemini) 기술로 빚어낸 강력하고 가벼운 최신 오픈 모델 라인업입니다.", "8K 컨텍스트, Sliding Window Attention 적용.", "Llama 3를 위협하는 강력한 벤치마크 점수 및 팩트 정확도", "특이한 파라미터 수(9B, 27B)로 인한 애매한 VRAM 요구량", "학술 논문 분석, 정확한 정보 검색", "9B: 6.5GB / 27B: 18GB VRAM"),
    ("Google Gemma 1 시리즈 (2B, 7B)", "Google DeepMind", "Gemma 라인업의 첫 번째 세대 모델입니다.", "Gemma 오리지널 아키텍처.", "모바일(2B)에서도 구동 가능한 범용성", "한국어 번역투 심함, 잦은 환각(Hallucination)", "저전력 디바이스(Edge) 텍스트 처리", "2B: 2.5GB / 7B: 5.5GB VRAM"),
    
    # Alibaba
    ("Qwen 2 시리즈 (0.5B ~ 72B)", "Alibaba Cloud", "현존 오픈소스 중 최고의 다국어 처리 능력과 코딩 능력을 자랑하는 모델입니다.", "최대 128K 컨텍스트, 29개국어 사전 학습.", "놀랍도록 자연스러운 한국어 구사, 수학/코딩 최상위권", "서구권 중심의 문화적/역사적 지식 부족", "다국어 번역기, 논리적 수학 문제 풀이", "7B: 5.5GB / 72B: 42GB VRAM"),
    ("Qwen 1.5 시리즈 (0.5B ~ 110B)", "Alibaba Cloud", "다양한 파라미터 선택지(14B, 32B 등)를 제공했던 훌륭한 이전 세대 모델입니다.", "32K 컨텍스트.", "내 그래픽카드 VRAM에 딱 맞게 고를 수 있는 다양한 체급", "Qwen 2 출시로 인한 성능 우위 상실", "특정 VRAM(16GB 등) 환경에 맞춘 서버 구축", "14B: 9GB / 32B: 20GB VRAM"),
    ("Qwen-VL / Audio", "Alibaba Cloud", "텍스트뿐만 아니라 이미지와 소리까지 이해하는 멀티모달(Multimodal) 모델입니다.", "시각 및 청각 인코더가 결합된 아키텍처.", "이미지 안의 글씨(OCR)나 상황을 정확히 인식함", "텍스트 전용 모델보다 VRAM을 훨씬 많이 차지함", "이미지 캡셔닝, 시각 장애인용 사진 묘사", "최소 10GB VRAM 이상"),
    
    # Microsoft
    ("Microsoft Phi-3 (Mini, Small, Medium)", "Microsoft", "SLM(소형언어모델)의 기적. 아주 작은 크기로 GPT-3.5급 논리를 펼칩니다.", "교과서(Textbook) 수준의 정제된 고품질 데이터 집중 훈련.", "극도로 적은 VRAM 소모, 압도적인 논리력", "세상의 모든 지식을 담기엔 모델 뇌가 너무 작아 환각 발생", "오프라인 모바일 앱, 단순 텍스트 요약", "Mini(3.8B): 3GB / Medium(14B): 9GB VRAM"),
    ("WizardLM 시리즈 (7B ~ 70B)", "Microsoft/WizardLM", "지시 복잡성(Instruction Complexity)을 훈련시켜 명령 수행력을 높인 모델입니다.", "Evol-Instruct 기법 적용.", "복잡하고 여러 단계로 꼬인 사용자의 지시를 정확히 따름", "최신 베이스 모델(Llama 3 등) 미적용 시 성능 한계", "복합적인 명령을 내리는 비서", "체급별 상이 (5.5GB ~ 40GB)"),
    
    # Mistral
    ("Mistral 7B & NeMo 12B", "Mistral AI", "오픈소스 생태계를 이끌어온 미스트랄의 핵심 단일(Dense) 모델 라인업입니다.", "GQA, SWA(Sliding Window Attention), Tekken 토크나이저.", "체급을 뛰어넘는 가성비, 검열이 적은 자유로운 텍스트", "안전장치가 부족해 상용 서비스 시 필터링 주의", "창의적 글쓰기, 웹소설 작성", "7B: 5.5GB / 12B: 8GB VRAM"),
    ("Mixtral (8x7B, 8x22B)", "Mistral AI", "여러 명의 전문가(Expert)가 협력하는 MoE 아키텍처 모델입니다.", "MoE(Mixture of Experts) 방식. 활성 파라미터는 전체의 약 1/4 수준.", "거대한 지식량을 가졌음에도 답변 출력 속도가 매우 빠름", "메모리(VRAM) 자체는 전체 크기만큼 거대하게 다 차지함", "기업용 다목적 챗봇, 종합 지식 검색", "8x7B: 26GB / 8x22B: 80GB VRAM"),
    
    # DeepSeek
    ("DeepSeek Coder (1.3B ~ 33B, V2)", "DeepSeek AI", "전 세계 수많은 프로그래머들의 로컬 코파일럿으로 쓰이는 코딩 모델입니다.", "2조 토큰 이상의 방대한 코드 및 수학 데이터 집중 학습.", "어지간한 70B 범용 모델을 압도하는 정교한 코드 작성 능력", "코딩 이외의 일반 대화는 다소 부자연스러움", "로컬 코드 에디터 연동, 사내 코드 리뷰", "6.7B: 5.5GB / 33B: 20GB VRAM"),
    ("DeepSeek LLM (7B, 67B)", "DeepSeek AI", "딥시크 기술력의 기반이 되는 강력한 범용 언어 모델입니다.", "중국어와 영어 중심의 대규모 사전 학습.", "수학적 사고력이 훌륭하고 매우 빠른 응답성", "한국어 번역이나 대화 시 어색함이 남음", "수학 논문 요약, 영-중 번역", "7B: 5.5GB / 67B: 38GB VRAM"),
    
    # Upstage (Korean Pride)
    ("Upstage Solar 10.7B", "Upstage", "대한민국의 업스테이지가 만들어 글로벌 1위를 달성했던 명작 모델입니다.", "Depth Up-Scaling (DUS) 기법을 통한 Llama 2 기반 확장 아키텍처.", "10B 체급에서 30B를 이기는 벤치마크, 훌륭한 한국어 이해", "최신 세대 모델들의 등장으로 가성비 약간 하락", "한국어 중심의 챗봇 서비스 구축", "7.5GB VRAM"),
    ("Upstage Solar Pro", "Upstage", "Solar 10.7B의 성공을 잇는 최신 업그레이드 버전입니다.", "대폭 개선된 한국어 튜닝 및 컨텍스트 확장.", "더욱 매끄러워진 한국어 문장력과 논리 추론", "해외 모델 대비 상대적으로 좁은 생태계 지원", "국내 기업용 사내망 AI 엔진", "8GB VRAM"),
    
    # TII (UAE)
    ("Falcon (7B, 40B, 180B)", "TII", "UAE에서 막대한 자본으로 훈련시켜 상업적 무료로 푼 혁신적 모델 라인업입니다.", "커스텀 트랜스포머 아키텍처.", "상업적 제약이 전혀 없는 완전한 오픈 라이선스, 방대한 지식(180B)", "구형 아키텍처로 인한 속도 및 토큰 효율성 저하", "라이선스 제약 없는 상용 서비스망 구축", "40B: 24GB / 180B: 100GB 이상"),
    
    # 01.AI (Yi)
    ("Yi 시리즈 (6B, 34B)", "01.AI", "중국 01.AI의 역작으로 긴 텍스트 문맥 유지에 특화된 모델입니다.", "최대 200K의 압도적인 컨텍스트 길이 지원.", "소설책 수십 권 분량을 한 번에 기억하는 엄청난 장기 기억력", "긴 컨텍스트 사용 시 급격히 증가하는 VRAM 소모량", "장편 소설 번역, 방대한 법률/의료 문서 검토", "6B: 5GB / 34B: 22GB VRAM"),
    
    # Cohere
    ("Command R (35B)", "Cohere", "RAG(검색 증강 생성)와 외부 도구(API) 사용에 극도로 특화된 모델입니다.", "35B 파라미터, 도구 사용(Tool Use) 특화 학습, 128K 컨텍스트.", "주어진 문서를 바탕으로 가장 정확하게 답변을 뽑아냄 (환각 최소화)", "로컬 구동 시 무거운 체급", "기업 사내 문서 기반 검색(RAG) 시스템", "22GB VRAM"),
    ("Command R+ (104B)", "Cohere", "Command R의 성능을 극한으로 끌어올린 엔터프라이즈급 104B 거대 모델입니다.", "104B 파라미터, 다국어 RAG 성능 최적화.", "오픈소스 최고 수준의 정확도와 도구 제어 능력", "개인 장비로는 절대 불가능한 엄청난 하드웨어 요구", "거대 데이터센터용 복합 에이전트 구축", "최소 60GB VRAM"),
    
    # Databricks & xAI
    ("DBRX (132B)", "Databricks", "데이터브릭스가 공개한 132B 크기의 초대형 오픈소스 MoE 모델입니다.", "세밀한 MoE (Fine-grained Mixture-of-Experts) 아키텍처.", "빠른 속도와 강력한 코딩/수학/논리 퍼포먼스", "무거운 용량", "대규모 기업용 분석 시스템", "80GB VRAM 이상"),
    ("Grok-1 (314B)", "xAI", "일론 머스크의 xAI가 공개한 현존 최대 크기의 314B 오픈소스 모델입니다.", "MoE 아키텍처, 314B 파라미터.", "상상을 초월하는 거대한 지식량과 재치 있는 답변 스타일", "슈퍼컴퓨터 급 장비가 아니면 다운로드조차 부담스러움", "대규모 AI 클러스터 연구용", "최소 200GB VRAM 이상"),
    
    # Others (Unique & Popular)
    ("Vicuna (7B, 13B, 33B)", "LMSYS", "가장 오랜 기간 사랑받아 온 대화형(Chat) 튜닝의 교과서 모델입니다.", "ShareGPT의 고품질 사용자 대화 데이터로 파인튜닝.", "마치 진짜 사람과 채팅하는 듯한 부드럽고 찰진 대화 톤", "최신 지식 및 다국어 지원 부족", "챗봇 UI/UX 프로토타입 제작", "체급별 상이"),
    ("Zephyr (7B, 141B)", "Hugging Face H4", "DPO(직접 선호 최적화) 기술을 널리 알린 매우 친절한 성격의 모델입니다.", "미스트랄 및 Mixtral 베이스에 DPO 강화학습 적용.", "사용자의 지시를 매우 긍정적이고 헌신적으로 수행함", "한국어로 물으면 영어로 대답하려는 경향", "영문 기반 친절한 고객지원 봇", "7B: 5.5GB / 141B: 80GB VRAM"),
    ("OpenChat 3.5", "OpenChat", "오픈소스 데이터만으로 벤치마크 상위권을 장악했던 기적의 튜닝 모델입니다.", "C-RLFT 기법 (조건부 강화학습).", "7B라는 작은 크기에서 나오는 완벽에 가까운 코딩과 일상 대화", "Llama 3 등장 이후 포지션이 겹쳐 사용 빈도 감소", "범용적인 로컬 비서", "5.5GB VRAM"),
    ("TinyLlama 1.1B", "Open Source", "웹 브라우저에서도 돌아갈 수 있게 만든 초미니 장난감(Toy) 모델입니다.", "1.1B 초소형 아키텍처, 3조 토큰 학습.", "이론상 라즈베리파이나 스마트워치에서도 구동되는 극한의 가벼움", "한국어 불가, 복잡한 논리 불가", "LLM 원리 교육 및 구조 테스트", "1.5GB VRAM 미만"),
    ("StarCoder 2 (3B, 7B, 15B)", "BigCode", "전 세계 개발자들이 연합하여 구축한 순수 오픈소스 코드 생성기입니다.", "600개 이상의 프로그래밍 언어로 훈련됨.", "거의 모든 마이너한 프로그래밍 언어까지 커버하는 방대한 코드 지식", "대화형(Chat) 능력이 심각하게 결여됨", "VSC 백그라운드 자동완성 서버", "15B: 10GB VRAM"),
    ("Jamba", "AI21 Labs", "전통적인 트랜스포머의 한계를 깬 혁신적인 하이브리드 모델입니다.", "Mamba (SSM) + Transformer 하이브리드 아키텍처.", "엄청나게 긴 텍스트를 처리할 때도 VRAM과 연산량이 크게 늘지 않음", "아직 지원하는 생태계 툴(Ollama 등)이 제한적임", "장편 소설 한 권 전체 분석", "12GB VRAM"),
    ("OLMo (1B, 7B)", "Allen AI", "AI 연구의 투명성을 위해 학습 코드와 데이터까지 전부 공개한 100% 진정한 오픈 모델입니다.", "학습 데이터(Dolma)와 트레이닝 스크립트 완전 공개.", "데이터 출처가 투명하여 라이선스 분쟁의 여지가 없음", "타 7B 모델 대비 벤치마크 퍼포먼스 자체는 낮음", "기업의 자체 파인튜닝을 위한 퓨어 베이스", "5.5GB VRAM"),
    ("Stable LM 2 (1.6B, 12B)", "Stability AI", "스테이블 디퓨전(Stable Diffusion)으로 유명한 회사에서 만든 언어 모델입니다.", "다양한 데이터셋의 최적 혼합 비율(Mix) 적용.", "투명하고 뛰어난 영문 생성 품질", "타사 모델에 비해 낮은 인지도와 한글 튜닝 부재", "가벼운 영문 텍스트 생성기", "1.6B: 2GB VRAM"),
    ("LLaVA 시리즈", "UW/MSR", "Llama 모델에 '눈'을 달아주어 이미지를 볼 수 있게 만든 멀티모달 선구자입니다.", "Vision Encoder (CLIP) + 언어 모델 (Llama/Vicuna) 결합.", "입력한 이미지의 내용을 텍스트로 아주 상세하고 정확하게 묘사함", "일반 텍스트만 처리할 때보다 무겁고 속도가 느림", "시각 기반 질의응답(VQA)", "최소 8GB VRAM"),
    ("Phind-CodeLlama 34B", "Phind", "개발자 전용 검색엔진 Phind에서 튜닝한 압도적인 코딩 모델입니다.", "CodeLlama 34B 베이스 + 고품질 프롬프트 응답 튜닝.", "복잡한 에러 코드를 던져주면 해결책을 귀신같이 찾아냄", "일반 유저가 돌리기 힘든 34B 체급의 무거움", "시니어 개발자의 코드 디버깅 보조", "22GB VRAM"),
    
    # Asia Focused Models
    ("InternLM 2 (1.8B, 7B, 20B)", "Shanghai AI Lab", "중국 상하이 AI 연구소에서 개발한 매우 긴 텍스트 처리 전문 모델입니다.", "최대 200K 컨텍스트, 탁월한 문서 요약력.", "거대한 문서를 통째로 넣고 요약할 때 정보 누락이 적음", "중국어 편향성 존재", "기업용 대규모 문서 분석기", "20B: 14GB VRAM"),
    ("Baichuan 2 (7B, 13B)", "Baichuan", "중국의 AI 벤처에서 만든 상업 및 의료 특화 다국어 모델입니다.", "영어와 중국어 중심의 2.6조 토큰 학습.", "중국 내 라이선스 및 상업 서비스용으로 각광", "한국어 및 서양 문화 지식 부재", "중화권 타겟 서비스 엔진", "13B: 8.5GB VRAM"),
    ("ChatGLM 3 (6B)", "Tsinghua Univ", "칭화대 연구진이 만든 중국 최초의 걸작 6B 모델입니다.", "효율적인 GLM 아키텍처 도입.", "낮은 VRAM 소모량 대비 탁월한 지식 검색 능력", "영-중 외의 다국어(한국어)는 사실상 불가능", "연구용 레퍼런스", "5GB VRAM"),
    ("Orion 14B", "OrionStar", "2.5조 토큰의 다국어 훈련을 받은 강력한 중형급 모델입니다.", "아시아 언어 처리에 특화된 14B 체급.", "일본어, 한국어 등 다국어 처리 효율이 상당히 높음", "Qwen 시리즈의 그늘에 가려진 인지도", "아시아 통합 다국어 챗봇", "9GB VRAM"),
    ("Xverse (7B, 13B, 65B)", "Xverse", "대규모 다국어 말뭉치를 집중적으로 훈련받은 모델입니다.", "3.2조 토큰의 거대 데이터셋 학습.", "65B 모델의 경우 GPT-3.5를 압도하는 훌륭한 추론력", "마찬가지로 중국어 중심의 편향", "대형 코퍼스 연구용", "65B: 38GB VRAM"),
    ("Aya 23 (8B, 35B)", "Cohere", "무려 23개의 언어를 원어민처럼 구사하기 위해 특별히 만들어진 다국어 최적화 모델입니다.", "다국어 특별 파인튜닝, Command R 베이스.", "한국어를 포함한 23개 언어를 놀랍도록 매끄럽게 번역하고 이해함", "영어 전용 모델에 비해 코딩 능력이 살짝 떨어짐", "글로벌 번역기, 다국어 CS 봇", "8B: 6GB / 35B: 22GB VRAM"),
    ("Breeze 7B (대만)", "MediaTek", "대만의 미디어텍(MediaTek)에서 번체 중국어(Taiwanese)에 특화시켜 만든 모델입니다.", "Mistral 7B 기반 번체 튜닝.", "대만의 문화와 번체 한자를 가장 완벽하게 묘사함", "한국인에게는 필요성이 매우 낮음", "대만 타겟 서비스 특화 봇", "5.5GB VRAM"),
    ("SeaLLM (7B, 13B)", "Alibaba", "동남아시아(SEA) 지역의 마이너한 언어들을 완벽하게 커버하기 위한 모델입니다.", "태국어, 베트남어, 인니어 등 소수 언어 집중 훈련.", "구글 번역기도 잘 못하는 동남아 소수 언어를 찰떡같이 번역함", "일반 범용 목적으론 활용도 낮음", "동남아 현지화 및 글로벌 게임 서비스", "13B: 8.5GB VRAM"),
    ("OpenHermes 2.5 (7B)", "Teknium", "오픈소스 튜너 Teknium이 수많은 데이터셋을 기가 막히게 배합하여 만든 명작 튜닝 모델입니다.", "Mistral 7B 베이스, 엄청난 양의 커스텀 데이터셋 조합.", "마치 실제 사람 비서처럼 코딩부터 일상 대화까지 센스 있게 대답함", "베이스가 구형이라 최신 Llama 3 8B에 벤치마크는 밀림", "로컬 비서의 훌륭한 레퍼런스", "5.5GB VRAM")
]

# Ensure we only have 40 models
models_data = models_data[:40]

template = """
# -*- coding: utf-8 -*-
import streamlit as st

MODEL_WIKI_DATA = {{
{dict_content}
}}

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
        st.markdown(f"<h4 style='text-align: center;'>페이지 {{st.session_state['wiki_page']}} / {{total_pages}}</h4>", unsafe_allow_html=True)
        
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
        
        with st.expander(f"📦 **{{start_idx + i + 1}}. {{data['title']}}**"):
            st.caption(f"**개발사:** {{data['developer']}}")
            st.markdown(f"**요약:** {{data['description']}}")
            
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

"""

dict_str = ""
for model in models_data:
    pros_cons = f"**장점 (Pros):**\\n- {model[4]}\\n\\n**단점 (Cons):**\\n- {model[5]}"
    dict_str += f'''    "{model[0]}": {{
        "title": "{model[0]}",
        "description": "{model[2]}",
        "developer": "{model[1]}",
        "architecture": "{model[3]}",
        "pros_cons": """{pros_cons}""",
        "use_cases": "- {model[6]}",
        "benchmark": "{model[7]}"
    }},\n'''

final_code = template.format(dict_content=dict_str)

with open(r"d:\princebyun\agent\llmBenchmark\views\tab_model_wiki.py", "w", encoding="utf-8") as f:
    f.write(final_code)

print("Successfully generated tab_model_wiki.py with 40 consolidated models.")
