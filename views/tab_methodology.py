import streamlit as st

def render():
    if st.session_state.lang == "ko":
        st.title("📚 측정 방법론 및 벤치마크 가이드 (Methodology)")
        st.markdown("""
        본 페이지는 **로컬 LLM 하드웨어 벤치마크** 사이트가 어떠한 환경에서, 어떤 계산 방식을 거쳐 귀하의 PC 하드웨어 성능을 평가하는지 투명하게 공개하는 기술 문서입니다. 
        로컬 AI 환경 구축에 관심이 있는 개발자와 연구자분들을 위한 상세한 가이드라인을 제공합니다.
        """)
        st.divider()

        st.header("📌 1. 벤치마크 개요 및 목적")
        st.markdown("""
        최근 ChatGPT, Claude와 같은 클라우드 기반 거대 언어 모델(LLM)에 의존하는 대신, 보안과 프라이버시, 그리고 지속적인 구독료 부담을 피하기 위해 **개인용 PC나 사내망(On-Premise) 내부에서 오프라인으로 작동하는 '로컬 LLM (Local LLM)'**의 수요가 폭발적으로 증가하고 있습니다.

        하지만 로컬 LLM을 원활하게 구동하기 위해서는 CPU, 시스템 메모리(RAM), 그리고 가장 중요한 **그래픽 카드(GPU)의 VRAM(비디오 메모리)** 등 복합적인 하드웨어 자원이 필요합니다. 
        이 웹앱은 사용자가 Ollama, LM Studio, vLLM, oMLX와 같은 로컬 구동 소프트웨어를 통해 자신의 기기에 설치해둔 다양한 AI 모델(Llama 3, Qwen 2, Gemma 등)을 자동으로 스캔하고, 표준화된 프롬프트를 전송하여 **실제 토큰 생성 속도(TPS)**와 대기 시간(TTFT)을 정밀하게 측정하는 것을 목적으로 합니다.
        이를 통해 사용자는 자신의 하드웨어가 현재 전 세계적인 하이엔드 서버 장비 기준 대비 어느 정도의 퍼포먼스를 내고 있는지 객관적으로 파악할 수 있습니다.
        """)

        st.header("🔧 2. 측정 환경 및 통신 조건")
        st.markdown("""
        벤치마크 테스트는 서버(Python)가 아닌 **사용자의 웹 브라우저(Client-Side Javascript)**에서 직접 수행됩니다.
        웹 브라우저가 사용자 PC의 로컬 LLM 서버(`localhost`)로 직접 REST API를 호출하여 스트리밍(Streaming) 방식으로 프롬프트를 전송하고 응답을 수신합니다.

        - **지원하는 로컬 서버 API:**
          - **Ollama:** `http://127.0.0.1:11434/api/chat` 엔드포인트를 통해 JSON 스트림 형태의 응답을 파싱합니다.
          - **LM Studio / vLLM / oMLX:** `http://127.0.0.1:1234` 등 OpenAI 호환(OpenAI-Compatible) API 규격을 사용하여 SSE (Server-Sent Events) 프로토콜을 분석합니다.
        - **보안 및 CORS 정책:**
          - 브라우저는 기본적으로 다른 도메인으로의 요청을 차단하지만, `http://127.0.0.1` (localhost)는 안전한 루프백 주소로 예외 취급되어 HTTPS 환경에서도 Mixed Content 오류 없이 통신이 가능합니다. (단, Safari 등 일부 브라우저 설정에 따라 다를 수 있음)
          - 로컬 서버(Ollama 등) 측에서 반드시 `OLLAMA_ORIGINS="*"`와 같은 CORS 허용 설정이 되어 있어야 브라우저가 응답을 읽을 수 있습니다.
        - **타임아웃(Timeout) 방어 로직:** 
          - 모델이 VRAM으로 최초 적재(Loading)되는 데 걸리는 콜드 스타트(Cold Start) 지연을 감안하여 초기 응답 대기 시간을 부여합니다.
        """)

        st.header("📐 3. 핵심 측정 지표 (Metrics) 상세 설명")
        st.markdown("""
        앱이 결과를 반환할 때 기록되는 핵심 지표들의 기술적 의미는 다음과 같습니다.

        * **TPS (Tokens Per Second)**
          - **클라이언트 TPS:** 첫 번째 토큰이 도착한 순간부터 마지막 토큰이 도착한 순간까지 걸린 총 시간(Total Time)으로 전체 생성된 토큰 수를 나눈 값입니다. 이는 실제 사용자가 화면에서 글자가 타이핑되는 것을 체감하는 최종적인 속도입니다.
          - **서버 TPS (Prompt Eval & Eval TPS):** Ollama와 같은 엔진이 내부적으로 GPU 연산을 마친 순수한 텍스트 생성 속도입니다. 네트워크 전송 지연(Latency)이 제외된 순수 하드웨어 연산 속도입니다.
        * **TTFT (Time To First Token)**
          - 사용자가 '엔터'를 누른 순간부터 AI가 첫 번째 글자를 내뱉기까지 걸린 시간입니다. 여기에는 모델이 RAM에서 GPU VRAM으로 올라가는 시간(Model Load Duration)과 사용자의 프롬프트를 AI가 이해하는 시간(Prompt Evaluation)이 모두 포함됩니다. TTFT가 2초 이내여야 실제 서비스(챗봇 등)에 투입할 때 사용자가 답답함을 느끼지 않습니다.
        * **달성률 (%)**
          - 측정된 TPS가 해당 모델 파라미터 체급별 글로벌 스탠다드(기준 TPS) 대비 몇 퍼센트의 퍼포먼스를 냈는지를 보여줍니다. 100%에 근접하거나 초과한다면 최상급 GPU 환경임을 의미합니다.
        """)

        st.header("🧮 4. 기준 TPS(Baseline) 산출 수학적 근거")
        st.markdown("""
        글로벌 리더보드와 비교하기 위한 **'기준 TPS'**는 단순히 임의로 정한 것이 아니라, 메모리 대역폭(Memory Bandwidth)과 파라미터 수의 반비례 관계를 응용한 휴리스틱 공식에 의해 산출됩니다.

        현재 본 벤치마크에서는 아래와 같은 동적 기준 공식을 채택하고 있습니다:
        > **기준 TPS = 200.0 / 모델의 파라미터 수(Billion)**

        - **공식의 근거:** 1B(10억 개) 파라미터를 가진 모델을 최고급 워크스테이션 GPU(예: RTX 4090 또는 A100)에서 구동할 때 평균적으로 발생하는 상한치(약 200 TPS)를 기준으로 잡았습니다.
        - **예시 계산:** 
          - **Llama 3 8B (80억 개):** `200.0 / 8 = 25.0 TPS`가 기준값이 됩니다. 즉 내 컴퓨터에서 Llama 3 8B가 초당 25 토큰 이상 나온다면, 글로벌 기준을 충족하는 매우 훌륭한 환경이라는 뜻입니다.
          - **Qwen 2 7B (70억 개):** `200.0 / 7 ≈ 28.5 TPS`가 기준값이 됩니다. 모델이 가벼워질수록 요구되는 기준 TPS 문턱은 높아집니다.
        """)

        st.header("⚙️ 5. 양자화(Quantization) 수준별 VRAM 추정 공식")
        st.markdown("""
        로컬 LLM을 돌릴 때 가장 치명적인 병목 현상(Bottleneck)은 시스템 메모리(RAM)가 아니라 **그래픽카드의 VRAM 용량**입니다. 원본(FP16) 모델은 크기가 너무 커서 양자화(Quantization)라는 압축 기술을 통해 가중치의 소수점 정밀도를 깎아내야 일반 소비자용 PC에 적재할 수 있습니다.

        리더보드 탭에서 제공되는 VRAM 추정치는 아래의 메모리 풋프린트(Memory Footprint) 계산식을 바탕으로 런타임 오버헤드(+1GB) 가산하여 계산됩니다.

        - **16-bit (FP16 / BF16 - 원본/비압축):** 
          - `VRAM(GB) = (파라미터 수 * 2.0) + 1.0`
          - 8B 모델 기준 약 17GB의 거대한 VRAM이 필요합니다. RTX 3090/4090 급의 하이엔드 장비가 요구됩니다.
        - **8-bit (INT8 / Q8 - 고품질 압축):** 
          - `VRAM(GB) = (파라미터 수 * 1.0) + 1.0`
          - 원본 대비 성능 저하가 거의 없으며, 8B 모델 기준 약 9GB의 VRAM을 소모합니다. RTX 3080/4070 급 환경에서 최적입니다.
        - **4-bit (INT4 / Q4 - 대중적인 초고효율 압축):** 
          - `VRAM(GB) = (파라미터 수 * 0.7) + 1.0`
          - 성능 저하를 인간이 거의 체감할 수 없는 수준으로 억제하면서 용량을 절반 이하로 줄이는 마법 같은 포맷(GGUF, AWQ 등)입니다. 8B 모델 기준 약 6.6GB VRAM만 소모하므로, 대중적인 RTX 3060 등 8GB VRAM 그래픽카드에서 가장 널리 쓰이는 표준 셋팅입니다.
        """)

        st.header("🌐 6. 글로벌 리더보드 데이터 출처")
        st.markdown("""
        이 앱의 두 번째 탭인 '글로벌 리더보드'에 표시되는 데이터는 세계 최대의 AI 오픈소스 커뮤니티인 **Hugging Face의 Open LLM Leaderboard** 데이터셋(`open-llm-leaderboard/contents`)에서 실시간 API(REST)를 통해 직접 가져옵니다.

        표기되는 '평균 점수(Average)'는 ARC, HellaSwag, MMLU, TruthfulQA, Winogrande, GSM8K 등 인간의 수능 시험과 유사한 6가지 핵심 벤치마크 테스트 논리력/추론력/수학 점수의 평균값입니다. 점수가 높을수록 모델의 지능이 높다고 볼 수 있습니다. (서버 연결 실패 시 백업된 로컬 데이터를 폴백으로 표기하도록 설계되어 있습니다.)
        """)
    else:
        st.title("📚 Benchmark Methodology Guide")
        st.markdown("""
        This page is a technical document that transparently discloses the environment and calculation methods used by the **Local LLM Hardware Benchmark** site to evaluate your PC's hardware performance. 
        It provides detailed guidelines for developers and researchers interested in building local AI environments.
        """)
        st.divider()

        st.header("📌 1. Benchmark Overview & Purpose")
        st.markdown("""
        Recently, instead of relying on cloud-based Large Language Models (LLMs) like ChatGPT or Claude, the demand for **'Local LLMs' operating offline on personal PCs or internal networks (On-Premise)** has exploded to avoid security, privacy issues, and continuous subscription fees.

        However, running a local LLM smoothly requires complex hardware resources such as CPU, system memory (RAM), and most importantly, **Graphic Card VRAM (Video Memory)**. 
        This web app aims to automatically scan various AI models (Llama 3, Qwen 2, Gemma, etc.) installed on your device via local software like Ollama, LM Studio, vLLM, and oMLX, and send standardized prompts to accurately measure the **actual token generation speed (TPS)** and latency (TTFT).
        This allows users to objectively understand how their hardware performs compared to global high-end server equipment standards.
        """)

        st.header("🔧 2. Measurement Environment & Communication Conditions")
        st.markdown("""
        Benchmark tests are conducted directly in the **user's web browser (Client-Side Javascript)**, not on the server (Python).
        The web browser makes REST API calls directly to the user's PC local LLM server (`localhost`) to send prompts and receive responses via Streaming.

        - **Supported Local Server APIs:**
          - **Ollama:** Parses JSON stream responses via the `http://127.0.0.1:11434/api/chat` endpoint.
          - **LM Studio / vLLM / oMLX:** Analyzes SSE (Server-Sent Events) protocols using the OpenAI-Compatible API standard at `http://127.0.0.1:1234`, etc.
        - **Security & CORS Policy:**
          - Browsers block cross-domain requests by default, but `http://127.0.0.1` (localhost) is treated as an exception as a safe loopback address, enabling communication without Mixed Content errors even in HTTPS environments. (May vary depending on browser settings like Safari)
          - The local server (e.g., Ollama) must have CORS allowed, such as `OLLAMA_ORIGINS="*"`, for the browser to read the response.
        - **Timeout Defense Logic:** 
          - Provides an initial response wait time considering the Cold Start delay required for the model to initially load into VRAM.
        """)

        st.header("📐 3. Key Metrics Detailed Explanation")
        st.markdown("""
        The technical meanings of the key metrics recorded when the app returns results are as follows:

        * **TPS (Tokens Per Second)**
          - **Client TPS:** Total generated tokens divided by the total time taken from when the first token arrived to the last token. This is the final speed the user perceives as text is typed on the screen.
          - **Server TPS (Prompt Eval & Eval TPS):** The pure text generation speed completed internally by engines like Ollama. It's the pure hardware computation speed excluding network transmission latency.
        * **TTFT (Time To First Token)**
          - The time it takes from pressing 'Enter' to when the AI outputs the first character. This includes the Model Load Duration (loading from RAM to GPU VRAM) and Prompt Evaluation (the AI understanding the user's prompt). TTFT should be under 2 seconds for users not to feel frustrated in actual services (like chatbots).
        * **Achievement (%)**
          - Shows what percentage of performance the measured TPS achieved compared to the global standard (Baseline TPS) for that model's parameter class. Approaching or exceeding 100% means a top-tier GPU environment.
        """)

        st.header("🧮 4. Baseline TPS Calculation Mathematical Basis")
        st.markdown("""
        The **'Baseline TPS'** for comparison with the global leaderboard is not simply arbitrarily set, but calculated by a heuristic formula applying the inverse relationship between Memory Bandwidth and Parameter Count.

        This benchmark currently adopts the following dynamic baseline formula:
        > **Baseline TPS = 200.0 / Model's Parameter Count (Billion)**

        - **Basis of the Formula:** Based on the average upper limit (about 200 TPS) occurring when running a 1B (1 billion) parameter model on a top-tier workstation GPU (e.g., RTX 4090 or A100).
        - **Example Calculation:** 
          - **Llama 3 8B (8 billion):** `200.0 / 8 = 25.0 TPS` becomes the baseline. If your computer achieves over 25 tokens per second with Llama 3 8B, it indicates an excellent environment meeting global standards.
          - **Qwen 2 7B (7 billion):** `200.0 / 7 ≈ 28.5 TPS` becomes the baseline. The lighter the model, the higher the required baseline TPS threshold.
        """)

        st.header("⚙️ 5. VRAM Estimation Formula by Quantization Level")
        st.markdown("""
        The most critical bottleneck when running a local LLM is not the system memory (RAM) but the **graphic card's VRAM capacity**. Original (FP16) models are too large, so they must be compressed through a technique called Quantization to reduce the precision of the weights to fit on consumer PCs.

        The VRAM estimates provided in the leaderboard tab are calculated based on the following Memory Footprint formula, adding runtime overhead (+1GB).

        - **16-bit (FP16 / BF16 - Original/Uncompressed):** 
          - `VRAM(GB) = (Parameter Count * 2.0) + 1.0`
          - Requires a massive VRAM of about 17GB for an 8B model. Needs high-end equipment like RTX 3090/4090.
        - **8-bit (INT8 / Q8 - High Quality Compression):** 
          - `VRAM(GB) = (Parameter Count * 1.0) + 1.0`
          - Almost no performance degradation compared to the original, consuming about 9GB VRAM for an 8B model. Optimal in an RTX 3080/4070 environment.
        - **4-bit (INT4 / Q4 - Popular Ultra-High Efficiency Compression):** 
          - `VRAM(GB) = (Parameter Count * 0.7) + 1.0`
          - A magical format (GGUF, AWQ, etc.) that cuts the capacity to less than half while suppressing performance degradation to a level almost imperceptible to humans. Consumes only about 6.6GB VRAM for an 8B model, making it the most widely used standard setting on popular 8GB VRAM graphic cards like RTX 3060.
        """)

        st.header("🌐 6. Global Leaderboard Data Source")
        st.markdown("""
        The data displayed in the second tab 'Global Leaderboard' of this app is directly fetched in real-time via REST API from the **Hugging Face Open LLM Leaderboard** dataset (`open-llm-leaderboard/contents`), the world's largest AI open-source community.

        The displayed 'Average Score' is the average of logical/reasoning/math scores across 6 key benchmark tests similar to human college entrance exams, including ARC, HellaSwag, MMLU, TruthfulQA, Winogrande, and GSM8K. A higher score implies higher model intelligence. (Designed to fallback to backed-up local data if server connection fails.)
        """)
