import streamlit as st
from views import tab_benchmark, tab_leaderboard, tab_history, tab_model_wiki, tab_methodology, tab_blog

# ==========================================
# 1. 페이지 설정 및 초기화
# ==========================================
st.set_page_config(
    page_title="로컬 LLM 하드웨어 벤치마크",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
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

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🚀 내 하드웨어 진단", 
    "📊 벤치마크 이력",
    "🏆 글로벌 리더보드", 
    "📖 모델 사전",
    "📚 측정 방법론",
    "📝 가이드 & 블로그"
])

with tab1:
    tab_benchmark.render()
    
with tab2:
    tab_history.render()
    
with tab3:
    tab_leaderboard.render()

    
with tab4:
    tab_model_wiki.render()
    
with tab5:
    tab_methodology.render()
    
with tab6:
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
