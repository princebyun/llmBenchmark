import streamlit as st
import pandas as pd
from config import PROMPT_TEMPLATES
from services.models import get_all_models
from services.benchmark import benchmark_model, get_baseline_tps
from services.history import save_benchmark_history
from charts import draw_gauge_chart

def render():
    st.subheader("진단 환경 설정")
    
    target_ip = st.text_input("🎯 벤치마크할 기기의 IP 주소", value="localhost")
    st.caption("외부 기기를 벤치마크하려면 해당 기기의 IP(예: 192.168.0.x)를 입력하세요. (단, 해당 기기의 Ollama/LM Studio 외부 접속이 허용되어 있어야 합니다.)")
    
    with st.expander("💡 외부 기기 접속 허용 설정 방법 보기"):
        st.markdown("""
        **Ollama의 경우 (서버 PC에서 설정 후 재시작):**
        - **Windows:** 명령 프롬프트에서 `set OLLAMA_HOST=0.0.0.0` 및 `set OLLAMA_ORIGINS="*"` 입력 후 `ollama serve` 실행
        - **Mac/Linux:** 터미널에서 `export OLLAMA_HOST=0.0.0.0` 및 `export OLLAMA_ORIGINS="*"` 입력 후 `ollama serve` 실행
        
        **LM Studio의 경우:**
        - Local Server 탭 설정에서 `Cross-Origin-Resource-Sharing (CORS)` 활성화
        - 외부 IP가 접근할 수 있도록 포트(1234) 방화벽 해제
        """)
    
    available_models = get_all_models(target_ip)
    
    if not available_models:
        st.warning(f"'{target_ip}'에서 감지된 로컬 모델이 없습니다. 서버가 실행 중인지, 외부 접속이 허용되어 있는지 확인해 주세요.")
    else:
        model_options = {}
        for m in available_models:
            param_text = f"{m['params']}B" if m['params'] > 0 else "Unknown"
            display_name = f"[{m['source']}] {m['name']} (Params: {param_text})"
            model_options[display_name] = m
            
        selected_options = st.multiselect(
            "진단할 모델을 선택하세요 (여러 개 선택 시 순차적으로 자동 벤치마크합니다):", 
            options=list(model_options.keys()),
            default=[list(model_options.keys())[0]] if model_options else []
        )
        
        prompt_category = st.selectbox("벤치마크 프롬프트 유형", list(PROMPT_TEMPLATES.keys()) + ["✏️ 직접 입력"])
        if prompt_category == "✏️ 직접 입력":
            prompt_text = st.text_area("벤치마크에 사용할 프롬프트를 직접 입력하세요:", height=100)
        else:
            prompt_text = PROMPT_TEMPLATES[prompt_category]
            st.info(f"**프롬프트 내용:**\n{prompt_text}")
        
        if st.button("벤치마크 일괄 시작", type="primary"):
            if not prompt_text.strip():
                st.error("프롬프트를 입력해주세요.")
            elif not selected_options:
                st.warning("벤치마크할 모델을 하나 이상 선택해주세요.")
            else:
                progress_bar = st.progress(0)
                status_text = st.empty()
                results_summary = []
                
                for i, option in enumerate(selected_options):
                    selected_model_info = model_options[option]
                    status_text.info(f"[{i+1}/{len(selected_options)}] **{selected_model_info['name']}** 벤치마크 진행 중...")
                    
                    progress_placeholder = st.empty()
                    with st.spinner(f"'{selected_model_info['name']}' 성능 측정 중... 잠시만 기다려주세요"):
                        result = benchmark_model(selected_model_info, target_ip, prompt_text, progress_placeholder)
                        
                    progress_placeholder.empty()
                    
                    if result["success"]:
                        target_tps = get_baseline_tps(selected_model_info)
                        save_benchmark_history(selected_model_info, prompt_category, result, target_tps)
                        st.success(f"✅ {selected_model_info['name']} 테스트 완료! (TPS: {result['tps']:.1f})")
                        
                        params = selected_model_info.get("params", 0)
                        expected_vram = (params * 0.7) + 1.0 if params > 0 else 0
                        
                        results_summary.append({
                            "모델명": selected_model_info["name"],
                            "TTFT (s)": round(result["ttft"], 2),
                            "측정 TPS": round(result["tps"], 1),
                            "달성률 (%)": round((result["tps"] / target_tps * 100) if target_tps > 0 else 0, 1),
                            "최소 요구 VRAM": f"{expected_vram:.1f} GB" if expected_vram > 0 else "알 수 없음"
                        })
                    else:
                        st.error(f"🚨 **{selected_model_info['name']} 벤치마크 실패!** 통신 중 오류 발생: `{result['error']}`")
                        
                    progress_bar.progress((i + 1) / len(selected_options))
                
                status_text.success("🎉 모든 벤치마크가 성공적으로 완료되었습니다! 전체 이력은 '벤치마크 이력' 탭에서 확인하실 수 있습니다.")
                
                if results_summary:
                    st.markdown("---")
                    st.subheader("📊 일괄 벤치마크 요약 결과")
                    df_summary = pd.DataFrame(results_summary)
                    st.dataframe(df_summary, width='stretch', hide_index=True)
                    
                    if len(results_summary) == 1:
                        st.subheader("성능 달성률 진단")
                        fig = draw_gauge_chart(results_summary[0]["측정 TPS"], get_baseline_tps(model_options[selected_options[0]]))
                        st.plotly_chart(fig, width='stretch')
