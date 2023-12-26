import os

# for imports #########################################################################################################
base_dir = os.path.dirname(os.path.abspath(__file__))

# for game #########################################################################################################
game_caption = "Endless Jumper"
FPS = 60

# colors #########################################################################################################
dark_grey_blue = (2,48,71)
grey_green_blue= (100,50,143)
sky_blue = (70,155,200)
black = (18,18,18)
red = (255,100,100)
green = (100,255,100)
# screen settings #########################################################################################################
screen_res = (1280,720)
border_thickness = screen_res[1]*0.05

# player settings #########################################################################################################
player_size = (screen_res[0]/18,screen_res[0]/9)
PLAYER_IMG_PATH_STAND = os.path.join(base_dir,'game_assets','imgs','P1_s.png')
PLAYER_IMG_PATH_JUMP = os.path.join(base_dir,'game_assets','imgs','P1_j.png')
player_position = ((screen_res[0] - player_size[0])/2 , screen_res[1]/2 - player_size[1])

# player motion #########################################################################################################
player_ver_speed = 14
player_hori_speed = 8

# over all motion #########################################################################################################
gravity_acc = 2


# level editor #########################################################################################################
platform_count = 8
platform_dim = (200,30)