# 完成任务后电脑进入睡眠
import os
import platform


import ctypes

# 使系统进入睡眠模式，不强制，不禁用唤醒事件
ctypes.windll.powrprof.SetSuspendState(False, True, True)
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