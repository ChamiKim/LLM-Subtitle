# translate_app.py

import streamlit as st
from io import StringIO, BytesIO
from openai import OpenAI
import os
from dotenv import load_dotenv


# .env 파일 불러오기
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# GPT 클라이언트 초기화
client = OpenAI(api_key=api_key)

# 2️⃣ 번역 스타일 프롬프트 사전
STYLE_PROMPTS = {
    "브이로그 스타일 (짧고 귀엽게)": (
        "You are a subtitle translator for YouTube vlogs. "
        "Translate Korean vlog subtitles into clear, casual, and natural-sounding English. "
        "Keep it short, snappy, and emotionally expressive — like YouTube subtitles.\n"
        "Examples:\n"
        "- 오늘 날씨가 정말 좋아요! → Beautiful day!\n"
        "- 꼭 가봐야 해요! → Must visit!\n"
        "- 너무 귀엽다! → So cute!"
    ),
    "정중한 말투 (설명형)": (
        "Translate the Korean subtitle into polite, formal English suitable for documentaries or interview-style content. "
        "Maintain accuracy and natural flow."
    ),
    "직역 스타일 (의역 최소화)": (
        "Translate as literally as possible. Keep the sentence structure and word choice close to the original Korean, "
        "even if the result sounds awkward in English."
    )
}

# 3️⃣ Streamlit 앱 시작
st.title("🌍 SRT 자막 스타일 번역기")

uploaded_file = st.file_uploader("📂 SRT 파일을 업로드하세요", type=["srt"])
selected_style = st.radio("🎨 원하는 번역 스타일을 선택하세요", list(STYLE_PROMPTS.keys()))

# 4️⃣ 번역 버튼 처리
if uploaded_file and selected_style:
    srt_text = uploaded_file.read().decode("utf-8")
    srt_lines = srt_text.splitlines()
    translated_lines = []

    with st.spinner("🔄 자막 번역 중..."):
        for line in srt_lines:
            if line.strip() and not line.strip().isdigit() and '-->' not in line:
                # 자막 문장만 번역
                prompt = f"{STYLE_PROMPTS[selected_style]}\n\n한국어 문장: {line.strip()}"
                response = client.chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[
                        {"role": "system", "content": "You are a professional subtitle translator for YouTube vlogs. "
                            "Your job is to translate Korean vlog subtitles into clear, casual, and natural-sounding English. "
                            "The translations should feel like something a friendly, cheerful vlogger would say. "
                            "Keep it short, snappy, and emotionally expressive — like something you'd see in YouTube subtitles. "},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=100
                )
                translated_text = response.choices[0].message.content.strip()
                translated_lines.append(translated_text + '\n')
            else:
                # 숫자/타임스탬프는 그대로
                translated_lines.append(line + '\n')

    # 5️⃣ 결과 미리보기
    st.subheader("📄 번역된 SRT 미리보기")
    st.text("".join(translated_lines[:20]))  # 앞부분 20줄만 출력

    # 6️⃣ SRT 다운로드
    translated_srt = "".join(translated_lines)
    srt_bytes = BytesIO(translated_srt.encode("utf-8"))
    st.download_button(
        label="💾 번역된 자막 다운로드 (.srt)",
        data=srt_bytes,
        file_name="translated_subtitles.srt",
        mime="text/plain"
    )