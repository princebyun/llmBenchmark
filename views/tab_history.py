import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from services.history import load_benchmark_history
import base64

def get_csv_download_link(df):
    """데이터프레임을 CSV로 변환하여 다운로드 링크를 생성합니다."""
    csv = df.to_csv(index=False, encoding='utf-8-sig')
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="benchmark_history.csv" class="btn">📥 CSV 파일로 내보내기</a>'
    return href

def render():
    st.subheader("📊 벤치마크 이력 및 비교")
    st.markdown("과거에 진행했던 벤치마크 결과들이 자동으로 저장되어 표시됩니다. (현재 세션 기반 유지)")
    
    history_data = load_benchmark_history()
    
    if not history_data:
        st.info("아직 저장된 벤치마크 이력이 없습니다. '내 하드웨어 진단' 탭에서 벤치마크를 한 번 실행해 보세요!")
    else:
        df_history = pd.DataFrame(history_data)
        df_history = df_history.sort_values(by="측정 일시", ascending=False)
        
        # CSV 다운로드 버튼
        st.markdown(get_csv_download_link(df_history), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.dataframe(
            df_history,
            use_container_width=True,
            hide_index=True
        )
        
        st.markdown("---")
        st.subheader("📈 모델별 평균 성능(TPS) 비교")
        
        if "서버 TPS" in df_history.columns:
            target_col = "서버 TPS"
            df_history["서버 TPS"] = df_history["서버 TPS"].fillna(df_history.get("클라이언트 TPS", df_history.get("TPS")))
        else:
            target_col = "클라이언트 TPS" if "클라이언트 TPS" in df_history.columns else "TPS"
            
        avg_tps = df_history.groupby("모델명")[target_col].mean().reset_index()
        avg_tps = avg_tps.sort_values(by=target_col, ascending=True)
        
        fig = go.Figure(go.Bar(
            x=avg_tps[target_col],
            y=avg_tps["모델명"],
            orientation='h',
            marker=dict(color='#4F46E5')
        ))
        fig.update_layout(
            title="모델별 평균 TPS (초당 토큰 처리량)",
            xaxis_title="TPS",
            yaxis_title="모델",
            height=max(300, len(avg_tps) * 50)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        if st.button("🗑️ 모든 이력 지우기", type="secondary"):
            from services.history import clear_benchmark_history
            clear_benchmark_history()
            st.success("모든 벤치마크 이력이 삭제되었습니다.")
            st.rerun()
