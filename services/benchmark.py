import time
import json
import requests

MAX_TOKENS = 1000  # 비정상적으로 긴 출력을 방지하기 위한 최대 토큰 수 제한
MAX_TIME_SECONDS = 120  # 최대 테스트 시간 (초) - 무한 대기 방지

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
    
    # 상세 지표용 변수
    server_tps = None
    prompt_tps = None
    load_time = None
    server_token_count = None
    
    try:
        if source == "Ollama":
            url = f"http://{target_ip}:11434/api/chat"
            payload = {
                "model": model_name,
                "messages": [{"role": "user", "content": prompt_text}],
                "stream": True
            }
            # 초기 로딩(콜드스타트)이 오래 걸리는 모델을 위해 timeout을 120초로 넉넉히 부여
            response = requests.post(url, json=payload, stream=True, timeout=120)
            response.raise_for_status()
            
            for line in response.iter_lines():
                if time.perf_counter() - start_time > MAX_TIME_SECONDS:
                    if progress_placeholder:
                        progress_placeholder.warning("⚠️ 최대 테스트 시간 초과로 측정을 강제 종료했습니다.")
                    break
                    
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
                    
                    if data.get("done", False):
                        load_time = data.get("load_duration", 0) / 1e9
                        prompt_eval_count = data.get("prompt_eval_count", 0)
                        prompt_eval_duration = data.get("prompt_eval_duration", 0) / 1e9
                        eval_count = data.get("eval_count", 0)
                        eval_duration = data.get("eval_duration", 0) / 1e9
                        
                        if prompt_eval_duration > 0:
                            prompt_tps = prompt_eval_count / prompt_eval_duration
                        if eval_duration > 0:
                            server_tps = eval_count / eval_duration
                        server_token_count = eval_count
                        break
                        
                    if token_count >= MAX_TOKENS:
                        if progress_placeholder:
                            progress_placeholder.warning("⚠️ 최대 토큰 수 초과로 측정을 강제 종료했습니다.")
                        break
                        
        elif source in ["LM Studio", "vLLM / oMLX"]:
            port = model_info.get("port", 1234)
            url = f"http://{target_ip}:{port}/v1/chat/completions"
            payload = {
                "model": model_name,
                "messages": [{"role": "user", "content": prompt_text}],
                "stream": True,
                "stream_options": {"include_usage": True}
            }
            # 초기 로딩(콜드스타트)이 오래 걸리는 모델을 위해 timeout을 120초로 넉넉히 부여
            response = requests.post(url, json=payload, stream=True, timeout=120)
            response.raise_for_status()
            
            for line in response.iter_lines():
                if time.perf_counter() - start_time > MAX_TIME_SECONDS:
                    if progress_placeholder:
                        progress_placeholder.warning("⚠️ 최대 테스트 시간 초과로 측정을 강제 종료했습니다.")
                    break
                    
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
                        if "content" in delta and delta["content"] is not None:
                            full_response += delta["content"]
                            token_count += 1
                            if progress_placeholder:
                                progress_placeholder.info(f"⏳ **벤치마크 진행 중...** 현재 {token_count}개의 토큰을 처리했습니다.")
                                
                    if "usage" in data and data["usage"] is not None:
                        usage = data["usage"]
                        server_token_count = usage.get("completion_tokens")
                        # OpenAI API는 duration을 제공하지 않으므로 client time 활용하여 근사치 계산
                        if server_token_count and first_token_time:
                            server_tps = server_token_count / (time.perf_counter() - first_token_time)
                                
                    if token_count >= MAX_TOKENS:
                        if progress_placeholder:
                            progress_placeholder.warning("⚠️ 최대 토큰 수 초과로 측정을 강제 종료했습니다.")
                        break

        end_time = time.perf_counter()
        
        ttft = first_token_time - start_time if first_token_time else 0
        total_time = end_time - first_token_time if first_token_time else 0
        client_tps = token_count / total_time if total_time > 0 else 0
        
        return {
            "success": True,
            "response": full_response,
            "ttft": ttft,
            "tps": client_tps,
            "server_tps": server_tps if server_tps else client_tps,
            "prompt_tps": prompt_tps,
            "load_time": load_time,
            "server_token_count": server_token_count if server_token_count else token_count
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
