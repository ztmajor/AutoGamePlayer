import cv2

from src.utils.mouse_action import doClick
from src.utils import random_sleep

from AutoGamePlayer.src.action import UnitActionBase


class SuperWorldAction(UnitActionBase):
    def __init__(self, img) -> None:
        super(SuperWorldAction, self).__init__(img)
        
        self.long_wait_seq = ["fight3", "default"]

    def gen_pos_dict(self, img):
        full_h, full_w, channal = img.shape

        botton_bar_unit_weight = int(full_w / 14)
        botton_bar_height = int(full_h - 50)

        self.pos_dict = {
            "default": (botton_bar_unit_weight * 7,  botton_bar_height), 
            "mainCity": (botton_bar_unit_weight * 1,  botton_bar_height), 
            "everGarden": (botton_bar_unit_weight * 9,  int(botton_bar_height - 400)), 
            "gardenReward": (botton_bar_unit_weight * 13,  int(botton_bar_height - 250)), 
            "野外": (botton_bar_unit_weight * 3,  botton_bar_height),
            "试炼之地": (botton_bar_unit_weight * 3,  int(full_h - 280)), 
            "联盟": (botton_bar_unit_weight * 5,  botton_bar_height), 
            "冒险": (botton_bar_unit_weight * 7,  botton_bar_height), 
            "smallGames": (botton_bar_unit_weight * 9,  botton_bar_height),                 # 比如拯救狗狗啥的
            "hero": (botton_bar_unit_weight * 11,  botton_bar_height), 
            "chat": (botton_bar_unit_weight * 13,  botton_bar_height), 
            "chat": (botton_bar_unit_weight * 13,  botton_bar_height), 
            "fight1": (botton_bar_unit_weight * 7, int(full_h - 180)), 
            "fight2": (botton_bar_unit_weight * 7, int(full_h - 180)), 
            "fight3": (botton_bar_unit_weight * 7, botton_bar_height), 
            "skip": (botton_bar_unit_weight * 13, botton_bar_height),
            "reward": (botton_bar_unit_weight * 13, int(full_h - 180)),
        }

    def back_to_main_page(self):
        """
        返回主城界面  
        """
        point_seq = ["mainCity"]

        self.act(point_seq)
        print("返回主界面！")

    def break_through_latest_levels(self):
        """
        过最新一关
        """
        point_seq = [
            "冒险", 
            "fight1", 
            "fight2", 
            "fight3", 
            "skip", 
            "default"
        ]

        self.act(point_seq, self.long_wait_seq)

    def receive_hook_rewards(pos_dict):
        """
        领取挂机奖励
        """
        point_seq = [
            "冒险", 
            "reward", 
            "default"
        ]

        for s in point_seq:
            x, y = pos_dict[s]

            print(f"click {s} at ({x}, {y})")
            
            doClick(int(x), int(y))
            random_sleep()


    def receive_graden_reward(pos_dict):
        """
        领取挂机奖励
        """
        point_seq = [
            "mainCity", 
            "everGarden", 
            "gardenReward",
            "default"
        ]

        for s in point_seq:
            x, y = pos_dict[s]

            print(f"click {s} at ({x}, {y})")
            
            doClick(int(x), int(y))
            random_sleep()

    def get_into_trial(pos_dict):
        """
        进入试炼之地
        """
        point_seq = [
            "野外", 
            "试炼之地", 
        ]

        for s in point_seq:
            x, y = pos_dict[s]

            print(f"click {s} at ({x}, {y})")
            doClick(int(x), int(y))
            random_sleep()


    def place_of_trial1(pos_dict):
        """
        试炼之地
        未获得skip权限
        """
        point_seq = [ 
            "fight3", 
            "fight3",
            "skip", 
            "default"
        ]

        for s in point_seq:
            x, y = pos_dict[s]

            print(f"click {s} at ({x}, {y})")
            
            doClick(int(x), int(y))

            if s in ["fight3", "default"]:
                random_sleep(2, 3)
            else:
                random_sleep()


    def place_of_trial2(pos_dict):
        """
        试炼之地
        获得skip权限
        """
        point_seq = [ 
            "fight3", 
            "fight3", 
            "default"
        ]

        for s in point_seq:
            x, y = pos_dict[s]

            print(f"click {s} at ({x}, {y})")
            
            doClick(int(x), int(y))

            if s in ["fight3", "default"]:
                random_sleep(2, 3)
            else:
                random_sleep()