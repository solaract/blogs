import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self,ai_settings,screen) -> None:
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        # pygame.image.load()返回一个表示飞船的surface
        self.image = pygame.image.load('images/ship.bmp')
        #get_rect()获取相应surface的属性rect
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings

        # 将每艘新飞船放在屏幕底部中央
        # 在Pygame中，原点(0, 0)位于屏幕左上角，向右下方移动时，坐标值将增大
        # 要将游戏元素居中，可设置相应rect对象的属性center、centerx或centery
        # 要让游戏元素与屏幕边缘对齐，可使用属性top、bottom、left或right
        # 要调整游戏元素的水平或垂直位置，可使用属性x和y，它们分别是相应矩形左上角的x和y坐标
        # 将self.rect.centerx（飞船中心的x坐标）设置为表示屏幕的矩形的属性centerx
        self.rect.centerx = self.screen_rect.centerx
        # 将self.rect.bottom（飞船下边缘的y坐标）设置为表示屏幕的矩形的属性bottom
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)


        # 移动标志
        self.moving_right = False
        self.moving_left = False

    
    def update(self):
        """根据移动标志调整飞船的位置""" 
        # 更新飞船的center值，而不是rect
        # 限制飞船活动范围
        if self.moving_right and self.rect.right < self.screen_rect.right:
        # if self.moving_right == True:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
        # if self.moving_left == True:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        
        # 根据self.center更新rect对象 
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船""" 
        self.screen.blit(self.image,self.rect)

    
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx