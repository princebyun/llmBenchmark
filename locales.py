def get_text(lang, key):
    return locales.get(lang, locales["ko"]).get(key, key)

locales = {
    "ko": {
        # app.py
        "seo_description": "내 PC의 하드웨어 사양을 진단하고 로컬 LLM(Ollama, LM Studio 등)의 구동 성능(TPS)을 글로벌 리더보드와 비교해 보는 하드웨어 벤치마크 툴입니다.",
        "app_title": "🚀 로컬 LLM 하드웨어 벤치마크 및 진단",
        "app_desc": "Ollama, LM Studio, vLLM, oMLX 등에 설치된 모델을 감지하고 내 PC의 성능(TPS)을 글로벌 기준과 비교합니다.",
        "sidebar_title": "LLM Benchmark",
        "sidebar_desc": "내 PC 하드웨어의 LLM모델 성능을 확인해보세요",
        "menu_benchmark": "벤치마크 실행",
        "menu_history": "벤치마크 이력",
        "menu_hardware": "PC 하드웨어 진단",
        "menu_leaderboard": "글로벌 리더보드",
        "menu_wiki": "모델 사전",
        "menu_methodology": "측정 방법론",
        "menu_blog": "가이드 & 블로그",
        "menu_about": "서비스 소개",
        "menu_privacy": "개인정보처리방침",
        "menu_contact": "문의하기",
        
        # tab_benchmark.py
        "bench_title": "🚀 로컬 기기 벤치마크 (Client-Side)",
        "bench_info": "현재 접속 중인 브라우저가 실행되고 있는 **사용자님의 PC(localhost)**를 진단합니다.",
        "bench_summary_title": "📊 일괄 벤치마크 요약 결과",
        "col_model": "모델명",
        "col_load": "모델 로딩 (s)",
        "col_prompt_tps": "프롬프트 TPS",
        "col_ttft": "TTFT (s)",
        "col_server_tps": "서버 자체 TPS",
        "col_client_tps": "클라이언트 TPS",
        "col_achieve": "달성률 (%)",
        "col_quality_score": "품질 점수",
        "col_eval_detail": "평가 상세",
        "col_total_score": "총 종합점수",
        "eval_acc": "정확도/문맥",
        "eval_qual": "형식",
        "eval_comp": "완성도",
        "score_formula_info": "ℹ️ **총 종합점수 산출 공식:** `(품질 점수 × {quality}%) + (하드웨어 달성률(%) × {speed}%)`\n\n*총 종합점수는 모델의 품질 점수와 기기의 이론적 스펙 대비 실제 달성률을 반영하여 절대적인 지표로 계산됩니다.*",
        "weight_settings_title": "⚙️ 벤치마크 순위 가중치 설정",
        "weight_mode_select": "순위 산출 방식 선택",
        "weight_mode_default": "기본 모드 (자동 가중치 적용)",
        "weight_mode_custom": "종합 랭킹 모드 (가중치 직접 조절)",
        "weight_slider_label": "🎯 품질(Score) 가중치 % (나머지는 속도 가중치)",
        "weight_guide_title": "💡 가중치 조절 가이드 (품질 vs 속도)",
        "weight_guide_content": """
        **1. 품질(Score) 위주 (예: 품질 90% / 속도 10%)**
        - **장점:** 똑똑하고 논리적인 답변을 하는 모델이 1위를 차지합니다. 챗봇, 블로그 글쓰기, 기획 등 문장력이 중요할 때 추천합니다.
        - **단점:** 속도가 느려도 점수만 높으면 상위권에 랭크되므로, 실시간 대화 시 답답할 수 있습니다.
        
        **2. 속도(Speed) 위주 (예: 품질 10% / 속도 90%)**
        - **장점:** 응답이 즉각적이고 쾌적한 모델이 1위를 차지합니다. 코드 자동완성, 실시간 번역, 단순 요약 등 속도가 생명인 작업에 추천합니다.
        - **단점:** 가끔 오답을 말하거나 문맥을 놓치는 등 퀄리티가 떨어지는 모델이 랭크될 수 있습니다.
        
        **3. 가장 정확하고 공정한 테스트 방법 (기본값: 품질 70% / 속도 30%)**
        - 최신 오픈소스 LLM 생태계에서는 모델 크기에 비해 '응답 품질'이 뛰어난 모델이 가장 가치가 높습니다. 
        - 속도는 하드웨어(PC 스펙)를 올리면 해결되지만, 모델 자체의 지능은 하드웨어로 커버할 수 없기 때문에 **품질에 더 높은 가중치(70%)를 부여**하는 것이 학술적/실무적으로 가장 객관적입니다.
        """,
        "multiturn_detail": "🔄 {model} 멀티턴 상세 분석",
        "single_detail": "🎯 {model} 종합 성능 분석",
        
        # tab_hardware.py
        "hw_title": "⚙️ 진단 환경 설정",
        "hw_desc": "벤치마크를 수행하기 전, 내 PC 사양과 대상 기기의 IP, 테스트할 모델을 설정합니다.",
        "hw_input_title": "#### 1. 내 PC 사양 입력 (선택)",
        "hw_input_desc": "사용 중인 그래픽카드(GPU)를 선택하세요",
        "hw_vram_info": "선택한 GPU의 VRAM은 **{vram}GB** 입니다.",
        "hw_recommended": "**추천 최대 구동 가능 모델:** {models}",
        "hw_cpu_warning": "GPU가 없어 CPU로 구동해야 합니다. 3B 이하 초소형 모델만 추천합니다.",
        
        # tab_history.py
        "hist_title": "📊 벤치마크 이력 및 비교",
        "hist_desc": "과거에 진행했던 벤치마크 결과들이 자동으로 저장되어 표시됩니다. (현재 세션 기반 유지)",
        "hist_empty": "아직 저장된 벤치마크 이력이 없습니다. '내 하드웨어 진단' 탭에서 벤치마크를 한 번 실행해 보세요!",
        "hist_download": "📥 CSV 파일로 내보내기",
        "hist_chart_title": "📈 모델별 평균 성능(TPS) 비교",
        "hist_chart_y": "모델",
        "hist_chart_x": "TPS",
        "hist_clear_btn": "🗑️ 모든 이력 지우기",
        "hist_cleared": "모든 벤치마크 이력이 삭제되었습니다.",
        
        # history columns
        "col_timestamp": "시간",
        "col_model_name": "모델명",
        "col_prompt_cat": "프롬프트 카테고리",
        "col_load_time": "모델 로딩 (s)",
        "col_prompt_tps_hist": "프롬프트 TPS",
        "col_ttft_hist": "TTFT (s)",
        "col_server_tps_hist": "서버 자체 TPS",
        "col_client_tps_hist": "클라이언트 TPS",
        "col_achieve_hist": "달성률 (%)",
        
        # charts.py
        "chart_gauge_title": "하드웨어 성능 달성률 (%)",
        "chart_radar_title": "종합 성능 진단 레이더",
        "chart_radar_cat1": "토큰 생성 속도(TPS)",
        "chart_radar_cat2": "질문 이해 속도(Prompt TPS)",
        "chart_radar_cat3": "초기 응답 지연(TTFT 역수)",
        "chart_radar_cat4": "초기 로딩 속도(역수)",
        "chart_radar_cat5": "하드웨어 달성률",
        "chart_multi_title": "멀티턴 문맥 증가에 따른 속도(TPS) 유지력",
        "chart_multi_x": "대화 턴",
        "chart_multi_y": "초당 토큰 처리량 (TPS)",
        "chart_multi_turn_prefix": "턴",

        # tab_leaderboard.py
        "ld_title": "🏆 글로벌 리더보드 (Hugging Face Open LLM Leaderboard 실시간 데이터)",
        "ld_desc": "현재 Hugging Face 데이터셋 서버에서 가져온 상위 100개 모델의 원본 데이터입니다. 필터를 이용해 원하는 카테고리와 양자화 수준별 추정 VRAM/TPS를 확인하세요.",
        "ld_search_placeholder": "🔍 모델명 검색 (예: llama, qwen, phi)",
        "ld_cat_label": "모델 크기 카테고리",
        "ld_cat_all": "전체 보기",
        "ld_cat_small": "소형 모델 (< 8B)",
        "ld_cat_medium": "중형 모델 (8B ~ 20B)",
        "ld_cat_large": "대형 모델 (> 20B)",
        "ld_quant_label": "양자화 수준 선택",
        "ld_quant_4": "4-bit (INT4 / Q4)",
        "ld_quant_8": "8-bit (INT8 / Q8)",
        "ld_quant_16": "16-bit (FP16 / BF16)",
        "ld_loading": "리더보드 데이터를 가져오는 중입니다...",
        "ld_col_model": "모델명",
        "ld_col_params": "파라미터 수 (B)",
        "ld_col_score": "평균 점수",
        "ld_col_vram": "요구 VRAM (GB)",
        "ld_col_tps": "예상 최고 TPS",
        "ld_error": "리더보드 데이터를 가져오지 못했습니다.",
        
        # tab_model_wiki.py
        "wiki_title": "📚 추천 로컬 LLM 모델 사전",
        "wiki_desc": "사양별로 구동하기 좋은 대표적인 오픈소스 모델들을 소개합니다. (2025년 기준 최신)",
        "wiki_desc_long": "이 페이지에서는 글로벌 리더보드를 장악하고 있는 **세계 최고 수준의 오픈소스 로컬 LLM 40종**에 대한 깊이 있는 정보를 제공합니다.\n**[2026년 6월 최신 업데이트]** Llama 4, Gemma 4, Qwen 3 등 가장 최신 트렌드를 반영한 40개의 거대한 모델 가문(Family)을 소개합니다.\n로컬 환경(내 PC)에 모델을 다운로드하기 전에, 아래 사전을 참고하여 내 PC 사양과 사용 목적에 딱 맞는 모델을 찾아보세요!",
        "wiki_param": "파라미터",
        "wiki_vram": "권장 VRAM (4-bit)",
        "wiki_ctx": "컨텍스트 길이",
        "wiki_lang": "한국어 지원",
        "wiki_yes": "우수",
        "wiki_normal": "보통",
        "wiki_no": "미지원",
        "wiki_feature": "특징",
        "wiki_search": "🔍 모델명 검색 (예: Llama, Gemma, Qwen)",
        "wiki_search_ph": "검색어를 입력하세요...",
        "wiki_prev": "⬅️ 이전 페이지",
        "wiki_page_text": "페이지",
        "wiki_next": "다음 페이지 ➡️",
        "wiki_empty": "검색 결과가 없습니다.",
        "wiki_dev": "개발사",
        "wiki_summary": "요약",
        "wiki_arch": "아키텍처 및 기술적 특징",
        "wiki_proscons": "장단점 분석 (Pros & Cons)",
        "wiki_usecase": "추천 활용 시나리오",
        "wiki_req": "벤치마크 퍼포먼스 및 요구사항",
        "wiki_bottom": "하단",
        
        # tab_methodology.py
        "meth_title": "📊 벤치마크 측정 방법론 안내",
        "meth_desc": "이 벤치마크 툴은 사용자 기기의 실질적인 LLM 구동 성능을 진단하기 위해 개발되었습니다.",
        "meth_metrics_title": "### 1. 주요 평가 지표",
        "meth_metric_1": "**초당 토큰 생성 수 (TPS, Tokens Per Second):**\n- 가장 중요한 성능 지표입니다.\n- 생성된 전체 토큰 수를 프롬프트 처리 이후 텍스트 생성에 걸린 시간으로 나눈 값입니다.\n- **글로벌 기준:** 인간의 평균 읽기 속도는 약 10~15 TPS입니다. 따라서 15 TPS 이상이면 '쾌적한 사용'이 가능한 기준으로 봅니다.",
        "meth_metric_2": "**초기 응답 지연 시간 (TTFT, Time To First Token):**\n- 질문을 던진 후 첫 번째 글자가 화면에 찍히기까지 걸리는 시간입니다.\n- 1~2초 이내가 이상적이며, 5초가 넘어가면 체감 대기 시간이 깁니다.",
        "meth_metric_3": "**프롬프트 처리 속도 (Prompt TPS):**\n- 사용자가 입력한 긴 질문이나 문서를 모델이 이해(인코딩)하는 속도입니다.\n- RAG(검색 증강 생성) 환경에서 긴 문서를 요약할 때 매우 중요합니다.",
        "meth_architecture_title": "### 2. 클라이언트-사이드 (Client-Side) 측정 방식",
        "meth_architecture_desc": "이 툴은 웹 브라우저의 JavaScript 엔진을 통해 **사용자의 로컬 PC(localhost)** 에 띄워진 API 서버(Ollama 등)로 직접 통신합니다.\n- **보안성:** 프롬프트나 결과 데이터가 외부 서버(오라클 클라우드 등)로 전송되지 않습니다.\n- **정확성:** 네트워크 지연(Ping)이 포함되지 않은 순수 기기 성능을 측정합니다.",
        
        # tab_blog.py
        "blog_title": "📘 로컬 LLM 테크 가이드 및 블로그",
        "blog_desc": "로컬 LLM 구축 및 활용에 관한 심도 있는 가이드와 아티클을 제공합니다.",
        "blog_article1_title": "### 📝 로컬 LLM 초보자 구축 가이드 (Ollama 편)",
        "blog_article1_desc": "Ollama는 복잡한 파이썬 환경 설정 없이 명령어 한 줄로 LLM을 실행할 수 있게 해주는 혁신적인 도구입니다...",
        "blog_article2_title": "### 🧠 양자화(Quantization)란 무엇인가?",
        "blog_article2_desc": "16비트(FP16) 모델을 4비트(INT4)로 압축하면 성능 저하 없이 VRAM 사용량을 1/3로 줄일 수 있습니다...",
        "blog_article3_title": "### ⚡ vLLM을 활용한 추론 속도 극대화",
        "blog_article3_desc": "PageAttention 기술을 활용해 서버 환경에서 수십 명의 요청을 동시에 처리하는 vLLM의 구조를 파헤칩니다...",
        
        # tab_about.py, tab_privacy.py, tab_contact.py
        "about_title": "💡 서비스 소개 (About)",
        "about_content": "본 로컬 LLM 하드웨어 벤치마크 툴은 사용자 기기의 실질적인 로컬 AI 구동 성능을 진단하기 위해 개발되었습니다.\n\n개인 PC(Edge Device)에서 구동되는 오픈소스 LLM의 중요성이 대두됨에 따라, 복잡한 파이썬 스크립트 작성 없이도 **브라우저 클릭 한 번으로 내 PC의 추론 성능(TPS)을 객관적으로 측정**할 수 있는 도구를 제공하고자 합니다.",
        
        "privacy_title": "🔒 개인정보처리방침 (Privacy Policy)",
        "privacy_content_1": "### 1. 데이터 처리 원칙\n본 서비스는 **Client-Side 기반 벤치마크**로 설계되었습니다. 귀하가 로컬 LLM에 입력하는 **프롬프트 내용과 생성된 모든 결과물은 외부(당사 서버 포함)로 전송되지 않습니다.**\n모든 추론 작업은 귀하의 브라우저(localhost)와 로컬 통신 포트(예: 11434, 1234) 간에 직접 이루어집니다.",
        "privacy_content_2": "### 2. 수집하는 정보\n본 서비스는 방문자의 통계적 분석(트래픽, 체류 시간 등)을 위해 **구글 애널리틱스(Google Analytics)** 등 익명화된 트래커를 사용하고 있습니다. 개인을 특정할 수 있는 이름, 이메일, IP 주소 등의 민감한 개인정보는 일절 수집하지 않습니다.",
        "privacy_content_3": "### 3. 정보의 보관 및 이용\n벤치마크 이력 데이터는 브라우저 세션(임시 메모리)에만 일시적으로 보관되며, 페이지를 닫거나 새로고침하면 영구적으로 소멸됩니다.",
        
        "contact_title": "📧 문의하기 (Contact)",
        "contact_content": "서비스에 대한 피드백, 버그 리포트, 또는 기타 협업 문의가 있으시다면 아래의 연락처로 이메일을 남겨주세요."
    },
    "en": {
        # app.py
        "seo_description": "A hardware benchmark tool that diagnoses your PC specs and compares the running performance (TPS) of local LLMs (Ollama, LM Studio, etc.) against the global leaderboard.",
        "app_title": "🚀 Local LLM Hardware Benchmark & Diagnostics",
        "app_desc": "Detect models installed in Ollama, LM Studio, vLLM, oMLX, and compare your PC's performance (TPS) with global standards.",
        "sidebar_title": "LLM Benchmark",
        "sidebar_desc": "Check the LLM model performance of your PC hardware",
        "menu_benchmark": "Run Benchmark",
        "menu_history": "Benchmark History",
        "menu_hardware": "Hardware Diagnostics",
        "menu_leaderboard": "Global Leaderboard",
        "menu_wiki": "Model Dictionary",
        "menu_methodology": "Methodology",
        "menu_blog": "Guide & Blog",
        "menu_about": "About",
        "menu_privacy": "Privacy Policy",
        "menu_contact": "Contact",
        
        # tab_benchmark.py
        "bench_title": "🚀 Local Device Benchmark (Client-Side)",
        "bench_info": "We are diagnosing **your PC (localhost)** where the current browser is running.",
        "bench_summary_title": "📊 Batch Benchmark Summary Results",
        "col_model": "Model Name",
        "col_load": "Model Load (s)",
        "col_prompt_tps": "Prompt TPS",
        "col_ttft": "TTFT (s)",
        "col_server_tps": "Server TPS",
        "col_client_tps": "Client TPS",
        "col_achieve": "Achievement (%)",
        "col_quality_score": "Quality Score",
        "col_eval_detail": "Eval Details",
        "col_total_score": "Total Score",
        "eval_acc": "Acc/Context",
        "eval_qual": "Format",
        "eval_comp": "Completeness",
        "score_formula_info": "ℹ️ **Total Score Formula:** `(Quality Score × {quality}%) + (Hardware Achievement(%) × {speed}%)`\n\n*The Total Score is calculated as an absolute metric reflecting the model's quality score and the actual achievement rate compared to the device's theoretical specs.*",
        "weight_settings_title": "⚙️ Benchmark Rank Weight Settings",
        "weight_mode_select": "Select Rank Calculation Mode",
        "weight_mode_default": "Default Mode (Auto Weight)",
        "weight_mode_custom": "Custom Ranking Mode (Adjust Weights)",
        "weight_slider_label": "🎯 Quality(Score) Weight % (Rest is Speed Weight)",
        "weight_guide_title": "💡 Weight Adjustment Guide (Quality vs Speed)",
        "weight_guide_content": """
        **1. Quality-Focused (e.g., Quality 90% / Speed 10%)**
        - **Pros:** Models that provide smart and logical answers rank highest. Recommended when writing quality, like chatbots, blog posts, or planning, is crucial.
        - **Cons:** Even slow models can rank high if their score is good, which might feel sluggish during real-time conversations.
        
        **2. Speed-Focused (e.g., Quality 10% / Speed 90%)**
        - **Pros:** Fast and responsive models rank highest. Recommended for tasks where speed is everything, like code auto-completion, real-time translation, or simple summaries.
        - **Cons:** Models with lower response quality, such as giving wrong answers or missing context, might rank high.
        
        **3. The Most Accurate & Fair Method (Default: Quality 70% / Speed 30%)**
        - In the modern open-source LLM ecosystem, models with outstanding 'response quality' relative to their size hold the most value.
        - Speed can be improved by upgrading hardware, but a model's inherent intelligence cannot. Therefore, **giving a higher weight to quality (70%)** is the most objective approach academically and practically.
        """,
        "multiturn_detail": "🔄 {model} Multi-turn Analysis",
        "single_detail": "🎯 {model} Comprehensive Performance Analysis",
        
        # tab_hardware.py
        "hw_title": "⚙️ Diagnostic Environment Setup",
        "hw_desc": "Before running the benchmark, set up your PC specs, target device IP, and models to test.",
        "hw_input_title": "#### 1. Enter PC Specs (Optional)",
        "hw_input_desc": "Select the graphics card (GPU) you are using",
        "hw_vram_info": "The VRAM of the selected GPU is **{vram}GB**.",
        "hw_recommended": "**Recommended Maximum Runnable Models:** {models}",
        "hw_cpu_warning": "No GPU detected. Must run on CPU. We recommend only micro models under 3B.",
        
        # tab_history.py
        "hist_title": "📊 Benchmark History and Comparison",
        "hist_desc": "Past benchmark results are automatically saved and displayed. (Maintained based on the current session)",
        "hist_empty": "No benchmark history saved yet. Try running a benchmark in the 'Hardware Diagnostics' tab!",
        "hist_download": "📥 Export to CSV File",
        "hist_chart_title": "📈 Average Performance (TPS) Comparison by Model",
        "hist_chart_y": "Model",
        "hist_chart_x": "TPS",
        "hist_clear_btn": "🗑️ Clear All History",
        "hist_cleared": "All benchmark history has been cleared.",
        
        # history columns
        "col_timestamp": "Timestamp",
        "col_model_name": "Model Name",
        "col_prompt_cat": "Prompt Category",
        "col_load_time": "Model Load (s)",
        "col_prompt_tps_hist": "Prompt TPS",
        "col_ttft_hist": "TTFT (s)",
        "col_server_tps_hist": "Server TPS",
        "col_client_tps_hist": "Client TPS",
        "col_achieve_hist": "Achievement (%)",
        
        # charts.py
        "chart_gauge_title": "Hardware Achievement (%)",
        "chart_radar_title": "Comprehensive Performance Radar",
        "chart_radar_cat1": "Token Gen Speed (TPS)",
        "chart_radar_cat2": "Prompt Understanding (Prompt TPS)",
        "chart_radar_cat3": "Initial Delay (1/TTFT)",
        "chart_radar_cat4": "Initial Load Speed (Inverse)",
        "chart_radar_cat5": "Hardware Achievement",
        "chart_multi_title": "Speed (TPS) Maintenance over Multi-turns",
        "chart_multi_x": "Conversation Turn",
        "chart_multi_y": "Tokens per Second (TPS)",
        "chart_multi_turn_prefix": "Turn",
        
        # tab_leaderboard.py
        "ld_title": "🏆 Global Leaderboard (Hugging Face Open LLM Live Data)",
        "ld_desc": "Raw data of top 100 models from Hugging Face. Filter to check estimated VRAM/TPS by size and quantization.",
        "ld_search_placeholder": "🔍 Search model name (e.g. llama, qwen, phi)",
        "ld_cat_label": "Model Size Category",
        "ld_cat_all": "View All",
        "ld_cat_small": "Small Models (< 8B)",
        "ld_cat_medium": "Medium Models (8B ~ 20B)",
        "ld_cat_large": "Large Models (> 20B)",
        "ld_quant_label": "Select Quantization Level",
        "ld_quant_4": "4-bit (INT4 / Q4)",
        "ld_quant_8": "8-bit (INT8 / Q8)",
        "ld_quant_16": "16-bit (FP16 / BF16)",
        "ld_loading": "Fetching leaderboard data...",
        "ld_col_model": "Model Name",
        "ld_col_params": "Parameters (B)",
        "ld_col_score": "Avg Score",
        "ld_col_vram": "Required VRAM (GB)",
        "ld_col_tps": "Estimated Max TPS",
        "ld_error": "Failed to fetch leaderboard data.",
        
        # tab_model_wiki.py
        "wiki_title": "📚 Recommended Local LLM Dictionary",
        "wiki_desc": "Introducing representative open-source models optimized for local hardware specs (As of 2025).",
        "wiki_desc_long": "This page provides in-depth information on the **world's top 40 open-source local LLMs** dominating global leaderboards.\n**[Latest Update: June 2026]** Features the latest trends including Llama 4, Gemma 4, and Qwen 3 families.\nBefore downloading a model to your local PC, consult this dictionary to find the perfect fit for your hardware and use case!",
        "wiki_param": "Parameters",
        "wiki_vram": "Rec. VRAM (4-bit)",
        "wiki_ctx": "Context Length",
        "wiki_lang": "Korean Support",
        "wiki_yes": "Excellent",
        "wiki_normal": "Average",
        "wiki_no": "Not Supported",
        "wiki_feature": "Features",
        "wiki_search": "🔍 Search Model Name (e.g. Llama, Gemma, Qwen)",
        "wiki_search_ph": "Enter search term...",
        "wiki_prev": "⬅️ Previous",
        "wiki_page_text": "Page",
        "wiki_next": "Next ➡️",
        "wiki_empty": "No matching models found.",
        "wiki_dev": "Developer",
        "wiki_summary": "Summary",
        "wiki_arch": "Architecture & Technical Features",
        "wiki_proscons": "Pros & Cons Analysis",
        "wiki_usecase": "Recommended Use Cases",
        "wiki_req": "Benchmark Performance & Requirements",
        "wiki_bottom": "Bottom",
        
        # tab_methodology.py
        "meth_title": "📊 Benchmark Methodology Guide",
        "meth_desc": "This tool is developed to diagnose the practical LLM running performance of your local device.",
        "meth_metrics_title": "### 1. Key Performance Metrics",
        "meth_metric_1": "**Tokens Per Second (TPS):**\n- The most critical performance indicator.\n- Calculated as total generated tokens divided by generation time (excluding prompt processing).\n- **Global Standard:** Average human reading speed is 10~15 TPS. Over 15 TPS provides a comfortable experience.",
        "meth_metric_2": "**Time To First Token (TTFT):**\n- The delay between asking a question and seeing the first character appear.\n- Ideal is under 1~2 seconds; over 5 seconds feels significantly slow.",
        "meth_metric_3": "**Prompt Processing Speed (Prompt TPS):**\n- How fast the model understands (encodes) the user's input prompt.\n- Extremely important for summarizing long documents in RAG environments.",
        "meth_architecture_title": "### 2. Client-Side Measurement Architecture",
        "meth_architecture_desc": "This tool uses your browser's JS engine to communicate directly with **your local PC API server (e.g. Ollama)**.\n- **Security:** Prompts and results are never sent to external servers.\n- **Accuracy:** Measures raw device performance without network latency (Ping) overhead.",
        
        # tab_blog.py
        "blog_title": "📘 Local LLM Tech Guide & Blog",
        "blog_desc": "In-depth guides and articles on building and utilizing local LLMs.",
        "blog_article1_title": "### 📝 Beginner's Guide to Local LLMs (Ollama)",
        "blog_article1_desc": "Ollama is a revolutionary tool that lets you run LLMs with a single command without complex Python setups...",
        "blog_article2_title": "### 🧠 What is Quantization?",
        "blog_article2_desc": "Compressing a 16-bit (FP16) model to 4-bit (INT4) cuts VRAM usage by 1/3 with minimal performance loss...",
        "blog_article3_title": "### ⚡ Maximizing Inference Speed with vLLM",
        "blog_article3_desc": "Explore vLLM's architecture, which leverages PageAttention to handle dozens of concurrent requests...",
        
        # tab_about.py, tab_privacy.py, tab_contact.py
        "about_title": "💡 About the Service",
        "about_content": "This LLM Hardware Benchmark tool was developed to diagnose the practical local AI running performance of user devices.\n\nAs the importance of open-source LLMs running on personal PCs (Edge Devices) grows, we aim to provide a tool that allows you to objectively measure your PC's inference performance (TPS) with a single browser click, without needing to write complex Python scripts.",
        
        "privacy_title": "🔒 Privacy Policy",
        "privacy_content_1": "### 1. Data Processing Principles\nThis service is designed as a **Client-Side based benchmark**. **The prompts you input into the local LLM and all generated results are never transmitted to external servers (including our own).**\nAll inference operations are strictly handled directly between your browser (localhost) and your local communication ports (e.g., 11434, 1234).",
        "privacy_content_2": "### 2. Information Collected\nThis service uses anonymized trackers such as **Google Analytics** for statistical analysis of visitors (traffic, duration of stay, etc.). We do not collect any sensitive personal information that can identify an individual, such as names, emails, or IP addresses.",
        "privacy_content_3": "### 3. Data Storage and Usage\nBenchmark history data is only temporarily stored in the browser session (temporary memory) and is permanently destroyed when you close or refresh the page.",
        
        "contact_title": "📧 Contact",
        "contact_content": "If you have feedback, bug reports, or other collaboration inquiries about the service, please leave an email at the contact below."
    }
}
