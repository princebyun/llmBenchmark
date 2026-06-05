import plotly.graph_objects as go
from locales import get_text
import streamlit as st

def t(key):
    return get_text(st.session_state.lang, key)

def draw_gauge_chart(achieved_tps, target_tps):
    """Plotly를 사용하여 하드웨어 달성률 게이지 차트를 그립니다."""
    percentage = (achieved_tps / target_tps) * 100 if target_tps > 0 else 0
    percentage = min(percentage, 150) # 최대 150% 까지만 시각화
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = percentage,
        title = {'text': t("chart_gauge_title"), 'font': {'size': 20}},
        number = {'suffix': "%", 'valueformat': ".1f"},
        gauge = {
            'axis': {'range': [None, 150]},
            'bar': {'color': "#1f77b4"},
            'steps': [
                {'range': [0, 50], 'color': "#ffcccb"},
                {'range': [50, 90], 'color': "#ffffcc"},
                {'range': [90, 150], 'color': "#ccffcc"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 100
            }
        }
    ))
    
    fig.update_layout(height=400, margin=dict(l=20, r=20, t=50, b=20))
    return fig

def draw_radar_chart(result_dict, lang='ko'):
    """모델의 종합 성능을 시각화하는 5각형 레이더 차트를 그립니다."""
    # 결과 딕셔너리의 키는 이미 번역된 상태일 수 있으므로 동적 접근 시 주의
    # 클라이언트 TPS 등은 번역된 키로 접근해야 할 수 있습니다.
    # tab_benchmark.py에서 번역된 키로 결과를 생성하므로 여기서도 번역된 키로 접근
    tps_key = get_text(lang, "col_client_tps")
    prompt_tps_key = get_text(lang, "col_prompt_tps")
    ttft_key = get_text(lang, "col_ttft")
    load_key = get_text(lang, "col_load")
    achieve_key = get_text(lang, "col_achieve")
    model_key = get_text(lang, "col_model")

    # 정규화 로직 (0~100 스케일)
    tps_score = min(100, (result_dict.get(tps_key, 0) / 100.0) * 100) # max_tps=100.0 (기본값 하드코딩)
    prompt_tps_score = min(100, (result_dict.get(prompt_tps_key, 0) / 200.0) * 100)
    
    # TTFT와 로딩시간은 낮을수록 좋으므로 역산
    ttft_val = result_dict.get(ttft_key, 0)
    ttft_score = max(0, 100 - (ttft_val / 5.0 * 100)) if ttft_val > 0 else 0
    
    load_val = result_dict.get(load_key, 0)
    load_score = max(0, 100 - (load_val / 10.0 * 100)) if load_val > 0 else 0
    
    achievement = min(100, result_dict.get(achieve_key, 0))
    
    categories = [
        get_text(lang, "chart_radar_cat1"),
        get_text(lang, "chart_radar_cat2"),
        get_text(lang, "chart_radar_cat3"),
        get_text(lang, "chart_radar_cat4"),
        get_text(lang, "chart_radar_cat5")
    ]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[tps_score, prompt_tps_score, ttft_score, load_score, achievement, tps_score],
        theta=categories + [categories[0]], # 닫힌 다각형
        fill='toself',
        name=result_dict.get(model_key, "Model")
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
        title=get_text(lang, "chart_radar_title"),
        height=400,
        margin=dict(l=40, r=40, t=50, b=40)
    )
    return fig

def draw_multiturn_line_chart(turn_results):
    """멀티턴 벤치마크 턴별 TPS 추이 라인 차트"""
    turn_prefix = t("chart_multi_turn_prefix")
    turns = [f"{turn_prefix} {t_res['턴']}" for t_res in turn_results]
    tps_values = [t_res["클라이언트 TPS"] for t_res in turn_results]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=turns, 
        y=tps_values, 
        mode='lines+markers+text',
        name='TPS',
        text=[f"{v:.1f}" for v in tps_values],
        textposition="top center"
    ))
    
    fig.update_layout(
        title=t("chart_multi_title"),
        xaxis_title=t("chart_multi_x"),
        yaxis_title=t("chart_multi_y"),
        yaxis=dict(rangemode="tozero"),
        height=350,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig
