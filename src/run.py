import datetime
import time
import sys
import win32gui, win32con
import numpy
import cv2

from utils import getAppScreen, random_sleep
from utils.page_actions import *
from utils.mouse_action import doClick
import utils.LogGenerator as logg
from PIL import Image

import matplotlib.pyplot as plt

# 句柄
FrameClass = "Chrome_WidgetWin_0"
FrameTitle = "超能世界"


def main():
    # 日志
    sys.stdout = logg.Logger(str(datetime.date.today()) + ".txt")
    #cv2.namedWindow('screen')

    # PointList = [begin_img, model_img]

    # 获取后台窗口的句柄，注意后台窗口不能最小化(使用SPY++获取类名和窗口标题)
    hwnd = win32gui.FindWindow(FrameClass, FrameTitle)
    if hwnd == 0:
        exit(-1)
    # cWin = win32gui.FindWindowEx(pWin, 0, "subWin", None)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    win32gui.SetForegroundWindow(hwnd)

    t = time.time()
    random_sleep(0.5, 2)  
    screen, screen_pil = getAppScreen(hwnd)

    pos_dict = gen_pos_dict(screen)
    temp_hour = -1

    while True:

        now_hour = datetime.datetime.now().hour

        if temp_hour != now_hour:
            back_to_main_page(pos_dict)
            # 拿奖励
            receive_hook_rewards(pos_dict)
            back_to_main_page(pos_dict)
            receive_graden_reward(pos_dict)
            back_to_main_page(pos_dict)

            # 推冒险进度200次
            for _ in range(2):
                pass_latest_levels(screen, pos_dict)
            back_to_main_page(pos_dict)

            # 推试炼之地200次
            for _ in range(2):
                get_into_trial(pos_dict)
            back_to_main_page(pos_dict)

            # cv2.imwrite("test" + ".jpg", draw)

        temp_hour = now_hour

        time.sleep(60 * 3) # 60 * 5 seconds
        # now_t = time.time()
        # print("用时：", now_t - t)

        
    print("done!")



if __name__ == "__main__":
    main()