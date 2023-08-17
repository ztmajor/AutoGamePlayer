import time
import random
from utils import random_sleep
from utils.mouse_action import doClick
from utils.log import init_logger


class UnitActionBase(object):
    def __init__(self, img, log_file='./default.txt') -> None:
        
        self.logger = init_logger(log_file=log_file)

        self.gen_pos_dict(img)
        self.long_wait_seq = ["default"]

    def gen_pos_dict(self, img):
        raise NotImplementedError("wait to be coded")

    def seq_click_act(
        self, 
        action_seq, 
        min_short_wait = 0.5, 
        max_short_wait = 1., 
        min_long_wait = 2, 
        max_long_wait = 3, 
    ):
        for s in action_seq:
            x, y = self.pos_dict[s]

            self.logger.info(f"click {s} at ({x}, {y})")
            doClick(int(x), int(y))

            if s in self.long_wait_seq:
                random_sleep(min_long_wait, max_long_wait)
            else:
                random_sleep(min_short_wait, max_short_wait)