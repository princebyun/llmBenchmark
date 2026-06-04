import streamlit as st
from services.hardware_info import GPU_VRAM_MAP, recommend_models

def render():
    st.subheader("⚙️ 진단 환경 설정")
    st.markdown("벤치마크를 수행하기 전, 내 PC 사양과 대상 기기의 IP, 테스트할 모델을 설정합니다.")
    
    # 1. 하드웨어 사양 자가 입력
    st.markdown("#### 1. 내 PC 사양 입력 (선택)")
    st.markdown("사용 중인 그래픽카드(GPU)를 선택하세요")
    gpu_choice = st.selectbox("사용 중인 그래픽카드(GPU)를 선택하세요", list(GPU_VRAM_MAP.keys()), label_visibility="collapsed")
    vram_val = GPU_VRAM_MAP[gpu_choice]
    
    if vram_val > 0:
        st.info(f"선택한 GPU의 VRAM은 **{vram_val}GB** 입니다.")
        recommended = recommend_models(vram_val)
        st.success(f"**추천 최대 구동 가능 모델:** {', '.join(recommended)}")
    elif vram_val == 0:
        st.warning("GPU가 없어 CPU로 구동해야 합니다. 3B 이하 초소형 모델만 추천합니다.")
        
    with st.expander("💡 벤치마크 필수 설정 (브라우저 CORS 허용 방법)"):
        st.markdown("""
        본 벤치마크는 오라클 서버가 아닌 **사용자님의 웹 브라우저가 직접 로컬 PC와 통신**합니다.
        따라서 방화벽 포트포워딩은 필요 없지만, 브라우저 보안 정책상 **CORS(교차 출처 리소스 공유)**를 허용해야 합니다.
        
        **1. Ollama의 경우:**
        - **Windows:** 시스템 환경 변수 편집에서 `OLLAMA_ORIGINS` 변수를 만들고 값을 `*` 로 설정한 뒤 Ollama 재시작
        - **Mac/Linux:** 터미널에서 `export OLLAMA_ORIGINS="*"` 입력 후 `ollama serve` 실행
        
        **2. LM Studio의 경우:**
        - 개발자 옵션(Local Server 탭)에서 `Cross-Origin-Resource-Sharing (CORS)` 활성화
        """)
