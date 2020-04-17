# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:37:06 2020

@author: 84583
"""

import pygame
class Ship():
    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images\ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.centerx = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.bottom= float(self.rect.bottom)
        self.speed_factor = 1.5
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.isStrong = False
        self.send_allow=8

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.speed_factor
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.speed_factor
        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom
        
    def change_speed(self, ad):
        self.speed_factor += ad
#        print(self.speed_factor)
        
    def change_allow(self,num):
        self.send_allow=num
#    def center_ship(self):
#        """让飞船在屏幕上居中"""
#        self.center = self.screen_rect.centerx
        
    def reset_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.centerx = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.bottom= float(self.rect.bottom)
        self.isStrong = False