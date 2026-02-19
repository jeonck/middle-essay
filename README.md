# 📝 중1 에세이 숙제 도우미

미국에 온 지 얼마 안 된 중학교 1학년 학생을 위한 영어 에세이 AI 학습 도우미입니다.
Google Gemini AI를 활용해 단계별로 에세이 작성을 도와줍니다.

---

## 주요 기능

| 탭 | 기능 |
|---|---|
| 1. 질문 이해하기 | 선생님이 준 에세이 주제를 AI가 한국어로 분석 및 아이디어 제공 |
| 2. 개요 잡기 | 서론·주제문·본론 구조 입력 시 AI가 피드백 및 개선안 제시 |
| 3. 문장 다듬기 | 한국어 → 영어 번역, 문법 교정, 표현 업그레이드, 핵심 어휘 추천 |

---

## 설치 및 실행

### 1. 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. Gemini API Key 발급
[Google AI Studio](https://aistudio.google.com/)에서 API Key를 발급받으세요.

### 3. 앱 실행
```bash
streamlit run app.py
```

### 4. API Key 입력
앱 실행 후 왼쪽 사이드바에서 Gemini API Key를 입력합니다.

---

## 기술 스택

- [Streamlit](https://streamlit.io/) — 웹 앱 프레임워크
- [Google Gemini API](https://ai.google.dev/) — AI 모델 (`gemini-3-flash-preview`)
- `google-genai` — Gemini 신버전 Python SDK

---

## 사용 모델

```
gemini-3-flash-preview
```

> Google AI Studio 무료 티어에서 사용 가능한 모델입니다.
