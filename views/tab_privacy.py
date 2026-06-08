import streamlit as st
from locales import get_text

def t(key):
    return get_text(st.session_state.lang, key)

def render():
    st.subheader(t("privacy_title"))
    
    st.markdown("---")
    
    # 데이터 처리 원칙 (가장 중요)
    st.info("💡 **Trust & Privacy First**")
    st.markdown(t("privacy_content_1"))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 수집하는 정보 (GA 트래킹 명시)
    st.markdown(t("privacy_content_2"))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 정보의 보관 및 이용
    st.markdown(t("privacy_content_3"))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.session_state.lang == "ko":
        st.markdown("""
        ### 4. 문의
        개인정보 처리와 관련된 문의사항은 언제든지 `princebyun@gmail.com`으로 연락해 주시기 바랍니다.
        """)
    else:
        st.markdown("""
        ### 4. Contact
        If you have any questions regarding privacy, please contact us at `princebyun@gmail.com`.
        """)
