import streamlit as st
from streamlit_option_menu import option_menu
from views import tab_settings, tab_benchmark, tab_leaderboard, tab_history, tab_model_wiki, tab_methodology, tab_blog

# ==========================================
# 1. 페이지 설정 및 초기화
# ==========================================
st.set_page_config(
    page_title="로컬 LLM 하드웨어 벤치마크",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 불필요한 기본 UI 요소 숨기기 및 반응형 최대 너비(900px) 설정
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        [data-testid="stAppDeployButton"] {display:none !important;}
        .block-container {
            max-width: 900px !important;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 메인 UI 및 탭 라우팅
# ==========================================
st.title("🚀 로컬 LLM 하드웨어 벤치마크 및 진단")
st.markdown("Ollama, LM Studio, vLLM, oMLX 등에 설치된 모델을 감지하고 내 PC의 성능(TPS)을 글로벌 기준과 비교합니다.")

with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #4F46E5; font-weight: 800; font-size: 26px;'>LLM Benchmark</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666; font-size: 13px; margin-top: -10px;'>내 PC 하드웨어 한계 돌파</p>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 10px 0px 20px 0px;'>", unsafe_allow_html=True)
    
    menu_choice = option_menu(
        menu_title=None,
        options=[
            "진단 환경 설정",
            "벤치마크 실행", 
            "벤치마크 이력",
            "글로벌 리더보드", 
            "모델 사전",
            "측정 방법론",
            "가이드 & 블로그"
        ],
        icons=[
            'sliders',
            'rocket', 
            'clock-history',
            'trophy', 
            'book-half',
            'calculator',
            'journal-code'
        ],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#4F46E5", "font-size": "18px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"5px 0px", "--hover-color": "#F1F5F9", "font-weight": "600"},
            "nav-link-selected": {"background-color": "#4F46E5", "color": "white", "font-weight": "700"},
        }
    )

if menu_choice == "진단 환경 설정":
    tab_settings.render()
elif menu_choice == "벤치마크 실행":
    tab_benchmark.render()
elif menu_choice == "벤치마크 이력":
    tab_history.render()
elif menu_choice == "글로벌 리더보드":
    tab_leaderboard.render()
elif menu_choice == "모델 사전":
    tab_model_wiki.render()
elif menu_choice == "측정 방법론":
    tab_methodology.render()
elif menu_choice == "가이드 & 블로그":
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
