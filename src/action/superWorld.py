import os
import cv2
import time
import pygetwindow

from action import UnitActionBase
from utils import random_sleep
from utils.screenshot_action import get_loc_on_screen

class SuperWorldAction(UnitActionBase):
    def __init__(self, log_file, title, platform="app") -> None:
        """
        parameters:
            platform:
                app
                smallProgram
        这里支持以下功能：
            1. 日常任务： daily_routine
            2. 单刷试炼之地： place_of_trial1 / place_of_trial2 （需要预先进入试炼之地）
            3. 单推最新章节： break_through_latest_levels （需要进入主界面）
            TODO:
            4. 推远古召唤，及其中间不同的洞窟
            5. 推勇者航线最新章节
            6. 15分钟自动竞技场打比自己弱的（如果没有打到3个不刷新）
            7. 英雄升级检测，英雄升级策略，按照顺序
         main_city   8. 联盟自动求助 以及 自动帮点-
            9. 神奇树洞一键探索（+点科技树）
            10. 游乐园自动抽奖
        """
        super(SuperWorldAction, self).__init__(log_file)
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

        
        self.long_wait_seq = ["fight3", "default"]

        # TODO: 有些东西需要自动判断，有些可以使用固定的位置
        # TODO: 使用应用内的相对位置，而不是电脑屏幕的绝对位置
        self.screen_h = screen.height
        self.screen_w = screen.width

        # 顶部/底部条宽高
        self.bar_w = int(self.screen_w)
        self.top_bar_h = 200
        self.botton_bar_h = 100

        self.title = title
        self.platform = platform
        if platform == "app":
            self.init_app()
        elif platform == 'smallProgram':
            self.init_smallProgram()
        else:
            raise NotImplementedError(f"Not implemented platform {platform}")

    def get_pic_path(self, platform, mode, name):
        dir = r"E:\project\AutoGamePlayer\data\template\superWorld"
        return os.path.join(dir, platform, mode, f"{name}.png")

    def init_app(self):
        """
        hard_code of some point
        """
        self.top_bar_h = 200
        self.botton_bar_h = 150

        top_bar_click_h = int(self.top_bar_h/2)
        botton_bar_click_h = int(self.screen_h - (self.botton_bar_h/2))

        bar_unit_w7 = int(self.bar_w / 14)
        bar_unit_w6 = int(self.bar_w / 12)

        self.pos_dict = {
            "default": (int(self.bar_w / 2),  botton_bar_click_h), 
            "avatar": (bar_unit_w7, top_bar_click_h), 
            "gift_code": (550, 450), 
            "input_line": (380, 700), 
            "dw": (385, 850), 
            "pos6_1": (bar_unit_w6, botton_bar_click_h), 
            "pos6_2": (bar_unit_w6*3, botton_bar_click_h), 
            "pos6_3": (bar_unit_w6*5, botton_bar_click_h), 
            "pos6_4": (bar_unit_w6*7, botton_bar_click_h), 
            "pos6_5": (bar_unit_w6*9, botton_bar_click_h), 
            "pos6_6": (bar_unit_w6*11, botton_bar_click_h), 
            "gift": (210, 500), 

            # == main city ==
            "main_city": (bar_unit_w7,  botton_bar_click_h), 
            # "ever_garden": (botton_bar_unit_weight * 9,  int(botton_bar_height - 400)), 
            # "garden_reward": (botton_bar_unit_weight * 13,  int(botton_bar_height - 250)), 

            # == wild ==
            "wild": (bar_unit_w7 * 3,  botton_bar_click_h),
            # "试炼之地": (botton_bar_unit_weight * 3,  int(full_h - 280)), 
            "alliance": (bar_unit_w7 * 5,  botton_bar_click_h), 

            # == adventure ==
            "adventure": (bar_unit_w7 * 7,  botton_bar_click_h), 
            "reward": (bar_unit_w7 * 13, int(self.screen_h - (self.botton_bar_h*1.5))),
            "fight1": (bar_unit_w7 * 7, int(self.screen_h - (self.botton_bar_h*1.5))), 
            "fight2": (bar_unit_w7 * 7, int(self.screen_h - (self.botton_bar_h*1.5))), 
            "fight3": (bar_unit_w7 * 7, botton_bar_click_h), 
            "skip": (bar_unit_w7 * 13, botton_bar_click_h),

            # == small games ==
            "small_games": (bar_unit_w7 * 9,  botton_bar_click_h), 
            # == hero ==
            "hero": (bar_unit_w7 * 11,  botton_bar_click_h), 
            # == chat ==
            "chat": (bar_unit_w7 * 13,  botton_bar_click_h), 
        }
    
    def init_smallProgram(self):
        # 底部条的横向位置
        botton_bar_unit_weight = int(self.full_w / 14)
        # 底部条的纵向位置
        botton_bar_height = int(self.full_h - 50)

        self.pos_dict = {
            "default": (botton_bar_unit_weight * 7,  botton_bar_height), 
            "avatar": (50, 100), 
            "gift_code": (450, 370), 
            "input_line": (330, 560), 
            "qw": (240, 610), 
            "dw": (300, 680), 
            "main_city": (botton_bar_unit_weight * 1,  botton_bar_height), 
            "ever_garden": (botton_bar_unit_weight * 9,  int(botton_bar_height - 400)), 
            "garden_reward": (botton_bar_unit_weight * 13,  int(botton_bar_height - 250)), 
            "wild": (botton_bar_unit_weight * 3,  botton_bar_height),
            "试炼之地": (botton_bar_unit_weight * 3,  int(full_h - 280)), 
            "alliance": (botton_bar_unit_weight * 5,  botton_bar_height), 
            "adventure": (botton_bar_unit_weight * 7,  botton_bar_height), 
            "small_games": (botton_bar_unit_weight * 9,  botton_bar_height),                 # 比如拯救狗狗啥的
            "hero": (botton_bar_unit_weight * 11,  botton_bar_height), 
            "chat": (botton_bar_unit_weight * 13,  botton_bar_height), 
            "fight1": (botton_bar_unit_weight * 7, int(full_h - 150)), 
            "fight2": (botton_bar_unit_weight * 7, int(full_h - 150)), 
            "fight3": (botton_bar_unit_weight * 7, botton_bar_height), 
            "skip": (botton_bar_unit_weight * 13, botton_bar_height),
            "reward": (botton_bar_unit_weight * 13, int(full_h - 180)),
        }

    def pos_dict_pic(self):
        pass

    def daily_routine(self):
        self.back_to_main_page()
        # 拿奖励
        self.receive_afk_rewards()
        self.back_to_main_page()
        self.receive_graden_rewards()
        self.back_to_main_page()

        # 推冒险进度200次
        for _ in range(80):
            self.break_through_latest_levels()

        # 为了衔接休息2min
        random_sleep(120, 130)
        self.back_to_main_page()


        # 推试炼之地200次
        self.get_into_trial()
        for _ in range(80):
            self.place_of_trial1()
            # self.place_of_trial2()
        self.back_to_main_page()

    def daily_routine_first(self):
        """
        每日日常操作，包括完成每日任务领取每日礼包等等
        """
        flag = input("Make sure you are on the Main City page! (y/n)")
        if flag != 'y':
            return

        # self.back_to_main_page()

        # ~ 第一次领取aft rewards
        # self.receive_afk_rewards()

        # # ~ 挑战冒险关卡一次
        # self.break_through_latest_levels()
        # while True:
        #     # 判断是否回到对应界面，不然就一直点，避免打到首领后面卡住
        #     pos = get_loc_on_screen(self.get_pic_path("app", "adventure", "adventure"), 
        #                             self.screen_rect, confidence=0.9)
        #     if pos is not None:
        #         self.logger.info("已返回冒险界面")
        #         break
        #     self.logger.info("未返回冒险界面")
        #     self.seq_click_act(["skip", "default"])
        #     random_sleep(10, 15)
        
        # # ~ 第二次领取aft rewards
        # self.receive_afk_rewards()

        # TODO: ~ 领各种礼包
        self.back_to_main_page()
        ## ~ 每日礼包
        self.logger.info("每日礼包")
        pos = get_loc_on_screen(self.get_pic_path("app", "maincity", "gift"), 
                                self.screen_rect, confidence=0.9)
        self.seq_click_act(["pos6_3", "gift", "pos6_4", "gift", "pos6_5", "gift", "pos6_1"])


    def back_to_main_page(self):
        self.logger.info("Return to main menu...")
        point_seq = ["main_city"]

        self.seq_click_act(point_seq)

    def break_through_latest_levels(self):
        self.logger.info("Start break through the latest levels")

        point_seq = [
            "adventure", 
            "fight1", 
            "fight2", 
            "fight3", 
            "skip", 
            "default"
        ]

        self.seq_click_act(point_seq)

    def receive_afk_rewards(self):
        self.logger.info("receive afk rewards")

        point_seq = [
            "adventure", 
            "reward", 
            "default"
        ]

        self.seq_click_act(point_seq)

    def receive_graden_rewards(self):
        self.logger.info("receive evergraden rewards")

        point_seq = [
            "main_city", 
            "ever_garden", 
            "garden_reward",
            "default"
        ]

        self.seq_click_act(point_seq)

    def get_into_trial(self):
        self.logger.info("get into trial...")

        point_seq = [
            "wild", 
            "试炼之地", 
        ]

        self.seq_click_act(point_seq)

    def place_of_trial1(self):
        self.logger.info("Start break through the place of trial 1(no skip right)")

        point_seq = [ 
            "fight3", 
            "fight3",
            "skip", 
            "default"
        ]

        self.seq_click_act(point_seq)

    def place_of_trial2(self):
        self.logger.info("Start break through the place of trial 2(skip right)")

        point_seq = [ 
            "fight3", 
            "fight3", 
            "default"
        ]

        self.seq_click_act(point_seq)

    def sea(self):
        self.logger.info("Start break through the sea")

        point_seq = [ 
            "fight1", 
            "fight2", 
            "fight3", 
            "skip", 
            "default"
        ]

        self.seq_click_act(point_seq)

    def input_activate_codes(self):
        self.logger.info("Start activate code")

        point_seq = [
            'avatar',
        ]
        self.seq_click_act(point_seq)

        for code in activate_code_list:
            point_seq = [
                'gift_code', 
                'input_line', 
            ]
            self.seq_click_act(point_seq)

            self.keyborad_input(code)
            # self.keyborad_input("enter")

            point_seq = [
                'dw',
                'dw', 
                'default', 
                'default', 
            ]
            self.seq_click_act(
                point_seq, 
                min_short_wait = 0.5, 
                max_short_wait = 1.,
                min_long_wait = 0.5, 
                max_long_wait = 1.,
            )
        
        # 返回主界面
        self.seq_click_act(['default'])

activate_code_list = [
    # 'CN666', 'CN888', 'CN999', 
    # 'GZYL666', 'GZTB666', 
    # 'CNFL5000', 'CNFL10000', 'CNFL50000', 'CNFL100000', 'CNFL200000', 
    # 'VIP666', 'VIP888', 'VIP999', 
    # 'XNKL111', 'XNKL222', 'XNKL333', 
    # 'CNWY666', 'CNWY888', 'CNWY999', 
    # 'WYKL666', 
    # 'CNCJ666', 'CNCJ888', 'CNCJ999', 
    # 'FZP001', 'JQFL999', 
    # 'CNSJ123', 'CNSJ666', 'CNSJ999', 'CNQX777', 
    # 'Hxdhxd', 'Gkdgkd', '648648', 
    # 'Cnznq111', 'Cnznq666', 'Cnznq999', 
    'qejfl52013', 'hanikezi', 'HNKZ'
]