from openai import OpenAI
import os
from dotenv import load_dotenv

# 1️⃣ 환경변수 로드
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
input_srt = os.getenv("INPUT_SRT")
output_srt = os.getenv("OUTPUT_SRT")

# 2️⃣ OpenAI client 초기화
client = OpenAI(api_key=api_key)

# 3️⃣ SRT 파일 읽기
with open(input_srt, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 4️⃣ 번역 처리
translated_lines = []
for line in lines:
    if line.strip() and not line.strip().isdigit() and '-->' not in line:
        # 한글 자막 라인 → GPT 번역 요청
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a professional translator."},
                {"role": "user", "content": f"다음 문장을 자연스럽게 말투를 반영해서 영어로 번역해줘:\n{line.strip()}"}
            ],
            max_tokens=100
        )
        translated_text = response.choices[0].message.content.strip()
        translated_lines.append(translated_text + '\n')
    else:
        # 번호 / 타임스탬프 라인은 그대로
        translated_lines.append(line)

# 5️⃣ 번역된 SRT 저장
with open(output_srt, 'w', encoding='utf-8') as f:
    f.writelines(translated_lines)

print("번역 완료! 🎉")