import pygame as pg
import sys
from config import *
from game import Game
from player import Player
from level import Level

pg.init()

def main():
    game = Game(sky_blue)
    clock = pg.time.Clock()
    level = Level()
    player = Player(player_size,PLAYER_IMG_PATH_STAND,PLAYER_IMG_PATH_JUMP,player_position)
    game.set_game_caption(game_caption)
    while True:
        clock.tick(FPS)
        if game.new_game:
            level = Level()
            player = Player(player_size,PLAYER_IMG_PATH_STAND,PLAYER_IMG_PATH_JUMP,player_position)
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type==pg.QUIT or keys[pg.K_ESCAPE]:
                pg.quit()
                sys.exit()
        if keys[pg.K_f]:
            game.new_game = False
        if not game.new_game:
            game.draw(player,level)

if __name__ == "__main__":
    main()
