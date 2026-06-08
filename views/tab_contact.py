import streamlit as st
from locales import get_text

def t(key):
    return get_text(st.session_state.lang, key)

def render():
    st.subheader(t("contact_title"))
    
    st.markdown("---")
    
    st.markdown(t("contact_content"))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; padding: 40px; background-color: #F8F9FA; border-radius: 12px; border: 1px solid #E5E7EB; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);'>
        <h2 style='color: #4F46E5; margin-bottom: 20px;'>✉️ Email</h2>
        <a href='mailto:princebyun@gmail.com' style='font-size: 24px; font-weight: bold; color: #1F2937; text-decoration: none;'>princebyun@gmail.com</a>
        <p style='color: #6B7280; margin-top: 15px;'>
            """ + ("언제든지 편하게 연락 주세요!" if st.session_state.lang == "ko" else "Feel free to reach out anytime!") + """
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.session_state.lang == "ko":
        st.info("💡 **빠른 확인이 필요한 버그 리포트의 경우**\n\n발생한 에러 메시지 캡처 화면과 사용 중이신 브라우저 종류, 로컬 LLM 이름(Ollama/LM Studio 등)을 함께 보내주시면 더 빠른 대응이 가능합니다.")
    else:
        st.info("💡 **For urgent bug reports**\n\nPlease include a screenshot of the error message, your browser type, and the local LLM name (Ollama/LM Studio, etc.) for a faster response.")
