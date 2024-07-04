import pyautogui
import time
import pygetwindow as pw
from pywinauto import application
# from tkinter import simpledialog, messagebox
# import tkinter as tk
import ctypes #用于关机
import pytesseract
import winsound

#需要安装tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def getfish(image_path, button_x, button_y, search_region, try_times, timeout):
    try_time = 0
    while True:
        if try_time >= try_times:
            print("任务完成!!!!")
            break

        pyautogui.moveTo(button_x, button_y, duration=0.3)
        pyautogui.leftClick()

        global start_time
        start_time = time.time()
        while True:
            try:
                #confidence准确率 region识别范围
                pyautogui.locateOnScreen(image_path, confidence=.97, region=search_region)
                pyautogui.moveTo(button_x, button_y, duration=0.1)
                #失败率较高
                # pyautogui.moveTo(button_x, button_y, duration=0.01)
                pyautogui.leftClick()
                print("found")
                try_time += 1
                break
            #没检测到, 执行
            #在异常增加太多代码会影响主句的判断, 导致无法收杆.
            except pyautogui.ImageNotFoundException:
                #如果不进行超时检测的话, 主要看设备的稳定性, 正常来说400次钓鱼能够顺利完成. 但有很多额外因素比如网络卡顿, 鼠标移动, 光圈收缩过快导致钓鱼中断.
                pass

                # if time.time() - start_time >= timeout:
                #     start_time = time.time()
                #     break

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

        #响铃
        # makeAlarm()

        #执行睡眠
        # if isClose:
        #     sleepComputer()

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


def getTrytimes():
    left = 331
    top = 163
    width = 56
    height = 29

    # 截取屏幕指定区域
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    # screenshot.show()  # 显示截取的区域图像

    # 识别数字
    text = pytesseract.image_to_string(screenshot, config='--psm 6 digits')
    text = text[:4]

    print("识别到的数字:", text)

    return int(text.strip())

def makeAlarm():
    count = 0
    while count < 10:
        winsound.Beep(1000, 300)


def main():
    image_path = "button_green2.png"
    button_x = 2095  # Replace with actual X coordinate
    button_y = 1015  # Replace with actual Y coordinate
    search_region = (2053, 876, 2318, 1133)
    timeout = 5  # 超时时间

    #显示游戏窗口
    activateWindow()

    #
    try_times = getTrytimes() // 10
    print("次数为:"+str(try_times))
    if not try_times:
        try_times = 400

    #getfish
    start(getfish, image_path, button_x, button_y, search_region, try_times, timeout)


if __name__ == '__main__':
    main()


#运行脚本, 将游戏画面置顶, 并弹出输入框输入钓鱼次数.✔️

#完成任务后电脑进入睡眠✔️

#自动识别可钓鱼次数✔️

#完成后响铃✔️