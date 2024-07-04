import pytesseract
import pyautogui
import time

# 设置 Tesseract OCR 的路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 截取屏幕指定区域的函数
def capture_screen_region(left, top, width, height):
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot

# 识别图像中的数字
def recognize_numbers(image):
    # 使用 pytesseract 识别图像中的内容
    text = pytesseract.image_to_string(image, config='--psm 6 digits')

    #取前4位
    text = text[:4]

    return text.strip()

# 示例：截取屏幕指定位置并识别数字
if __name__ == "__main__":

    start_time = time.time()
    # 指定区域的左上角坐标和宽高
    left = 331
    top = 163
    width = 56
    height = 29

    # 截取屏幕指定区域
    image = capture_screen_region(left, top, width, height)
    image.show()  # 显示截取的区域图像

    # 识别数字
    numbers = recognize_numbers(image)
    print("识别到的数字:", numbers)
    if not numbers:
        print("没识别到")
    end_time = time.time()
    print(end_time - start_time)