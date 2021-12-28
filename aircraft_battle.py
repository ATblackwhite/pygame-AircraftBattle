import pygame
from settings import Settings
from background import Background
from ship import Ship
from bullet import shipBullet
from enemy import Enemy
from time import sleep
from explode import Explode
from scoreboard import Scoreboard
from enemybullet import enemyBullet
from ship_explode import Ship_explode
from button import Button

# 添加相关背景音乐
pygame.init()
pygame.mixer.music.load("music/bgLoop.wav")
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1, 0)

class AircraftBattle:
    #管理游戏的类    
    def __init__(self):
        #初始化游戏
        pygame.init()
        self.settings = Settings()
        # 创建游戏窗口:pygame.display.set_mode(width, height)  返回Surface类
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        # 设置游戏标题
        pygame.display.set_caption("aircraftBattle") 
        self.ship = Ship(self)
        self.ship_bullets = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.explodes = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        # 背景交替滚动
        self.backgrounds = pygame.sprite.Group() 
        bg1 = Background(self)
        bg2 = Background(self)
        bg2.rect.y = -bg2.rect.height
        self.backgrounds.add(bg1, bg2)
        #设置自定义事件
        self.create_enemy = pygame.USEREVENT
        self.create_enemy_bullet = pygame.USEREVENT + 1
        #添加系统时钟
        self.clock = pygame.time.Clock()
        #设置定时器,每一秒出现一架敌机
        self.timer1 = pygame.time.set_timer(self.create_enemy,self.settings.create_enemy_time)
        self.timer2 = pygame.time.set_timer(self.create_enemy_bullet,self.settings.create_enemy_bullet_time)
        #设置得分版
        self.score = 0
        self.sb = Scoreboard(self)
        #设置游戏状态,0开始游戏，1游戏开始，2游戏结束
        self.game_active = 0
        #创建按钮
        self.play_button = Button(self, "play")
        self.replay_button = Button(self, "replay")
        

    def run_game(self):
        #游戏循环,保证游戏开始运行时不会立即终止
        while True:
            #设置刷新帧率
            self.clock.tick(self.settings.fps)
            self.__check_events()
            if self.game_active == 1:
                # 每次循环重绘屏幕
                # 判断碰撞与否
                self.__collide_bullet_enemy()
                #类更新
                self.backgrounds.update()
                self.ship.update()
                self.explodes.update()
                self.ship_bullets.update()
                self.enemys.update()
                self.enemy_bullets.update()
            #更新屏幕
            self.__update_screen()


    def __collide_bullet_enemy(self):
        collision_enemy = pygame.sprite.groupcollide(self.enemys, self.ship_bullets, True, True)
        for enemy in collision_enemy.keys():
            explode = Explode()
            explode.rect = enemy.rect
            self.explodes.add(explode)
            self.score += 15 * enemy.type
            self.sb.prep_score(self.score) 
        # 子弹相互碰撞
        collision_bullets = pygame.sprite.groupcollide(self.ship_bullets, self.enemy_bullets, True, True)
        for enemybullet in collision_bullets.keys():
            explode = Explode()
            explode.rect = enemybullet.rect
            self.explodes.add(explode)
            self.score += 5
            self.sb.prep_score(self.score)
        if pygame.sprite.spritecollideany(self.ship, self.enemys) or pygame.sprite.spritecollideany(self.ship, self.enemy_bullets):
            explode = Ship_explode(self)
            explode.rect = self.ship.rect
            self.explodes.add(explode)

            sound = pygame.mixer.Sound("music/planeExplode.wav")
            sound.play()
            # sleep(0.5)
            # print("ship hit!")
            # exit()

    def __update_screen(self):
        #更新屏幕上的图像，并切换到新屏幕
        self.backgrounds.draw(self.screen)
        if self.game_active == 1:
            self.ship.blitme()
            self.ship_bullets.draw(self.screen)
            self.explodes.draw(self.screen)
            self.enemy_bullets.draw(self.screen)
            # for bullet in self.ship_bullets.sprites():
            #     bullet.draw_bullet()
            self.sb.show_score()
            self.enemys.draw(self.screen)
        elif self.game_active == 0:
            self.play_button.draw_button()
        elif self.game_active == 2:
            self.replay_button.draw_button()
        #让最近绘制的屏幕可见
        pygame.display.update()

    # def _check_keydown_events(self, event):
    # 响应按键
    # if event.key == pygame.K_RIGHT:
    #     self.ship.moving_right = True
    # elif event.key == pygame.K_LEFT:
    #     self.ship.moving_left = True
    # elif event.key == pygame.K_UP:
    #     self.ship.moving_up = True
    # elif event.key == pygame.K_DOWN:
    #     self.ship.moving_down = True
    # if event.key == pygame.K_q:
    #     exit()
    # elif event.key == pygame.K_SPACE:
    #     self._fire_bullet()

    # def _check_keyup_events(self, event):
    #     #相应松开
    #     if event.key == pygame.K_RIGHT:
    #         self.ship.moving_right = False
    #     elif event.key == pygame.K_LEFT:
    #         self.ship.moving_left = False
    #     elif event.key == pygame.K_UP:
    #         self.ship.moving_up = False
    #     elif event.key == pygame.K_DOWN:
    #         self.ship.moving_down = False

    def __check_events(self):
        #响应按键和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                elif event.key == pygame.K_SPACE:
                    self.__fire_bullet()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.game_active == 0:
                    self.play_button.check_button(self,mouse_pos)
                elif self.game_active == 2:
                    self.replay_button.check_button(self,mouse_pos)
                    self.sb.prep_score(0)
            elif event.type == self.create_enemy:
                self.enemys.add(Enemy(self))
            elif event.type == self.create_enemy_bullet:
                for enemyplane in self.enemys:
                    if enemyplane.type <= 3:
                        self.enemy_bullets.add(enemyBullet(enemyplane))

        #     elif event.type == pygame.KEYDOWN:
        #         self._check_keydown_events(event)
        #     elif event.type == pygame.KEYUP:
        #         self._check_keyup_events(event)
  
    def __fire_bullet(self):
        #创建一颗子弹并添加到ship_bullets中
        # for i in (0,1,2): 
        #     bullet = Bullet()
        #     bullet.rect.bottom=self.ship.rect.top+i*20
        #     bullet.rect.centerx=self.ship.rect.centerx
        if len(self.ship_bullets) <= self.settings.bullet_allowed:
            self.ship_bullets.add(shipBullet(self))
            sound = pygame.mixer.Sound("music/laser.wav")
            sound.play()
     
    # 更新背景
    # def __update_background(self):
    #     self.backgrounds.update()
    #     self.backgrounds.draw(self.screen)


    # 更新子弹    
    # def __update_bullet(self):
    #     self.ship_bullets.update()
    #     #删除消失的子弹
    #     for bullet in self.ship_bullets.copy():
    #         if(bullet.rect.bottom < 0):
    #             self.ship_bullets.remove(bullet)
# 测试删除是否成功 print("remove bullet")

    # def __update_enemy(self):
    #     self.enemys.update()
    #     #删除消失的敌人
    #     for enemy in self.enemys.copy():
    #         if(enemy.rect.top > self.settings.screen_height):
    #             self.enemys.remove(enemy)
#测试删除是否成功  print("remove enemy")


if __name__ == '__main__':
    ab = AircraftBattle()
    ab.run_game()
