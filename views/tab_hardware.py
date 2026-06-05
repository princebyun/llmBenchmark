import streamlit as st
from services.hardware_info import GPU_VRAM_MAP, recommend_models
from locales import get_text

def t(key):
    return get_text(st.session_state.lang, key)

def render():
    st.subheader(t("hw_title"))
    st.markdown(t("hw_desc"))
    
    # 1. 하드웨어 사양 자가 입력
    st.markdown(t("hw_input_title"))
    st.markdown(t("hw_input_desc"))
    gpu_choice = st.selectbox(t("hw_input_desc"), list(GPU_VRAM_MAP.keys()), label_visibility="collapsed")
    vram_val = GPU_VRAM_MAP[gpu_choice]
    
    if vram_val > 0:
        st.info(t("hw_vram_info").format(vram=vram_val))
        recommended = recommend_models(vram_val)
        st.success(t("hw_recommended").format(models=', '.join(recommended)))
    elif vram_val == 0:
        st.warning(t("hw_cpu_warning"))
        
    with st.expander("💡 벤치마크 필수 설정 (브라우저 CORS 허용 방법)" if st.session_state.lang == "ko" else "💡 Benchmark Prerequisite (Browser CORS Policy)"):
        st.markdown("""
        본 벤치마크는 오라클 서버가 아닌 **사용자님의 웹 브라우저가 직접 로컬 PC와 통신**합니다.
        따라서 방화벽 포트포워딩은 필요 없지만, 브라우저 보안 정책상 **CORS(교차 출처 리소스 공유)**를 허용해야 합니다.
        
        **1. Ollama의 경우:**
        - **Windows:** 시스템 환경 변수 편집에서 `OLLAMA_ORIGINS` 변수를 만들고 값을 `*` 로 설정한 뒤 Ollama 재시작
        - **Mac/Linux:** 터미널에서 `export OLLAMA_ORIGINS="*"` 입력 후 `ollama serve` 실행
        
        **2. LM Studio의 경우:**
        - 개발자 옵션(Local Server 탭)에서 `Cross-Origin-Resource-Sharing (CORS)` 활성화
        """ if st.session_state.lang == "ko" else """
        This benchmark relies on **your web browser communicating directly with your local PC**, not the Oracle server.
        Therefore, firewall port forwarding is not required, but you must allow **CORS (Cross-Origin Resource Sharing)** due to browser security policies.
        
        **1. For Ollama:**
        - **Windows:** Edit System Environment Variables, add `OLLAMA_ORIGINS` with value `*`, then restart Ollama.
        - **Mac/Linux:** In terminal, run `export OLLAMA_ORIGINS="*"` and then `ollama serve`.
        
        **2. For LM Studio:**
        - Enable `Cross-Origin-Resource-Sharing (CORS)` toggle in Developer Options (Local Server tab).
        """)
        
        
