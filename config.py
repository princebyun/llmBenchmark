# 서버 통신 설정
OLLAMA_PORT = 11434
LMSTUDIO_PORT = 1234
VLLM_PORT = 8000

# 벤치마크 안전장치 설정
MAX_TOKENS = 1000  # 비정상적으로 긴 출력을 방지하기 위한 최대 토큰 수 제한

# 기본 제공 프롬프트 템플릿 (한국어)
PROMPT_TEMPLATES_KO = {
    "📝 일반 설명 (기본적인 텍스트 생성 속도 벤치마크)": "양자 역학의 불확정성 원리를 고등학생이 이해할 수 있도록 3문단으로 요약하고, 일상생활의 예시를 하나 들어 설명해 줘.",
    "💻 코드 작성 (복잡한 논리 연산 및 코딩 성능 벤치마크)": "파이썬으로 A* 경로 탐색 알고리즘을 구현하고, 주석을 상세히 달아줘. 그리고 간단한 2D 미로 예제도 함께 만들어줘.",
    "🌐 번역 (다국어 처리 및 문맥 이해력 벤치마크)": "다음 한국어 기사를 자연스러운 비즈니스 영어로 번역해 줘: '최근 인공지능 기술의 발전은 기업들의 업무 효율성을 극대화하고 있습니다. 특히 로컬 LLM 환경은 데이터 보안 측면에서 큰 강점을 가집니다.'",
    "🧮 수학/논리 추론 (복잡한 추론 속도 벤치마크)": "피보나치 수열의 첫 20항을 구하는 알고리즘을 반복문, 재귀함수, 동적 프로그래밍 3가지 방식으로 각각 구현하고 시간 복잡도를 비교 분석해 줘.",
    "📚 긴 텍스트 요약 (프롬프트 처리 속도 벤치마크)": "다음 지문을 읽고 핵심 내용 3가지를 요약해 줘: [인공지능의 역사는 1950년대 앨런 튜링의 논문으로부터 시작되었습니다. 그 후 전문가 시스템을 거쳐 딥러닝의 시대로 발전했으며... (중략) ... 최근에는 트랜스포머 아키텍처를 기반으로 한 거대 언어 모델이 상식 수준의 추론 능력까지 보여주고 있습니다.]",
    "⚡ 짧은 응답 (TTFT 반응속도 벤치마크)": "대한민국의 수도는?",
    "🔄 멀티턴 대화 (3턴) (문맥 유지 및 일관성 벤치마크)": "멀티턴 대화 모드입니다." # 실제로는 아래 시나리오 변수를 사용
}

# 기본 제공 프롬프트 템플릿 (영어)
PROMPT_TEMPLATES_EN = {
    "📝 General Explanation (Basic Text Generation)": "Explain the uncertainty principle of quantum mechanics in 3 paragraphs so a high school student can understand it, and give an example from everyday life.",
    "💻 Code Writing (Logic & Coding Performance)": "Implement the A* pathfinding algorithm in Python and add detailed comments. Also, create a simple 2D maze example.",
    "🌐 Translation (Multilingual & Contextual Understanding)": "Translate the following English article into natural business Korean: 'Recent advancements in AI technology are maximizing business efficiency. Especially, local LLM environments have a great advantage in terms of data security.'",
    "🧮 Math/Logic Reasoning (Complex Reasoning)": "Implement an algorithm to find the first 20 terms of the Fibonacci sequence in 3 different ways: iteration, recursion, and dynamic programming. Compare and analyze their time complexities.",
    "📚 Long Text Summarization (Prompt Processing Speed)": "Read the following passage and summarize the 3 main points: [The history of artificial intelligence began with Alan Turing's paper in the 1950s. After passing through expert systems, it developed into the era of deep learning... (omitted) ... Recently, large language models based on the transformer architecture are showing reasoning abilities at the level of common sense.]",
    "⚡ Short Response (TTFT Reaction Speed)": "What is the capital of South Korea?",
    "🔄 Multi-turn Conversation (3 Turns) (Context Maintenance)": "This is multi-turn conversation mode."
}

# 멀티턴 대화 시나리오 (한국어)
MULTI_TURN_SCENARIO_KO = [
    "양자 역학의 불확정성 원리를 설명해 줘.",
    "방금 설명한 원리와 관련된 역사적 실험 3가지를 알려줘.",
    "그 중 가장 유명한 실험의 핵심 아이디어를 3문단으로 정리해 줘."
]

# 멀티턴 대화 시나리오 (영어)
MULTI_TURN_SCENARIO_EN = [
    "Explain the uncertainty principle of quantum mechanics.",
    "Tell me 3 historical experiments related to the principle you just explained.",
    "Summarize the core idea of the most famous experiment among them in 3 paragraphs."
]

def get_prompts(lang):
    if lang == "en":
        return PROMPT_TEMPLATES_EN, MULTI_TURN_SCENARIO_EN
    return PROMPT_TEMPLATES_KO, MULTI_TURN_SCENARIO_KO
