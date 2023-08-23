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
        elif type == "activate_codes":
            engine.input_activate_codes()
        else:
            print(f"wrong solo push type {type}")
            break

        
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
    # DEBUG
    # # cv2.imwrite("test" + ".jpg", screen)
    # full_h, full_w, channal = screen.shape

    # # 底部条的横向位置
    # botton_bar_unit_weight = int(full_w / 14)
    # # 底部条的纵向位置
    # botton_bar_height = int(full_h - 50)

    # center = (botton_bar_unit_weight * 7, int(full_h - 180))
    # screen = cv2.circle(screen, center, 5, (0,255,0), 8)
    # # Display the image
    # cv2.imshow("Image", screen)
    
    # # Wait for the user to press a key
    # cv2.waitKey(0)
    
    # # Close all windows
    # cv2.destroyAllWindows()
    # import pdb
    # pdb.set_trace()

    matchingWindows = pygetwindow.getWindowsWithTitle(FrameTitle)
    win = matchingWindows[0]
    win.activate()
    # win.maximize()
    win.moveTo(0, 0)

    # sleep 为了等待activate响应，然后截屏，避免截到其他窗口
    # time.sleep(1)
    # screen = pyautogui.screenshot(region=(win.left, win.top, win.width, win.height))

    engine = SuperWorldAction(screen, 
                              log_file='../log/default.txt', 
                              title=FrameTitle)

    mode = input(
        "please select mode. \n"
        "1: daily, "
        "2: levels, "
        "3: trial1, "
        "4: trial2, "
        "5: sea, "
        "6: activate_codes "
        ":\n")    


    if mode == "1":
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
        solo_push(engine, "activate_codes")
    else:
        raise NotImplementedError("")
    
    print("done!")


if __name__ == "__main__":
    main()