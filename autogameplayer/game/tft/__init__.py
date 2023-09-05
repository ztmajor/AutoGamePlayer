#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2023/08/31 10:27:27
@Author  :   Mei Yu 
@Version :   1.0
@Desc    :   Teamfight Tactics Mobile 金铲铲之战
'''

import numpy as np
from typing import List, Tuple


class GameInfoBase(object):
    """统计分析保存一个对局的信息类
        
    1. 整局排名情况，1-8的用户ID
    2. 不同排名的阵容（羁绊+棋子名称与星级）
    3. hextech
    4. 其他信息（英雄之力s9/）
    """
    def __init__(self, gameInfoDict) -> None:

        self.ranks = []

        # rank 1-8
        self.user_id = []
        self.lineup = []

        # 英雄之力
        self.legend = []
        self.hextech = []

    def from_img(self, img):
        # 分割结算界面/结果界面的内容，提取对应信息

        pass

    def __getitem__(self, item):
        return self.smiles[item], self.graphs[item], self.labels[item], self.masks[item]

    def __len__(self):
        return len(self.smiles)



class LineUpBase(object):
    """阵容

    1. 阵容棋子位置，棋子带的装备
    2. 不同阶段进行什么操作（几级搜什么牌）
    """
    def __init__(self) -> None:
        self.chess_board = np.zeros((4,12))


class InterfaceBase(object):
    """界面信息

    1. 不同按钮、信息静态位置
    2. 选秀，小小英雄的动态位置
    3. 爆的装备的动态生成的静态位置
    4. 判断当前阶段、状态（战斗阶段，准备操作阶段，选秀阶段，）

    """
    def __init__(self) -> None:
        """初始化阶段，在界面找到对应位置
        TODO
        1. 当前阶段,胜负记录位置
        2. 排名以及用户ID，血量
        3. 激活，未激活的羁绊（场上的）
        4. 发消息，表情的位置
        5. 经济，经验条，购买经验，刷新位置
        6. 买牌位置，买牌锁定位置
        7. 备战区
        8. 敌我经济情况，海克斯，场上棋子（战斗时读取信息）
        9. 装备位置
        10. 初始国度选择位置(s9)
        """
        pass

    def get_position(self, name):
        pass


class PlayerBase(object):
    """玩家信息

    1. 玩家的经济状况，hextect
    2. 玩家场上，备战席上的棋子
    3. 玩家的装备
    """
    def __init__(self) -> None:
        pass
        
        # synergy 协同作用, 激活的羁绊
        self.synergy = None


class ChessBase(object):
    """棋子信息

    1. 
    """
    def __init__(self, name: str, equipment: List[str]=None) -> None:
        self.name = name

        self.equipment = equipment

    def equip(self, equipment):
        self.equipment.append(equipment.name)
        equipment.equipped = True

    def get_equipment(self):
        return ",".join(self.equipment)

    def __str__(self) -> str:
        return f"{self.name} | {self.get_equipment()}"
    

class EquipmentBase(object):
    """装备信息

    Args:
        object (_type_): _description_
    """
    # TODO: 后期可实现的功能，决策考虑装备。
    # TODO: 可附加功能，考虑灵凤的存在，移动棋子避免被灵凤吹到
    def __init__(self, name, equipped=False) -> None:
        self.name = name
        self.equipped = equipped
