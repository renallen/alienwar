# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:06:01 2020

@author: 84583
"""
import sys
import pygame
from bullet import Bullet
from alien import Alien
import random
from time import sleep
def check_events(screen,states,sb,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
#            print(event.key)
            check_keydown_events(event,screen, states,sb,ship,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def check_keydown_events(event,screen,states,sb, ship,bullets):
    """键盘左右键移动 上键加移速"""
    if event.key == pygame.K_RIGHT:
        #向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down= True
    elif event.key == pygame.K_EQUALS:
        if(ship.speed_factor<5):
            ship.change_speed(0.5)
    elif event.key == pygame.K_MINUS:
        if(ship.speed_factor>1):
            ship.change_speed(-0.5)
    elif event.key == pygame.K_SPACE:
        
    # 创建一颗子弹，并将其加入到编组bullets中
        fire_bullet( screen, ship, bullets)
    elif event.key == pygame.K_b:
        if ship.isStrong:
            ship.isStrong=False         
        else:
            ship.isStrong=True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_s:
        states.game_stop= not states.game_stop
        
    elif event.key == pygame.K_g:
        states.game_active=True
        if states.ships_left==0:
            states.reset_states()
            sb.prep_board("Score: "+str(states.score))
            sb.prep_ship("Ships: "+str(states.ships_left))
        
            
def check_keyup_events(event, ship):
    """键盘松开取消连续移动"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
def remove_bullet(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        
def update_screen(ai_settings,sb, st,screen, ship,aliens,bullets,states):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 让最近绘制的屏幕可见
    for alien in aliens:
        alien.blitme()
    
    sb.show_board(screen.get_rect().width-80,20)
#    st.prep_board("")
    gmstates=False
    if states.game_stop:
        st.prep_board("PUASE Press \"s\" to continue")
        gmstates=True
    if ( not states.game_active) and states.ships_left==ai_settings.ship_limit:
        st.prep_board("Ready? Press \"g\" to start")
        gmstates=True
    elif (( not states.game_active) and states.ships_left<=ai_settings.ship_limit):
        st.prep_board("YOU LOSS, NO.{} in the rank list, Press  \"g\" to restart".format(states.rank)) if states.rank!=0 else st.prep_board("YOU LOSS, not in rank list, Press  \"g\" to restart")
        gmstates=True
    if gmstates:
        st.show_board(screen.get_rect().centerx, screen.get_rect().centery)
#    aliens.draw(screen)
    pygame.display.flip()
    
    
def fire_bullet( screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    if len(bullets) < ship.send_allow:
            new_bullet = Bullet(screen, ship)
            bullets.add(new_bullet)
            
def update_bullets(ship,bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    
    if(ship.isStrong):
        t=0
        for bullet in bullets:
            bullet.update(ship,t)
            t+=1
            if(t==3):
                t=0
    else:
        bullets.update(ship)
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
#def isGame_over(screen,aliens,ship):
#    for alien in aliens:
#        if alien.rect.y>screen.bottom:
#            print("death")
#            return True
#    return False
    
    
def create_aliens(screen,aliens,alien_num):
    #创建外星人战队
    
    for i in range(len(aliens),alien_num):
        creat_alien(screen, aliens)
        
def creat_alien(screen, aliens):
    #创建单个外星人
    alien = Alien(screen)
    l=int((screen.get_rect().right-80)/2/alien.rect.width)
    alien.x = float(random.randint(0,l-1)*2+random.random())*alien.rect.width
    alien.rect.x=alien.x
    alien.y = float(random.random())*alien.rect.height
    alien.rect.y=alien.y
    aliens.add(alien)
    
def update_aliens(screen,states,sb,aliens,alien_num,bullets,ship):
    #监测是否子弹有击中外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    isUpss=False
    if collisions:
        for a in collisions.values():
            states.score +=  len(a)
        creat_alien(screen, aliens)
        isUpss=True
    for alien in aliens:
        alien.update()
        if alien.rect.bottom>screen.get_rect().bottom:
            ship_hit( alien_num,states, screen, ship, aliens, bullets)
            isUpss=True
#            sb.prep_board("Score: "+str(states.score),"Ships: "+str(states.ships_left))
            break
            
            
    if pygame.sprite.spritecollideany(ship, aliens):
       ship_hit(alien_num,states, screen, ship, aliens, bullets)
       isUpss=True
    if isUpss:
       sb.prep_board("Score: "+str(states.score))
       sb.prep_ship("Ships: "+str(states.ships_left))
def ship_hit(alien_num, states, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    # 将ships_left减1
    if states.ships_left > 0:
        
        states.ships_left -= 1
        
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_aliens(screen,  aliens,alien_num)
        ship.reset_ship()
        # 暂停
        sleep(0.5)
    else:
        states.game_active = False
        ship.reset_ship()
        if states.score>50:
             rank_score("rank.txt",states)
             
def rank_score(File,states):
    ##读写历史分数排序
    stm=[]
    use=False
    r=1
    with open("rank.txt", 'r+') as f:
        scores=f.readlines()
            
        for i in scores:
            if (states.score>=int(i.rstrip())) and not use:
                stm.append(str(states.score)+"\n")
                use=True
            stm.append(i)
            if not use:
                r=r+1
        f.seek(0)
        if len(stm)>10:
            f.writelines(stm[:10])
        else:
            f.writelines(stm)
    states.rank=r


            