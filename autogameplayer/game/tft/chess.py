#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   chess.py
@Time    :   2023/08/31 16:49:14
@Author  :   Mei Yu 
@Version :   1.0
@Desc    :   None
'''


from typing import List, Dict
from autogameplayer.game.tft import ChessBase



class Chess(ChessBase):
    def __init__(self, name: str, metaDataDict:Dict[str, str], equipment: List[str]=None) -> None:
        super().__init__(name, equipment)

        self.metaDataDict = metaDataDict