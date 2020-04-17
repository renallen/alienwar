# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:21:50 2020

@author: 84583
"""

class GameStates():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_states()
        self.game_active = False
        self.score=0
        self.game_stop=False
        self.rank=0
    def reset_states(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.score=0
        self.ships_left = self.ai_settings.ship_limit
        self.rank=0