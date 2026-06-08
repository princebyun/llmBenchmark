import streamlit as st
from datetime import datetime

def save_benchmark_history(model_info, prompt_category, result, target_tps):
    """벤치마크 결과를 메모리(세션 상태)에 저장합니다."""
    if "benchmark_history" not in st.session_state:
        st.session_state.benchmark_history = []
        
    st.session_state.benchmark_history.append({
        "측정 일시": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "모델명": model_info["name"],
        "플랫폼": model_info["source"],
        "파라미터 (B)": model_info["params"],
        "프롬프트 유형": prompt_category,
        "TTFT (s)": round(result["ttft"], 2),
        "서버 TPS": round(result.get("server_tps", result["tps"]), 1),
        "클라이언트 TPS": round(result["tps"], 1),
        "프롬프트 TPS": round(result.get("prompt_tps", 0) or 0, 1),
        "모델 로딩 시간 (s)": round(result.get("load_time", 0) or 0, 2),
        "품질 점수": result.get("total_quality", 0),
        "평가 상세": f"정확도/문맥:{result.get('acc', 0)} 형식:{result.get('qual', 0)} 완성도:{result.get('comp', 0)}",
        "기준 TPS": round(target_tps, 1),
        "달성률 (%)": round((result["tps"] / target_tps * 100) if target_tps > 0 else 0, 1)
    })

def load_benchmark_history():
    """저장된 벤치마크 이력을 불러옵니다."""
    if "benchmark_history" not in st.session_state:
        return []
    return st.session_state.benchmark_history

def clear_benchmark_history():
    """벤치마크 이력을 초기화합니다."""
    if "benchmark_history" in st.session_state:
        st.session_state.benchmark_history = []
