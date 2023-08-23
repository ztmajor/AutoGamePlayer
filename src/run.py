import datetime
import time
import sys
import win32gui, win32con
import numpy
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import pygetwindow
import pyautogui


from utils.screen import getAppScreen
from action.superWorld import SuperWorldAction


# 句柄
FrameClass = "Chrome_WidgetWin_0"
# FrameTitle = "超能世界"
FrameTitle = "腾讯手游助手【标准引擎】"


def daily_routine(engine):
    temp_hour = -1
    while True:

        now_hour = datetime.datetime.now().hour

        # 小时数不同就运行一次
        if temp_hour != now_hour:
            engine.daily_routine()

            # cv2.imwrite("test" + ".jpg", draw)

        temp_hour = now_hour

        time.sleep(60 * 3) # 60 * 5 seconds
        # now_t = time.time()
        # print("用时：", now_t - t)


def solo_push(engine, type="levels"):
    while True:
        if type == "levels":
            engine.break_through_latest_levels()
        elif type == "trial1":
            engine.place_of_trial1()
        elif type == "trial2":
            engine.place_of_trial2()
        elif type == "sea":
            engine.sea()
        else:
            print(f"wrong solo push type {type}")
            break

        
def main():
    engine = SuperWorldAction(log_file='../log/default.txt', 
                              title=FrameTitle)

    mode = input(
        "please select mode. \n"
        "0: daily |"
        "1: shua | "
        "2: levels | "
        "3: trial1 | "
        "4: trial2 | "
        "5: sea | "
        "6: activate_codes | "
        "-1: DEBUG"
        ":\n")    


    if mode == "0":
        engine.daily_routine_first()
    elif mode == "1":
        daily_routine(engine)
    elif mode == "2":
        solo_push(engine, "levels")
    elif mode == "3":
        solo_push(engine, "trial1")
    elif mode == "4":
        solo_push(engine, "trial2")
    elif mode == "5":
        solo_push(engine, "sea")
    elif mode == "6":
        engine.input_activate_codes()
    elif mode == "-1":
        engine.ever_garden(reward=False, playground=False, hole=True)
    else:
        raise NotImplementedError("")
    
    print("done!")


if __name__ == "__main__":
    main()