import pygame
class enemyBullet(pygame.sprite.Sprite):
    #管理飞船发射的类
    def __init__(self,enemyplane):
        pygame.sprite.Sprite.__init__(self)
        self.settings = enemyplane.settings
        self.image = pygame.image.load("images/enemy_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = enemyplane.rect.midbottom
        self.speed = enemyplane.speed + 4

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > self.settings.screen_height:
            self.kill()




