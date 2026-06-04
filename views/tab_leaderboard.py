import streamlit as st
import pandas as pd
from services.leaderboard import fetch_global_leaderboard

def render():
    st.subheader("🏆 글로벌 리더보드 (Hugging Face Open LLM Leaderboard 실시간 데이터)")
    st.markdown("현재 Hugging Face 데이터셋 서버에서 가져온 상위 100개 모델의 원본 데이터입니다. 필터를 이용해 원하는 카테고리와 양자화 수준별 추정 VRAM/TPS를 확인하세요.")
    
    search_query = st.text_input("🔍 모델명 검색 (예: llama, qwen, phi)", placeholder="검색어를 입력하세요...")
    filter_col1, filter_col2 = st.columns(2)
    with filter_col1:
        category = st.selectbox("모델 크기 카테고리", ["전체 보기", "소형 모델 (< 8B)", "중형 모델 (8B ~ 20B)", "대형 모델 (> 20B)"])
    with filter_col2:
        quantization = st.selectbox("양자화 수준 선택", ["4-bit (INT4 / Q4)", "8-bit (INT8 / Q8)", "16-bit (FP16 / BF16)"])
        
    with st.spinner("리더보드 데이터를 가져오는 중입니다..."):
        raw_data = fetch_global_leaderboard()
        
    if raw_data:
        filtered_data = []
        for row in raw_data:
            model_name_str = row["모델명"]
            params = row["파라미터 수 (B)"]
            
            if search_query and search_query.lower() not in model_name_str.lower():
                continue
            
            if category == "소형 모델 (< 8B)" and params >= 8: continue
            if category == "중형 모델 (8B ~ 20B)" and (params < 8 or params > 20): continue
            if category == "대형 모델 (> 20B)" and params <= 20: continue
            
            if "16-bit" in quantization:
                vram = params * 2.0 + 1.0
                tps = 100.0 / params if params > 0 else 0
            elif "8-bit" in quantization:
                vram = params * 1.0 + 1.0
                tps = 150.0 / params if params > 0 else 0
            else:
                vram = params * 0.7 + 1.0
                tps = 200.0 / params if params > 0 else 0
                
            filtered_data.append({
                "모델명": row["모델명"],
                "파라미터 수 (B)": params,
                "평균 점수": row["평균 점수"],
                "요구 VRAM (GB)": round(vram, 1),
                "예상 최고 TPS": round(tps, 1)
            })
            
        df = pd.DataFrame(filtered_data)
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "파라미터 수 (B)": st.column_config.NumberColumn(format="%.1f B"),
                "평균 점수": st.column_config.NumberColumn(format="%.2f"),
                "요구 VRAM (GB)": st.column_config.NumberColumn(format="%.1f GB"),
                "예상 최고 TPS": st.column_config.NumberColumn(format="%.1f tokens/s"),
            }
        )
    else:
        st.warning("리더보드 데이터를 가져오지 못했습니다.")
