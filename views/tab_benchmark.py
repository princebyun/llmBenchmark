import streamlit as st
import pandas as pd
from config import get_prompts, OLLAMA_PORT, LMSTUDIO_PORT, VLLM_PORT
from components.client_engine import benchmark_engine
from services.scoring import get_baseline_tps
from services.history import save_benchmark_history
from services.semantic_scoring import compute_semantic_similarity
from components.charts import draw_gauge_chart, draw_radar_chart, draw_multiturn_line_chart
from locales import get_text

def t(key):
    return get_text(st.session_state.lang, key)

def evaluate_quality(prompt_category, response_text):
    if not response_text:
        return 0, 0, 0
        
    accuracy = 0
    quality = 0
    completeness = 0
    
    response_lower = response_text.lower()
    
    # 1. Accuracy (50 pts) - 카테고리별 정밀 검사
    
    # [추가] Sentence-Transformer를 이용한 문맥 유사도 측정 시도
    # -1이 반환되면 정답지가 없거나 에러인 경우이므로 기존 키워드 매칭으로 Fallback
    semantic_score = compute_semantic_similarity(prompt_category, response_text)
    
    if semantic_score != -1:
        # 일반 설명, 번역, 요약 등 정답지가 있는 카테고리는 의미론적 유사도 점수를 그대로 사용
        accuracy = semantic_score
    else:
        # 코딩, 수학, 짧은 응답 등 정답지가 없거나 가변적인 카테고리는 기존 키워드 매칭 사용
        if "일반 설명" in prompt_category or "General" in prompt_category:
            paras = len([p for p in response_text.split("\n\n") if len(p.strip()) > 10])
            if paras >= 2: accuracy += 25
            if "예" in response_text or "example" in response_lower: accuracy += 25
            
        elif "코드" in prompt_category or "Code" in prompt_category:
            if "```" in response_text: accuracy += 10
            if "def " in response_text: accuracy += 15
            if "#" in response_text: accuracy += 10
            if "[" in response_text and "]" in response_text: accuracy += 15
            
        elif "번역" in prompt_category or "Translation" in prompt_category:
            if "efficiency" in response_lower: accuracy += 20
            if "security" in response_lower: accuracy += 20
            if "local" in response_lower: accuracy += 10
            
        elif "수학" in prompt_category or "Math" in prompt_category:
            if "def " in response_text: accuracy += 10
            if "o(n)" in response_lower: accuracy += 20
            if "o(2^n)" in response_lower or "o(1." in response_lower: accuracy += 20
                
        elif "요약" in prompt_category or "Summarization" in prompt_category:
            if "1." in response_text and "2." in response_text and "3." in response_text: accuracy += 50
            elif "1" in response_text and "2" in response_text and "3" in response_text: accuracy += 30
                
        elif "짧은 응답" in prompt_category or "Short" in prompt_category:
            if "서울" in response_text or "seoul" in response_lower: accuracy += 50
                
        elif "멀티턴" in prompt_category or "Multi-turn" in prompt_category:
            paras = len([p for p in response_text.split("\n\n") if len(p.strip()) > 10])
            if paras >= 2: accuracy += 25
            if "슬릿" in response_text or "slit" in response_lower or "슈뢰딩거" in response_text or "schrodinger" in response_lower: accuracy += 25
        else:
            if len(response_text) > 30: accuracy += 50
        
    # 2. Quality (30 pts)
    # 너무 짧으면 감점 (단답형 제외), 너무 길면 감점
    words = len(response_text.split())
    if "짧은 응답" in prompt_category or "Short" in prompt_category:
        if words <= 15: quality += 30
        else: quality += 10
    else:
        if words >= 30: quality += 10
        if words >= 60: quality += 10
        if words <= 800: quality += 10
        
    # 3. Completeness (20 pts)
    # 문장 종결 및 회피성 멘트 검사
    if response_text.strip()[-1] in [".", "!", "?", "요", "다", "함", "음", ">", "`"]:
        completeness += 10
        
    refusals = ["as an ai", "i cannot", "죄송합니다", "할 수 없습니다", "i'm sorry", "언어 모델로서", "i don't have"]
    if not any(r in response_lower for r in refusals):
        completeness += 10
        
    return accuracy, quality, completeness

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
        
        **3. vLLM / oMLX의 경우:**
        - 서버 실행 명령어 뒤에 `--cors-allowed-origins "*"` 옵션을 추가하여 터미널에서 구동
        """ if st.session_state.lang == "ko" else """
        This benchmark relies on **your web browser communicating directly with your local PC**, not the Oracle server.
        Therefore, firewall port forwarding is not required, but you must allow **CORS (Cross-Origin Resource Sharing)** due to browser security policies.
        
        **1. For Ollama:**
        - **Windows:** Edit System Environment Variables, add `OLLAMA_ORIGINS` with value `*`, then restart Ollama.
        - **Mac/Linux:** In terminal, run `export OLLAMA_ORIGINS="*"` and then `ollama serve`.
        
        **2. For LM Studio:**
        - Enable `Cross-Origin-Resource-Sharing (CORS)` toggle in Developer Options (Local Server tab).
        
        **3. For vLLM / oMLX:**
        - Add the `--cors-allowed-origins "*"` flag to your server start command in the terminal.
        """)
        
    st.markdown("---")
    st.subheader("⚙️ 벤치마크 순위 가중치 설정")
    
    bench_mode = st.radio("순위 산출 방식 선택", ["기본 모드 (자동 가중치 적용)", "종합 랭킹 모드 (가중치 직접 조절)"], index=0, horizontal=True)
    
    weight_quality = 70
    weight_speed = 30
    
    if bench_mode == "종합 랭킹 모드 (가중치 직접 조절)":
        weight_quality = st.slider("🎯 품질(Score) 가중치 % (나머지는 속도 가중치)", min_value=0, max_value=100, value=70, step=10)
        weight_speed = 100 - weight_quality
        
        with st.expander("💡 가중치 조절 가이드 (품질 vs 속도)"):
            st.markdown("""
            **1. 품질(Score) 위주 (예: 품질 90% / 속도 10%)**
            - **장점:** 똑똑하고 논리적인 답변을 하는 모델이 1위를 차지합니다. 챗봇, 블로그 글쓰기, 기획 등 문장력이 중요할 때 추천합니다.
            - **단점:** 속도가 느려도 점수만 높으면 상위권에 랭크되므로, 실시간 대화 시 답답할 수 있습니다.
            
            **2. 속도(Speed) 위주 (예: 품질 10% / 속도 90%)**
            - **장점:** 응답이 즉각적이고 쾌적한 모델이 1위를 차지합니다. 코드 자동완성, 실시간 번역, 단순 요약 등 속도가 생명인 작업에 추천합니다.
            - **단점:** 가끔 오답을 말하거나 문맥을 놓치는 등 퀄리티가 떨어지는 모델이 랭크될 수 있습니다.
            
            **3. 가장 정확하고 공정한 테스트 방법 (기본값: 품질 70% / 속도 30%)**
            - 최신 오픈소스 LLM 생태계에서는 모델 크기에 비해 '응답 품질'이 뛰어난 모델이 가장 가치가 높습니다. 
            - 속도는 하드웨어(PC 스펙)를 올리면 해결되지만, 모델 자체의 지능은 하드웨어로 커버할 수 없기 때문에 **품질에 더 높은 가중치(70%)를 부여**하는 것이 학술적/실무적으로 가장 객관적입니다.
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
            
            # 품질 평가 수행
            acc, qual, comp = evaluate_quality(prompt_category, res.get("response", ""))
            total_quality_score = acc + qual + comp
            
            summary_item = {
                t("col_model"): model_info["name"],
                "품질 점수": total_quality_score,
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
        
        # 종합 점수 계산 (가중치 적용)
        max_tps = display_df[t("col_client_tps")].max() if len(display_df) > 0 else 1
        if max_tps == 0: max_tps = 1
        
        display_df["종합 점수"] = (display_df["품질 점수"] * (weight_quality / 100)) + ((display_df[t("col_client_tps")] / max_tps * 100) * (weight_speed / 100))
        display_df["종합 점수"] = display_df["종합 점수"].round(1)
        
        # 종합 점수 순으로 정렬
        display_df = display_df.sort_values(by="종합 점수", ascending=False)
        
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
