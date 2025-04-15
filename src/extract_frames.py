import os
import subprocess
from datetime import datetime

def extract_frames(video_path, fps=1):
    """
    ffmpeg를 이용해 영상에서 프레임을 추출합니다.
    :param video_path: 비디오 파일 경로
    :param fps: 초당 프레임 수 (기본값 1초에 1프레임)
    """
    # 비디오 파일에서 날짜 추출 (예: 20250226.mp4 -> 20250226)
    video_name = os.path.basename(video_path)
    video_date = video_name.split('.')[0]  # '20250226'

    # 출력 폴더 생성 (비디오 날짜 + "_frames_1s")
    output_folder = f"../data/frames/{video_date}_{fps}"
    os.makedirs(output_folder, exist_ok=True)

    # ffmpeg 명령어 구성
    command = [
        "ffmpeg",  # ffmpeg 명령어
        "-i", video_path,  # 입력 비디오 파일
        "-vf", f"fps={fps}",  # fps 옵션
        f"{output_folder}/frame_%05d.jpg"  # 출력 파일 경로
    ]

    try:
        # ffmpeg 명령어 실행
        subprocess.run(command, check=True)
        print(f"✅ 프레임 추출 완료: {output_folder}")
    except subprocess.CalledProcessError as e:
        print(f"❌ 프레임 추출 실패: {e}")

if __name__ == "__main__":
    video_path = input("🔗 비디오 파일 경로를 입력하세요: ").strip()
    fps = float(input("⏱ 초당 프레임 수를 입력하세요 (예: 1초에 1프레임 -> 1): ").strip())

    # 프레임 추출 함수 실행
    extract_frames(video_path, fps)