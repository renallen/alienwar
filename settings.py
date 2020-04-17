# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:21:39 2020

@author: 84583
"""

class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.title = "Alien Invasion"
        self.bg_color = (230, 230, 230)
        self.bullets_allowed = 5
        self.alien_num=8
        self.ship_limit = 3