from typing import Any
import pygame as pg
from config import *
import random
import time



class Platform():
    def __init__(self,platform_dim,platform_pos):
        self.platform_dim = platform_dim
        self.platform_pos = platform_pos



class Level():
    def __init__(self):
        self.platform_list = []
    
    def draw_platforms(self,game):
        if len(self.platform_list) < platform_count:
            for a in range(platform_count - len(self.platform_list)):
                if len(self.platform_list)>0:
                    curr = self.platform_list[-1]
                    
                    x_cor_left = random.randint(max(curr.platform_pos[0]-400,border_thickness),max(curr.platform_pos[0]-platform_dim[0],border_thickness))
                    x_cor_right = min(random.randint(curr.platform_pos[0]+platform_dim[0],curr.platform_pos[0]+400),screen_res[0]-border_thickness-platform_dim[0])
                    if x_cor_left == border_thickness:
                        x_cor = x_cor_right
                    elif x_cor_right == screen_res[0]-border_thickness-platform_dim[0]:
                        x_cor = x_cor_left
                    else:
                        x_cor = random.choice([x_cor_left,x_cor_right])
                    platform_pos = [x_cor,
                                    random.randint(curr.platform_pos[1]-platform_dim[0],curr.platform_pos[1]-200)]
                else:
                    platform_pos = [(screen_res[0]-platform_dim[0])/2,(screen_res[1])/2]
                self.platform_list.append(Platform(platform_dim,platform_pos))

        if self.platform_list[0].platform_pos[1] > screen_res[1]:
            self.platform_list.pop(0)
            game.score +=1 
    def draw_level(self,window,game_stared,game):
        self.draw_platforms(game)
        for plat in self.platform_list:
            plat_rect = pg.Rect(plat.platform_pos[0], plat.platform_pos[1], plat.platform_dim[0], plat.platform_dim[1])
            pg.draw.rect(window, grey_green_blue, plat_rect)
            if game_stared:
                plat.platform_pos[1] += game.gravity_acc
        if game.score%7==0 and game.score!=0 and game.diff_reset and game.gravity_acc<8:
            game.gravity_acc += 1
            game.diff_reset=False
            print('diff increased',game.gravity_acc)

        if not game.diff_reset and game.score%7!=0:
            print('diff reset')
            game.diff_reset =True

    