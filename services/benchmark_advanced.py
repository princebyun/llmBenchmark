import time
from services.benchmark import benchmark_model
from config import MULTI_TURN_SCENARIO

def benchmark_multiturn(model_info, target_ip, progress_placeholder):
    """
    3턴 연속 대화 벤치마크. 이전 턴의 응답을 다음 턴에 포함하여 문맥 유지 능력을 테스트합니다.
    """
    messages = []
    turn_results = []
    
    # 누적된 대화 텍스트 (단순 프롬프트 결합)
    accumulated_prompt = ""
    
    for turn_idx, user_msg in enumerate(MULTI_TURN_SCENARIO):
        if progress_placeholder:
            progress_placeholder.info(f"🔄 **멀티턴 벤치마크 진행 중...** [턴 {turn_idx + 1}/3] 응답 생성 중")
            
        accumulated_prompt += f"User: {user_msg}\nAssistant:"
        
        # 벤치마크 실행
        result = benchmark_model(model_info, target_ip, accumulated_prompt, progress_placeholder=None)
        
        if not result.get("success"):
            return {"success": False, "error": result.get("error", "Unknown error in multi-turn")}
            
        assistant_response = result.get("response", "")
        accumulated_prompt += f" {assistant_response}\n\n"
        
        turn_results.append({
            "턴": turn_idx + 1,
            "TTFT": round(result.get("ttft", 0), 2),
            "클라이언트 TPS": round(result.get("tps", 0), 1),
            "서버 TPS": round(result.get("server_tps", result.get("tps", 0)), 1),
            "토큰 수": result.get("server_token_count", 0),
            "응답 내용": assistant_response
        })
        
        # 턴 사이 딜레이 (자연스러운 대화 모방 및 서버 숨고르기)
        time.sleep(1)
        
    # 평균 TPS 계산
    avg_tps = sum(t["클라이언트 TPS"] for t in turn_results) / len(turn_results) if turn_results else 0
    avg_server_tps = sum(t["서버 TPS"] for t in turn_results) / len(turn_results) if turn_results else 0
    
    return {
        "success": True,
        "turns": turn_results,
        "tps": avg_tps,
        "server_tps": avg_server_tps,
        "ttft": turn_results[0]["TTFT"], # 첫 턴의 TTFT를 대표값으로
        "load_time": turn_results[0].get("load_time", 0) # 첫 턴 로딩
    }
