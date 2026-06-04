import os

models_data = [
    # Llama Family
    ("Meta Llama 3 8B", "Meta AI", "메타(Meta)에서 공개한 Llama 3 시리즈 중 8B(80억 개) 파라미터를 가진 소형-중형 모델입니다.", "8K 컨텍스트, Grouped Query Attention(GQA) 적용, 15조 토큰 학습.", "압도적인 성능 대비 크기, 최적화 용이성", "짧은 기본 컨텍스트 길이, 지엽적 지식 부족", "개인 비서, 코드 생성, 번역", "4-bit 양자화 기준 최소 6GB VRAM 요구"),
    ("Meta Llama 3 70B", "Meta AI", "Llama 3 시리즈의 하이엔드 70B 모델로 상용 API와 맞먹는 지능을 보여줍니다.", "70B 파라미터, GQA 적용, 8K 컨텍스트.", "GPT-4 급의 엄청난 추론 능력과 풍부한 상식", "최소 40GB 이상의 거대한 VRAM 요구", "전문적인 텍스트 분석, 복잡한 롤플레잉", "4-bit 기준 40GB VRAM 이상 요구 (Mac Studio 권장)"),
    ("Meta Llama 2 7B", "Meta AI", "로컬 LLM 생태계를 폭발적으로 성장시킨 전설적인 Llama 2 시리즈의 기본 모델입니다.", "7B 파라미터, 4K 컨텍스트 길이.", "생태계 호환성 최고, 매우 가벼움", "Llama 3 대비 크게 떨어지는 지능 및 코딩 능력", "단순 요약, 파인튜닝 연구용 베이스", "4-bit 기준 5.5GB VRAM"),
    ("Meta Llama 2 13B", "Meta AI", "Llama 2 7B의 상위 호환 버전으로 밸런스가 가장 좋았던 모델입니다.", "13B 파라미터, 4K 컨텍스트 길이.", "7B보다 눈에 띄게 좋아진 논리력과 안정성", "Llama 3 8B 출시 이후 가성비 하락", "과거 프로젝트의 유지보수 및 레거시 비교", "4-bit 기준 8.5GB VRAM"),
    ("Meta Llama 2 70B", "Meta AI", "Llama 2 시리즈의 가장 강력한 버전으로, 기업용 사내망 구축에 많이 쓰였습니다.", "70B 파라미터, Grouped-Query Attention.", "오픈소스 중 최고 수준의 안정성과 생태계", "엄청난 컴퓨팅 자원 요구", "엔터프라이즈 AI 서버, 대규모 문서 처리", "4-bit 기준 40GB VRAM"),
    
    # Gemma Family
    ("Google Gemma 2 9B", "Google DeepMind", "구글 제미나이 기술을 적용하여 만든 9B 크기의 고성능 개방형 모델입니다.", "9B 파라미터, 8K 컨텍스트, Sliding Window Attention.", "탁월한 한국어 및 추론 능력, 팩트 중심 답변", "동급 8B 모델 대비 살짝 더 높은 메모리 점유율", "학술 및 논문 요약, 정보 검색", "4-bit 기준 6.5GB VRAM"),
    ("Google Gemma 2 27B", "Google DeepMind", "Gemma 2 시리즈의 최상위 모델로 70B급 성능을 27B 체급에서 구현했습니다.", "27B 파라미터, 구글 최신 트레이닝 기법 적용.", "비교적 적은 용량으로 최고의 지능 달성", "RTX 3090/4090 1대로는 턱걸이 구동", "복잡한 데이터 분석, 전문가 수준의 코딩", "4-bit 기준 18GB VRAM"),
    ("Google Gemma 2B", "Google DeepMind", "모바일 및 초경량 디바이스를 위해 극단적으로 다이어트한 모델입니다.", "2B 파라미터, Gemma 1 기반 아키텍처.", "CPU나 스마트폰에서도 원활한 구동", "극심한 환각 현상, 복잡한 지시 불가", "단순 키워드 추출, 엣지(Edge) AI", "4-bit 기준 2.5GB VRAM"),
    ("Google Gemma 7B", "Google DeepMind", "초기 버전인 Gemma 1 시리즈의 7B 모델입니다.", "7B 파라미터, 구글 고유의 구조.", "빠른 응답 속도", "한국어 번역투가 다소 심하고 Gemma 2 대비 지능 낮음", "과거 버전 성능 비교 테스트용", "4-bit 기준 5.5GB VRAM"),
    
    # Qwen Family
    ("Alibaba Qwen 2 7B", "Alibaba Cloud", "중국 알리바바가 공개한 동급 최강의 다국어 및 수학/코딩 특화 모델입니다.", "7B 파라미터, 최대 128K 컨텍스트 지원.", "압도적인 아시아 언어(한국어) 성능, 코딩 및 수학 최상위", "서구권 역사나 팝컬처 편향 부족", "전문 번역기, 코딩 챗봇", "4-bit 기준 5.5GB VRAM"),
    ("Alibaba Qwen 2 72B", "Alibaba Cloud", "Qwen 2 라인업의 플래그십 모델로 Llama 3 70B를 압도하는 벤치마크를 기록했습니다.", "72B 파라미터, 29개국어 사전 학습.", "오픈소스 LLM 중 1,2위를 다투는 종합 지능", "엄청난 VRAM 요구량", "데이터센터용 번역 및 종합 추론 엔진", "4-bit 기준 42GB VRAM"),
    ("Alibaba Qwen 1.5 7B", "Alibaba Cloud", "Qwen 2 출시 전까지 로컬계를 호령했던 Qwen 1.5의 베스트셀러 모델입니다.", "7B 파라미터, 32K 컨텍스트.", "안정적인 성능과 매우 부드러운 한국어", "Qwen 2 등장으로 포지션 애매해짐", "기존 인프라 유지보수용", "4-bit 기준 5.5GB VRAM"),
    ("Alibaba Qwen 1.5 14B", "Alibaba Cloud", "7B의 아쉬운 지능과 32B의 무거움 사이에서 완벽한 타협을 이룬 미들급 모델입니다.", "14B 파라미터.", "16GB VRAM 그래픽카드(RTX 4060 Ti)에 완벽하게 들어가는 최고의 가성비", "한국어 답변이 가끔 중국어 번역투로 빠짐", "일반적인 비서 및 스토리텔링", "4-bit 기준 9GB VRAM"),
    ("Alibaba Qwen 1.5 32B", "Alibaba Cloud", "고성능 하이엔드 유저들을 타겟으로 한 32B 체급의 모델입니다.", "32B 파라미터.", "Mac Studio 등 32GB 이상 램 환경에서 극강의 가성비 발휘", "24GB VRAM GPU 1대로 돌리기 빡셈", "전문적인 프로그래밍 어시스턴트", "4-bit 기준 20GB VRAM"),
    ("Alibaba Qwen 1.5 72B", "Alibaba Cloud", "과거 리더보드를 지배했던 Qwen 1.5 시리즈의 최강자입니다.", "72B 파라미터.", "뛰어난 지식량과 방대한 컨텍스트", "하드웨어 장벽이 너무 높음", "기업용 폐쇄망 AI", "4-bit 기준 42GB VRAM"),
    
    # Phi Family
    ("Microsoft Phi-3 Mini (3.8B)", "Microsoft", "소형언어모델(SLM)의 가능성을 보여준 마이크로소프트의 3.8B 모델입니다.", "3.8B 파라미터, 교과서(Textbook) 수준 고정밀 데이터로 훈련.", "극도로 가벼우면서도 GPT-3.5 수준의 논리력 확보", "상식 지식 부족으로 환각 발생 잦음", "노트북, 라즈베리파이 등 오프라인 구동", "4-bit 기준 3GB VRAM"),
    ("Microsoft Phi-3 Small (7B)", "Microsoft", "Phi-3 라인업 중 7B 체급으로 확장하여 상식 지식을 보완한 모델입니다.", "7B 파라미터, 다국어 처리 능력 향상.", "Mini의 아쉬운 지능을 완벽히 보완", "용량이 커져 모바일 구동은 힘들어짐", "데스크탑 챗봇", "4-bit 기준 5.5GB VRAM"),
    ("Microsoft Phi-3 Medium (14B)", "Microsoft", "Phi-3의 강력한 추론 능력을 14B 체급으로 끌어올린 모델입니다.", "14B 파라미터.", "수학 및 논리 문제에서 압도적인 성능", "한국어보다는 영어 성능에 치중됨", "알고리즘 및 수학 문제 풀이", "4-bit 기준 9GB VRAM"),
    
    # Mistral & Mixtral
    ("Mistral 7B Instruct", "Mistral AI", "Llama 3 등장 전까지 오픈소스 생태계를 지배했던 전설적인 가성비 모델입니다.", "7B 파라미터, GQA 및 SWA 최초 도입.", "검열이 적어 자유로운 답변 생성, 빠른 속도", "최신 모델 대비 떨어지는 한국어 능력", "창의적 글쓰기, 롤플레잉", "4-bit 기준 5.5GB VRAM"),
    ("Mistral NeMo 12B", "Mistral AI & NVIDIA", "미스트랄과 엔비디아가 협력하여 12B 체급으로 새롭게 내놓은 최신 모델입니다.", "12B 파라미터, 128K 컨텍스트, 새로운 토크나이저(Tekken) 적용.", "12B라는 독특한 체급에서 나오는 최적의 밸런스와 방대한 컨텍스트", "아직 지원하지 않는 로컬 툴들이 일부 존재", "대형 문서 읽기 및 요약", "4-bit 기준 8GB VRAM"),
    ("Mixtral 8x7B", "Mistral AI", "MoE(Mixture of Experts) 아키텍처를 오픈소스에 유행시킨 선구적인 모델입니다.", "8개의 7B 전문가 모델 결합(총 47B), 실제 활성화는 13B 수준.", "47B 지식을 가졌지만 13B 속도로 작동하는 기적의 가성비", "MoE 특성상 VRAM은 결국 47B 전체 용량을 차지함", "다양한 주제를 다루는 종합 챗봇", "4-bit 기준 26GB VRAM"),
    ("Mixtral 8x22B", "Mistral AI", "초대형 MoE 모델로 GPT-4급 성능을 목표로 만들어졌습니다.", "8개의 22B 전문가 모델 결합(총 141B).", "압도적인 지식량과 뛰어난 추론", "개인 PC에서는 구동 불가능한 램 용량 요구", "기업용 거대 데이터센터 서빙", "4-bit 기준 80GB VRAM 이상"),
    
    # DeepSeek
    ("DeepSeek Coder 6.7B", "DeepSeek AI", "개발자들을 위해 코딩(프로그래밍) 작성에 특화된 전문 모델입니다.", "6.7B 파라미터, 2조 토큰 코딩/수학 데이터 학습.", "어지간한 70B 모델을 뛰어넘는 미친 코딩 작성 능력", "일반 대화나 요약 등 일상적인 질문에는 멍청함", "VSC 연동 코파일럿, 사내 코드 리뷰", "4-bit 기준 5.5GB VRAM"),
    ("DeepSeek Coder 33B", "DeepSeek AI", "더 복잡한 프로젝트 구조를 파악하기 위해 체급을 키운 코딩 모델입니다.", "33B 파라미터.", "16K 이상의 긴 코드베이스 전체 문맥 파악", "무거워서 일반 개발자 PC에서는 버벅임", "엔터프라이즈 레벨 코드 리팩토링", "4-bit 기준 20GB VRAM"),
    ("DeepSeek LLM 7B", "DeepSeek AI", "중국의 기술력을 보여준 딥시크의 기본 언어 모델입니다.", "7B 파라미터.", "빠르고 안정적인 답변", "Qwen에 비해 다국어 성능이 살짝 밀림", "일반 대화 및 번역", "4-bit 기준 5.5GB VRAM"),
    ("DeepSeek LLM 67B", "DeepSeek AI", "딥시크의 67B 하이엔드 모델입니다.", "67B 파라미터.", "강력한 수학적 사고력", "최소 2장의 3090급 GPU 필요", "수학 논문 분석", "4-bit 기준 38GB VRAM"),
    
    # Solar (Upstage)
    ("Solar 10.7B", "Upstage", "한국의 업스테이지(Upstage)가 Llama 2를 기반으로 개조하여 만든 세계 1위 출신 모델입니다.", "10.7B 파라미터, Depth Up-Scaling(DUS) 기법 사용.", "10B 체급에서 30B 체급을 이기는 놀라운 효율성, 뛰어난 한국어", "Llama 3 등장 이후 약간 빛을 바램", "한국어 특화 서비스 구축", "4-bit 기준 7.5GB VRAM"),
    ("Upstage Solar Pro", "Upstage", "Solar의 후속작으로 더 뛰어난 한국어 능력과 긴 컨텍스트를 장착했습니다.", "새로운 아키텍처 및 한국어 튜닝 극대화.", "가장 완벽하고 자연스러운 한국어 구사 능력", "글로벌 생태계 지원 속도", "한국어 전용 챗봇 및 요약 엔진", "4-bit 기준 8GB VRAM"),
    
    # Falcon
    ("Falcon 7B", "TII", "UAE 기술혁신연구소에서 공개하여 화제가 되었던 고성능 모델입니다.", "7B 파라미터.", "오픈소스 생태계 초창기의 선구자적 역할", "현재 기준으로는 매우 구형 아키텍처", "구형 하드웨어 벤치마크 대조군", "4-bit 기준 5.5GB VRAM"),
    ("Falcon 40B", "TII", "공개 당시 리더보드 1위를 휩쓸었던 팔콘의 중형 모델입니다.", "40B 파라미터.", "상업적 사용이 완전 무료인 강력한 라이선스", "최신 7B 모델들에게 밀리는 성능", "기업 상업용 무료 엔진", "4-bit 기준 24GB VRAM"),
    ("Falcon 180B", "TII", "가장 거대한 오픈소스 모델 중 하나로, 파라미터 수가 1800억 개에 달합니다.", "180B 파라미터.", "압도적인 체급에서 나오는 지식", "개인은 절대 구동 불가능", "연구소 및 클러스터 컴퓨팅 테스트", "4-bit 기준 100GB VRAM 이상"),
    
    # Yi
    ("Yi 6B", "01.AI", "리 카이푸(Li Kaifu)가 설립한 01.AI에서 만든 초고성능 중국발 모델입니다.", "6B 파라미터.", "6B라는 애매한 사이즈 대비 강력한 벤치마크 점수", "영어/중국어 위주의 편향", "단순 영-중 번역", "4-bit 기준 5GB VRAM"),
    ("Yi 34B", "01.AI", "Yi 시리즈의 진정한 명작으로 34B 체급에서 최강을 자랑했습니다.", "34B 파라미터, 매우 긴 200K 컨텍스트 지원.", "엄청난 컨텍스트 창 덕분에 책 수십 권 분량 한 번에 처리", "로컬 구동 시 속도 저하 큼", "장편 소설 번역, 법률 문서 검토", "4-bit 기준 22GB VRAM"),
    
    # Vicuna & WizardLM & Others
    ("Vicuna 7B", "LMSYS", "Llama 1 시절부터 이어져 온 챗봇 튜닝의 대명사 격인 모델입니다.", "7B 파라미터, ShareGPT 데이터로 파인튜닝.", "인간의 대화 패턴에 가장 자연스럽게 훈련됨", "구형 베이스 모델의 한계", "챗봇 UI/UX 테스트용", "4-bit 기준 5.5GB VRAM"),
    ("Vicuna 13B", "LMSYS", "Vicuna 7B의 상위 호환 버전입니다.", "13B 파라미터.", "자연스러운 대화 흐름 유지", "성능 대비 무거운 요구 사항", "구형 로컬 봇 서비스", "4-bit 기준 8.5GB VRAM"),
    ("WizardLM 13B", "Microsoft/WizardLM", "지시 복잡성(Instruction Complexity)을 훈련시켜 논리력을 극대화한 모델입니다.", "13B 파라미터, Evol-Instruct 기법 적용.", "복잡하고 여러 단계의 지시사항을 잘 따름", "구형 Llama 2 베이스로 인한 한계", "복합적인 명령 수행 비서", "4-bit 기준 8.5GB VRAM"),
    ("Zephyr 7B", "Hugging Face", "미스트랄 7B를 기반으로 DPO(Direct Preference Optimization)를 적용해 정렬(Alignment)을 극대화했습니다.", "7B 파라미터, DPO 강화학습 적용.", "매우 친절하고 긍정적인 답변 스타일", "한국어 능력 부족", "영문 친화적 AI 비서", "4-bit 기준 5.5GB VRAM"),
    ("OpenChat 3.5", "OpenChat", "미스트랄 기반으로 아주 뛰어난 튜닝을 거쳐 벤치마크 상위권을 장악했던 모델입니다.", "7B 파라미터, C-RLFT 기법 적용.", "7B 체급에서 코딩과 챗봇 모두 최상위권", "Llama 3 등장 이후 포지션 겹침", "코딩 및 일상 대화 보조", "4-bit 기준 5.5GB VRAM"),
    ("TinyLlama 1.1B", "Open Source", "단 1.1B 파라미터로 초경량의 끝을 보여주는 장난감(Toy) 모델입니다.", "1.1B 파라미터, 3조 토큰 학습.", "웹 브라우저에서도 돌아갈 정도로 극도로 가벼움", "한국어 거의 불가능", "연구 교육용 교보재", "4-bit 기준 1.5GB VRAM 미만"),
    ("StarCoder 15.5B", "BigCode", "전 세계 개발자들이 힘을 모아 만든 순수 오픈소스 코딩 특화 모델입니다.", "15.5B 파라미터.", "다양한 개발 언어 지원 및 뛰어난 코드 완성", "일반 언어 능력이 매우 떨어짐", "순수 코드 자동완성(Autocomplete) 서버", "4-bit 기준 10GB VRAM")
]

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
    로컬 환경(내 PC)에 모델을 다운로드하기 전에, 아래 사전을 참고하여 내 PC 사양과 사용 목적에 딱 맞는 모델을 찾아보세요!
    ''')
    st.divider()
    
    # ---------------------------------------------------------
    # 검색 기능
    # ---------------------------------------------------------
    search_query = st.text_input("🔍 모델명 검색 (예: Llama, Qwen)", placeholder="검색어를 입력하세요...")
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

print("Successfully generated tab_model_wiki.py with 40 models.")
