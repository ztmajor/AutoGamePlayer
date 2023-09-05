import time
import random
from autogameplayer.utils import random_sleep
from autogameplayer.utils.io.mouse_action import doClick, drag
from autogameplayer.utils.io.keyboard_action import keyborad_press
from autogameplayer.utils.log import init_logger


class UnitActionBase(object):
    def __init__(self, log_file='./default.txt') -> None:
        
        self.logger = init_logger(log_file=log_file)

        self.long_wait_seq = ["default"]

    def click_act(
            self, 
            x, 
            y, 
            press_time = 0.1,
            min_wait = 1., 
            max_wait = 2.
        ):
        doClick(int(x), int(y), press_time)

        random_sleep(min_wait, max_wait)

    def seq_click_act(
        self, 
        action_seq, 
        press_time = 0.1, 
        min_short_wait = 1., 
        max_short_wait = 2., 
        min_long_wait = 3., 
        max_long_wait = 5., 
    ):
        for s in action_seq:
            x, y = self.abs_pos_dict[s]

            self.logger.info(f"click {s} at ({x}, {y})")
            doClick(int(x), int(y), press_time)

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
        code_str, 
        min_wait=0.2,
        max_wait=0.5,
    ):
        self.logger.info(f"input {code_str}")
        for s in code_str:
            keyborad_press(s)
            random_sleep(min_wait, max_wait)
        
        random_sleep(min_wait, max_wait)
