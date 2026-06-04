import streamlit as st
from services.models import get_all_models
from services.security import validate_target_ip
from services.hardware_info import GPU_VRAM_MAP, recommend_models
from components.spinner import show_custom_spinner

def render():
    st.subheader("⚙️ 진단 환경 설정")
    st.markdown("벤치마크를 수행하기 전, 내 PC 사양과 대상 기기의 IP, 테스트할 모델을 설정합니다.")
    
    # 1. 하드웨어 사양 자가 입력
    st.markdown("#### 1. 내 PC 사양 입력 (선택)")
    gpu_choice = st.selectbox("사용 중인 그래픽카드(GPU)를 선택하세요", list(GPU_VRAM_MAP.keys()))
    vram_val = GPU_VRAM_MAP[gpu_choice]
    
    if vram_val > 0:
        st.info(f"선택한 GPU의 VRAM은 **{vram_val}GB** 입니다.")
        recommended = recommend_models(vram_val)
        st.success(f"**추천 최대 구동 가능 모델:** {', '.join(recommended)}")
    elif vram_val == 0:
        st.warning("GPU가 없어 CPU로 구동해야 합니다. 3B 이하 초소형 모델만 추천합니다.")
        
    st.markdown("---")
    
    # 2. IP 입력 및 보안 검증
    st.markdown("#### 2. 대상 기기 연결")
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
        if st.button("연결 적용", use_container_width=True):
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
            
    st.caption("외부 기기를 벤치마크하려면 해당 기기의 IP를 입력하세요. 서버 관리용 메타데이터 IP 등은 보안상 차단됩니다.")
    
    with st.expander("💡 외부 기기 방화벽 및 접속 허용 설정 방법 보기"):
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
        
    st.markdown("---")
    
    # 3. 모델 스캔 및 큐 관리
    st.markdown("#### 3. 진단할 모델 선택")
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
            st.info("🎯 IP 주소를 입력하여 연결을 활성화해 주세요.")
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
            "대기열에 추가할 모델:", 
            options=options,
            key="temp_model_selector",
            on_change=on_model_select
        )
        
        # 실제 모델 딕셔너리를 접근하기 위해 st.session_state에 model_options 저장 (benchmark에서 꺼내 쓰기 위함)
        st.session_state.model_options = model_options
        
        selected_options = st.session_state.selected_models_list
        if selected_options:
            st.markdown("**✅ 벤치마크 진행 대기열:**")
            for m in selected_options:
                colA, colB = st.columns([10, 1])
                with colA:
                    st.info(m)
                with colB:
                    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
                    if st.button("❌", key=f"remove_{m}", help="이 모델을 대기열에서 제거합니다"):
                        st.session_state.selected_models_list.remove(m)
                        st.rerun()
