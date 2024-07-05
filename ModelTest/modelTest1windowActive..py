# import pygetwindow as pw
# # from pywinauto import application
#
# # 仙境传说游戏置顶
# game_window = pw.getWindowsWithTitle('仙境传说RO：新启航')[0]
# # app = application.Application().connect(handle=game_window._hWnd)
# # window = app.window(handle=game_window._hWnd)
# game_window.activate()

import pygetwindow as gw
from pywinauto import application

# 获取游戏窗口
game_windows = gw.getWindowsWithTitle('仙境传说RO：新启航')
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