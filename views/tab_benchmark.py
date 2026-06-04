import streamlit as st
import pandas as pd
from config import PROMPT_TEMPLATES
from services.models import get_all_models
from services.benchmark import benchmark_model, get_baseline_tps
from services.history import save_benchmark_history
from charts import draw_gauge_chart

def render():
    st.subheader("진단 환경 설정")
    
    if "target_ip" not in st.session_state:
        st.session_state.target_ip = ""
        
    col1, col2 = st.columns([5, 1])
    with col1:
        target_ip_input = st.text_input("🎯 벤치마크할 기기의 IP 주소", value=st.session_state.target_ip)
        
    # 텍스트 입력창에서 엔터를 쳐서 값이 변경되었을 때 자동 적용
    if target_ip_input != st.session_state.target_ip:
        st.session_state.target_ip = target_ip_input
        if "available_models" in st.session_state:
            del st.session_state["available_models"]

    with col2:
        # 텍스트 입력창 높이와 맞추기 위한 CSS 마진
        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        if st.button("적용", use_container_width=True):
            st.session_state.target_ip = target_ip_input
            if "available_models" in st.session_state:
                del st.session_state["available_models"]
                
    target_ip = st.session_state.target_ip
    
    st.caption("외부 기기를 벤치마크하려면 해당 기기의 IP(예: 192.168.0.x)를 입력 후 '적용'을 누르세요. (단, 해당 기기의 LLM 프로그램(Ollama, LM Studio, vLLM, oMLX 등) 외부 접속이 허용되어 있어야 합니다.)")
    
    with st.expander("💡 외부 기기 접속 허용 설정 방법 보기"):
        st.markdown("""
        **1. Ollama의 경우 (서버 PC에서 설정 후 재시작):**
        - **Windows:** 명령 프롬프트에서 `set OLLAMA_HOST=0.0.0.0` 및 `set OLLAMA_ORIGINS="*"` 입력 후 `ollama serve` 실행
        - **Mac/Linux:** 터미널에서 `export OLLAMA_HOST=0.0.0.0` 및 `export OLLAMA_ORIGINS="*"` 입력 후 `ollama serve` 실행
        
        **2. LM Studio의 경우:**
        - 개발자 옵션(Local Server 탭)에서 `Cross-Origin-Resource-Sharing (CORS)` 활성화
        - 외부 IP가 접근할 수 있도록 포트(1234) 방화벽 해제
        
        **3. vLLM의 경우:**
        - 서버 실행 명령어에 `--host 0.0.0.0` 옵션을 추가하여 실행하세요. (예: `python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --model <모델명>`)
        
        **4. oMLX의 경우:**
        - 서버 실행 명령어에 `--host 0.0.0.0` 옵션을 추가하여 실행하거나, 앱 내 네트워크 설정에서 외부 접속을 허용해 주세요.
        """)
    
    if "available_models" not in st.session_state:
        if target_ip.strip() == "":
            st.session_state.available_models = []
        else:
            with st.spinner("🤖 모델 목록을 스캔하고 있습니다... 잠시만 기다려주세요"):
                st.session_state.available_models = get_all_models(target_ip)
            
    available_models = st.session_state.available_models
    
    if not available_models:
        if target_ip.strip() == "":
            st.info("🎯 벤치마크할 기기의 IP 주소를 입력하고 '적용 및 새로고침' 버튼을 눌러주세요. (현재 PC라면 localhost 입력)")
        else:
            st.warning(f"'{target_ip}'에서 감지된 로컬 모델이 없습니다. 서버가 실행 중인지, 외부 접속이 허용되어 있는지 확인해 주세요.")
    else:
        model_options = {}
        for m in available_models:
            param_text = f"{m['params']}B" if m['params'] > 0 else "Unknown"
            display_name = f"[{m['source']}] {m['name']} (Params: {param_text})"
            model_options[display_name] = m
            
        st.markdown("""
        <style>
        /* 드롭다운 옵션 텍스트 줄바꿈/잘림 방지 */
        div[role="listbox"] li {
            white-space: normal !important;
            word-wrap: break-word !important;
        }
        /* 선택된 칩(태그) 텍스트 잘림 방지 */
        span[data-baseweb="tag"] span {
            white-space: normal !important;
            overflow: visible !important;
            text-overflow: clip !important;
            max-width: none !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        selected_options = st.multiselect(
            "진단할 모델 (여러 개 선택 시 순차적으로 자동 벤치마크합니다):", 
            options=list(model_options.keys()),
            default=[],
            placeholder="진단할 모델을 선택하세요"
        )
        
        prompt_category = st.selectbox("벤치마크 프롬프트 유형", list(PROMPT_TEMPLATES.keys()))
        prompt_text = PROMPT_TEMPLATES[prompt_category]
        
        if st.button("벤치마크 일괄 시작", type="primary"):
            if not prompt_text.strip():
                st.error("프롬프트를 입력해주세요.")
            elif not selected_options:
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
                            "모델 로딩 (s)": round(result.get("load_time", 0) or 0, 2),
                            "프롬프트 TPS": round(result.get("prompt_tps", 0) or 0, 1),
                            "TTFT (s)": round(result["ttft"], 2),
                            "서버 자체 TPS": round(result.get("server_tps", result["tps"]) or 0, 1),
                            "클라이언트 TPS": round(result["tps"], 1),
                            "달성률 (%)": round((result["tps"] / target_tps * 100) if target_tps > 0 else 0, 1),
                            "최소 요구 VRAM": f"{expected_vram:.1f} GB" if expected_vram > 0 else "알 수 없음"
                        })
                    else:
                        st.error(f"🚨 **{selected_model_info['name']} 벤치마크 실패!** 통신 중 오류 발생: `{result['error']}`")
                        has_error = True
                        
                        with st.expander("💡 벤치마크 실패(타임아웃 등 에러) 시 대처 방법 보기"):
                            st.markdown("""
                            **1. 'Read timed out' (대기 시간 초과) 에러가 발생한 경우:**
                            - **원인:** 서버가 멈춘 것이 아니라, 하드디스크에서 무거운 모델을 VRAM으로 불러오느라(Loading) 응답이 늦어지는 상태입니다.
                            - **대처법 (재시도):** 약 10~20초 정도 기다렸다가 다시 '벤치마크 시작' 버튼을 눌러보세요. 이미 로딩이 끝나서 두 번째부터는 정상 측정될 확률이 높습니다.
                            - **대처법 (모델 변경):** 여러 번 재시도해도 동일하다면 기기 사양에 비해 모델이 너무 무거운 것이니, 더 작은 파라미터의 모델로 변경하세요.
                            
                            **2. 연결 거부(Connection Refused) 에러인 경우:**
                            - 백그라운드에서 LLM 프로그램(Ollama, LM Studio, vLLM, oMLX 등) 서버가 켜져 있는지 확인하세요.
                            - 외부 기기를 측정 중이라면 상단의 '외부 기기 접속 허용 설정'을 참고하여 개방해야 합니다.
                            """)
                        
                    progress_bar.progress((i + 1) / len(selected_options))
                
                if has_error:
                    status_text.warning("⚠️ 일부 벤치마크 과정에서 오류가 발생했습니다. 아래 메시지를 확인해 주세요.")
                else:
                    status_text.success("🎉 모든 벤치마크가 성공적으로 완료되었습니다! 전체 이력은 '벤치마크 이력' 탭에서 확인하실 수 있습니다.")
                
                if results_summary:
                    st.markdown("---")
                    st.subheader("📊 일괄 벤치마크 요약 결과")
                    df_summary = pd.DataFrame(results_summary)
                    st.dataframe(df_summary, width='stretch', hide_index=True)
                    
                    with st.expander("💡 벤치마크 지표 용어 설명 (클릭하여 닫기/열기)", expanded=True):
                        st.markdown("""
                        * **모델 로딩 (s)**: 인공지능 뇌(모델)를 메모리에 불러오는 데 걸린 시간입니다. **(낮을수록 좋음 ⬇️)**
                        * **프롬프트 TPS**: 질문(프롬프트)을 인공지능이 얼마나 빨리 읽고 이해하는지 나타내는 처리 속도입니다. **(높을수록 좋음 ⬆️)**
                        * **TTFT (s)**: Time To First Token. 질문을 던지고 첫 번째 대답 글자가 화면에 찍히기까지 걸린 대기 시간입니다. **(낮을수록 좋음 ⬇️)**
                        * **서버 자체 TPS**: 모델이 순수하게 답변 글자를 만들어내는 초당 생성 속도입니다. **(높을수록 좋음 ⬆️)**
                        * **클라이언트 TPS**: 네트워크 통신 시간까지 포함하여, 실제 사용자 화면에 글자가 찍히는 '체감' 초당 생성 속도입니다. **(높을수록 좋음 ⬆️)**
                        * **달성률 (%)**: 이 모델이 낼 수 있는 최고 속도 대비 현재 내 컴퓨터 환경에서 끌어내고 있는 속도의 비율입니다. 100%에 가까울수록 하드웨어 성능을 알차게 쓰고 있다는 뜻입니다. **(높을수록 좋음 ⬆️)**
                        * **최소 요구 VRAM**: 이 모델을 버벅거림 없이 쾌적하게 돌리기 위해 필요한 그래픽카드 메모리의 최소 용량입니다.
                        """)
                    
                    if len(results_summary) == 1:
                        st.subheader("성능 달성률 진단")
                        fig = draw_gauge_chart(results_summary[0]["클라이언트 TPS"], get_baseline_tps(model_options[selected_options[0]]))
                        st.plotly_chart(fig, width='stretch')
