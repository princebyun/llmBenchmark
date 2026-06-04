import time
import json
import requests

def get_baseline_tps(model_info):
    """모델의 실제 파라미터 수를 기반으로 동적 기준 TPS를 계산합니다."""
    params = model_info.get("params", 0)
    if params and params > 0:
        return 200.0 / params
    return 30.0 # 파라미터 수를 모를 경우 30 TPS를 기본값으로 사용

def benchmark_model(model_info, target_ip="localhost", prompt_text="", progress_placeholder=None):
    """선택된 모델에 벤치마크 프롬프트를 전송하고 성능을 측정합니다."""
    model_name = model_info["name"]
    source = model_info["source"]
    
    start_time = time.perf_counter()
    first_token_time = None
    token_count = 0
    full_response = ""
    
    try:
        if source == "Ollama":
            url = f"http://{target_ip}:11434/api/chat"
            payload = {
                "model": model_name,
                "messages": [{"role": "user", "content": prompt_text}],
                "stream": True
            }
            response = requests.post(url, json=payload, stream=True)
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    if first_token_time is None:
                        first_token_time = time.perf_counter()
                    data = json.loads(line)
                    if "message" in data and "content" in data["message"]:
                        chunk = data["message"]["content"]
                        full_response += chunk
                        token_count += 1 
                        if progress_placeholder:
                            progress_placeholder.info(f"⏳ **벤치마크 진행 중...** 현재 {token_count}개의 토큰을 처리했습니다.")
                        
        elif source == "LM Studio":
            url = f"http://{target_ip}:1234/v1/chat/completions"
            payload = {
                "model": model_name,
                "messages": [{"role": "user", "content": prompt_text}],
                "stream": True
            }
            response = requests.post(url, json=payload, stream=True)
            response.raise_for_status()
            
            for line in response.iter_lines():
                line = line.decode('utf-8')
                if line.startswith("data: "):
                    data_str = line[6:]
                    if data_str == "[DONE]":
                        break
                    if first_token_time is None:
                        first_token_time = time.perf_counter()
                    data = json.loads(data_str)
                    if "choices" in data and len(data["choices"]) > 0:
                        delta = data["choices"][0].get("delta", {})
                        if "content" in delta:
                            full_response += delta["content"]
                            token_count += 1
                            if progress_placeholder:
                                progress_placeholder.info(f"⏳ **벤치마크 진행 중...** 현재 {token_count}개의 토큰을 처리했습니다.")

        end_time = time.perf_counter()
        
        ttft = first_token_time - start_time if first_token_time else 0
        total_time = end_time - first_token_time if first_token_time else 0
        tps = token_count / total_time if total_time > 0 else 0
        
        return {
            "success": True,
            "response": full_response,
            "ttft": ttft,
            "tps": tps
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
