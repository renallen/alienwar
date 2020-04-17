# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:51:59 2020

@author: 84583
"""

import pygame.font
from pygame.sprite import Group
from ship import Ship
class Board():
    """显示得分信息的类"""
    def __init__(self, ai_settings, screen, states,string1="",string2=""):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.states = states
        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # 准备初始得分图像
        self.images=[]
        self.prep_board(string1)
        self.prep_ship(string2)
#        self.prep_ships()
    def prep_board(self,string,*arg):
        """将得分转换为一幅渲染的图像"""
        score_str = string
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        
        # 将得分放在屏幕右上角
    def prep_ship(self,string):
        ship_str = string
        self.ship_image = self.font.render(ship_str, True, self.text_color,
                                            self.ai_settings.bg_color)
    def show_board(self,x,y):
        """在屏幕上显示得分"""
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = x
        self.score_rect.centery = y
        self.screen.blit(self.score_image, self.score_rect)
        self.ship_rect = self.ship_image.get_rect()
        self.ship_rect.centerx = x
        self.ship_rect.centery = y+50
        self.screen.blit(self.ship_image, self.ship_rect)
#        self.ships.draw(self.screen)
#    def prep_ships(self):
#        """显示还余下多少艘飞船"""
#        self.ships = Group()
#        for ship_number in range(self.states.ships_left):
#                ship = Ship( self.screen)
#                ship.rect.x = 10 + ship_number * ship.rect.width
#                ship.rect.y = 10
#                self.ships.add(ship)