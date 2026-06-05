import streamlit as st
from data.blog_data import BLOG_POSTS, BLOG_POSTS_EN
from locales import get_text

def t(key):
    return get_text(st.session_state.lang, key)

def render():
    st.title(t("blog_title"))
    st.markdown(t("blog_desc"))
    st.divider()

    tip_text = "💡 **Tip:** 모든 글은 초보자부터 전문가까지 읽기 쉽도록 팁과 예시를 포함하고 있습니다." if st.session_state.lang == "ko" else "💡 **Tip:** All articles include tips and examples for both beginners and experts."
    st.info(tip_text)
    st.markdown("<br>", unsafe_allow_html=True)
    
    posts = BLOG_POSTS_EN if st.session_state.lang == "en" else BLOG_POSTS
    
    for i, post in enumerate(posts):
        with st.expander(f"📖 **Article {i+1}.** {post['title']}"):
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(post['content'])
            st.markdown("<br>", unsafe_allow_html=True)
            caption_text = "작성자: princebyun.com | 저작권 ⓒ 2026. All rights reserved." if st.session_state.lang == "ko" else "Author: princebyun.com | Copyright ⓒ 2026. All rights reserved."
            st.caption(caption_text)
            
    st.divider()
    footer_text = "더 많은 기술 포스트가 주기적으로 업데이트 될 예정입니다. 계속 방문해 주세요!" if st.session_state.lang == "ko" else "More technical posts will be updated periodically. Keep visiting!"
    st.markdown(footer_text)
