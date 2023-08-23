import time
import random
from utils import random_sleep
from utils.mouse_action import doClick
from utils.keyboard_action import keyborad_press
from utils.log import init_logger


class UnitActionBase(object):
    def __init__(self, log_file='./default.txt') -> None:
        
        self.logger = init_logger(log_file=log_file)

        self.long_wait_seq = ["default"]

    def seq_click_act(
        self, 
        action_seq, 
        min_short_wait = 1., 
        max_short_wait = 2., 
        min_long_wait = 3., 
        max_long_wait = 5., 
    ):
        for s in action_seq:
            x, y = self.pos_dict[s]

            self.logger.info(f"click {s} at ({x}, {y})")
            doClick(int(x), int(y))

            if s in self.long_wait_seq:
                random_sleep(min_long_wait, max_long_wait)
            else:
                random_sleep(min_short_wait, max_short_wait)

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
