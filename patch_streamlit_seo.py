import os
import streamlit as st
import re

def patch_streamlit_index():
    # Streamlit 패키지 경로 탐색
    st_dir = os.path.dirname(st.__file__)
    index_path = os.path.join(st_dir, "static", "index.html")

    if not os.path.exists(index_path):
        print(f"[-] 파일을 찾을 수 없습니다: {index_path}")
        return

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 이미 패치되었는지 확인
    if 'property="og:title"' in html:
        print("[!] 이미 SEO 메타태그가 패치되어 있습니다.")
        return

    # 삽입할 SEO 메타 태그
    seo_tags = """
    <title>LLM 하드웨어 벤치마크</title>
    <meta name="description" content="내 PC의 하드웨어 사양을 진단하고 로컬 LLM(Ollama, LM Studio 등)의 구동 성능(TPS)을 글로벌 리더보드와 비교해 보는 하드웨어 벤치마크 툴입니다." />
    
    <!-- Open Graph (KakaoTalk, Facebook 등 공유용) -->
    <meta property="og:type" content="website" />
    <meta property="og:title" content="로컬 LLM 하드웨어 벤치마크 & 진단" />
    <meta property="og:description" content="내 PC의 하드웨어 사양을 진단하고 로컬 LLM(Ollama, LM Studio 등)의 구동 성능(TPS)을 글로벌 리더보드와 비교해 보는 하드웨어 벤치마크 툴입니다." />
    <meta property="og:url" content="http://llmbenchmark.princebyun.com" />
    <meta property="og:image" content="https://streamlit.io/images/brand/streamlit-mark-color.png" />
    """

    # <title>Streamlit</title> 부분을 통째로 교체
    new_html = re.sub(r'<title>Streamlit</title>', seo_tags, html)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_html)

    print("[+] Streamlit static/index.html 패치 완료! (서버 재시작 필요)")

if __name__ == "__main__":
    patch_streamlit_index()
