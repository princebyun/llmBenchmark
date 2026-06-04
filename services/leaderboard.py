import streamlit as st
import requests

@st.cache_data(ttl=3600)
def fetch_global_leaderboard():
    """Hugging Face Open LLM Leaderboard 데이터셋에서 실제 리더보드 데이터를 가져옵니다."""
    url = "https://datasets-server.huggingface.co/rows?dataset=open-llm-leaderboard/contents&config=default&split=train&offset=0&length=100"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        rows = data.get("rows", [])
        
        leaderboard = []
        for r in rows:
            row_data = r.get("row", {})
            model_name = row_data.get("fullname", "Unknown")
            params = row_data.get("#Params (B)", 0)
            score = row_data.get("Average ⬆️", 0)
            
            if not isinstance(params, (int, float)) or params <= 0:
                continue
            
            leaderboard.append({
                "모델명": model_name,
                "파라미터 수 (B)": round(params, 1),
                "평균 점수": round(score, 2),
            })
            
        leaderboard = sorted(leaderboard, key=lambda x: x["평균 점수"], reverse=True)
        return leaderboard
    except Exception as e:
        st.warning("⚠️ **Hugging Face 서버가 일시적으로 불안정하여 실시간 리더보드를 불러오지 못했습니다.**\n\n대신 로컬에 저장된 기본 데이터를 표시합니다.")
        
        fallback_data = [
            {"모델명": "Llama 3 8B Instruct", "파라미터 수 (B)": 8.0, "평균 점수": 68.4},
            {"모델명": "Gemma 2 9B", "파라미터 수 (B)": 9.0, "평균 점수": 71.3},
            {"모델명": "Qwen 2 7B", "파라미터 수 (B)": 7.0, "평균 점수": 70.5},
            {"모델명": "Phi-3 Mini", "파라미터 수 (B)": 3.8, "평균 점수": 69.0},
            {"모델명": "Mistral 7B Instruct", "파라미터 수 (B)": 7.3, "평균 점수": 62.5},
            {"모델명": "Gemma 2B", "파라미터 수 (B)": 2.5, "평균 점수": 46.1},
        ]
        return sorted(fallback_data, key=lambda x: x["평균 점수"], reverse=True)
