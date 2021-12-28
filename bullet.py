import pygame
import random
from pygame.sprite import Sprite
class shipBullet(Sprite):
    #管理飞船发射的类
    def __init__(self,ab_game):
        #在飞船当前位置创建一个飞船对象
        # 精灵的初始化
        pygame.sprite.Sprite.__init__(self)
        self.screen = ab_game.screen
        self.image = pygame.image.load('images/' + self.randomBullet())
        self.rect = self.image.get_rect()
        self.rect.midtop = ab_game.ship.rect.midtop
        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        #向上移动子弹
        self.y -= self.speed
        #更新子弹位置
        self.rect.y = self.y
        if self.rect.y < 0 :
            self.kill()

    def randomBullet(self):
        ship_bullet_list = [('bullet1.png', 8), ('bullet2.png', 9), ('bullet3.png', 10), ('bullet4.png', 11), ('bullet5.png', 12), ('bullet6.png', 13) , ('bullet7.png', 14)]
        index = random.randint(0, len(ship_bullet_list) - 1)
        self.speed = ship_bullet_list[index][1]
        return ship_bullet_list[index][0]