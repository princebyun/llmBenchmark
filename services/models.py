import re
import requests

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
        response = requests.get(f"http://{target_ip}:11434/api/tags", timeout=2)
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

def get_lmstudio_models(target_ip="localhost"):
    """LM Studio 서버에서 모델 목록을 가져옵니다."""
    models = []
    try:
        response = requests.get(f"http://{target_ip}:1234/v1/models", timeout=2)
        if response.status_code == 200:
            data = response.json()
            for model in data.get("data", []):
                name = model["id"]
                params = extract_params_from_name(name)
                models.append({
                    "name": name, 
                    "source": "LM Studio",
                    "params": params
                })
    except requests.exceptions.RequestException:
        pass
    return models

def get_all_models(target_ip="localhost"):
    return get_ollama_models(target_ip) + get_lmstudio_models(target_ip)
