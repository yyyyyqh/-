import pyautogui
import time


def getfish(image_path, button_x, button_y, search_region, try_times, timeout):
    try_time = 0
    while True:
        if try_time >= try_times:
            print("任务完成!!!!")
            break;

        pyautogui.moveTo(button_x, button_y, duration=0.3)
        pyautogui.leftClick()

        start_time = time.time()
        while True:
            try:
                button7location = pyautogui.locateOnScreen(image_path, confidence=.97, region=search_region)
                if button7location is None:
                    # 超时检测, 10s
                    if time.time() - start_time >= timeout:
                        start_time = time.time()
                        break
                    time.sleep(0.2)
                else:
                    pyautogui.moveTo(button_x, button_y, duration=0.1)
                    pyautogui.leftClick()
                    print("found")
                    try_time += 1
                    break
            except pyautogui.ImageNotFoundException:
                print("not found")

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
        print(f"Total elapsed time: {elapsed_time:.2f} seconds")





if __name__ == '__main__':
    image_path = "button_green2.png"
    button_x = 2095  # Replace with actual X coordinate
    button_y = 1015  # Replace with actual Y coordinate
    search_region = (2053, 876, 2318, 1133)
    try_time = 0
    try_times = 3  # 钓鱼次数
    timeout = 10  # 超时时间

    start(getfish, image_path, button_x, button_y, search_region, try_times, timeout)


#运行脚本, 将游戏画面置顶, 并弹出输入框输入钓鱼次数.