import streamlit as st
import pandas as pd
from config import PROMPT_TEMPLATES
from services.models import get_all_models
from services.benchmark import benchmark_model, get_baseline_tps
from services.benchmark_advanced import benchmark_multiturn
from services.history import save_benchmark_history
from services.security import validate_target_ip
from services.hardware_info import GPU_VRAM_MAP, recommend_models
from components.charts import draw_gauge_chart, draw_radar_chart, draw_multiturn_line_chart
from components.spinner import show_custom_spinner

def render():
    st.subheader("진단 환경 설정")
    
    # 1. 하드웨어 사양 자가 입력 (선택)
    with st.expander("💻 내 PC 사양 입력 및 모델 추천 (선택)", expanded=False):
        gpu_choice = st.selectbox("사용 중인 그래픽카드(GPU)를 선택하세요", list(GPU_VRAM_MAP.keys()))
        vram_val = GPU_VRAM_MAP[gpu_choice]
        
        if vram_val > 0:
            st.info(f"선택한 GPU의 VRAM은 **{vram_val}GB** 입니다.")
            recommended = recommend_models(vram_val)
            st.success(f"**추천 최대 구동 가능 모델:** {', '.join(recommended)}")
        elif vram_val == 0:
            st.warning("GPU가 없어 CPU로 구동해야 합니다. 3B 이하 초소형 모델만 추천합니다.")
    
    # 2. IP 입력 및 보안 검증
    if "target_ip" not in st.session_state:
        st.session_state.target_ip = ""
        
    col1, col2 = st.columns([5, 1])
    with col1:
        target_ip_input = st.text_input("🎯 벤치마크할 기기의 IP 주소", value=st.session_state.target_ip)
        
    if target_ip_input != st.session_state.target_ip:
        if target_ip_input.strip() == "":
            st.session_state.target_ip = ""
            if "available_models" in st.session_state:
                del st.session_state["available_models"]
        else:
            is_safe, msg = validate_target_ip(target_ip_input)
            if not is_safe:
                st.error(f"🚨 접근 차단: {msg}")
            else:
                st.session_state.target_ip = target_ip_input
                if "available_models" in st.session_state:
                    del st.session_state["available_models"]

    with col2:
        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        if st.button("적용", use_container_width=True):
            if target_ip_input.strip() == "":
                st.session_state.target_ip = ""
                if "available_models" in st.session_state:
                    del st.session_state["available_models"]
            else:
                is_safe, msg = validate_target_ip(target_ip_input)
                if not is_safe:
                    st.error(f"🚨 접근 차단: {msg}")
                else:
                    st.session_state.target_ip = target_ip_input
                    if "available_models" in st.session_state:
                        del st.session_state["available_models"]
                
    target_ip = st.session_state.target_ip
    
    if target_ip.strip() != "":
        is_safe, _ = validate_target_ip(target_ip)
        if not is_safe:
            return
    else:
        # IP가 비어있으면 이 시점에서 아래 내용(모델 선택 등)을 렌더링하기 전 중단할 수 있지만,
        # 아래 스캔 로직에서 빈 값일 때 안내를 하므로 그대로 통과시킵니다.
        pass
        
    st.caption("외부 기기를 벤치마크하려면 해당 기기의 IP를 입력하세요. 서버 관리용 메타데이터 IP 등은 보안상 차단됩니다.")
    
    # 3. 모델 스캔
    if "available_models" not in st.session_state:
        if target_ip.strip() == "":
            st.session_state.available_models = []
        else:
            popup = st.empty()
            popup.markdown(show_custom_spinner("🤖 모델 목록을 스캔하고 있습니다... 잠시만 기다려주세요"), unsafe_allow_html=True)
            st.session_state.available_models = get_all_models(target_ip)
            popup.empty()
            
    available_models = st.session_state.available_models
    
    if not available_models:
        if target_ip.strip() == "":
            st.info("🎯 IP 주소를 입력해 주세요.")
        else:
            st.warning(f"'{target_ip}'에서 감지된 로컬 모델이 없습니다. 서버 실행 여부와 방화벽을 확인하세요.")
    else:
        model_options = {}
        for m in available_models:
            param_text = f"{m['params']}B" if m['params'] > 0 else "Unknown"
            display_name = f"[{m['source']}] {m['name']} (Params: {param_text})"
            model_options[display_name] = m
            
        if "selected_models_list" not in st.session_state:
            st.session_state.selected_models_list = []
            
        def on_model_select():
            selected = st.session_state.get("temp_model_selector")
            if selected and selected != "선택하세요":
                if selected not in st.session_state.selected_models_list:
                    st.session_state.selected_models_list.append(selected)

        options = ["선택하세요"] + list(model_options.keys())
        st.selectbox(
            "진단할 모델 추가:", 
            options=options,
            key="temp_model_selector",
            on_change=on_model_select
        )
        
        selected_options = st.session_state.selected_models_list
        if selected_options:
            st.markdown("**✅ 벤치마크 진행 대기열:**")
            for m in selected_options:
                colA, colB = st.columns([10, 1])
                with colA:
                    st.info(m)
                with colB:
                    if st.button("❌", key=f"remove_{m}", help="목록에서 제거"):
                        st.session_state.selected_models_list.remove(m)
                        st.rerun()
        
        prompt_category = st.selectbox("벤치마크 프롬프트 유형", list(PROMPT_TEMPLATES.keys()))
        prompt_text = PROMPT_TEMPLATES[prompt_category]
        is_multiturn = "멀티턴" in prompt_category
        
        if st.button("벤치마크 일괄 시작", type="primary"):
            if not selected_options:
                st.warning("벤치마크할 모델을 하나 이상 선택해주세요.")
            else:
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
                    st.dataframe(display_df, width='stretch', hide_index=True)
                    
                    for r in results_summary:
                        if is_multiturn and "턴별 결과" in r:
                            st.markdown(f"#### 🔄 {r['모델명']} 멀티턴 상세 분석")
                            colA, colB = st.columns([1, 1])
                            with colA:
                                st.dataframe(pd.DataFrame(r["턴별 결과"])[["턴", "TTFT", "클라이언트 TPS", "토큰 수"]], width='stretch', hide_index=True)
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
