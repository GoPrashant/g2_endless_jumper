import pygame as pg
from config import *
import time

class Game():
    def __init__(self,bg_color):
        self.window = pg.display.set_mode(screen_res)
        self.bg_color = bg_color
        self.gravity_acc = gravity_acc
        self.game_stared = False
        self.new_game = False
        self.score = 0
        self.best_score = 0
        self.diff_reset = True

    def draw_border(self):
        top = pg.Rect(0, 0, screen_res[0], border_thickness)
        pg.draw.rect(self.window, dark_grey_blue, top)

        right = pg.Rect(screen_res[0] - border_thickness, 0, border_thickness, screen_res[1])
        pg.draw.rect(self.window, dark_grey_blue, right)

        bottom = pg.Rect(0, screen_res[1]-border_thickness, screen_res[0], border_thickness)
        pg.draw.rect(self.window, dark_grey_blue, bottom)

        left = pg.Rect(0, 0, border_thickness, screen_res[1])
        pg.draw.rect(self.window, dark_grey_blue, left)

    def draw_score(self):
        text = pg.font.SysFont('comicsansms',25).render("Score: "+ str(self.score), True, black)
        self.window.blit(text,(screen_res[0]/20,screen_res[1]/20))

    def draw_game_over(self):
        text_surface_go = pg.font.SysFont('comicsansms',55).render("GAME OVER", True, red)
        text_rect_go = text_surface_go.get_rect(center=(screen_res[0] / 2, screen_res[1] / 2.2))
        self.window.blit(text_surface_go,text_rect_go)
        text_surface_sc = pg.font.SysFont('comicsansms',50).render("Your Score: "+ str(self.score), True, green)
        text_rect_sc = text_surface_sc.get_rect(center=(screen_res[0] / 2, screen_res[1] / 1.8))
        self.window.blit(text_surface_sc,text_rect_sc)

        text_surface_sc = pg.font.SysFont('comicsansms',50).render("Press 'F' to restart the GAME", True, dark_grey_blue)
        text_rect_sc = text_surface_sc.get_rect(center=(screen_res[0] / 2, screen_res[1] / 3))
        self.window.blit(text_surface_sc,text_rect_sc)

    def draw(self,player,level):
        self.window.fill(self.bg_color)

        level.draw_level(self.window,self.game_stared,self)
        player.calculate_player_motion(level,self)
        player.draw_player(self.window)
        self.draw_score()
        self.draw_border()
        if player.player_rect.y>= screen_res[1] - player.player_size[1] - border_thickness:
            self.new_game = True
            self.draw_game_over()
            if self.score>self.best_score:
                self.best_score = self.score
            self.score = 0
            self.gravity_acc=2
        pg.display.update()
        

    def set_game_caption(self,caption):
        pg.display.set_caption(caption)


