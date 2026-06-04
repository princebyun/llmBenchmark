import streamlit as st
from views import tab_benchmark, tab_leaderboard, tab_history, tab_model_wiki, tab_methodology, tab_blog

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
    st.markdown("### Menu")
    menu_choice = st.radio(
        "Navigation",
        [
            "🚀 내 하드웨어 진단", 
            "📊 벤치마크 이력",
            "🏆 글로벌 리더보드", 
            "📖 모델 사전",
            "📚 측정 방법론",
            "📝 가이드 & 블로그"
        ],
        label_visibility="collapsed"
    )

if menu_choice == "🚀 내 하드웨어 진단":
    tab_benchmark.render()
elif menu_choice == "📊 벤치마크 이력":
    tab_history.render()
elif menu_choice == "🏆 글로벌 리더보드":
    tab_leaderboard.render()
elif menu_choice == "📖 모델 사전":
    tab_model_wiki.render()
elif menu_choice == "📚 측정 방법론":
    tab_methodology.render()
elif menu_choice == "📝 가이드 & 블로그":
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
