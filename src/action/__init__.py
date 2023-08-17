import time
import random
from utils import random_sleep
from utils.mouse_action import doClick


class UnitActionBase(object):
    def __init__(self, img) -> None:
        
        self.gen_pos_dict(img)
        

    def gen_pos_dict(self, img):
        raise NotImplementedError("wait to be coded")

    def act(
        self, 
        action_seq, 
        long_wait_seq=None
    ):
        for s in action_seq:
            x, y = self.pos_dict[s]

            print(f"click {s} at ({x}, {y})")
            doClick(int(x), int(y))

            if long_wait_seq is not None and s in long_wait_seq:
                random_sleep(2, 3)
            else:
                random_sleep()