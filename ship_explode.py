import pygame
class Ship_explode(pygame.sprite.Sprite):
    #初始化爆炸
    def __init__(self,ab_game):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load("images/planeDie"+str(i)+".png") for i in range(1,4)]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.ready_to_change = 0
        self.state = ab_game

    def update(self):
        if self.image_index < 2:
            self.ready_to_change += 1
            if self.ready_to_change % 7 == 0:
                self.image_index += 1
                self.image = self.images[self.image_index]
        else:
            self.ready_to_change += 1
            if self.ready_to_change % 7 == 0:
                self.kill()
                self.clear_game_state()
            # exit()

    def clear_game_state(self):
        self.state.game_active = 2
        self.state.enemys.empty()
        self.state.explodes.empty()
        self.state.enemy_bullets.empty()
        self.state.ship_bullets.empty()
        self.state.ship.center_ship()
        self.state.score = 0
        pygame.mouse.set_visible(True)