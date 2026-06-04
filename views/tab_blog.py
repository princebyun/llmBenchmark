import streamlit as st
from data.blog_data import BLOG_POSTS
def render():
    st.title("📝 로컬 LLM 테크 가이드 및 블로그")
    st.markdown("""
    로컬 LLM 환경 구축에 입문하시는 분들을 위해 준비한 **전문가 가이드 및 튜토리얼 아티클**입니다. 
    아래의 각 포스트 제목을 클릭하여 숨겨진 본문 내용을 확장해 보세요. 로컬 AI 시대의 생존 지식을 넓힐 수 있습니다.
    """)
    st.divider()

    st.info("💡 **Tip:** 모든 글은 초보자부터 전문가까지 읽기 쉽도록 팁과 예시를 포함하고 있습니다.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    for i, post in enumerate(BLOG_POSTS):
        with st.expander(f"📖 **Article {i+1}.** {post['title']}"):
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(post['content'])
            st.markdown("<br>", unsafe_allow_html=True)
            st.caption("작성자: Princebyun | 저작권 ⓒ 2026. All rights reserved.")
            
    st.divider()
    st.markdown("더 많은 기술 포스트가 주기적으로 업데이트 될 예정입니다. 계속 방문해 주세요!")
