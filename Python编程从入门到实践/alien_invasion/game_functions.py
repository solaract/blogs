import sys
import pygame

from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # # 创建一颗子弹，并将其加入到编组bullets中
        # if len(bullets) < ai_settings.bullets_allowed:
        #     new_bullet = Bullet(ai_settings,screen,ship)
        #     bullets.add(new_bullet)
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
            

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        
        # 隐藏光标 
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()



def check_evets(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    """响应按键和鼠标事件"""
    # 监视键盘和鼠标事件
    # 方法pygame.event.get()访问Pygame检测到的事件
    for event in pygame.event.get():
        # 玩家单击游戏窗口的关闭按钮时，将检测到pygame.QUIT事件
        if event.type == pygame.QUIT:
            sys.exit()
        # 每次按键都被注册为一个KEYDOWN事件
        elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = True
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = True
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = False
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = False
            check_keyup_events(event,ship)
        # 无论玩家单击屏幕的什么地方，Pygame都将检测到一个MOUSEBUTTONDOWN事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # pygame.mouse. get_pos()，它返回一个元组，其中包含玩家单击时鼠标的x和y坐标
            mouse_x,mouse_y = pygame.mouse.get_pos()
            # collidepoint()检查鼠标单击位置是否在Play按钮的rect内
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x, mouse_y)

            

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 方法screen.fill()，用背景色填充屏幕；这个方法只接受一个实参：一种颜色
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    
    ship.blitme()
    # alien.blitme()
    # 对编组调用draw()时，Pygame自动绘制编组的每个元素，绘制位置由元素的属性rect决定
    aliens.draw(screen)

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    # 移动游戏元素时，pygame.display.flip()将不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果
    pygame.display.flip()


def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    # 当你对Group调用update()时，Group将自动对其中的每个Sprite调用update()，因此代码行bullets.update()将为Groupbullets中的每颗子弹调用bullet.update()
    bullets.update()
    # # 检查是否有子弹击中了外星人
    # # 如果是这样，就删除相应的子弹和外星人
    # # 遍历编组bullets中的每颗子弹，再遍历编组aliens中的每个外星人。每当有子弹和外星人的rect重叠时，groupcollide()就在它返回的字典中添加一个键-值对
    # # 两个实参True告诉Pygame删除发生碰撞的子弹和外星人
    # collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    # if len(aliens) == 0:
    #     # 删除现有的子弹并新建一群外星人
    #     bullets.empty()
    #     create_fleet(ai_settings,screen,ship,aliens)
      
    # 删除已消失的子弹
    # 在for循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本
    # 使用方法copy()来设置for循环，这让我们能够在循环中修改bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)


def check_high_score(stats,sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """响应子弹和外星人的碰撞"""
    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    # 遍历编组bullets中的每颗子弹，再遍历编组aliens中的每个外星人。每当有子弹和外星人的rect重叠时，groupcollide()就在它返回的字典中添加一个键-值对
    # 与外星人碰撞的子弹都是字典collisions中的一个键；而与每颗子弹相关的值都是一个列表，其中包含该子弹撞到的外星人
    # 两个实参True告诉Pygame删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    if len(aliens) == 0:
        # 删除现有的子弹，加快游戏速度，并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        # 如果整群外星人都被消灭，就提高一个等级
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)


def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有到达限制，就发射一颗子弹""" 
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少行外星人"""
    # 可用垂直空间：将屏幕高度减去第一行外星人的上边距（外星人高度）、飞船的高度以及最初外星人群与飞船的距离（外星人高度的两倍）
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    # 每行下方都要留出一定的空白区域，设置为外星人的高度，可容纳的行数为可用垂直空间除以外星人高度的两倍
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings,alien_width):
    """计算每行可容纳多少个外星人"""
    # 屏幕两边都留下一定的边距，设置为外星人的宽度，可用于放置外星人的水平空间为屏幕宽度减去外星人宽度的两倍
    available_space_x = ai_settings.screen_width - 2 * alien_width
    # 显示一个外星人所需的水平空间为外星人宽度的两倍：一个宽度用于放置外星人，另一个宽度为外星人右边的空白区域
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    # 第一行外星人上方留出与外星人等高的空白区域。相邻外星人行的y坐标相差外星人高度的两倍，因此我们将外星人高度乘以2，再乘以行号。第一行的行号为0，因此第一行的垂直位置不变，而其他行都沿屏幕依次向下放置
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群""" 
    # 创建一个外星人，并计算一行可容纳多少个外星人 
    # 外星人间距为外星人宽度 
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    # alien_width = alien.rect.width
    # available_space_x = ai_settings.screen_width - 2 * alien_width
    # number_aliens_x = int(available_space_x / (2 * alien_width))

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            # alien = Alien(ai_settings,screen)
            # alien.x = alien_width + 2 * alien_width * alien_number
            # alien.rect.x = alien.x
            # aliens.add(alien)
            create_alien(ai_settings,screen,aliens,alien_number,row_number)


def check_fleet_edges(ai_settings,aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break


def change_fleet_direction(ai_settings,aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1

        # 更新记分牌 
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
            break



def update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """检查是否有外星人位于屏幕边缘，并更新整群外星人的位置"""
    # 检测外星人和飞船之间的碰撞
    # 方法spritecollideany()接受两个实参：一个精灵和一个编组。它检查编组是否有成员与精灵发生了碰撞，并在找到与精灵发生了碰撞的成员后就停止遍历编组
    # 如果没有发生碰撞，spritecollideany()将返回None。如果找到了与飞船发生碰撞的外星人，它就返回这个外星人
    if pygame.sprite.spritecollideany(ship,aliens):
        # print("ship hit!")
        ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
    
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets)
    
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    

    
