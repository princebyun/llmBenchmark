import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from services.history import load_benchmark_history
import base64
from locales import get_text

def t(key):
    return get_text(st.session_state.lang, key)

def get_csv_download_link(df):
    """데이터프레임을 CSV로 변환하여 다운로드 링크를 생성합니다."""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode('utf-8-sig')).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="benchmark_history.csv" class="btn">{t("hist_download")}</a>'
    return href

def render():
    st.subheader(t("hist_title"))
    st.markdown(t("hist_desc"))
    
    history_data = load_benchmark_history()
    
    if not history_data:
        st.info(t("hist_empty"))
    else:
        df_history = pd.DataFrame(history_data)
        if "측정 일시" in df_history.columns:
            df_history = df_history.sort_values(by="측정 일시", ascending=False)
            
        # 영문 변환 맵핑
        if st.session_state.lang == "en":
            rename_map = {
                "측정 일시": t("col_timestamp"),
                "모델명": t("col_model_name"),
                "프롬프트 카테고리": t("col_prompt_cat"),
                "모델 로딩 (s)": t("col_load_time"),
                "프롬프트 TPS": t("col_prompt_tps_hist"),
                "TTFT (s)": t("col_ttft_hist"),
                "서버 TPS": t("col_server_tps_hist"),
                "클라이언트 TPS": t("col_client_tps_hist"),
                "달성률 (%)": t("col_achieve_hist"),
                "품질 점수": t("col_quality_score"),
                "평가 상세": t("col_eval_detail"),
                "TPS": "TPS"
            }
            # 데이터프레임에 존재하는 컬럼만 변경
            df_history = df_history.rename(columns={k: v for k, v in rename_map.items() if k in df_history.columns})
        
        # CSV 다운로드 버튼
        st.markdown(get_csv_download_link(df_history), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.dataframe(
            df_history,
            use_container_width=True,
            hide_index=True
        )
        
        st.markdown("---")
        st.subheader(t("hist_chart_title"))
        
        # 차트 출력 로직: 영어일 경우 바뀐 컬럼명을 사용해야 함
        col_server_tps = "Server TPS" if st.session_state.lang == "en" else "서버 TPS"
        col_client_tps = "Client TPS" if st.session_state.lang == "en" else "클라이언트 TPS"
        col_model = "Model Name" if st.session_state.lang == "en" else "모델명"
        
        target_col = col_server_tps if col_server_tps in df_history.columns else col_client_tps if col_client_tps in df_history.columns else "TPS"
        
        if target_col in df_history.columns and col_model in df_history.columns:
            if col_server_tps in df_history.columns:
                df_history[col_server_tps] = df_history[col_server_tps].fillna(df_history.get(col_client_tps, df_history.get("TPS")))

            avg_tps = df_history.groupby(col_model)[target_col].mean().reset_index()
            avg_tps = avg_tps.sort_values(by=target_col, ascending=True)
            
            fig = go.Figure(go.Bar(
                x=avg_tps[target_col],
                y=avg_tps[col_model],
                orientation='h',
                marker=dict(color='#4F46E5')
            ))
            fig.update_layout(
                title=t("hist_chart_title"),
                xaxis_title=t("hist_chart_x"),
                yaxis_title=t("hist_chart_y"),
                height=max(300, len(avg_tps) * 50)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        if st.button(t("hist_clear_btn"), type="secondary"):
            from services.history import clear_benchmark_history
            clear_benchmark_history()
            st.success(t("hist_cleared"))
            st.rerun()
