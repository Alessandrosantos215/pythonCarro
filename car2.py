import pygame
from pygame.locais import
import ramdom

pygame.init()

#create the window
width = 500
heigth = 500
screen_size = (width, heigth)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Car Game')

#colors
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

# road and marker sizes
road_width = 300
marker_width =10
marker_height = 50

# lane coordinates
left_lane = 150
center_lane =250
rigth_lane = 350
lanes = [left_lane, center_lane, rigth_lane]

#road and edge markers
road =(100,0, road_width,height)
left_edge_meker = (95, 0, marker_width, heith)
rigth_edge_meker = (395, 0, marker_width, heith)

#for animating movement of the lane markes
lane_marker_move_y = 0

#player´s starting coordinates
player_x = 250
player_y = 400

#frame settings
clock = pygame.time.clock()
fps = 120

#game settings
gameover = false
speed = 2
score = 0
 class Vehicle(pygame.sprite.Sprite):

     def _init_(self, imag, x, y):
         pygame.sprite.Aprite._init_(self)

         #scale the image down so it´s not wider than the lane linha 59 https://github.com/clickclackcode/python-car-game/blob/main/car_game.py