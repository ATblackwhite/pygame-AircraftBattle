from random import randint
class Settings:
    def __init__(self):
        #屏幕设置
        self.screen_width = 900
        self.screen_height = 800
        #设置刷新率
        self.fps = 60
        #设置背景
        # self.bg_color = (230,230,230)
        #飞船移动速度
  
        self.ship_xspeed = 8
        self.ship_yspeed = 8
        # 设置一次最多发射的子弹数量
        self.bullet_allowed = 5

        #设置敌人刷新时间间隔
        self.create_enemy_time = 700
        # 设置敌机发射子弹的频率
        self.create_enemy_bullet_time = 1300

        #设置按钮大小
        self.button_width = 200
        self.button_height = 50
        self.button_color = (255, 255, 255)
        self.button_text_color = (0, 0, 0)

        #计分板设置
        self.scoreboard_text_color = (255, 255, 255)