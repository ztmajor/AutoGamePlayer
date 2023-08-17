import datetime
import time
import sys
import win32gui, win32con
import numpy
import cv2

from utils import random_sleep
from utils.screen import getAppScreen
from AutoGamePlayer.src.action.superWorld import *
from utils.mouse_action import doClick
import AutoGamePlayer.src.utils.log as logg
from PIL import Image

import matplotlib.pyplot as plt


from src.action.superWorld import SuperWorldAction


# 句柄
FrameClass = "Chrome_WidgetWin_0"
FrameTitle = "超能世界"


def main():
    # 获取后台窗口的句柄，注意后台窗口不能最小化(使用SPY++获取类名和窗口标题)
    hwnd = win32gui.FindWindow(FrameClass, FrameTitle)
    if hwnd == 0:
        print("Window not found!")
        exit(-1)
    # cWin = win32gui.FindWindowEx(pWin, 0, "subWin", None)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    win32gui.SetForegroundWindow(hwnd)

    screen, screen_pil = getAppScreen(hwnd)
    superWorld = SuperWorldAction(screen, log_file='/media/my/workspace/fun/AutoGamePlayer/log/default.txt')

    temp_hour = -1
    while True:

        now_hour = datetime.datetime.now().hour

        # 小时数不同就运行一次
        if temp_hour != now_hour:
            superWorld.daily_routine()

            # cv2.imwrite("test" + ".jpg", draw)

        temp_hour = now_hour

        time.sleep(60 * 3) # 60 * 5 seconds
        # now_t = time.time()
        # print("用时：", now_t - t)

        
    print("done!")


if __name__ == "__main__":
    main()