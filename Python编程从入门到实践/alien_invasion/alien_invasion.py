
import sys
import pygame

from settings import Settings


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
    bg_color = ai_settings.bg_color

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        # 方法pygame.event.get()访问Pygame检测到的事件
        for event in pygame.event.get():
            # 玩家单击游戏窗口的关闭按钮时，将检测到pygame.QUIT事件
            if event.type == pygame.QUIT:
                sys.exit()
        
        # 方法screen.fill()，用背景色填充屏幕；这个方法只接受一个实参：一种颜色
        screen.fill(bg_color)
        # 让最近绘制的屏幕可见
        # 移动游戏元素时，pygame.display.flip()将不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果
        pygame.display.flip()


run_game()