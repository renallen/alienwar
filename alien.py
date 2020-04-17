# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:36:49 2020

@author: 84583
"""

import pygame
from pygame.sprite import Sprite
import random
class Alien(Sprite):

    """表示单个外星人的类"""
    def __init__(self,screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen=screen
        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images\\alien.png')
        self.rect = self.image.get_rect()
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float( self.rect.y )
        self.speed_factory=0.1
        self.speed_factorx=1.5
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值

        self.y += self.speed_factory
        # 更新表示子弹的rect的位置
        self.rect.y = self.y
        r = random.randint(-1,1)
        self.x += self.speed_factorx*r
        # 更新表示子弹的rect的位置
        self.rect.x = self.x
        
        if self.rect.right >= self.screen.get_rect().right or self.rect.left <= 0:
            self.x+=-self.speed_factorx*r

