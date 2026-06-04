import streamlit as st
import pandas as pd
from config import PROMPT_TEMPLATES
from services.benchmark import benchmark_model, get_baseline_tps
from services.benchmark_advanced import benchmark_multiturn
from services.history import save_benchmark_history
from components.charts import draw_gauge_chart, draw_radar_chart, draw_multiturn_line_chart

def render():
    st.subheader("🚀 벤치마크 실행")
    
    # 설정 탭에서 설정된 값들을 가져옵니다.
    target_ip = st.session_state.get("target_ip", "")
    selected_options = st.session_state.get("selected_models_list", [])
    model_options = st.session_state.get("model_options", {})
    
    if not target_ip:
        st.warning("먼저 '진단 환경 설정' 메뉴에서 대상 기기의 IP 주소를 설정해주세요.")
        return
        
    if not selected_options:
        st.warning("먼저 '진단 환경 설정' 메뉴에서 테스트할 모델을 대기열에 추가해주세요.")
        return
        
    st.markdown("### 📋 벤치마크 대기열")
    for m in selected_options:
        st.info(m)
        
    st.markdown("### 🎯 프롬프트 설정 및 실행")
    prompt_category = st.selectbox("벤치마크 프롬프트 유형", list(PROMPT_TEMPLATES.keys()))
    prompt_text = PROMPT_TEMPLATES[prompt_category]
    is_multiturn = "멀티턴" in prompt_category
    
    if st.button("벤치마크 일괄 시작", type="primary", use_container_width=True):
        progress_bar = st.progress(0)
        status_text = st.empty()
        results_summary = []
        has_error = False
        
        for i, option in enumerate(selected_options):
            selected_model_info = model_options[option]
            status_text.info(f"[{i+1}/{len(selected_options)}] **{selected_model_info['name']}** 벤치마크 진행 중...")
            
            progress_placeholder = st.empty()
            
            if is_multiturn:
                result = benchmark_multiturn(selected_model_info, target_ip, progress_placeholder)
            else:
                result = benchmark_model(selected_model_info, target_ip, prompt_text, progress_placeholder)
                
            progress_placeholder.empty()
            
            if result.get("success"):
                target_tps = get_baseline_tps(selected_model_info)
                save_benchmark_history(selected_model_info, prompt_category, result, target_tps)
                st.success(f"✅ {selected_model_info['name']} 완료! (평균 TPS: {result['tps']:.1f})")
                
                params = selected_model_info.get("params", 0)
                
                summary_item = {
                    "모델명": selected_model_info["name"],
                    "모델 로딩 (s)": round(result.get("load_time", 0) or 0, 2),
                    "프롬프트 TPS": round(result.get("prompt_tps", 0) or 0, 1),
                    "TTFT (s)": round(result.get("ttft", 0), 2),
                    "서버 자체 TPS": round(result.get("server_tps", result.get("tps", 0)) or 0, 1),
                    "클라이언트 TPS": round(result.get("tps", 0), 1),
                    "달성률 (%)": round((result.get("tps", 0) / target_tps * 100) if target_tps > 0 else 0, 1)
                }
                
                if is_multiturn:
                    summary_item["턴별 결과"] = result["turns"]
                    
                results_summary.append(summary_item)
            else:
                st.error(f"🚨 **{selected_model_info['name']} 실패!** 오류: `{result.get('error')}`")
                has_error = True
                
            progress_bar.progress((i + 1) / len(selected_options))
        
        if has_error:
            status_text.warning("⚠️ 일부 벤치마크 과정에서 오류가 발생했습니다.")
        else:
            status_text.success("🎉 모든 벤치마크가 성공적으로 완료되었습니다!")
        
        if results_summary:
            st.markdown("---")
            st.subheader("📊 일괄 벤치마크 요약 결과")
            
            display_df = pd.DataFrame([{k: v for k, v in r.items() if k != "턴별 결과"} for r in results_summary])
            st.dataframe(display_df, use_container_width=True, hide_index=True)
            
            for r in results_summary:
                if is_multiturn and "턴별 결과" in r:
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
                    with colA:
                        fig_gauge = draw_gauge_chart(r["클라이언트 TPS"], get_baseline_tps(model_options[[opt for opt in selected_options if model_options[opt]['name'] == r['모델명']][0]]))
                        st.plotly_chart(fig_gauge, use_container_width=True)
                    with colB:
                        fig_radar = draw_radar_chart(r)
                        st.plotly_chart(fig_radar, use_container_width=True)
