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
        
    st.markdown("---")
    st.subheader("💡 멀티 플랫폼 최적화 가이드")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🍎 macOS (Apple Silicon)
        Apple Silicon(M1~M4)은 CPU와 GPU가 메모리를 공유하는 **Unified Memory(통일 메모리)** 아키텍처를 사용합니다. 
        즉, RAM 용량이 곧 모델 크기의 상한선이 됩니다. (Ollama 구동 시 Metal 백엔드가 자동 활성화됩니다.)
        
        **[RAM별 권장 최대 모델]**
        - **8~16GB:** 7~8B 모델 쾌적 구동 (Gemma 3, Llama 3 8B 등)
        - **18~36GB:** 14~32B 모델 쾌적 구동 (Qwen 2.5 14B 등)
        - **64GB 이상:** 70B 이상의 대형 모델 구동 가능
        """)
        
    with col2:
        st.markdown("""
        ### 🟥 AMD APU (Ryzen 내장 그래픽)
        Ryzen 5000G, 6000, 7000, 8000 시리즈 사용자라면, 아래 설정을 통해 CPU 렌더링 대신 **GPU 오프로드를 활성화**하여 비약적인 속도 향상을 얻을 수 있습니다.
        
        1. **BIOS 설정:** `UMA Frame Buffer Size`를 4GB 이상으로 변경
        2. **듀얼 채널 RAM 필수:** 싱글 채널 대비 속도가 2배 차이 납니다.
        3. **환경변수 설정 후 Ollama 실행:**
        ```cmd
        set OLLAMA_NUM_GPU=999
        set HSA_OVERRIDE_GFX_VERSION=11.0.0
        ollama serve
        ```
        *(※ GFX 버전: 5000G는 9.0.0, 6000은 10.3.0, 7000/8000은 11.0.0)*
        """)
