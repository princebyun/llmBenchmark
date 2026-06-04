def get_baseline_tps(model_info):
    """모델의 실제 파라미터 수를 기반으로 동적 기준 TPS를 계산합니다."""
    params = model_info.get("params", 0)
    if params and params > 0:
        return 200.0 / params
    return 30.0 # 파라미터 수를 모를 경우 30 TPS를 기본값으로 사용
