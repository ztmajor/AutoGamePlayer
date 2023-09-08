import os
import cv2
import time
import pygetwindow

from autogameplayer.game.superworld import UnitActionBase
from autogameplayer.utils import random_sleep
from autogameplayer.platform.win.io import get_loc_on_screen, get_all_loc_on_screen

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
            3. 单推最新章节： adventure_latest （需要进入主界面）
            8. 联盟自动帮点-
            9. 神奇树洞一键探索
            10. 游乐园自动抽奖
            14. 自动收送爱心
            15. 使用点金手
            TODO:
            4. 推远古召唤，及其中间不同的洞窟
            5. 推勇者航线最新章节
            6. 15分钟自动竞技场打比自己弱的（如果没有打到3个不刷新）
            7. 英雄升级检测，英雄升级策略，按照顺序
            11. 神奇树洞点科技树
            12. 联盟自动求助
            13. 冒险3星补全
            16. 打狩猎战
            17. 联盟打桩
            18. 勇者航线
            19. 橡木酒馆
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
        # self.top_bar_h = 200
        # self.botton_bar_h = 100

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

        self.abs_pos_dict = {
            "default": (int(self.bar_w / 2),  botton_bar_click_h), 
            "add_coin": (725, top_bar_click_h), 
            "diamond2coin": (bar_unit_w7*7, int(self.screen_h - (self.botton_bar_h*2))), 
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

            # == main city ==
            "main_city": (bar_unit_w7,  botton_bar_click_h), 
            "ever_garden": (bar_unit_w7*9,  int(self.screen_h - (self.botton_bar_h*5))), 
            "garden_reward": (bar_unit_w6*11,  int(self.screen_h - (self.botton_bar_h*2.5))), 
            "cljy": (380, 530), 
            "explore_reward": (bar_unit_w7*2, int(self.screen_h - (self.botton_bar_h*2))),
            "fast_explore": (bar_unit_w6*11, int(self.screen_h - (self.botton_bar_h*2))), 
            "explore": (bar_unit_w6*6, int(self.screen_h - (self.botton_bar_h*2))), 
            "back2hall": (bar_unit_w6*2, botton_bar_click_h), 
            "raffle": (bar_unit_w6*6, int(self.screen_h - (self.botton_bar_h*1.5))), # 抽奖
            "attack": (bar_unit_w6*3, int(self.screen_h - (self.botton_bar_h*3))), 
            "gift": (70, 525), 
            "get_gift1": (210, 500), 
            "get_gift2": (550, 870), 
            "friend": (bar_unit_w7*13, int(self.screen_h - (self.botton_bar_h*4.5))), 
            "give_receice_heart": (bar_unit_w7*11, int(self.screen_h - (self.botton_bar_h*1))), 

            # == wild ==
            "wild": (bar_unit_w7 * 3,  botton_bar_click_h),
            "trial": (bar_unit_w7 * 3,  int(self.screen_h - (self.botton_bar_h*2.5))), 
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
            "chat_alliance": (bar_unit_w7*8, int(self.screen_h - (self.botton_bar_h*2)))
        }
    
    def init_smallProgram(self):
        self.top_bar_h = 80
        self.botton_bar_h = 100

        top_bar_click_h = int(self.top_bar_h/2)
        botton_bar_click_h = int(self.screen_h - (self.botton_bar_h/2))

        bar_unit_w7 = int(self.bar_w / 14)
        bar_unit_w6 = int(self.bar_w / 12)

        # # 底部条的横向位置
        # botton_bar_unit_weight = int(self.full_w / 14)
        # # 底部条的纵向位置
        # botton_bar_height = int(self.full_h - 50)

        self.abs_pos_dict = {
            "default": (int(self.bar_w / 2),  botton_bar_click_h), 
            "avatar": (50, 100), 
            "gift_code": (450, 370), 
            "input_line": (330, 560), 
            "qw": (240, 610), 
            "dw": (300, 680), 
            "pos6_1": (bar_unit_w6, botton_bar_click_h), 
            "pos6_2": (bar_unit_w6*3, botton_bar_click_h), 
            "pos6_3": (bar_unit_w6*5, botton_bar_click_h), 
            "pos6_4": (bar_unit_w6*7, botton_bar_click_h), 
            "pos6_5": (bar_unit_w6*9, botton_bar_click_h), 
            "pos6_6": (bar_unit_w6*11, botton_bar_click_h), 
            "gift": (50, 430), 

            # == main city ==
            "main_city": (bar_unit_w7,  botton_bar_click_h), 
            "ever_garden": (bar_unit_w7*9,  int(self.screen_h - (self.botton_bar_h*5))), 
            "garden_reward": (bar_unit_w6*11,  int(self.screen_h - (self.botton_bar_h*2.5))), 
            "cljy": (300, 430), 
            "explore_reward": (bar_unit_w7*2, int(self.screen_h - (self.botton_bar_h*2))),
            "fast_explore": (bar_unit_w6*11, int(self.screen_h - (self.botton_bar_h*2))), 
            "explore": (bar_unit_w6*6, int(self.screen_h - (self.botton_bar_h*2))), 
            "back2hall": (bar_unit_w6*2, botton_bar_click_h), 
            "raffle": (bar_unit_w6*6, int(self.screen_h - (self.botton_bar_h*1.5))), # 抽奖
            "attack": (bar_unit_w6*3, int(self.screen_h - (self.botton_bar_h*3))), 

            # == wild ==
            "wild": (bar_unit_w7 * 3,  botton_bar_click_h),
            "trial": (bar_unit_w7 * 3,  int(self.screen_h - (self.botton_bar_h*2.5))), 
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
            "chat_alliance": (bar_unit_w7*8, int(self.screen_h - (self.botton_bar_h*2)))
        }

    def daily_routine(
            self, 
            weekday, 
            adventrue_loop=100,
            trail_loop=20, 
            skip_right=False, 
            after1720=False
        ):

        self.back_to_main_page()
        # 拿奖励
        self.receive_afk_rewards()
        self.back_to_main_page()
        self.ever_garden(reward=True, hole=True, playground=False)
        self.back_to_main_page()

        # 推冒险进度
        self.adventure_latest(loop=adventrue_loop)
        # while get_loc_on_screen(self.get_pic_path(self.platform, "adventure", "adventure"), 
        #                             self.screen_rect, confidence=0.9) is not None:
        #     # 判断是否回到对应界面，不然就一直点，避免打到首领卡住
        #     self.logger.info("未返回冒险界面")
        #     self.seq_click_act(["skip", "default"])
        #     random_sleep(10, 15)

        # 为了衔接休息2min
        random_sleep(120, 130)
        self.back_to_main_page()

        # 推试炼之地
        if after1720:
            if weekday in [2, 6]:
                self.trial(loop=trail_loop, direct=False, skip_right=True, mode='dark')
            if weekday in [1, 3, 6]:
                self.trial(loop=trail_loop, direct=False, skip_right=True, mode='human')
            if weekday in [2, 6]:
                self.trial(loop=trail_loop, direct=False, skip_right=True, mode='orc')
            if weekday in [3, 5, 6]:
                self.trial(loop=trail_loop, direct=False, skip_right=True, mode='spirit')

            self.trial(loop=trail_loop, direct=False, skip_right=skip_right, mode='default')
        else:
            self.trial(loop=trail_loop, direct=False, skip_right=skip_right)
        # self.back_to_main_page()

    def daily_routine_first(self):
        """
        每日日常操作，包括完成每日任务领取每日礼包等等
        """
        flag = input("Make sure you are on the Main City page! (y/n)")
        if flag != 'y':
            return
        # 按照每日任务的顺序做
        self.back_to_main_page()

        # == 1 挑战【冒险】关卡1次 + 收取挂机收益2次 ==
        # ~ 第一次领取aft rewards
        self.receive_afk_rewards()

        # ~ 挑战冒险关卡一次
        self.adventure_latest()
        # # TODO: 此处的图像识别除了问题
        # while get_loc_on_screen(self.get_pic_path(self.platform, "adventure", "adventure"), 
        #                             self.screen_rect, confidence=0.9) is not None:
        #     # 判断是否回到对应界面，不然就一直点，避免打到首领卡住
        #     self.logger.info("未返回冒险界面")
        #     self.seq_click_act(["skip", "default"])
        #     random_sleep(10, 15)
        # 为了衔接休息2min
        random_sleep(120, 130)
        self.back_to_main_page()
        
        self.logger.info("已返回冒险界面")
        # ~ 第二次领取aft rewards
        self.receive_afk_rewards()
        self.back_to_main_page()

        # == 2 花园收取资源2次 ==
        # ~ 永绿花园
        self.ever_garden(reward=True, playground=True, hole=True)
        self.ever_garden(reward=True, playground=False, hole=False)

        # == 3 赠送爱心1次 ==
        self.friend()

        # == 4 使用5次点金手 == 
        self.add_coin(times=5)

        # == -2 签到 ==


        # == -1 领礼包 ==
        # TODO: ~ 领各种礼包
        self.back_to_main_page()
        ## ~ 每日礼包
        self.logger.info("每日礼包")
        self.seq_click_act(["gift"])
        self.seq_click_act(["pos6_3", "get_gift1", "get_gift2", "pos6_3", 
                            "pos6_4", "get_gift1", "get_gift2", "pos6_3", 
                            "pos6_5", "get_gift1", "get_gift2", "pos6_3", 
                            "pos6_1"])
        
        # 联盟求助
        self.alliance_help()

    def back_to_main_page(self):
        self.logger.info("Return to main menu...")
        point_seq = ["main_city"]

        self.seq_click_act(point_seq)

    def adventure_latest(self, loop=1):
        self.logger.info(f"Try break through the latest levels {loop} times.")

        point_seq = ["adventure"]
        point_seq += [
            "fight1", 
            "fight2", 
            "fight3", 
            "skip", 
            "default"
        ] * loop

        self.seq_click_act(point_seq)

    def adventure_full_star(self):
        self.logger.info("进行星星补全成3星")
        raise NotImplementedError()
        # point_seq = [
        #     "adventure", 
        #     "fight1", 
        #     "fight2", 
        #     "fight3", 
        #     "skip", 
        #     "default"
        # ]

        # self.seq_click_act(point_seq)

    def receive_afk_rewards(self):
        self.logger.info("receive afk rewards")

        point_seq = [
            "adventure", 
            "reward", 
            "default"
        ]

        self.seq_click_act(point_seq)

    def add_coin(self, times=5):
        self.logger.info(f"add_coin.")
        point_seq = ["add_coin"]
        point_seq += ["diamond2coin"]*times
        point_seq += ["default"]

        self.seq_click_act(point_seq)

    def friend(self):
        self.logger.info(f"Friend.")
        point_seq = ["friend", "give_receice_heart", "default"]

        self.seq_click_act(point_seq)

    def ever_garden(self, reward=False, playground=False, hole=False):
        self.logger.info(f"Ever Garden. 收菜 {reward} | 游乐园抽奖 {playground} | 树洞 {hole}")

        # point_seq = []
        point_seq = ["ever_garden"]

        if reward:
            point_seq += ["garden_reward", "default"]
        if hole:
            point_seq += ['pos6_3', 'cljy', 
                          'explore_reward', 'default', 
                          'fast_explore', 'explore', 'default', 'default', 
                          'back2hall', 'pos6_1']

        self.seq_click_act(point_seq)

        if playground:
            self.seq_click_act(['pos6_6'])
            self.seq_click_act(['raffle'], press_time=1.0)

            while get_loc_on_screen(self.get_pic_path(self.platform, "maincity", "subscribe_privilege"), 
                                    self.screen_rect, confidence=0.9) is None:
                # check stop, 是否出现订阅特权
                print("抽奖未结束~")

                is_attack = get_loc_on_screen(self.get_pic_path(self.platform, "maincity", "select_attack"), 
                                    self.screen_rect, confidence=0.9) is not None
                # check attack, 是否进入攻击状态
                if is_attack:
                    # TODO: 之后遇到双弓的时候再进行修补， 已完成三弓的情况
                    # 攻击的话会有龙的长时间的攻击动画
                    self.seq_click_act(['attack'], min_short_wait=12, max_short_wait=15)
                    
                    # 领取奖励的位置
                    self.seq_click_act(['pos6_6'])

                random_sleep(10, 20)

            self.seq_click_act(['default', 'pos6_1'])
        self.seq_click_act(['pos6_1'])

    def trial(self, loop=1, direct=False, skip_right=False, mode=None, return_main=True):
        """

        Args:
            loop (int, optional): 循环操作次数 Defaults to 1.
            direct (bool, optional): 是否直接开始，还是需要先进入trail. Defaults to False.
            skip_right (bool, optional): _description_. Defaults to False.
            mode (str, optional): trial mode, can be dark, human, orc, spirit, default and None. None means 未通过17-20未打开其他试炼之地. Defaults to None.
        """
        self.logger.info(f"Try trail {mode} {loop} times. direct {direct} | skip right {skip_right}")

        # point_seq = []
        point_seq = ["wild", "trial"] if not direct else []
        self.seq_click_act(point_seq)

        # select mode
        if mode is not None:
            # 17-20之后，需要选择对应洞窟
            pos = get_loc_on_screen(self.get_pic_path(self.platform, "wild", mode), 
                                    self.screen_rect, confidence=0.9)
            self.click_act(pos[0], pos[1])

        point_seq = []
        if skip_right:
            point_seq += ["fight3", "fight3", "default"] * loop
        else:
            point_seq += ["fight3", "fight3", "skip", "default"] * loop

        point_seq += ['pos6_1']
        if return_main:
            point_seq += ['pos6_1', 'main_city']

        self.seq_click_act(point_seq)

    def alliance_help(self):
        """
        联盟寻求帮助与帮助别人
        """
        self.logger.info("alliance ask for help and help others...")

        point_seq = [
            "chat", 
            "chat_alliance", 
        ]

        self.seq_click_act(point_seq)

        # TODO: 这里有一个问题，可能是因为会把图片都处理成灰度图，所以帮助都会点。甚至点两遍（图截的不好）
        pos_list = get_all_loc_on_screen(self.get_pic_path(self.platform, "chat", "help_green"), 
                                    self.screen_rect, confidence=0.9)

        if pos_list is not None:
            for pos in pos_list:
                self.click_act(pos[0], pos[1])

        self.seq_click_act(['main_city'])

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