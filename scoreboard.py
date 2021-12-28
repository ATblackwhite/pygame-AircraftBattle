import pygame.font

class Scoreboard:
    #显示得分信息的类
    def __init__(self,ab_game):
        #初始化得分涉及的属性
        self.screen = ab_game.screen
        self.screen_rect = self.screen.get_rect()
        self.setings = ab_game.settings
        #显示得分信息时使用的字体设置
        self.text_color = self.setings.scoreboard_text_color
        self.font = pygame.font.SysFont(None, 48)
        #准备初始化得分图像
        self.prep_score(0)

    def prep_score(self,score):
        #将得分转换为一幅渲染的图像
        score_str = str(score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        #在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        #在屏幕上显示得分
        self.screen.blit(self.score_image, self.score_rect)
