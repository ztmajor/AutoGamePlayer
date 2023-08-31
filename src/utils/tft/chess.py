#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   chess.py
@Time    :   2023/08/31 16:49:14
@Author  :   Mei Yu 
@Version :   1.0
@Desc    :   None
'''


from typing import List
from tft import ChessBase



class Chess(ChessBase):
    def __init__(self, name: str, trait: List[str], equipment=None) -> None:
        super().__init__(name, trait, equipment)

        pass