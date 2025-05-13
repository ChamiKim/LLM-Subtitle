# 🌍 LLM Subtitle Translator

**LLM Subtitle Translator**는 기존 `.srt` 자막 파일을  
사용자가 원하는 **말투와 스타일**로, **GPT-4 Turbo API**를 이용해  
영어 또는 일본어로 자연스럽게 번역하고, 다시 `.srt`로 저장할 수 있는 **Streamlit 기반 자막 번역 앱**입니다.

> 유튜브 브이로그, 여행, 감성 룩북 영상에 어울리는 해외 구독자용 자막을 손쉽게 만들 수 있어요 ✨

---

## 🧠 주요 기능

| 기능 | 설명 |
|------|------|
| 📂 SRT 자막 업로드 | 기존 한글 자막 파일을 업로드 |
| ✍️ 말투/톤 직접 입력 | "짧고 귀엽게", "정중하게", "직역 중심" 등 원하는 스타일 자유롭게 입력 |
| 🌐 번역 언어 선택 | 영어 / 일본어 |
| 🤖 GPT-4 Turbo로 번역 | 스타일과 언어에 맞게 자연스러운 번역 수행 |
| 💾 `.srt`로 저장 | 번역 결과를 자막 파일로 저장 가능 |

---

## 🚀 실행 방법

### 1. 환경 세팅

```bash
conda create -n monu python=3.10
conda activate monu
pip install -r requirements.txt

또는 직접 설치:

pip install streamlit openai python-dotenv


⸻

2. .env 파일 생성

루트 디렉토리에 .env 파일을 만들고, OpenAI API 키를 아래와 같이 입력하세요:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

.env 파일은 Git에 커밋되지 않도록 .gitignore에 반드시 포함해야 합니다:

.env


⸻

3. Streamlit 앱 실행

streamlit run translate_app.py

실행 후 브라우저에서 자동으로 앱이 열립니다:
http://localhost:8501

⸻

✨ 스타일 입력 가이드

말투나 번역 스타일은 사용자가 직접 자유롭게 작성할 수 있습니다. 아래는 입력 예시입니다:

유튜브 브이로그에 어울리는 짧고 감성적인 말투로 번역해주세요.  
감탄사나 말 끝 흐림 표현을 살려주세요.  
명령문과 구어체 표현을 자연스럽게 사용해주세요.

변환 예시

원문 자막	영어 번역	일본어 번역
으아 태닝키티 못 참지ㅠㅠ	Ahh I can’t resist this tanned Kitty 😭	うわぁ〜日焼けキティ、我慢できない〜ㅠㅠ


⸻

📁 프로젝트 구조

monu/
├── data/
│   └── srt/               # 원본 및 번역된 자막 저장 폴더
│
├── translate.py       # 🧠 Streamlit 기반 자막 번역 앱
├── .env                   # OpenAI API 키 (비공개)
├── .gitignore             # 환경 설정 제외
├── requirements.txt       # 패키지 목록
└── README.md              # 프로젝트 설명서


⸻

📌 향후 개선 예정
	•	.vtt, .txt 자막 포맷 추가 지원
	•	자주 사용하는 스타일 프리셋 제공
	•	자막 번역 전/후 미리보기 및 비교 기능
	•	음성 인식 + 자막 자동 생성 기능 연동 (선택 사항)

⸻

🧡 Credits
	•	유튜브 채널 monu.monu_3
	•	OpenAI GPT-4 Turbo
	•	Streamlit, Python, dotenv

⸻

📄 License

MIT License

---

필요하다면 이 README와 함께 사용할 `requirements.txt`도 바로 만들어드릴 수 있어요!