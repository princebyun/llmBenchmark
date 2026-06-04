import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import time
import json
import re
import os
from datetime import datetime

HISTORY_FILE = "benchmark_history.json"

# ==========================================
# 1. 페이지 설정 및 초기화
# ==========================================
st.set_page_config(
    page_title="로컬 LLM 하드웨어 벤치마크",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 불필요한 기본 UI 요소(Deploy 버튼 등) 숨기기
st.markdown("""
    <style>
        .stDeployButton {display:none;}
    </style>
""", unsafe_allow_html=True)

# 기본 제공 프롬프트 템플릿
PROMPT_TEMPLATES = {
    "📝 일반 설명 (기본)": "양자 역학의 불확정성 원리를 고등학생이 이해할 수 있도록 3문단으로 요약하고, 일상생활의 예시를 하나 들어 설명해 줘.",
    "💻 코드 작성 (파이썬)": "파이썬으로 A* 경로 탐색 알고리즘을 구현하고, 주석을 상세히 달아줘. 그리고 간단한 2D 미로 예제도 함께 만들어줘.",
    "🌐 번역 (한→영)": "다음 한국어 기사를 자연스러운 비즈니스 영어로 번역해 줘: '최근 인공지능 기술의 발전은 기업들의 업무 효율성을 극대화하고 있습니다. 특히 로컬 LLM 환경은 데이터 보안 측면에서 큰 강점을 가집니다.'"
}

# ==========================================
# 2. 리더보드 실제 데이터 연동 (Hugging Face API)
# ==========================================
@st.cache_data(ttl=3600)
def fetch_global_leaderboard():
    """Hugging Face Open LLM Leaderboard 데이터셋에서 실제 리더보드 데이터를 가져옵니다."""
    # Datasets Server API를 활용하여 리더보드 데이터의 첫 100개 모델 정보를 실시간으로 가져옵니다.
    url = "https://datasets-server.huggingface.co/rows?dataset=open-llm-leaderboard/contents&config=default&split=train&offset=0&length=100"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        rows = data.get("rows", [])
        
        leaderboard = []
        for r in rows:
            row_data = r.get("row", {})
            model_name = row_data.get("fullname", "Unknown")
            params = row_data.get("#Params (B)", 0)
            score = row_data.get("Average ⬆️", 0)
            
            # 파라미터 정보가 없는 경우는 제외
            if not isinstance(params, (int, float)) or params <= 0:
                continue
            
            leaderboard.append({
                "모델명": model_name,
                "파라미터 수 (B)": round(params, 1),
                "평균 점수": round(score, 2),
            })
            
        # 점수 순으로 정렬
        leaderboard = sorted(leaderboard, key=lambda x: x["평균 점수"], reverse=True)
        return leaderboard
    except Exception as e:
        st.warning("⚠️ **Hugging Face 서버가 일시적으로 불안정하여 실시간 리더보드를 불러오지 못했습니다.**\n\n대신 로컬에 저장된 기본 데이터를 표시합니다.")
        
        # API 실패 시 보여줄 오프라인 폴백(Fallback) 데이터
        fallback_data = [
            {"모델명": "Llama 3 8B Instruct", "파라미터 수 (B)": 8.0, "평균 점수": 68.4},
            {"모델명": "Gemma 2 9B", "파라미터 수 (B)": 9.0, "평균 점수": 71.3},
            {"모델명": "Qwen 2 7B", "파라미터 수 (B)": 7.0, "평균 점수": 70.5},
            {"모델명": "Phi-3 Mini", "파라미터 수 (B)": 3.8, "평균 점수": 69.0},
            {"모델명": "Mistral 7B Instruct", "파라미터 수 (B)": 7.3, "평균 점수": 62.5},
            {"모델명": "Gemma 2B", "파라미터 수 (B)": 2.5, "평균 점수": 46.1},
        ]
        return sorted(fallback_data, key=lambda x: x["평균 점수"], reverse=True)

# ==========================================
# 3. 로컬 모델 자동 감지 기능 및 파라미터 파싱
# ==========================================
def extract_params_from_name(name):
    """모델 이름에서 파라미터 수(예: 8b, 7B)를 정규식으로 추출합니다."""
    match = re.search(r'(\d+(?:\.\d+)?)[bB]', name)
    if match:
        return float(match.group(1))
    return 0.0

def get_ollama_models(target_ip="localhost"):
    """Ollama 서버에서 모델 목록과 실제 파라미터 크기를 가져옵니다."""
    models = []
    try:
        response = requests.get(f"http://{target_ip}:11434/api/tags", timeout=2)
        if response.status_code == 200:
            data = response.json()
            for model in data.get("models", []):
                # Ollama API가 제공하는 실제 parameter_size 파싱
                param_size_str = model.get("details", {}).get("parameter_size", "")
                params = 0.0
                if param_size_str and "B" in param_size_str.upper():
                    try:
                        params = float(param_size_str.upper().replace("B", ""))
                    except ValueError:
                        pass
                
                # 만약 API에서 제공하지 않았다면 이름에서 추정
                if params == 0.0:
                    params = extract_params_from_name(model["name"])
                    
                models.append({
                    "name": model["name"], 
                    "source": "Ollama",
                    "params": params
                })
    except requests.exceptions.RequestException:
        pass
    return models

def get_lmstudio_models(target_ip="localhost"):
    """LM Studio 서버에서 모델 목록을 가져옵니다."""
    models = []
    try:
        response = requests.get(f"http://{target_ip}:1234/v1/models", timeout=2)
        if response.status_code == 200:
            data = response.json()
            for model in data.get("data", []):
                name = model["id"]
                # LM Studio는 파라미터 크기를 명시적으로 주지 않으므로 이름에서 추출
                params = extract_params_from_name(name)
                models.append({
                    "name": name, 
                    "source": "LM Studio",
                    "params": params
                })
    except requests.exceptions.RequestException:
        pass
    return models

def get_all_models(target_ip="localhost"):
    return get_ollama_models(target_ip) + get_lmstudio_models(target_ip)

# ==========================================
# 4. 벤치마크 이력 관리 로직
# ==========================================
def save_benchmark_history(model_info, prompt_category, result, target_tps):
    """벤치마크 결과를 로컬 JSON 파일에 저장합니다."""
    history = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
        except:
            pass
            
    history.append({
        "측정 일시": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "모델명": model_info["name"],
        "플랫폼": model_info["source"],
        "파라미터 (B)": model_info["params"],
        "프롬프트 유형": prompt_category,
        "TTFT (s)": round(result["ttft"], 2),
        "TPS": round(result["tps"], 1),
        "기준 TPS": round(target_tps, 1),
        "달성률 (%)": round((result["tps"] / target_tps * 100) if target_tps > 0 else 0, 1)
    })
    
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def load_benchmark_history():
    """저장된 벤치마크 이력을 불러옵니다."""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return []

# ==========================================
# 5. 벤치마크 및 통신 로직
# ==========================================
def get_baseline_tps(model_info):
    """모델의 실제 파라미터 수를 기반으로 동적 기준 TPS를 계산합니다."""
    params = model_info.get("params", 0)
    if params and params > 0:
        return 200.0 / params
    return 30.0 # 파라미터 수를 모를 경우 30 TPS를 기본값으로 사용

def benchmark_model(model_info, target_ip="localhost", prompt_text="", progress_placeholder=None):
    """선택된 모델에 벤치마크 프롬프트를 전송하고 성능을 측정합니다."""
    model_name = model_info["name"]
    source = model_info["source"]
    
    start_time = time.perf_counter()
    first_token_time = None
    token_count = 0
    full_response = ""
    
    try:
        if source == "Ollama":
            url = f"http://{target_ip}:11434/api/chat"
            payload = {
                "model": model_name,
                "messages": [{"role": "user", "content": prompt_text}],
                "stream": True
            }
            response = requests.post(url, json=payload, stream=True)
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    if first_token_time is None:
                        first_token_time = time.perf_counter()
                    data = json.loads(line)
                    if "message" in data and "content" in data["message"]:
                        chunk = data["message"]["content"]
                        full_response += chunk
                        token_count += 1 
                        if progress_placeholder:
                            progress_placeholder.info(f"⏳ **벤치마크 진행 중...** 현재 {token_count}개의 토큰을 처리했습니다.")
                        
        elif source == "LM Studio":
            url = f"http://{target_ip}:1234/v1/chat/completions"
            payload = {
                "model": model_name,
                "messages": [{"role": "user", "content": prompt_text}],
                "stream": True
            }
            response = requests.post(url, json=payload, stream=True)
            response.raise_for_status()
            
            for line in response.iter_lines():
                line = line.decode('utf-8')
                if line.startswith("data: "):
                    data_str = line[6:]
                    if data_str == "[DONE]":
                        break
                    if first_token_time is None:
                        first_token_time = time.perf_counter()
                    data = json.loads(data_str)
                    if "choices" in data and len(data["choices"]) > 0:
                        delta = data["choices"][0].get("delta", {})
                        if "content" in delta:
                            full_response += delta["content"]
                            token_count += 1
                            if progress_placeholder:
                                progress_placeholder.info(f"⏳ **벤치마크 진행 중...** 현재 {token_count}개의 토큰을 처리했습니다.")

        end_time = time.perf_counter()
        
        ttft = first_token_time - start_time if first_token_time else 0
        total_time = end_time - first_token_time if first_token_time else 0
        tps = token_count / total_time if total_time > 0 else 0
        
        return {
            "success": True,
            "response": full_response,
            "ttft": ttft,
            "tps": tps
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# ==========================================
# 5. 차트 렌더링 함수
# ==========================================
def draw_gauge_chart(achieved_tps, target_tps):
    """Plotly를 사용하여 하드웨어 달성률 게이지 차트를 그립니다."""
    percentage = (achieved_tps / target_tps) * 100 if target_tps > 0 else 0
    percentage = min(percentage, 150) # 최대 150% 까지만 시각화
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = percentage,
        title = {'text': "하드웨어 성능 달성률 (%)", 'font': {'size': 20}},
        number = {'suffix': "%", 'valueformat': ".1f"},
        gauge = {
            'axis': {'range': [None, 150]},
            'bar': {'color': "#1f77b4"},
            'steps': [
                {'range': [0, 50], 'color': "#ffcccb"},
                {'range': [50, 90], 'color': "#ffffcc"},
                {'range': [90, 150], 'color': "#ccffcc"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 100
            }
        }
    ))
    
    fig.update_layout(height=400, margin=dict(l=20, r=20, t=50, b=20))
    return fig

# ==========================================
# 6. UI 및 앱 메인 로직
# ==========================================
st.title("🚀 로컬 LLM 하드웨어 벤치마크 및 진단")
st.markdown("Ollama 및 LM Studio에 설치된 모델을 감지하고 내 PC의 성능(TPS)을 글로벌 기준과 비교합니다.")

tab1, tab2, tab3 = st.tabs(["🚀 내 하드웨어 진단", "🏆 글로벌 리더보드", "📊 벤치마크 이력"])

with tab1:
    st.subheader("진단 환경 설정")
    
    # 타겟 IP 입력 추가
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
        # 모델 정보 텍스트 구성 (파라미터 수 표기)
        model_options = {}
        for m in available_models:
            param_text = f"{m['params']}B" if m['params'] > 0 else "Unknown"
            display_name = f"[{m['source']}] {m['name']} (Params: {param_text})"
            model_options[display_name] = m
            
        selected_option = st.selectbox("진단할 모델을 선택하세요:", list(model_options.keys()))
        selected_model_info = model_options[selected_option]
        
        # 프롬프트 선택 UI
        prompt_category = st.selectbox("벤치마크 프롬프트 유형", list(PROMPT_TEMPLATES.keys()) + ["✏️ 직접 입력"])
        if prompt_category == "✏️ 직접 입력":
            prompt_text = st.text_area("벤치마크에 사용할 프롬프트를 직접 입력하세요:", height=100)
        else:
            prompt_text = PROMPT_TEMPLATES[prompt_category]
            st.info(f"**프롬프트 내용:**\n{prompt_text}")
        
        if st.button("벤치마크 시작", type="primary"):
            if not prompt_text.strip():
                st.error("프롬프트를 입력해주세요.")
            else:
                progress_placeholder = st.empty()
                with st.spinner("벤치마크를 진행 중입니다. 잠시만 기다려주세요..."):
                    result = benchmark_model(selected_model_info, target_ip, prompt_text, progress_placeholder)
                
            progress_placeholder.empty()
                
            if result["success"]:
                st.success("벤치마크가 완료되었습니다!")
                
                # 결과 지표 표시
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("TTFT (첫 응답 시간)", f"{result['ttft']:.2f} s")
                col2.metric("측정된 TPS (초당 토큰)", f"{result['tps']:.1f} tokens/s")
                
                target_tps = get_baseline_tps(selected_model_info)
                col3.metric("기준 TPS (Baseline)", f"{target_tps:.1f} tokens/s")
                
                # 벤치마크 이력 자동 저장
                save_benchmark_history(selected_model_info, prompt_category, result, target_tps)
                
                # 하드웨어 측정값 (요구 VRAM) 표시
                params = selected_model_info.get("params", 0)
                expected_vram = (params * 0.7) + 1.0 if params > 0 else 0
                vram_text = f"{expected_vram:.1f} GB" if expected_vram > 0 else "알 수 없음"
                col4.metric("최소 요구 VRAM (4-bit)", vram_text)
                
                st.markdown("---")
                
                st.subheader("성능 달성률 진단")
                fig = draw_gauge_chart(result['tps'], target_tps)
                st.plotly_chart(fig, width='stretch')
            else:
                st.error(f"🚨 **벤치마크 실패!**\n\n모델 서버와의 통신 중 오류가 발생했습니다.\n\n**상세 오류:** `{result['error']}`")
                st.toast("벤치마크에 실패했습니다. 서버 상태를 확인해주세요.", icon="🚨")

with tab2:
    st.subheader("🏆 글로벌 리더보드 (Hugging Face Open LLM Leaderboard 실시간 데이터)")
    st.markdown("현재 Hugging Face 데이터셋 서버에서 가져온 상위 100개 모델의 원본 데이터입니다. 필터를 이용해 원하는 카테고리와 양자화 수준별 추정 VRAM/TPS를 확인하세요.")
    
    # 필터 UI
    search_query = st.text_input("🔍 모델명 검색 (예: llama, qwen, phi)", placeholder="검색어를 입력하세요...")
    filter_col1, filter_col2 = st.columns(2)
    with filter_col1:
        category = st.selectbox("모델 크기 카테고리", ["전체 보기", "소형 모델 (< 8B)", "중형 모델 (8B ~ 20B)", "대형 모델 (> 20B)"])
    with filter_col2:
        quantization = st.selectbox("양자화 수준 선택", ["4-bit (INT4 / Q4)", "8-bit (INT8 / Q8)", "16-bit (FP16 / BF16)"])
        
    with st.spinner("리더보드 데이터를 가져오는 중입니다..."):
        raw_data = fetch_global_leaderboard()
        
    if raw_data:
        filtered_data = []
        for row in raw_data:
            model_name_str = row["모델명"]
            params = row["파라미터 수 (B)"]
            
            # 검색어 필터링
            if search_query and search_query.lower() not in model_name_str.lower():
                continue
            
            # 카테고리 필터링
            if category == "소형 모델 (< 8B)" and params >= 8: continue
            if category == "중형 모델 (8B ~ 20B)" and (params < 8 or params > 20): continue
            if category == "대형 모델 (> 20B)" and params <= 20: continue
            
            # 양자화 동적 계산
            if "16-bit" in quantization:
                vram = params * 2.0 + 1.0
                tps = 100.0 / params if params > 0 else 0
            elif "8-bit" in quantization:
                vram = params * 1.0 + 1.0
                tps = 150.0 / params if params > 0 else 0
            else: # 4-bit
                vram = params * 0.7 + 1.0
                tps = 200.0 / params if params > 0 else 0
                
            filtered_data.append({
                "모델명": row["모델명"],
                "파라미터 수 (B)": params,
                "평균 점수": row["평균 점수"],
                "요구 VRAM (GB)": round(vram, 1),
                "예상 최고 TPS": round(tps, 1)
            })
            
        df = pd.DataFrame(filtered_data)
        st.dataframe(
            df,
            width='stretch',
            hide_index=True,
            column_config={
                "파라미터 수 (B)": st.column_config.NumberColumn(format="%.1f B"),
                "평균 점수": st.column_config.NumberColumn(format="%.2f"),
                "요구 VRAM (GB)": st.column_config.NumberColumn(format="%.1f GB"),
                "예상 최고 TPS": st.column_config.NumberColumn(format="%.1f tokens/s"),
            }
        )
    else:
        st.warning("리더보드 데이터를 가져오지 못했습니다.")

with tab3:
    st.subheader("📊 벤치마크 이력 및 비교")
    st.markdown("과거에 진행했던 벤치마크 결과들이 자동으로 저장되어 표시됩니다. 모델 간 성능을 비교하거나 하드웨어 변경에 따른 성능 변화를 추적하세요.")
    
    history_data = load_benchmark_history()
    
    if not history_data:
        st.info("아직 저장된 벤치마크 이력이 없습니다. '내 하드웨어 진단' 탭에서 벤치마크를 한 번 실행해 보세요!")
    else:
        df_history = pd.DataFrame(history_data)
        
        # 최신 순으로 정렬
        df_history = df_history.sort_values(by="측정 일시", ascending=False)
        
        st.dataframe(
            df_history,
            width='stretch',
            hide_index=True
        )
        
        st.markdown("---")
        st.subheader("📈 모델별 평균 성능(TPS) 비교")
        
        # 모델별 평균 TPS 계산하여 막대 차트로 시각화
        avg_tps = df_history.groupby("모델명")["TPS"].mean().reset_index()
        avg_tps = avg_tps.sort_values(by="TPS", ascending=True)
        
        fig = go.Figure(go.Bar(
            x=avg_tps["TPS"],
            y=avg_tps["모델명"],
            orientation='h',
            marker=dict(color='#1f77b4')
        ))
        fig.update_layout(
            title="모델별 평균 TPS (초당 토큰 처리량)",
            xaxis_title="TPS",
            yaxis_title="모델",
            height=max(300, len(avg_tps) * 50)
        )
        st.plotly_chart(fig, width='stretch')
        
        # 기록 삭제 버튼
        if st.button("🗑️ 모든 이력 지우기", type="secondary"):
            if os.path.exists(HISTORY_FILE):
                os.remove(HISTORY_FILE)
            st.success("모든 벤치마크 이력이 삭제되었습니다. (새로고침 시 반영됩니다)")
