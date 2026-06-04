import json
import os
from datetime import datetime
from config import HISTORY_FILE

def save_benchmark_history(model_info, prompt_category, result, target_tps):
    """벤치마크 결과를 로컬 JSON 파일에 저장합니다."""
    history = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
        except:
            pass
            
    history.append({
        "측정 일시": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "모델명": model_info["name"],
        "플랫폼": model_info["source"],
        "파라미터 (B)": model_info["params"],
        "프롬프트 유형": prompt_category,
        "TTFT (s)": round(result["ttft"], 2),
        "TPS": round(result["tps"], 1),
        "기준 TPS": round(target_tps, 1),
        "달성률 (%)": round((result["tps"] / target_tps * 100) if target_tps > 0 else 0, 1)
    })
    
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def load_benchmark_history():
    """저장된 벤치마크 이력을 불러옵니다."""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return []
