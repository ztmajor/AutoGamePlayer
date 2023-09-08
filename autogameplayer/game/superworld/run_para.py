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


from autogameplayer.platform.win.screen import getAppScreen
# from autogameplayer.game.tft.action import SuperWorldAction


def solo_push(engine, loop=1, solo_task="advanture"):
    while True:
        if solo_task == "advanture":
            engine.adventure_latest(loop=loop)
        elif solo_task == "trial":
            engine.trial(loop=loop, direct=False, skip_right=False)
        elif solo_task == "trial_skip":
            engine.trial(loop=loop, direct=False, skip_right=True)
        elif solo_task == "trial_dark":
            engine.trial(loop=loop, direct=False, skip_right=True, mode='dark')
        elif solo_task == "trial_human":
            engine.trial(loop=loop, direct=False, skip_right=True, mode='human')
        elif solo_task == "trial_orc":
            engine.trial(loop=loop, direct=False, skip_right=True, mode='orc')
        elif solo_task == "trial_spirit":
            engine.trial(loop=loop, direct=False, skip_right=True, mode='spirit')
        elif solo_task == "trial_default":
            engine.trial(loop=loop, direct=False, skip_right=True, mode='default')

        elif solo_task == "sea":
            engine.sea()
        else:
            print(f"wrong solo push type {type}")
            break


def try_trial(engine, loop=10):
    now = datetime.datetime.now()
    weekday = now.weekday()
    weekday_str = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'][weekday]
    print("今天是", weekday_str)
    if weekday in [0, 2, 6]:
        engine.trial(loop=loop, direct=True, skip_right=True, mode='dark', return_main=False)
    if weekday in [1, 3, 6]:
        engine.trial(loop=loop, direct=True, skip_right=True, mode='human', return_main=False)
    if weekday in [2, 4, 6]:
        engine.trial(loop=loop, direct=True, skip_right=True, mode='orc', return_main=False)
    if weekday in [3, 5, 6]:
        engine.trial(loop=loop, direct=True, skip_right=True, mode='spirit', return_main=False)
    engine.trial(loop=loop, direct=True, skip_right=True, mode='default', return_main=False)


        
def main(FrameTitle, platform, skip_right, after1720):
    engine = SuperWorldAction(log_file='../log/default.txt', 
                              title=FrameTitle, 
                              platform=platform)
    now = datetime.datetime.now()
    weekday = now.weekday()
    # weekday_str = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'][weekday]
    # print(now)
    # print(weekday)
    # print(weekday_str)

    mode = 2
    # mode = input(
    #     "please select mode. \n"
    #     "0: DEBUG | "
    #     "1: daily_first | "
    #     "2: daily_routine | "
    #     "3: advanture | "
    #     "4: solo_push | "
    #     "5: trial | "
    #     "6: activate_codes | "
    #     ":\n")    


    if mode == "0":
        # DEBUG
        # engine.daily_routine(weekday, adventrue_loop=2, trail_loop=2, skip_right=True, after1720=True)
        engine.ever_garden(reward=True, playground=False, hole=False)
        # engine.alliance_help()
    elif mode == "1":
        engine.daily_routine_first()
    elif mode == "2":
        engine.daily_routine(weekday, 
                            adventrue_loop=100, 
                            trail_loop=50, 
                            skip_right=skip_right, 
                            after1720=after1720)
    elif mode == "3":
        solo_push(engine, "advanture")
    elif mode == "4":
        solo_task = input("please select solo task (advanture, trial, trial_skip, trial_skip,trial_dark, trial_human, trial_orc, trial_spirit, trial_default, sea):")
        solo_push(engine, solo_task)
    elif mode == "5":
        try_trial(engine, loop=1)
    elif mode == "6":
        engine.input_activate_codes()
    else:
        raise NotImplementedError("")
    
    print("done!")


if __name__ == "__main__":
    # 句柄
    FrameClass = "Chrome_WidgetWin_0"
    # FrameTitle = "超能世界"
    FrameTitle = "腾讯手游助手【标准引擎】"

    config1 = {
        "FrameTitle": "腾讯手游助手【标准引擎】",
        "platform": "app", 
        "skip_right": True, 
        "after1720": True
    }
    config2 = {
        "FrameTitle": "超能世界",
        "platform": "smallProgram", 
        "skip_right": True, 
        "after1720": False
    }

    temp_hour = -10
    while True:
        now = datetime.datetime.now()
        weekday = now.weekday()
        weekday_str = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'][weekday]
        print("今天是", weekday_str)
        now_hour = now.hour
        print(f"现在时间为 {now_hour}, 上一次运行时间为 {temp_hour}, 间隔 {now_hour - temp_hour}")

        if (now_hour - temp_hour) >= 7:
            for cfg in [config1, config2]:
            # for cfg in [config1]:

                main(**cfg)

        temp_hour = now_hour

        time.sleep(60 * 20)
