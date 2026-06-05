import streamlit as st
import math
from data.model_wiki_data import MODEL_WIKI_DATA, MODEL_WIKI_DATA_EN
from locales import get_text

def t(key):
    return get_text(st.session_state.lang, key)

def render():
    st.title(t("wiki_title"))
    st.markdown(t("wiki_desc_long"))
    st.divider()
    
    # ---------------------------------------------------------
    # 검색 기능
    # ---------------------------------------------------------
    search_query = st.text_input(t("wiki_search"), placeholder=t("wiki_search_ph"))
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
        if st.button(t("wiki_prev"), disabled=(st.session_state['wiki_page'] <= 1), use_container_width=True):
            st.session_state['wiki_page'] -= 1
            st.rerun()
            
    with col2:
        st.markdown(f"<h4 style='text-align: center;'>{t('wiki_page_text')} {st.session_state['wiki_page']} / {total_pages}</h4>", unsafe_allow_html=True)
        
    with col3:
        if st.button(t("wiki_next"), disabled=(st.session_state['wiki_page'] >= total_pages), use_container_width=True):
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
        st.warning(t("wiki_empty"))
    
    wiki_data = MODEL_WIKI_DATA_EN if st.session_state.lang == "en" else MODEL_WIKI_DATA
    
    for i, model_name in enumerate(page_models):
        data = wiki_data[model_name]
        
        with st.expander(f"📦 **{start_idx + i + 1}. {data['title']}**"):
            st.caption(f"**{t('wiki_dev')}:** {data['developer']}")
            st.markdown(f"**{t('wiki_summary')}:** {data['description']}")
            
            st.subheader(f"🧬 {t('wiki_arch')}")
            st.markdown(data["architecture"])
            
            st.subheader(f"⚖️ {t('wiki_proscons')}")
            st.markdown(data["pros_cons"])
            
            st.subheader(f"💡 {t('wiki_usecase')}")
            st.markdown(data["use_cases"])
            
            st.subheader(f"📊 {t('wiki_req')}")
            st.info(data["benchmark"])
            
    # 하단 네비게이션 복제
    st.divider()
    b_col1, b_col2, b_col3 = st.columns([1, 2, 1])
    with b_col1:
        if st.button(f"{t('wiki_prev')} ({t('wiki_bottom')})", disabled=(st.session_state['wiki_page'] <= 1), use_container_width=True, key="bottom_prev"):
            st.session_state['wiki_page'] -= 1
            st.rerun()
    with b_col3:
        if st.button(f"{t('wiki_next')} ({t('wiki_bottom')})", disabled=(st.session_state['wiki_page'] >= total_pages), use_container_width=True, key="bottom_next"):
            st.session_state['wiki_page'] += 1
            st.rerun()

