import plotly.graph_objects as go

def draw_gauge_chart(achieved_tps, target_tps):
    """Plotly를 사용하여 하드웨어 달성률 게이지 차트를 그립니다."""
    percentage = (achieved_tps / target_tps) * 100 if target_tps > 0 else 0
    percentage = min(percentage, 150) # 최대 150% 까지만 시각화
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = percentage,
        title = {'text': "하드웨어 성능 달성률 (%)", 'font': {'size': 20}},
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
