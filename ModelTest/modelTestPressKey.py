import time

import keyboard

def on_hotkey():
    print("按下")



keyboard.add_hotkey('win+s', on_hotkey)


while keyboard.wait('win+s'):
    time.sleep(1)
