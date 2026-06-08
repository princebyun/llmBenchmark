import streamlit as st
from locales import get_text

def t(key):
    return get_text(st.session_state.lang, key)

def render():
    st.subheader(t("about_title"))
    
    st.markdown(t("about_content"))
    
    if st.session_state.lang == "ko":
        st.markdown("""
        ### 주요 기능
        1. **Client-Side 벤치마크**: 사용자 브라우저와 127.0.0.1 간의 직접 통신을 통해 순수 로컬 기기의 성능만 정확히 측정합니다.
        2. **멀티턴 스트레스 테스트**: 단순 1회성 질문을 넘어, 대화 문맥(Context)이 쌓였을 때 성능 저하가 일어나는지 검증합니다.
        3. **하드웨어 커스텀 가이드**: 사용자의 GPU 사양을 기반으로 최적화된 로컬 모델을 실시간 추천합니다.
        """)
    else:
        st.markdown("""
        ### Key Features
        1. **Client-Side Benchmark**: Measures pure local device performance through direct communication between your browser and 127.0.0.1.
        2. **Multi-turn Stress Test**: Beyond single questions, it tests whether performance drops as conversation context builds up.
        3. **Hardware Custom Guide**: Recommends optimized local models in real-time based on your GPU specs.
        """)
