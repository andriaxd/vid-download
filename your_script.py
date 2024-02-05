# your_script.py
import os
from pytube import YouTube

def download_video(youtube_link, download_path):
    try:
        yt = YouTube(youtube_link)
        video = yt.streams.get_highest_resolution()
        video.download(download_path)
        print(f"Downloaded: {yt.title}")
        return True, f"Downloaded: {yt.title}"
    except Exception as e:
        error_message = f"Error: {e}"
        print(error_message)
        return False, error_message
