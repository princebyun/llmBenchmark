import streamlit as st
import pandas as pd
from config import PROMPT_TEMPLATES, MULTI_TURN_SCENARIO, OLLAMA_PORT, LMSTUDIO_PORT, VLLM_PORT
from components.client_engine import benchmark_engine
from services.scoring import get_baseline_tps
from services.history import save_benchmark_history
from components.charts import draw_gauge_chart, draw_radar_chart, draw_multiturn_line_chart

def render():
    st.subheader("🚀 로컬 기기 벤치마크 (Client-Side)")
    
    st.info("현재 접속 중인 브라우저가 실행되고 있는 **사용자님의 PC(localhost)**를 진단합니다.")
    
    # JS 엔진에 넘겨줄 설정
    config = {
        "ollama_port": OLLAMA_PORT,
        "lmstudio_port": LMSTUDIO_PORT,
        "vllm_port": VLLM_PORT,
        "multiturn_scenario": MULTI_TURN_SCENARIO
    }
    
    # 브라우저에서 실행될 JS 컴포넌트 호출
    # 컴포넌트가 완료되면 결과를 JSON(dict)으로 반환합니다.
    result_payload = benchmark_engine(
        prompts=PROMPT_TEMPLATES,
        config=config,
        key="benchmark_main"
    )
    
    # 결과 수신 후 시각화
    if result_payload and "results" in result_payload:
        results = result_payload["results"]
        if not results:
            return
            
        st.markdown("---")
        st.subheader("📊 일괄 벤치마크 요약 결과")
        
        results_summary = []
        
        for item in results:
            model_info = item["modelInfo"]
            prompt_category = item["promptCategory"]
            res = item["result"]
            is_multiturn = "멀티턴" in prompt_category
            
            target_tps = get_baseline_tps(model_info)
            save_benchmark_history(model_info, prompt_category, res, target_tps)
            
            summary_item = {
                "모델명": model_info["name"],
                "모델 로딩 (s)": round(res.get("load_time", 0) or 0, 2),
                "프롬프트 TPS": round(res.get("prompt_tps", 0) or 0, 1),
                "TTFT (s)": round(res.get("ttft", 0), 2),
                "서버 자체 TPS": round(res.get("server_tps", res.get("tps", 0)) or 0, 1),
                "클라이언트 TPS": round(res.get("tps", 0), 1),
                "달성률 (%)": round((res.get("tps", 0) / target_tps * 100) if target_tps > 0 else 0, 1)
            }
            
            if is_multiturn:
                summary_item["턴별 결과"] = res["turns"]
                
            results_summary.append(summary_item)
            
        # 테이블 표시 (턴별 결과 제외)
        display_df = pd.DataFrame([{k: v for k, v in r.items() if k != "턴별 결과"} for r in results_summary])
        st.dataframe(display_df, use_container_width=True, hide_index=True)
        
        # 상세 차트
        for r in results_summary:
            if "턴별 결과" in r:
                st.markdown(f"#### 🔄 {r['모델명']} 멀티턴 상세 분석")
                colA, colB = st.columns([1, 1])
                with colA:
                    st.dataframe(pd.DataFrame(r["턴별 결과"])[["턴", "TTFT", "클라이언트 TPS", "토큰 수"]], use_container_width=True, hide_index=True)
                with colB:
                    fig = draw_multiturn_line_chart(r["턴별 결과"])
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.markdown(f"#### 🎯 {r['모델명']} 종합 성능 분석")
                colA, colB = st.columns([1, 1])
                
                # 모델 정보를 찾기 (get_baseline_tps에 전달하기 위해)
                matching_model_info = next(item["modelInfo"] for item in results if item["modelInfo"]["name"] == r["모델명"])
                baseline = get_baseline_tps(matching_model_info)
                
                with colA:
                    fig_gauge = draw_gauge_chart(r["클라이언트 TPS"], baseline)
                    st.plotly_chart(fig_gauge, use_container_width=True)
                with colB:
                    fig_radar = draw_radar_chart(r)
                    st.plotly_chart(fig_radar, use_container_width=True)
