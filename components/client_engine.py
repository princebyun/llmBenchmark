import os
import streamlit.components.v1 as components

# frontend 폴더의 절대 경로 지정
_COMPONENT_DIR = os.path.join(os.path.dirname(__file__), "frontend")
_component_func = components.declare_component("llm_benchmark_engine", path=_COMPONENT_DIR)

def benchmark_engine(prompts, config, key=None):
    """
    JS 엔진을 Streamlit에 임베드하고, 벤치마크 완료 시 결과를 수신합니다.
    
    Args:
        prompts (dict): 프롬프트 템플릿 딕셔너리
        config (dict): 통신 포트 등 설정 정보 (예: OLLAMA_PORT 등)
        key (str): 컴포넌트 고유 키
        
    Returns:
        dict or None: 모든 벤치마크가 완료된 후 JS에서 전송한 최종 결과 JSON
    """
    component_value = _component_func(
        prompts=prompts,
        config=config,
        key=key,
        default=None
    )
    
    return component_value
