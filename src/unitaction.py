import time
import random
from utils import random_sleep
from utils.mouse_action import doClick


class UnitAction(object):
    def __init__(self, img) -> None:
        
        self.pos_dict = self.build_pos_dict(img)
        

    def build_pos_dict(self, img):
        full_h, full_w, channal = img.shape

        botton_bar_unit_weight = int(full_w / 14)
        botton_bar_height = int(full_h - 50)

        pos_dict = {
            "default": (botton_bar_unit_weight * 7,  botton_bar_height), 
            "main_city": (botton_bar_unit_weight * 1,  botton_bar_height), 
            "everGarden": (botton_bar_unit_weight * 9,  int(botton_bar_height - 400)), 
            "garden_reward": (botton_bar_unit_weight * 13,  int(botton_bar_height - 250)), 
            "yw": (botton_bar_unit_weight * 3,  botton_bar_height), 
            "slzd": (botton_bar_unit_weight * 3,  int(full_h - 280)), 
            "lm": (botton_bar_unit_weight * 5,  botton_bar_height), 
            "mx": (botton_bar_unit_weight * 7,  botton_bar_height), 
            "gg": (botton_bar_unit_weight * 9,  botton_bar_height), 
            "hero": (botton_bar_unit_weight * 11,  botton_bar_height), 
            "chat": (botton_bar_unit_weight * 13,  botton_bar_height), 
            "chat": (botton_bar_unit_weight * 13,  botton_bar_height), 
            "fight1": (botton_bar_unit_weight * 7, int(full_h - 180)), 
            "fight2": (botton_bar_unit_weight * 7, int(full_h - 180)), 
            "fight3": (botton_bar_unit_weight * 7, botton_bar_height), 
            "skip": (botton_bar_unit_weight * 13, botton_bar_height),
            "reward": (botton_bar_unit_weight * 13, int(full_h - 180)),
        }

        return pos_dict


    def act(self, action_seq, long_wait_seq=["default"]):

        for s in action_seq:
            x, y = self.pos_dict[s]

            print(f"click {s} at ({x}, {y})")
            
            doClick(int(x), int(y))

            if s in long_wait_seq:
                random_sleep(2, 3)
            else:
                random_sleep()