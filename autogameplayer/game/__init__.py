import time
import random
from typing import List, Tuple

from autogameplayer.utils import random_sleep
from autogameplayer.platform.win.io import doClick, drag, keyborad_press, get_loc_on_screen, get_all_loc_on_screen, get_window
from autogameplayer.utils.log import init_logger


window_info = {
    "Tencent_Mobile_Game_Assistant_TFT": {
        "FrameTitle": "腾讯手游助手(64位)",
    },

    "Tencent_Mobile_Game_Assistant_Superworld": {
        "FrameTitle": "腾讯手游助手【标准引擎】",
        "platform": "app", 
        "skip_right": True, 
        "after1720": True
    },
    
    "superWorld": {
        "FrameTitle": "超能世界",
        "platform": "smallProgram", 
        "skip_right": True, 
        "after1720": False
    }

}


class UnitActionBase(object):
    def __init__(self, log_file='./default.txt') -> None:
        self.logger = init_logger(log_file=log_file)

        self.long_wait_seq = ["default"]

    def click(
        self, 
        position,
        interval: float = 0.1,
        min_wait: float = 0.5, 
        max_wait: float = 1.
    ):
        doClick(int(position[0]), int(position[1]), interval)
        random_sleep(min_wait, max_wait)

    def wait_and_find(self, pic_path, verbose=False):
        while get_loc_on_screen(pic_path, 
                                self.window_rect, confidence=0.9) is None:
            # 判断是否找到对应界面
            if verbose:
                self.logger.info("未找到开始游戏界面")
            random_sleep(10, 15, verbose=verbose)

    def seq_click(
        self, 
        action_seq: List[str], 
        interval: float = 0.1, 
        min_short_wait: float = 0.5, 
        max_short_wait: float = 1., 
        min_long_wait: float = 3., 
        max_long_wait: float = 5., 
    ):
        for s in action_seq:
            x, y = self.str2pos[s]

            self.logger.info(f"click {s} at ({x}, {y})")
            doClick(int(x), int(y), interval)

            if s in self.long_wait_seq:
                random_sleep(min_long_wait, max_long_wait)
            else:
                random_sleep(min_short_wait, max_short_wait)

    def mouse_drag(self, start, end, duration, button='left'):
        """_summary_

        Args:
            start (Tuple[int, int]): drag start point
            end (Tuple[int, int]): drag end point
            duration (int): drag duration
            button (str, optional): left right. Defaults to 'left'.
        """
        self.logger.info(f"Drag from {start} to {end} duraring {duration} with {button} button")
        drag(start, end, duration, button)

    def keyborad_input(
        self, 
        str_input, 
        min_wait=0.2,
        max_wait=0.5,
    ):
        self.logger.info(f"input {str_input}")
        for s in str_input:
            keyborad_press(s, interval=random.uniform(min_wait, max_wait))
        
        random_sleep(min_wait, max_wait)
