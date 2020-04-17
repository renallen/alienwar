# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:10:12 2020

@author: 84583
"""

#import sys     
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
#from alien import Alien
from game_states import GameStates
from scoreboard import Board
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    
    states = GameStates(ai_settings)
    
    pygame.display.set_caption(ai_settings.title)
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    sb = Board(ai_settings, screen, states)
    sb.prep_board("Score: 0")
    sb.prep_ship( "Ships: {}".format(ai_settings.ship_limit))
    st=Board(ai_settings, screen, states)
    ship=Ship(screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    aliens = Group()   
#    alien=Alien(screen)
    # 创建外星人群
    gf.create_aliens(screen, aliens,ai_settings.alien_num)
    # 开始游戏的主循环
    while True:
        
    # 监视键盘和鼠标事件
        gf.check_events(screen,states,sb,ship,bullets)
        if states.game_active :
            if(not states.game_stop):
                ship.update()
                gf.update_bullets(ship,bullets)
                gf.update_aliens(screen,states,sb,aliens,ai_settings.alien_num,bullets,ship)
    #        gf.remove_bullet(bullets)
        else: 
#            sb.prep_score()
            pass
        gf.update_screen(ai_settings, sb , st,screen, ship, aliens, bullets, states)
        


if __name__ == '__main__':
    run_game()