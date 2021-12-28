import pygame
from pygame.sprite import Sprite
class Background(Sprite):
    def __init__(self, ab_game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/background.png')
        self.rect = self.image.get_rect()
        self.settings = ab_game.settings
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= self.settings.screen_height:
            self.rect.y = -self.settings.screen_height
    
    

    
