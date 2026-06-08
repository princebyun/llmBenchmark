import streamlit as st
import pandas as pd
from config import get_prompts, OLLAMA_PORT, LMSTUDIO_PORT, VLLM_PORT
from components.client_engine import benchmark_engine
from services.scoring import get_baseline_tps
from services.history import save_benchmark_history
from components.charts import draw_gauge_chart, draw_radar_chart, draw_multiturn_line_chart
from locales import get_text

def t(key):
    return get_text(st.session_state.lang, key)

def render():
    st.subheader(t("bench_title"))
    
    st.info(t("bench_info"))
    
    with st.expander("💡 벤치마크 필수 설정 (브라우저 CORS 허용 방법)" if st.session_state.lang == "ko" else "💡 Benchmark Prerequisite (Browser CORS Policy)"):
        st.markdown("""
        본 벤치마크는 오라클 서버가 아닌 **사용자님의 웹 브라우저가 직접 로컬 PC와 통신**합니다.
        따라서 방화벽 포트포워딩은 필요 없지만, 브라우저 보안 정책상 **CORS(교차 출처 리소스 공유)**를 허용해야 합니다.
        
        **1. Ollama의 경우:**
        - **Windows:** 시스템 환경 변수 편집에서 `OLLAMA_ORIGINS` 변수를 만들고 값을 `*` 로 설정한 뒤 Ollama 재시작
        - **Mac/Linux:** 터미널에서 `export OLLAMA_ORIGINS="*"` 입력 후 `ollama serve` 실행
        
        **2. LM Studio의 경우:**
        - 개발자 옵션(Local Server 탭)에서 `Cross-Origin-Resource-Sharing (CORS)` 활성화
        """ if st.session_state.lang == "ko" else """
        This benchmark relies on **your web browser communicating directly with your local PC**, not the Oracle server.
        Therefore, firewall port forwarding is not required, but you must allow **CORS (Cross-Origin Resource Sharing)** due to browser security policies.
        
        **1. For Ollama:**
        - **Windows:** Edit System Environment Variables, add `OLLAMA_ORIGINS` with value `*`, then restart Ollama.
        - **Mac/Linux:** In terminal, run `export OLLAMA_ORIGINS="*"` and then `ollama serve`.
        
        **2. For LM Studio:**
        - Enable `Cross-Origin-Resource-Sharing (CORS)` toggle in Developer Options (Local Server tab).
        """)
        
    # 설정 언어에 따라 프롬프트 템플릿 가져오기
    prompts, multiturn_scenario = get_prompts(st.session_state.lang)
    
    # JS 엔진에 넘겨줄 설정
    config = {
        "ollama_port": OLLAMA_PORT,
        "lmstudio_port": LMSTUDIO_PORT,
        "vllm_port": VLLM_PORT,
        "multiturn_scenario": multiturn_scenario,
        "lang": st.session_state.lang
    }
    
    # 브라우저에서 실행될 JS 컴포넌트 호출
    # 컴포넌트가 완료되면 결과를 JSON(dict)으로 반환합니다.
    result_payload = benchmark_engine(
        prompts=prompts,
        config=config,
        key=f"benchmark_main_{st.session_state.lang}"
    )
    
    if result_payload and "results" in result_payload:
        results = result_payload["results"]
        if not results:
            st.error(t("bench_all_failed") if "bench_all_failed" in st.session_state else "⚠️ 모든 모델의 벤치마크 테스트가 실패했습니다. 에러 로그를 확인해주세요.")
            return
            
        st.markdown("---")
        st.subheader(t("bench_summary_title"))
        
        successful_results = []
        failed_results = []
        
        for item in results:
            model_info = item["modelInfo"]
            prompt_category = item["promptCategory"]
            res = item["result"]
            
            # 실패한 결과 분리
            if res.get("success") is False:
                failed_results.append({
                    "model_name": model_info["name"],
                    "error": res.get("error", "알 수 없는 에러 발생")
                })
                continue
                
            is_multiturn = ("멀티턴" in prompt_category or "Multi-turn" in prompt_category)
            
            target_tps = get_baseline_tps(model_info)
            save_benchmark_history(model_info, prompt_category, res, target_tps)
            
            summary_item = {
                t("col_model"): model_info["name"],
                t("col_load"): round(res.get("load_time", 0) or 0, 2),
                t("col_prompt_tps"): round(res.get("prompt_tps", 0) or 0, 1),
                t("col_ttft"): round(res.get("ttft", 0), 2),
                t("col_server_tps"): round(res.get("server_tps", res.get("tps", 0)) or 0, 1),
                t("col_client_tps"): round(res.get("tps", 0), 1),
                t("col_achieve"): round((res.get("tps", 0) / target_tps * 100) if target_tps > 0 else 0, 1)
            }
            
            if is_multiturn:
                summary_item["턴별 결과"] = res["turns"]
                
            successful_results.append(summary_item)
            
        # 1. 실패한 모델 에러 표시
        if failed_results:
            st.error("⚠️ 다음 모델들은 벤치마크 진행 중 에러가 발생하여 제외되었습니다.")
            for fail in failed_results:
                st.markdown(f"- **{fail['model_name']}**: `{fail['error']}`")
            st.markdown("---")

        # 2. 성공한 모델 데이터 표시
        if not successful_results:
            return
            
        # 테이블 표시 (턴별 결과 제외)
        display_df = pd.DataFrame([{k: v for k, v in r.items() if k != "턴별 결과"} for r in successful_results])
        st.dataframe(display_df, use_container_width=True, hide_index=True)
        
        # 상세 차트
        for r in successful_results:
            if "턴별 결과" in r:
                st.markdown(t("multiturn_detail").format(model=r[t("col_model")]))
                colA, colB = st.columns([1, 1])
                with colA:
                    st.dataframe(pd.DataFrame(r["턴별 결과"])[["턴", "TTFT", "클라이언트 TPS", "토큰 수"]], use_container_width=True, hide_index=True)
                with colB:
                    fig = draw_multiturn_line_chart(r["턴별 결과"])
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.markdown(t("single_detail").format(model=r[t("col_model")]))
                colA, colB = st.columns([1, 1])
                
                # 모델 정보를 찾기 (get_baseline_tps에 전달하기 위해)
                matching_model_info = next(item["modelInfo"] for item in results if item["modelInfo"]["name"] == r[t("col_model")])
                baseline = get_baseline_tps(matching_model_info)
                
                with colA:
                    fig_gauge = draw_gauge_chart(r[t("col_client_tps")], baseline)
                    st.plotly_chart(fig_gauge, use_container_width=True)
                with colB:
                    # 차트에 사용할 영문 키 변환을 피하기 위해 r 자체를 넘기되, 내부적으로 draw_radar_chart도 다국어를 적용해야 할 수 있음.
                    # 여기서는 우선 영문키/다국어키 맵핑이 복잡하므로 r 그대로 넘김 (추가 수정 필요할 수도 있음)
                    fig_radar = draw_radar_chart(r, lang=st.session_state.lang)
                    st.plotly_chart(fig_radar, use_container_width=True)
