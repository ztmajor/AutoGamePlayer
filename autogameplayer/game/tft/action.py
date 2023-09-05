import os
import cv2
import time
import pygetwindow

from autogameplayer.game.superworld import UnitActionBase
from autogameplayer.utils import random_sleep
from autogameplayer.utils.screenshot_action import get_loc_on_screen, get_all_loc_on_screen

class TFTAction(UnitActionBase):
    def __init__(self, log_file, title) -> None:
        """
        parameters:
            
        支持以下功能：
            
            TODO:
            1. 自动买牌（判断牌的内容）
            2. 自动捡道具球
            3. 
            
        """
        super(TFTAction, self).__init__(log_file)
        # get window
        matchingWindows = pygetwindow.getWindowsWithTitle(title)
        if len(matchingWindows) == 0:
            raise Exception('Could not find a window with %s in the title' % (title))
        elif len(matchingWindows) > 1:
            raise Exception(
                'Found multiple windows with %s in the title: %s' % (title, [str(win) for win in matchingWindows])
            )

        screen = matchingWindows[0]
        screen.activate()
        screen.moveTo(0, 0)
        self.screen_rect = (screen.left, screen.top, screen.width, screen.height)
        # sleep 为了等待activate响应，然后截屏，避免截到其他窗口
        time.sleep(1)

        # TODO: 有些东西需要自动判断，有些可以使用固定的位置
        # TODO: 使用应用内的相对位置，而不是电脑屏幕的绝对位置
        self.screen_h = screen.height
        self.screen_w = screen.width


        self.title = title


