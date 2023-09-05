import datetime
import time
import sys
# import win32gui, win32con
import numpy
import cv2
from PIL import Image
import matplotlib.pyplot as plt
# import pygetwindow
import pyautogui


from autogameplayer.utils.screen import getAppScreen
from autogameplayer.game.tft.action import TFTAction

        
def main(FrameTitle):
    engine = TFTAction(log_file='../log/tft_default.txt', 
                       title=FrameTitle)

    mode = input(
        "please select mode. \n"
        "0: DEBUG | "
        "1: daily_first | "
        ":\n")    


    if mode == "0":
        # DEBUG
        pass

    else:
        raise NotImplementedError("")
    
    print("done!")


if __name__ == "__main__":
    config1 = {
        "FrameTitle": "腾讯手游助手【标准引擎】",       # 句柄
        "platform": "app", 
        "skip_right": True, 
        "after1720": True
    }
    
    for cfg in [config1]:
        main(**cfg)