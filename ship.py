import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    #管理飞船的类
    def __init__(self,ab_game):
        #精灵的初始化
        pygame.sprite.Sprite.__init__(self)
        #初始化飞船并设置其初始位置
        self.screen = ab_game.screen
        self.settings = ab_game.settings
        self.screen_rect = ab_game.screen.get_rect()
        #加载飞船图像并获取其位置矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        #对于每艘新飞船，都将其放在屏幕底部中央
        # 移动标志
        # self.moving_right = False
        # self.moving_left = False
        # self.moving_up = False
        # self.moving_down = False



    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 根据移动标志调整飞船位置
        # 更新飞船而不是rect对象的值
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        #     self.rect.x += self.settings.ship_xspeed
        # if self.moving_left and self.rect.left > 0:
        #     self.rect.x -= self.settings.ship_xspeed
        # if self.moving_up and self.rect.y > 0:
        #     self.rect.y -= self.settings.ship_yspeed
        # if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        #     self.rect.y += self.settings.ship_yspeed
        # 根据self更新rect对象
        # self.rect.x = self.rect.x
        # self.rect.y = self.rect.y

        # 返回按键元组  
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.settings.ship_yspeed
        if keys[pygame.K_DOWN] and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_yspeed
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_xspeed
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.settings.ship_xspeed

    def center_ship(self):
        #让飞船在屏幕底端居中
        self.rect.midbottom = self.screen_rect.midbottom




        