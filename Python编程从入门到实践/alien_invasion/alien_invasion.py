
# import sys
import os
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


# 修改当前工作目录为指定目录
os.chdir('Python编程从入门到实践\\alien_invasion')
# 打印修改后的当前工作目录
print("修改后的工作目录:", os.getcwd())

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 初始化设置对象
    ai_settings = Settings()
    # 调用pygame.display.set_mode()来创建一个名为screen的显示窗口
    # 实参(1200, 800)是一个元组，指定了游戏窗口的尺寸
    # 对象screen是一个surface。在Pygame中，surface是屏幕的一部分，用于显示游戏元素
    # display.set_mode()返回的surface表示整个游戏窗口
    # 激活游戏的动画循环后，每经过一次循环都将自动重绘这个surface
    # screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 设置背景色
    # Pygame默认创建一个黑色屏幕
    # bg_color = (230,230,230)
    # bg_color = ai_settings.bg_color

    # 创建 Clock 对象
    clock = pygame.time.Clock()

    ship = Ship(ai_settings,screen)
    # alien = Alien(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # 开始游戏的主循环
    while True:
        # # 监视键盘和鼠标事件
        # # 方法pygame.event.get()访问Pygame检测到的事件
        # for event in pygame.event.get():
        #     # 玩家单击游戏窗口的关闭按钮时，将检测到pygame.QUIT事件
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        # 通过隔离事件循环，将事件管理与游戏的其他方面（如更新屏幕）分离
        gf.check_evets(ai_settings,screen,ship,bullets)
        

        ship.update()


        # # 当你对Group调用update()时，Group将自动对其中的每个Sprite调用update()，因此代码行bullets.update()将为Groupbullets中的每颗子弹调用bullet.update()
        # bullets.update()

        # # 删除已消失的子弹
        # # 在for循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本
        # # 使用方法copy()来设置for循环，这让我们能够在循环中修改bullets
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings,aliens)
        # 将输出写入到终端而花费的时间比将图形绘制到游戏窗口花费的时间还多
        # print(len(bullets))

        # # 方法screen.fill()，用背景色填充屏幕；这个方法只接受一个实参：一种颜色
        # screen.fill(bg_color)
        # ship.blitme()

        # # 让最近绘制的屏幕可见
        # # 移动游戏元素时，pygame.display.flip()将不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果
        # pygame.display.flip()
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

        # 控制帧率为每秒 60 帧
        clock.tick(120)


run_game()