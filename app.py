import streamlit as st
from google import genai

st.set_page_config(page_title="딸을 위한 에세이 멘토", page_icon="📝")

st.title("📝 중1 에세이 숙제 도우미")
st.info("미국 온 지 2달, 정말 대단해! 아빠가 도와줄게. 😊")

# --- 초기 세션 상태 ---
if 'api_key' not in st.session_state:
    st.session_state['api_key'] = ''

# --- 사이드바: API Key ---
with st.sidebar:
    st.header("⚙️ 설정")
    user_key = st.text_input("Gemini API Key", value=st.session_state['api_key'], type="password")
    if user_key:
        st.session_state['api_key'] = user_key
        st.success("API Key 저장됨!")
    st.caption("Google AI Studio에서 API Key를 발급받으세요.")


def call_gemini(prompt_text: str) -> str:
    client = genai.Client(api_key=st.session_state['api_key'])
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt_text
    )
    return response.text


# --- 탭 구성 ---
tab1, tab2, tab3 = st.tabs(["1. 질문 이해하기", "2. 개요 잡기", "3. 문장 다듬기"])

with tab1:
    st.header("선생님이 주신 질문(Prompt)을 적어줘")
    homework_prompt = st.text_area("Homework Prompt:", placeholder="예: Write an essay about a hero in your life.")
    if st.button("분석 시작"):
        if not st.session_state['api_key']:
            st.error("사이드바에 Gemini API Key를 먼저 입력해줘!")
        elif not homework_prompt.strip():
            st.warning("숙제 프롬프트를 입력해줘!")
        else:
            prompt_text = f"""
당신은 중학교 1학년 한국 학생의 영어 에세이 선생님입니다.
학생이 방금 미국에 온 지 2달 된 초보자입니다.
아래 에세이 숙제 질문을 분석해서 한국어로 쉽게 설명해주세요:

1. 이 에세이에서 핵심적으로 다뤄야 할 내용
2. 미국식 에세이 작성의 핵심 팁 (thesis statement 등)
3. 이 주제로 쓸 수 있는 아이디어 3가지

에세이 숙제 질문: "{homework_prompt}"
"""
            with st.spinner("Gemini가 분석 중..."):
                try:
                    st.markdown(call_gemini(prompt_text))
                except Exception as e:
                    st.error(f"오류가 발생했습니다: {e}")

with tab2:
    st.header("에세이의 뼈대 세우기")
    intro = st.text_input("서론 (Intro): 독자의 관심을 끌 만한 문장")
    thesis = st.text_input("주제문 (Thesis): 이 글에서 네가 하고 싶은 말")
    body_ideas = st.text_area("본론 아이디어 (Body): 주제문을 뒷받침할 이유나 예시")

    if st.button("구조 확인"):
        if not st.session_state['api_key']:
            st.error("사이드바에 Gemini API Key를 먼저 입력해줘!")
        elif not thesis.strip():
            st.warning("주제문(Thesis)을 입력해줘!")
        else:
            prompt_text = f"""
당신은 중학교 1학년 한국 학생의 영어 에세이 선생님입니다.
학생이 작성한 에세이 구조를 검토하고 한국어로 피드백을 주세요.

서론: {intro}
주제문: {thesis}
본론 아이디어: {body_ideas}

다음을 포함해서 피드백해주세요:
1. 구조의 좋은 점
2. 개선할 부분
3. 더 강력한 thesis statement 예시 1개
"""
            with st.spinner("Gemini가 검토 중..."):
                try:
                    st.markdown(call_gemini(prompt_text))
                except Exception as e:
                    st.error(f"오류가 발생했습니다: {e}")

with tab3:
    st.header("영어로 멋지게 바꾸기")
    korean_text = st.text_area("한국어로 생각한 내용을 적어봐:")
    user_english = st.text_area("(선택) 영어로 써본 내용이 있으면 적어봐:")

    if st.button("에세이 표현으로 변환"):
        if not st.session_state['api_key']:
            st.error("사이드바에 Gemini API Key를 먼저 입력해줘!")
        elif not korean_text.strip():
            st.warning("한국어 내용을 입력해줘!")
        else:
            prompt_text = f"""
당신은 중학교 1학년 한국 학생의 영어 에세이 선생님입니다.
학생이 방금 미국에 온 지 2달 된 초보자입니다.
아래 내용을 바탕으로 다음을 수행해주세요:

1. **영어 번역**: 한국어 내용을 중학생 수준의 자연스러운 에세이 영어로 번역
2. **Grammar Check**: 학생이 쓴 영어가 있다면 문법 오류 수정
3. **표현 업그레이드**: 더 세련된 에세이 표현으로 개선
4. **핵심 단어**: 관련 어휘 3개 (단어 - 뜻 - 예문)

한국어 내용: "{korean_text}"
학생이 쓴 영어: "{user_english if user_english.strip() else '없음'}"
"""
            with st.spinner("Gemini가 분석 중..."):
                try:
                    st.markdown(call_gemini(prompt_text))
                    st.balloons()
                except Exception as e:
                    st.error(f"오류가 발생했습니다: {e}")
