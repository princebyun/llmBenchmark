import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
from config import HISTORY_FILE
from services.history import load_benchmark_history

def render():
    st.subheader("📊 벤치마크 이력 및 비교")
    st.markdown("과거에 진행했던 벤치마크 결과들이 자동으로 저장되어 표시됩니다. 모델 간 성능을 비교하거나 하드웨어 변경에 따른 성능 변화를 추적하세요.")
    
    history_data = load_benchmark_history()
    
    if not history_data:
        st.info("아직 저장된 벤치마크 이력이 없습니다. '내 하드웨어 진단' 탭에서 벤치마크를 한 번 실행해 보세요!")
    else:
        df_history = pd.DataFrame(history_data)
        
        df_history = df_history.sort_values(by="측정 일시", ascending=False)
        
        st.dataframe(
            df_history,
            width='stretch',
            hide_index=True
        )
        
        st.markdown("---")
        st.subheader("📈 모델별 평균 성능(TPS) 비교")
        
        avg_tps = df_history.groupby("모델명")["TPS"].mean().reset_index()
        avg_tps = avg_tps.sort_values(by="TPS", ascending=True)
        
        fig = go.Figure(go.Bar(
            x=avg_tps["TPS"],
            y=avg_tps["모델명"],
            orientation='h',
            marker=dict(color='#1f77b4')
        ))
        fig.update_layout(
            title="모델별 평균 TPS (초당 토큰 처리량)",
            xaxis_title="TPS",
            yaxis_title="모델",
            height=max(300, len(avg_tps) * 50)
        )
        st.plotly_chart(fig, width='stretch')
        
        if st.button("🗑️ 모든 이력 지우기", type="secondary"):
            if os.path.exists(HISTORY_FILE):
                os.remove(HISTORY_FILE)
            st.success("모든 벤치마크 이력이 삭제되었습니다. (새로고침 시 반영됩니다)")
