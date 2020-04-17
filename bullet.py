# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:16:39 2020

@author: 84583
"""

import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.width = 3
        self.height = 15
        self.color = 60, 60, 60
        self.speed_factor = 1
    # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.width ,
                                self.height )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.allowed=5;
    def update(self,ship,t=0):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        if ship.isStrong:#子弹加强
            self.rect.height = 30
            self.rect.width=6
            self.color = 250, 60, 60
            self.speed_factor = 1.5
            ship.change_allow(10)
            
        else:
            self.rect.height = 15
            self.rect.width=3
            self.color = 60, 60, 60
            self.speed_factor = 1
            ship.change_allow(5)
        if t==1:
            self.rect.x -= self.speed_factor
            if self.rect.x<=0:
                self.rect.x +=self.speed_factor
        elif t==2:
            self.rect.x += 2*self.speed_factor
            if  self.rect.x>=self.screen.get_rect().right:
                self.rect.x-= 2*self.speed_factor
        else:
            pass
   
            
        self.y -= self.speed_factor
        #更新表示子弹的rect的位置
        self.rect.y = self.y
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
        

        
        

        