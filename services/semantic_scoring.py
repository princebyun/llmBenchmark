import streamlit as st
import numpy as np

# Lazy Loading the Sentence Transformer Model
@st.cache_resource
def load_semantic_model():
    from sentence_transformers import SentenceTransformer
    # paraphrase-multilingual-MiniLM-L12-v2 is fast and supports Ko/En
    model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    return model

# Golden Answers for Semantic Evaluation
GOLDEN_ANSWERS = {
    # 한국어 프롬프트 매칭 키워드
    "일반 설명": "양자 역학의 불확정성 원리는 미시 세계의 입자, 예를 들어 전자의 위치와 운동량을 동시에 정확히 알 수 없다는 원리입니다. 하이젠베르크가 제안했으며, 관측 행위 자체가 입자 상태에 영향을 주기 때문입니다. 일상생활의 예로, 빠르게 달리는 자동차의 속도계(운동량)를 정확히 찍으려 하면 자동차가 흔들려 위치가 흐리게 찍히고, 반대로 위치를 선명히 찍으려면 셔터스피드를 짧게 해야 해서 현재 속도 측정이 불가능해지는 사진 촬영 현상에 비유할 수 있습니다.",
    "번역": "Recent advancements in artificial intelligence technology are maximizing business efficiency for companies. Especially, local LLM environments have a great advantage in terms of data security.",
    "요약": "1. 인공지능의 역사는 1950년대 앨런 튜링의 연구에서 출발했습니다.\n2. 이후 전문가 시스템을 거치며 인공지능은 딥러닝 시대로 진입했습니다.\n3. 최근에는 트랜스포머 아키텍처 기반의 거대 언어 모델(LLM)이 상식 수준의 추론 능력을 보여주며 크게 발전하고 있습니다.",
    
    # 영어 프롬프트 매칭 키워드
    "General": "The uncertainty principle of quantum mechanics states that the more precisely you know the position of a particle, the less precisely you can know its momentum, and vice versa. Proposed by Heisenberg, this is because the act of measurement itself affects the particle. For an everyday example, imagine trying to take a picture of a fast-moving car. If you use a fast shutter speed to freeze its exact position, you have no idea how fast it was going from the photo. If you use a slow shutter speed to capture the motion blur (momentum), its exact position becomes blurry.",
    "Translation": "최근 인공지능 기술의 발전은 기업들의 업무 효율성을 극대화하고 있습니다. 특히 로컬 LLM 환경은 데이터 보안 측면에서 큰 강점을 가집니다.",
    "Summarization": "1. The history of artificial intelligence started with Alan Turing's paper in the 1950s.\n2. AI progressed through expert systems and eventually evolved into the era of deep learning.\n3. Recently, large language models based on transformer architecture are demonstrating common-sense reasoning abilities."
}

def compute_semantic_similarity(prompt_category, response_text):
    """
    Sentence-Transformers 기반 문맥 유사도 측정.
    정답(Golden Answer)과 생성된 응답의 Cosine Similarity를 계산.
    반환: 0 ~ 50점 사이의 점수 (기존 accuracy 50점 만점을 대체하기 위함), 실패 시 -1 반환
    """
    if not response_text:
        return 0
        
    # 카테고리에 맞는 정답지 찾기
    golden_text = None
    for key, text in GOLDEN_ANSWERS.items():
        if key in prompt_category:
            golden_text = text
            break
            
    if not golden_text:
        # 매칭되는 정답지가 없으면 (예: 코딩/수학 등), -1 반환하여 키워드 매칭으로 Fallback
        return -1
        
    try:
        model = load_semantic_model()
        
        # 임베딩 생성
        golden_emb = model.encode([golden_text])
        response_emb = model.encode([response_text])
        
        # Cosine Similarity 계산
        from sentence_transformers import util
        cos_sim = util.cos_sim(golden_emb, response_emb).item()  # -1.0 ~ 1.0
        
        # 0점 처리 보정: 0.3 이하: 0점, 0.3 ~ 0.85: 비례 점수, 0.85 이상: 만점(50점) 처리
        score = max(0, (cos_sim - 0.3) / (0.85 - 0.3)) * 50
        return min(50, round(score))
    except Exception as e:
        print(f"Semantic scoring error: {e}")
        return -1
