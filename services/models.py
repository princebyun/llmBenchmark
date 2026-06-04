import re
import requests
from config import OLLAMA_PORT, LMSTUDIO_PORT, VLLM_PORT

def extract_params_from_name(name):
    """모델 이름에서 파라미터 수(예: 8b, 7B)를 정규식으로 추출합니다."""
    match = re.search(r'(\d+(?:\.\d+)?)[bB]', name)
    if match:
        return float(match.group(1))
    return 0.0

def get_ollama_models(target_ip="localhost"):
    """Ollama 서버에서 모델 목록과 실제 파라미터 크기를 가져옵니다."""
    models = []
    try:
        response = requests.get(f"http://{target_ip}:{OLLAMA_PORT}/api/tags", timeout=2)
        if response.status_code == 200:
            data = response.json()
            for model in data.get("models", []):
                param_size_str = model.get("details", {}).get("parameter_size", "")
                params = 0.0
                if param_size_str and "B" in param_size_str.upper():
                    try:
                        params = float(param_size_str.upper().replace("B", ""))
                    except ValueError:
                        pass
                
                if params == 0.0:
                    params = extract_params_from_name(model["name"])
                    
                models.append({
                    "name": model["name"], 
                    "source": "Ollama",
                    "params": params
                })
    except requests.exceptions.RequestException:
        pass
    return models

def get_openai_compatible_models(target_ip="localhost", port=1234, source_name="LM Studio"):
    """OpenAI 호환 API(vLLM, oMLX, LM Studio 등) 서버에서 모델 목록을 가져옵니다."""
    models = []
    try:
        response = requests.get(f"http://{target_ip}:{port}/v1/models", timeout=2)
        if response.status_code == 200:
            data = response.json()
            for model in data.get("data", []):
                name = model["id"]
                params = extract_params_from_name(name)
                models.append({
                    "name": name, 
                    "source": source_name,
                    "params": params,
                    "port": port
                })
    except requests.exceptions.RequestException:
        pass
    return models

def get_all_models(target_ip="localhost"):
    models = get_ollama_models(target_ip)
    # 각 모델 소스별로 포트 저장
    for m in models:
        m["port"] = OLLAMA_PORT
        
    models += get_openai_compatible_models(target_ip, port=LMSTUDIO_PORT, source_name="LM Studio")
    models += get_openai_compatible_models(target_ip, port=VLLM_PORT, source_name="vLLM / oMLX")
    return models
