import pygame
import random
class Enemy(pygame.sprite.Sprite):
    # 初始化敌人
    def __init__(self, ab_game):
        pygame.sprite.Sprite.__init__(self)
        self.settings = ab_game.settings
        self.image = pygame.image.load('images/' + self.randomEnemy())
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.right)
        self.rect.bottom = 0

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > self.settings.screen_height:
            self.kill()

    def randomEnemy(self):
        enemy_list = ['enemy1.png', 'enemy2.png', 'enemy3.png', 'enemy4.png', 'enemy5.png', 'enemy6.png']
        index = random.randint(0, len(enemy_list) - 1)
        self.type = index + 1
        self.speed = index + 2
        return enemy_list[index]


