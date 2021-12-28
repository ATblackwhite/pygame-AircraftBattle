import pygame
class Explode(pygame.sprite.Sprite):
    #初始化爆炸
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load("images/explode"+str(i)+".png") for i in range(1,4)]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.ready_to_change = 0
        sound = pygame.mixer.Sound("music/enemyExplode.wav")
        sound.play()

    def update(self):
        if self.image_index < 2:
            self.ready_to_change += 1
            if self.ready_to_change % 5 == 0:
                self.image_index += 1
                self.image = self.images[self.image_index]
        else:
            self.ready_to_change += 1
            if self.ready_to_change % 5 == 0:
                self.kill()