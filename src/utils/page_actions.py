from OutputSimulator import doClick
from utils import random_sleep
import cv2


def gen_pos_dict(img):
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
    
def back_to_main_page(pos_dict):
    point_seq = [
        "main_city",
    ]

    for s in point_seq:
        x, y = pos_dict[s]

        print(f"click {s} at ({x}, {y})")
        doClick(int(x), int(y))
        random_sleep()
    
    print("返回主界面！")


def pass_latest_levels(img, pos_dict):
    """
    过最新一关
    """
    point_seq = [
        "mx", 
        "fight1", 
        "fight2", 
        "fight3", 
        "skip", 
        "default"
    ]

    for s in point_seq:
        x, y = pos_dict[s]

        print(f"click {s} at ({x}, {y})")
        
        doClick(int(x), int(y))

        if s == "fight3":
            random_sleep(2, 3)
        else:
            random_sleep()

    # draw = cv2.circle(img, point_pos, 5, (0,255,0), 8)



def receive_hook_rewards(pos_dict):
    """
    领取挂机奖励
    """
    point_seq = [
        "mx", 
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
        "main_city", 
        "everGarden", 
        "garden_reward",
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
        "yw", 
        "slzd", 
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


