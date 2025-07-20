import requests
import tkinter as tk
from tkinter import messagebox


def download_music():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'
    }
    url = entry.get()
    try:
        res = requests.get(url, headers=headers)
        messagebox.showinfo("状态码", f"请求状态码: {res.status_code}")
        if res.status_code == 200:
            with open('音乐.mp3', 'wb') as f:
                f.write(res.content)
            messagebox.showinfo("下载完成", "下载成功！")
        else:
            messagebox.showerror("下载失败", f"请求失败，状态码: {res.status_code}")
    except Exception as e:
        messagebox.showerror("错误", f"发生错误: {str(e)}")


# 创建主窗口
root = tk.Tk()
root.title("QQ 音乐下载器")
root.geometry("300x200")

# 创建标签
label = tk.Label(root, text="请输入 QQ 音乐的网址：")
label.pack(pady=10)

# 创建输入框
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# 创建下载按钮
button = tk.Button(root, text="下载", command=download_music)
button.pack(pady=20)

# 运行主循环
root.mainloop()

