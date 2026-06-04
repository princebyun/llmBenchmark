import streamlit as st
from pages import tab_benchmark, tab_leaderboard, tab_history

# ==========================================
# 1. 페이지 설정 및 초기화
# ==========================================
st.set_page_config(
    page_title="로컬 LLM 하드웨어 벤치마크",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 불필요한 기본 UI 요소(Deploy 버튼 등) 숨기기
st.markdown("""
    <style>
        .stDeployButton {display:none;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 메인 UI 및 탭 라우팅
# ==========================================
st.title("🚀 로컬 LLM 하드웨어 벤치마크 및 진단")
st.markdown("Ollama 및 LM Studio에 설치된 모델을 감지하고 내 PC의 성능(TPS)을 글로벌 기준과 비교합니다.")

tab1, tab2, tab3 = st.tabs(["🚀 내 하드웨어 진단", "🏆 글로벌 리더보드", "📊 벤치마크 이력"])

with tab1:
    tab_benchmark.render()
    
with tab2:
    tab_leaderboard.render()
    
with tab3:
    tab_history.render()
