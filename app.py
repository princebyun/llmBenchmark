import streamlit as st
import streamlit.components.v1 as stc
from streamlit_option_menu import option_menu
from views import tab_hardware, tab_benchmark, tab_leaderboard, tab_history, tab_model_wiki, tab_methodology, tab_blog
from locales import get_text

# ==========================================
# 1. 페이지 설정 및 초기화
# ==========================================
st.set_page_config(
    page_title="LLM Benchmark",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 세션 상태 초기화 (언어 및 메뉴 인덱스 기본값 설정)
if "lang" not in st.session_state:
    st.session_state.lang = "ko"
if "menu_index" not in st.session_state:
    st.session_state.menu_index = 0

def t(key):
    return get_text(st.session_state.lang, key)

# 언어 변경 콜백
def toggle_lang():
    st.session_state.lang = "en" if st.session_state.lang == "ko" else "ko"

# 불필요한 기본 UI 요소 숨기기 및 반응형 최대 너비(900px) 설정
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        [data-testid="stAppDeployButton"] {display:none !important;}
        [data-testid="stHeader"] {display:none !important;}
        [data-testid="stToolbar"] {display:none !important;}
        .block-container {
            max-width: 900px !important;
            padding-top: 2rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# 상단 언어 선택 버튼 (우측 상단 완전히 밀착)
_, btn_col = st.columns([8.5, 1.5])
with btn_col:
    btn_text = "🌐 English" if st.session_state.lang == "ko" else "🌐 한국어"
    st.button(btn_text, on_click=toggle_lang, use_container_width=True)

# ==========================================
# 2. 메인 UI 및 탭 라우팅
# ==========================================
st.title(t("app_title"))
st.markdown(t("app_desc"))

with st.sidebar:
    st.markdown(f"<h2 style='text-align: center; color: #4F46E5; font-weight: 800; font-size: 26px;'>{t('sidebar_title')}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #666; font-size: 13px; margin-top: -10px;'>{t('sidebar_desc')}</p>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 10px 0px 20px 0px;'>", unsafe_allow_html=True)
    
    options_list = [
        t("menu_benchmark"), 
        t("menu_history"),
        t("menu_hardware"),
        t("menu_leaderboard"), 
        t("menu_wiki"),
        t("menu_methodology"),
        t("menu_blog")
    ]
    
    menu_choice = option_menu(
        menu_title=None,
        options=options_list,
        icons=[
            'rocket', 
            'clock-history',
            'sliders',
            'trophy', 
            'book-half',
            'calculator',
            'journal-code'
        ],
        menu_icon="cast",
        default_index=st.session_state.menu_index,
        key=f"menu_{st.session_state.lang}",
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#4F46E5", "font-size": "18px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"5px 0px", "--hover-color": "#F1F5F9", "font-weight": "600"},
            "nav-link-selected": {"background-color": "#4F46E5", "color": "white", "font-weight": "700"},
        }
    )

    if menu_choice in options_list:
        st.session_state.menu_index = options_list.index(menu_choice)

selected_index = st.session_state.menu_index

if selected_index == 2:
    tab_hardware.render()
elif selected_index == 0:
    tab_benchmark.render()
elif selected_index == 1:
    tab_history.render()
elif selected_index == 3:
    tab_leaderboard.render()
elif selected_index == 4:
    tab_model_wiki.render()
elif selected_index == 5:
    tab_methodology.render()
elif selected_index == 6:
    tab_blog.render()

# ==========================================
# 3. 푸터 (저작권 표시)
# ==========================================
st.markdown("""
    <hr style='margin-top: 50px; margin-bottom: 20px; border: 0; border-top: 1px solid #e0e0e0;'>
    <div style='text-align: center; color: #888888; font-size: 13px; font-family: sans-serif;'>
        Copyright ⓒ 2026 Princebyun. All rights reserved.
    </div>
""", unsafe_allow_html=True)
