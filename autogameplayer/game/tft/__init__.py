#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2023/08/31 10:27:27
@Author  :   Mei Yu 
@Version :   1.0
@Desc    :   Teamfight Tactics 金铲铲之战
'''

from typing import List, Tuple


class PlayerBase(object):
    """

    Args:
        object (_type_): _description_
    """
    def __init__(self) -> None:
        pass
        
        # synergy 协同作用
        self.synergy = None

    
    def get_synergy_str(self):
        return ""



class ChessBase(object):
    def __init__(self, name: str, trait: List[str], equipment=None) -> None:
        """
        

        Args:
            name (str): 英雄特性
            trait (List[str]): _description_
            equipment (_type_, optional): _description_. Defaults to None.
        """
        self.name = name
        self.trait = trait

        self.equipment = equipment

    
    def info_str(self):
        return f"{self.name} | trait: {self.trait} | {self.equipment}"
