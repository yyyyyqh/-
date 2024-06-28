import pyautogui
import time


image_path = "button_green2.png"
button_x = 2095  # Replace with actual X coordinate
button_y = 1015  # Replace with actual Y coordinate
search_region = (2053, 876, 2318, 1133)
try_time = 0
try_times = 34 #钓鱼次数
timeout = 10 #超时时间

while True:
    if try_time >= try_times:
        print("任务完成!!!!")
        break;

    # time.sleep(0.5)
    pyautogui.moveTo(button_x, button_y, duration=0.3)
    pyautogui.leftClick()


    start_time = time.time()
    while True:
        try:
            button7location = pyautogui.locateOnScreen(image_path, confidence=.97, region=search_region)
            # button7location = pyautogui.locateOnScreen('button_green.png', grayscale=True, confidence=.5)
            if button7location is None:
                #超时检测, 10s
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
        # print(button7location)
        # print("found")


    time.sleep(3.5)



# eg.1. 需要opencv
# try:
#     button7location = pyautogui.locateOnScreen('calc7key.png', grayscale=True, confidence=.8)
#     print("found")
# except pyautogui.ImageNotFoundException:
#     print("not found")
