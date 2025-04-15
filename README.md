# LLM-Translation

# 🎞️ Monu Subtitle Pipeline

`monu`는 유튜브 영상 속 **하드 자막(영상에 박힌 한글 자막)**을 추출하고,
**monu.monu_3 스타일**로 영어/일본어로 번역한 후, `.srt` 자막 파일로 자동 저장해주는 파이프라인입니다.

> 브이로그, 여행, 감성 룩북 같은 영상에서 해외 구독자 자막까지 한 번에 처리할 수 있어요 ✨

---

## 🧩 파이프라인 순서

1. 🎬 **유튜브 영상 다운로드** (`yt-dlp`)
2. 🖼️ **영상 → 프레임 이미지 추출** (OpenCV)
3. 🔍 **하드 자막 → 텍스트 추출** (Tesseract OCR)
4. 🌐 **GPT API로 스타일 번역** (영어/일본어, monu 스타일 프롬프트 사용)
5. 📝 **자막 파일 `.srt` 형식으로 저장** (한글/영어/일본어)
6. (선택) **유튜브 자막 업로드**

---

## 📁 폴더 구조

```
monu/
├── data/
│   ├── raw/              # 다운로드한 영상 (video.mp4)
│   ├── frames/           # 프레임 이미지 저장
│   └── srt/              # 생성된 자막 파일 (.srt)
│
├── src/
│   ├── extract_frames.py     # 영상 → 프레임
│   ├── ocr_to_srt.py         # OCR → 자막 추출
│   └── translate.py          # GPT로 스타일 번역
│
├── run_pipeline.py           # 전체 실행 스크립트
├── README.md
└── .gitignore
```

---

## 🚀 실행 방법

### 1. 환경 세팅 (conda 권장)
```bash
conda create -n monu python=3.10
conda activate monu
pip install -r requirements.txt
```

또는 직접 설치:
```bash
pip install opencv-python pytesseract Pillow openai
```

Tesseract 설치도 필요합니다. (한글 언어팩 포함)

---

### 2. 유튜브 영상 다운로드 (예: yt-dlp)
```bash
yt-dlp https://www.youtube.com/watch?v=xxxxx -o data/raw/video.mp4
```

---

### 3. 전체 파이프라인 실행
```bash
python run_pipeline.py
```

---

## ✨ monu 스타일 번역 프롬프트 예시

```text
다음 한국어 자막을 monu.monu_3 채널의 말투처럼 자연스럽고 밝은 영어로 번역해줘.
말 끝 흐림, 감탄사, 친근한 느낌을 살려줘.

예시:
한국어: 으아 태닝키티 못 참지ㅠㅠ
영어: Ahh I can’t resist this tanned Kitty 😭
```

---

## 📦 결과 예시

| 원문 자막 | 영어 번역 | 일본어 번역 |
|-----------|-----------|--------------|
| 으아 태닝키티 못 참지ㅠㅠ | Ahh I can't resist this tanned Kitty 😭 | うわぁ〜日焼けキティ、我慢できない〜ㅠㅠ |

---

## 📌 향후 추가 예정
- [ ] GPT API로 `.srt` 직접 번역 자동화
- [ ] 감정/스타일 태깅 기능
- [ ] GUI 인터페이스 (drag & drop 방식)

---

## 🧡 Credits
- 유튜브 채널 [monu.monu_3](https://www.youtube.com/@monu.monu_3)
- 오픈소스 OCR, OpenAI API 기반

---

## 📄 라이선스
MIT License
