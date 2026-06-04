import streamlit as st
import math
from data.model_wiki_data import MODEL_WIKI_DATA
def render():
    st.title("📖 모델 사전 (LLM Model Wiki)")
    st.markdown('''
    이 페이지에서는 글로벌 리더보드를 장악하고 있는 **세계 최고 수준의 오픈소스 로컬 LLM 40종**에 대한 깊이 있는 정보를 제공합니다. 
    **[2026년 6월 최신 업데이트]** Llama 4, Gemma 4, Qwen 3 등 가장 최신 트렌드를 반영한 40개의 거대한 모델 가문(Family)을 소개합니다.
    로컬 환경(내 PC)에 모델을 다운로드하기 전에, 아래 사전을 참고하여 내 PC 사양과 사용 목적에 딱 맞는 모델을 찾아보세요!
    ''')
    st.divider()
    
    # ---------------------------------------------------------
    # 검색 기능
    # ---------------------------------------------------------
    search_query = st.text_input("🔍 모델명 검색 (예: Llama, Gemma, Qwen)", placeholder="검색어를 입력하세요...")
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

