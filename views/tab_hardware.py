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
        

