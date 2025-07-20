import requests
import tkinter as tk
from tkinter import messagebox
from moviepy import VideoFileClip, AudioFileClip


def download_and_merge():
    video_url = video_entry.get()
    audio_url = audio_entry.get()

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
        'referer': 'https://www.bilibili.com/video/BV1oDfwYXEx7/?spm_id_from=333.1007.tianma.2-1-3.click&vd_source=4b343812c2b3abadd32bb4671558a27a'
    }

    try:
        # 下载视频
        video_res = requests.get(video_url, headers=headers)
        with open("视频.mp4", "wb") as f:
            f.write(video_res.content)

        # 下载音频
        audio_res = requests.get(audio_url, headers=headers)
        with open("音频.mp3", "wb") as f:
            f.write(audio_res.content)

        # 合成最终完整视频
        video = VideoFileClip("视频.mp4")
        audio = AudioFileClip("音频.mp3")
        final_video = video.with_audio(audio)
        final_video.write_videofile("完整视频.mp4")

        messagebox.showinfo("提示", "下载完成")
    except Exception as e:
        messagebox.showerror("错误", f"下载过程中出现错误: {e}")


def paste(event):
    widget = event.widget
    widget.event_generate("<<Paste>>")
    return "break"


# 创建主窗口
root = tk.Tk()
root.title("哔哩哔哩")
root.config(width=60,height=90,bg="grey")
# 创建视频 URL 输入框
video_label = tk.Label(root, text="请输入哔哩哔哩上的视频 URL 网址:")
video_label.pack(pady=10)
video_entry = tk.Entry(root)
video_entry.pack(pady=5)
video_entry.bind("<Control-v>", paste)
video_entry.bind("<Control-V>", paste)

# 创建音频 URL 输入框
audio_label = tk.Label(root, text="请输入哔哩哔哩上的音频 URL 网址:")
audio_label.pack(pady=10)
audio_entry = tk.Entry(root)
audio_entry.pack(pady=5)
audio_entry.bind("<Control-v>", paste)
audio_entry.bind("<Control-V>", paste)

# 创建下载按钮
download_button = tk.Button(root, text="开始下载", command=download_and_merge)
download_button.pack(pady=20)

# 运行主循环
root.mainloop()
    