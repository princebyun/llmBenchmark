import streamlit as st
import pandas as pd
from services.leaderboard import fetch_global_leaderboard
from locales import get_text

def t(key):
    return get_text(st.session_state.lang, key)

def render():
    st.subheader(t("ld_title"))
    st.markdown(t("ld_desc"))
    
    search_query = st.text_input(t("ld_search_placeholder"), placeholder=t("ld_search_placeholder"))
    filter_col1, filter_col2 = st.columns(2)
    with filter_col1:
        category = st.selectbox(t("ld_cat_label"), [t("ld_cat_all"), t("ld_cat_small"), t("ld_cat_medium"), t("ld_cat_large")])
    with filter_col2:
        quantization = st.selectbox(t("ld_quant_label"), [t("ld_quant_4"), t("ld_quant_8"), t("ld_quant_16")])
        
    with st.spinner(t("ld_loading")):
        raw_data = fetch_global_leaderboard()
        
    if raw_data:
        filtered_data = []
        for row in raw_data:
            model_name_str = row["모델명"]
            params = row["파라미터 수 (B)"]
            
            if search_query and search_query.lower() not in model_name_str.lower():
                continue
            
            if category == t("ld_cat_small") and params >= 8: continue
            if category == t("ld_cat_medium") and (params < 8 or params > 20): continue
            if category == t("ld_cat_large") and params <= 20: continue
            
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
                t("ld_col_model"): row["모델명"],
                t("ld_col_params"): params,
                t("ld_col_score"): row["평균 점수"],
                t("ld_col_vram"): round(vram, 1),
                t("ld_col_tps"): round(tps, 1)
            })
            
        df = pd.DataFrame(filtered_data)
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                t("ld_col_params"): st.column_config.NumberColumn(format="%.1f B"),
                t("ld_col_score"): st.column_config.NumberColumn(format="%.2f"),
                t("ld_col_vram"): st.column_config.NumberColumn(format="%.1f GB"),
                t("ld_col_tps"): st.column_config.NumberColumn(format="%.1f tokens/s"),
            }
        )
    else:
        st.warning(t("ld_error"))
