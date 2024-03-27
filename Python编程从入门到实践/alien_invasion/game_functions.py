import sys
import pygame

from bullet import Bullet


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
            

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_evets(ai_settings,screen,ship,bullets):
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
            

def update_screen(ai_settings,screen,ship,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 方法screen.fill()，用背景色填充屏幕；这个方法只接受一个实参：一种颜色
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    
    ship.blitme()

    # 让最近绘制的屏幕可见
    # 移动游戏元素时，pygame.display.flip()将不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    # 当你对Group调用update()时，Group将自动对其中的每个Sprite调用update()，因此代码行bullets.update()将为Groupbullets中的每颗子弹调用bullet.update()
    bullets.update()


    # 删除已消失的子弹
    # 在for循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本
    # 使用方法copy()来设置for循环，这让我们能够在循环中修改bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有到达限制，就发射一颗子弹""" 
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)