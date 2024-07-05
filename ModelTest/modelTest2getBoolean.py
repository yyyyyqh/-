from tkinter import simpledialog, messagebox
import os
import tkinter as tk

# 隐藏主窗口
root = tk.Tk()
root.withdraw()

# 获取尝试次数
try_times = simpledialog.askinteger("Input", "Please enter the number of fishing attempts:")

# 获取是否需要关机的布尔值
shutdown = messagebox.askyesno("Shutdown", "Do you want to shutdown the computer after the script completes?")

# 关闭Tkinter根窗口
root.destroy()

# 打印获取到的值用于调试
print(f"Number of attempts: {try_times}")
print(f"Shutdown after completion: {shutdown}")