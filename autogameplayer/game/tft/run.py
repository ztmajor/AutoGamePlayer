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
from autogameplayer.game.tft.action import TFTAction

        
def main(FrameTitle, log_file, data_dir):
    engine = TFTAction(log_file=log_file, 
                       title=FrameTitle,
                       data_dir=data_dir)

    mode = input(
        "please select mode. \n"
        "0: DEBUG | "
        "1: play | "
        "2: analysis"
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
        "lig_file": "../../log/tft_default.txt",
        "data_dir": r"E:\project\AutoGamePlayer\data\template\tft", 
    }
    
    for cfg in [config1]:
        main(**cfg)