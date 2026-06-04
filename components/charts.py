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

def draw_radar_chart(result_dict, max_tps=100.0, max_ttft=5.0):
    """모델의 종합 성능을 시각화하는 5각형 레이더 차트를 그립니다."""
    # 정규화 로직 (0~100 스케일)
    tps_score = min(100, (result_dict.get("클라이언트 TPS", 0) / max_tps) * 100)
    prompt_tps_score = min(100, (result_dict.get("프롬프트 TPS", 0) / (max_tps * 2)) * 100)
    
    # TTFT와 로딩시간은 낮을수록 좋으므로 역산
    ttft_val = result_dict.get("TTFT (s)", 0)
    ttft_score = max(0, 100 - (ttft_val / max_ttft * 100)) if ttft_val > 0 else 0
    
    load_val = result_dict.get("모델 로딩 (s)", 0)
    load_score = max(0, 100 - (load_val / 10.0 * 100)) if load_val > 0 else 0
    
    achievement = min(100, result_dict.get("달성률 (%)", 0))
    
    categories = ['토큰 생성 속도(TPS)', '질문 이해 속도(Prompt TPS)', '초기 응답 지연(TTFT 역수)', '초기 로딩 속도(역수)', '하드웨어 달성률']
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[tps_score, prompt_tps_score, ttft_score, load_score, achievement, tps_score],
        theta=categories + [categories[0]], # 닫힌 다각형
        fill='toself',
        name=result_dict.get("모델명", "모델")
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
        title="종합 성능 진단 레이더",
        height=400,
        margin=dict(l=40, r=40, t=50, b=40)
    )
    return fig

def draw_multiturn_line_chart(turn_results):
    """멀티턴 벤치마크 턴별 TPS 추이 라인 차트"""
    turns = [f"턴 {t['턴']}" for t in turn_results]
    tps_values = [t["클라이언트 TPS"] for t in turn_results]
    
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
        title="멀티턴 문맥 증가에 따른 속도(TPS) 유지력",
        xaxis_title="대화 턴",
        yaxis_title="초당 토큰 처리량 (TPS)",
        yaxis=dict(rangemode="tozero"),
        height=350,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig
