# GPU 사양에 따른 추정 VRAM(GB)
GPU_VRAM_MAP = {
    # 🟢 NVIDIA RTX 50 시리즈 (최신)
    "NVIDIA RTX 5090 (32GB)": 32,
    "NVIDIA RTX 5080 (16GB)": 16,
    "NVIDIA RTX 5070 Ti (16GB)": 16,
    "NVIDIA RTX 5070 (12GB)": 12,
    "NVIDIA RTX 5060 Ti (12GB)": 12,
    "NVIDIA RTX 5060 (8GB)": 8,
    
    # 🟢 NVIDIA RTX 40 시리즈
    "NVIDIA RTX 4090 (24GB)": 24,
    "NVIDIA RTX 4080 Super (16GB)": 16,
    "NVIDIA RTX 4080 (16GB)": 16,
    "NVIDIA RTX 4070 Ti Super (16GB)": 16,
    "NVIDIA RTX 4070 Ti (12GB)": 12,
    "NVIDIA RTX 4070 Super (12GB)": 12,
    "NVIDIA RTX 4070 (12GB)": 12,
    "NVIDIA RTX 4060 Ti (16GB)": 16,
    "NVIDIA RTX 4060 Ti (8GB)": 8,
    "NVIDIA RTX 4060 (8GB)": 8,
    
    # 🟢 NVIDIA RTX 30 시리즈
    "NVIDIA RTX 3090 Ti (24GB)": 24,
    "NVIDIA RTX 3090 (24GB)": 24,
    "NVIDIA RTX 3080 Ti (12GB)": 12,
    "NVIDIA RTX 3080 (10GB)": 10,
    "NVIDIA RTX 3070 Ti (8GB)": 8,
    "NVIDIA RTX 3070 (8GB)": 8,
    "NVIDIA RTX 3060 (12GB)": 12,
    "NVIDIA RTX 3060 (8GB)": 8,
    "NVIDIA RTX 3050 (8GB)": 8,

    # 🔴 AMD Radeon 8000 시리즈 (최신)
    "AMD Radeon RX 8900 XTX (24GB)": 24,
    "AMD Radeon RX 8800 XT (16GB)": 16,
    "AMD Radeon RX 8700 XT (12GB)": 12,
    "AMD Radeon RX 8600 XT (8GB)": 8,

    # 🔴 AMD Radeon 7000 시리즈
    "AMD Radeon RX 7900 XTX (24GB)": 24,
    "AMD Radeon RX 7900 XT (20GB)": 20,
    "AMD Radeon RX 7900 GRE (16GB)": 16,
    "AMD Radeon RX 7800 XT (16GB)": 16,
    "AMD Radeon RX 7700 XT (12GB)": 12,
    "AMD Radeon RX 7600 XT (16GB)": 16,
    "AMD Radeon RX 7600 (8GB)": 8,
    
    # 🔴 AMD Radeon 6000 시리즈
    "AMD Radeon RX 6950 XT (16GB)": 16,
    "AMD Radeon RX 6900 XT (16GB)": 16,
    "AMD Radeon RX 6800 XT (16GB)": 16,
    "AMD Radeon RX 6800 (16GB)": 16,
    "AMD Radeon RX 6750 XT (12GB)": 12,
    "AMD Radeon RX 6700 XT (12GB)": 12,
    "AMD Radeon RX 6600 XT (8GB)": 8,
    "AMD Radeon RX 6600 (8GB)": 8,

    # 🍎 Apple Silicon (M4 / M3 / M2 / M1) - UMA 메모리 할당 가정
    "Apple M4 Ultra (256GB/192GB)": 192,
    "Apple M4 Max (128GB)": 128,
    "Apple M4 Pro (64GB)": 64,
    "Apple M4 (32GB)": 32,
    "Apple M3 Max (128GB)": 128,
    "Apple M3 Pro (36GB)": 36,
    "Apple M3 (24GB)": 24,
    "Apple M2 Ultra (192GB)": 192,
    "Apple M2 Max (96GB)": 96,
    "Apple M2 Pro (32GB)": 32,
    "Apple M2 (24GB)": 24,
    "Apple M1 Ultra (128GB)": 128,
    "Apple M1 Max (64GB)": 64,
    "Apple M1 Pro (32GB)": 32,
    "Apple M1 (16GB)": 16,
    "Apple M1 (8GB)": 8,

    # ⚪ 기타
    "CPU 전용 (GPU 없음)": 0,
    "기타 (직접 입력)": -1
}

def recommend_models(vram_gb: float) -> list:
    """VRAM 용량에 따라 구동 가능한 최대 모델 체급을 추천합니다. (4-bit 양자화 기준: 파라미터 * 0.7 + 1GB)"""
    if vram_gb < 4:
        return ["TinyLlama 1.1B", "Gemma 2B"]
    elif vram_gb < 8:
        return ["Phi-3 Mini (3.8B)", "Qwen 2 7B", "Llama 3 8B"]
    elif vram_gb < 16:
        return ["Llama 3 8B", "Gemma 2 9B", "Mistral NeMo 12B", "Qwen 3.7 (14B)"]
    elif vram_gb < 24:
        return ["Qwen 3.7 (14B)", "Gemma 2 27B", "Yi 34B"]
    elif vram_gb < 48:
        return ["Gemma 2 27B", "Llama 3 70B", "Qwen 2 72B"]
    else:
        return ["Llama 3 70B", "Command R+", "Llama 4 Scout (109B)"]
