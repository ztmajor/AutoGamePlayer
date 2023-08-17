import cv2

from action import UnitActionBase


class SuperWorldAction(UnitActionBase):
    def __init__(self, img, log_file) -> None:
        """
        这里支持以下功能：
            1. 日常任务： daily_routine
            2. 单刷试炼之地： place_of_trial1 / place_of_trial2 （需要预先进入试炼之地）
            3. 单推最新章节： break_through_latest_levels （需要进入主界面）
            TODO:
            4. 推远古召唤，及其中间不同的洞窟
            5. 推勇者航线最新章节
            6. 15分钟自动竞技场打比自己弱的（如果没有打到3个不刷新）
            7. 英雄升级检测，英雄升级策略，按照顺序
            8. 联盟自动求助 以及 自动帮点


        """
        super(SuperWorldAction, self).__init__(img, log_file)
        
        self.long_wait_seq = ["fight3", "default"]

    def gen_pos_dict(self, img):
        # TODO: 有些东西需要自动判断，有些可以使用固定的位置
        # TODO: 使用应用内的相对位置，而不是电脑屏幕的绝对位置
        full_h, full_w, channal = img.shape

        # 底部条的横向位置
        botton_bar_unit_weight = int(full_w / 14)
        # 底部条的纵向位置
        botton_bar_height = int(full_h - 50)

        self.pos_dict = {
            "default": (botton_bar_unit_weight * 7,  botton_bar_height), 
            "mainCity": (botton_bar_unit_weight * 1,  botton_bar_height), 
            "everGarden": (botton_bar_unit_weight * 9,  int(botton_bar_height - 400)), 
            "gardenReward": (botton_bar_unit_weight * 13,  int(botton_bar_height - 250)), 
            "wild": (botton_bar_unit_weight * 3,  botton_bar_height),
            "试炼之地": (botton_bar_unit_weight * 3,  int(full_h - 280)), 
            "alliance": (botton_bar_unit_weight * 5,  botton_bar_height), 
            "adventure": (botton_bar_unit_weight * 7,  botton_bar_height), 
            "smallGames": (botton_bar_unit_weight * 9,  botton_bar_height),                 # 比如拯救狗狗啥的
            "hero": (botton_bar_unit_weight * 11,  botton_bar_height), 
            "chat": (botton_bar_unit_weight * 13,  botton_bar_height), 
            "fight1": (botton_bar_unit_weight * 7, int(full_h - 150)), 
            "fight2": (botton_bar_unit_weight * 7, int(full_h - 150)), 
            "fight3": (botton_bar_unit_weight * 7, botton_bar_height), 
            "skip": (botton_bar_unit_weight * 13, botton_bar_height),
            "reward": (botton_bar_unit_weight * 13, int(full_h - 180)),
        }

    def daily_routine(self):
        self.back_to_main_page()
        # 拿奖励
        self.receive_afk_rewards()
        self.back_to_main_page()
        self.receive_graden_rewards()
        self.back_to_main_page()

        # 推冒险进度200次
        for _ in range(200):
            self.break_through_latest_levels()
        self.back_to_main_page()

        # 推试炼之地200次
        self.get_into_trial()
        for _ in range(200):
            self.place_of_trial1()
            # self.place_of_trial2()
        self.back_to_main_page()

    def back_to_main_page(self):
        self.logger.info("Return to main menu...")
        point_seq = ["mainCity"]

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
            "mainCity", 
            "everGarden", 
            "gardenReward",
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
