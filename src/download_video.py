import subprocess
import os
import json

def get_video_info(url: str) -> dict:
    """yt-dlp로 유튜브 영상 metadata 가져오기"""
    command = ["yt-dlp", "--print-json", "--skip-download", url]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.returncode != 0:
        raise Exception("❌ 영상 정보를 가져오지 못했습니다.")
    
    return json.loads(result.stdout)

def download_youtube_video(url: str):
    try:
        info = get_video_info(url)
        upload_date = info.get("upload_date", "unknown")  # 예: '20240408'
        # title = info.get("title", "video").replace(" ", "_").replace("/", "_")  # 안전한 파일명 처리

        filename = f"{upload_date}.mp4"
        output_path = f"data/raw/{filename}"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        print(f"📥 유튜브 영상 다운로드 중...: {url}")
        command = [
            "yt-dlp",
            "-f", "bestvideo+bestaudio",
            "--merge-output-format", "mp4",
            url,
            "-o", output_path
        ]

        subprocess.run(command, check=True)
        print(f"✅ 다운로드 완료: {output_path}")

    except Exception as e:
        print(f"❌ 다운로드 실패: {e}")

if __name__ == "__main__":
    url = input("🔗 다운로드할 유튜브 영상 URL을 입력하세요: ").strip()
    
    if url:
        download_youtube_video(url)
    else:
        print("⚠️ URL이 입력되지 않았습니다.")