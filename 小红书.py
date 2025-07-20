import requests
import tkinter as tk
from tkinter import simpledialog,messagebox

def on_button_click():
  user_input = simpledialog.askstring("input", "correct URL:", parent=root)
  if not user_input:
        messagebox.showwarning("warn！", "The input cannot be empty")
        return
  url = user_input
  headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"}
  video_res = requests.get(url,headers=headers)
  with open("video.mp4", "wb") as f:
            f.write(video_res.content)

def create_new_window():
    # 创建新窗口（Toplevel窗口）
    new_window = tk.Toplevel(root)
    new_window.geometry("300x200")  
    new_window.resizable(False, False)  

    text_label = tk.Label(
        new_window,
        text="The download was completed successfully!",
        font=("SimHei", 12),  
        fg="#160808",  
        justify="center"  
    )
    text_label.pack(pady=50)  # 放置标签，设置垂直间距


root = tk.Tk()
root.title("rednote video download")  
root.geometry("400x300")  
# 添加标签控件
label = tk.Label(root, text="Welcome to the downloader!", font=("SimHei", 16))
label.pack()  
    
button = tk.Button(
    root,
    text="click to use",
    command=on_button_click,  
    font=("SimHei", 12),
    padx=20,
    pady=10
)
button.pack(expand=True)  # 居中显示按钮

root.mainloop()
