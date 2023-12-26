import pygame as pg
from config import *
import time


class Player():
    def __init__(self,player_size,PLAYER_IMG_PATH_STAND,PLAYER_IMG_PATH_JUMP,player_position):
        self.player_size = player_size

        # player facing right
        # standing / runing
        self.PLAYER_IMG_STAND_R = pg.image.load(PLAYER_IMG_PATH_STAND)
        self.PLAYER_STAND_R = pg.transform.scale(self.PLAYER_IMG_STAND_R, self.player_size)
        # jumping
        self.PLAYER_IMG_JUMP_R = pg.image.load(PLAYER_IMG_PATH_JUMP)
        self.PLAYER_JUMP_R = pg.transform.scale(self.PLAYER_IMG_JUMP_R, self.player_size)

        #player facing left
        # standing / runing
        self.PLAYER_IMG_STAND_L = pg.transform.flip(pg.image.load(PLAYER_IMG_PATH_STAND), True, False)
        self.PLAYER_STAND_L = pg.transform.scale(self.PLAYER_IMG_STAND_L, self.player_size)
        # jumping
        self.PLAYER_IMG_JUMP_L = pg.transform.flip(pg.image.load(PLAYER_IMG_PATH_JUMP), True, False)
        self.PLAYER_JUMP_L = pg.transform.scale(self.PLAYER_IMG_JUMP_L, self.player_size)
        
        self.current_img = self.PLAYER_STAND_R
        self.player_rect = pg.Rect(player_position[0],player_position[1], self.player_size[0], self.player_size[1])
        self.x_vel = 0
        self.y_vel = 0
        self.y_time = 0

    def player_verticle_motion(self,keys,level,game):
        result = False
        for plat in level.platform_list:
            part_1 = self.player_rect.y + self.player_size[1] <= plat.platform_pos[1] + 5
            part_3 = plat.platform_pos[1] <= self.player_rect.y + self.y_vel + self.player_size[1]
            part_2 = plat.platform_pos[0] - self.player_size[0]<= self.player_rect.x <= plat.platform_pos[0] + platform_dim[0]

            if part_1 and part_2 and part_3:
                result = True
                col_plat = plat.platform_pos
        
        if self.y_time == 0:
            if keys[pg.K_w]:
                self.y_vel = - player_ver_speed
                self.y_time = time.time()
                game.game_stared = True
            elif self.y_vel == game.gravity_acc:
                self.y_time = time.time()

        elif self.player_rect.y + self.y_vel >= screen_res[1] - self.player_size[1] - border_thickness:
            self.y_time = 0
            self.y_vel = 0
            self.player_rect.y = screen_res[1] - self.player_size[1] - border_thickness
            game.game_stared = False

        elif result and self.y_vel>0 and self.y_vel != game.gravity_acc:
            self.y_time = 0
            self.y_vel = game.gravity_acc
            self.player_rect.y = col_plat[1] - self.player_size[1]

        else:
            self.y_vel += game.gravity_acc*(time.time()-self.y_time)

        if keys[pg.K_s] and self.y_time != 0:
            self.y_vel += 1
            
    def player_horizontal_motion(self,keys):
        if keys[pg.K_a]:
            self.x_vel = - player_hori_speed
        if keys[pg.K_d]:
            self.x_vel = player_hori_speed
        
        if self.x_vel>0:
            self.x_vel -= 0.5
        elif self.x_vel<0:
            self.x_vel += 0.5

    def calculate_player_motion(self,level,game):
        keys = pg.key.get_pressed()
        self.player_verticle_motion(keys,level,game)
        self.player_horizontal_motion(keys)

        self.player_rect.x += self.x_vel
        self.player_rect.y += self.y_vel
    
    def draw_player(self,window):
        # player standing
        if self.y_vel == 0:
            if self.x_vel < 0:
                self.current_img = self.PLAYER_STAND_L
            elif self.x_vel > 0:
                self.current_img = self.PLAYER_STAND_R
            elif self.x_vel == 0:
                if self.current_img == self.PLAYER_JUMP_L:
                    self.current_img = self.PLAYER_STAND_L
                elif self.current_img == self.PLAYER_JUMP_R:
                    self.current_img = self.PLAYER_STAND_R
        # player jumping
        elif self.y_vel != 0:
            if self.x_vel < 0:
                self.current_img = self.PLAYER_JUMP_L
            elif self.x_vel > 0:
                self.current_img = self.PLAYER_JUMP_R
            elif self.x_vel == 0:
                if self.current_img == self.PLAYER_STAND_L:
                    self.current_img = self.PLAYER_JUMP_L
                elif self.current_img == self.PLAYER_STAND_R:
                    self.current_img = self.PLAYER_JUMP_R

        # player img drawing
        window.blit(self.current_img, (self.player_rect.x,self.player_rect.y))