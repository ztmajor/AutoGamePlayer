import os
import cv2
import time
import pygetwindow

from autogameplayer.game import UnitActionBase
from autogameplayer.utils import random_sleep
from autogameplayer.platform.win.io import get_loc_on_screen, get_all_loc_on_screen, get_window


class TFTAction(UnitActionBase):
    def __init__(self, log_file, title, data_dir=None, platform="app") -> None:
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
        window = get_window(title, maximize=False, moveTo=(0,0), save_path=None)
        
        self.window_rect = (window.left, window.top, window.width, window.height)

        # TODO: 有些东西需要自动判断，有些可以使用固定的位置
        # TODO: 使用应用内的相对位置，而不是电脑屏幕的绝对位置
        self.window_h = window.height
        self.window_w = window.width

        self.title = title
        self.data_dir = data_dir if data_dir is not None else ''
        self.platform = platform

    def template_path(self, subfolder, name):
        return os.path.join(self.data_dir, self.platform, subfolder, f"{name}.png")

    def play_tft(self):
        # == 准备阶段 ==
        # 1.1 点击开始游戏
        self.wait_and_find(self.template_path("normal", "start_game"), verbose=True)

        pos = get_loc_on_screen(self.template_path("normal", "start_game"), 
                                self.window_rect, 
                                confidence=0.9)
        self.click(pos)

        # 1.2 点击接受


        # （1.3 选择城邦）

        # == 下棋阶段 ==
        # 在1-1进行全局解析


        # == 结算阶段 ==


