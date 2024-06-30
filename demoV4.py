import pyautogui
import time
import pygetwindow as pw
from pywinauto import application
from tkinter import simpledialog, messagebox
import tkinter as tk
import ctypes #用于关机

#在开始的钓鱼次数选项中添加一个boolean选项, 选择是否在完成后睡眠
#一次大概是9.75秒, 考虑最后要不要添加一个超时后, 强制睡眠

#文档
#pyautogui
#https://pyautogui.readthedocs.io/en/latest/search.html?q=locateOnScreen&check_keywords=yes&area=default



def getfish(image_path, button_x, button_y, search_region, try_times, timeout):
    try_time = 0
    while True:
        if try_time >= try_times:
            print("任务完成!!!!")
            break

        pyautogui.moveTo(button_x, button_y, duration=0.3)
        pyautogui.leftClick()

        start_time = time.time()
        while True:
            try:
                #confidence准确率 region识别范围
                pyautogui.locateOnScreen(image_path, confidence=.97, region=search_region)
                pyautogui.moveTo(button_x, button_y, duration=0.1)
                pyautogui.leftClick()
                print("found")
                try_time += 1
                break
            #如果没检测到指定图片那么对直接执行异常里的语句
            except pyautogui.ImageNotFoundException:
                end_time = time.time()
                print(end_time)
                # 超时检测
                if end_time - start_time >= timeout:
                    start_time = time.time()
                    print("超时, 将重新执行")
                    break
                print("没找到, 等待0.2秒")
                time.sleep(0.2)
                # print("not found")

        time.sleep(3.5)

def start(func,  *args, **kwargs):
    # 定义统计时间的函数
    start_time = time.time()  # 记录程序开始时间
    try:
        func(*args, **kwargs)  # 执行传入的函数
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        end_time = time.time()  # 记录程序结束时间
        elapsed_time = end_time - start_time
        #输出总共耗费时长
        print(f"Total elapsed time: {elapsed_time:.2f} seconds")
        #显示每次需要时间
        if isClose:
            # print("close")
            sleepComputer()


def activateWindow():
    # 获取游戏窗口
    game_windows = pw.getWindowsWithTitle('仙境传说RO：新启航')
    if not game_windows:
        print("Window not found!")
    else:
        game_window = game_windows[0]

        # 使用 pywinauto 激活窗口
        app = application.Application().connect(handle=game_window._hWnd)
        window = app.window(handle=game_window._hWnd)

        # 激活窗口
        window.set_focus()

        print(f"Activated window: {game_window.title}")


def sleepComputer():
    # 使系统进入睡眠模式，不强制，不禁用唤醒事件
    ctypes.windll.powrprof.SetSuspendState(False, True, True)

def questionDash():
    pass
def main():
    image_path = "button_green2.png"
    button_x = 2095  # Replace with actual X coordinate
    button_y = 1015  # Replace with actual Y coordinate
    search_region = (2053, 876, 2318, 1133)
    timeout = 5  # 超时时间

    #显示游戏窗口
    activateWindow()


    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    try_times = simpledialog.askinteger("Input", "Please enter the number of fishing attempts:")
    global isClose
    isClose = messagebox.askyesno("Shutdown", "Do you want to shutdown the computer after the script completes?")
    if isClose is None:
        isClose = False
    root.destroy()

    #getfish
    start(getfish, image_path, button_x, button_y, search_region, try_times, timeout)


if __name__ == '__main__':
    main()


#运行脚本, 将游戏画面置顶, 并弹出输入框输入钓鱼次数.✔️

#完成任务后电脑进入睡眠
# import os
#
# # Identify the operating system
# os_name = platform.system()
#
# # Choose the appropriate sleep command based on the OS
# if os_name == "Windows":
#     sleep_command = "rundll32 powercpl.dll,SetSuspendState 0,1,0"
# elif os_name == "Darwin":  # macOS
#     sleep_command = "pmset sleepnow"
# elif os_name == "Linux":  # Linux distributions may vary
#     sleep_command = "sudo pm-suspend"
# else:
#     print("Unsupported operating system:", os_name)
#     exit()
#
# # Execute the sleep command using os.system()
# os.system(sleep_command)