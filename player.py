import pygame
from settings import *
pygame.init()
global player_moving
player_moving = False
player_position = [640,360] #starting position of the player

player_direction = "down" #starting direction of the player sprite



def button_action(buttons):
    if buttons[pygame.K_w]:
        move("up")
    if buttons[pygame.K_s]:
        move("down")
    if buttons[pygame.K_a]:
        move("left")
    if buttons[pygame.K_d]:
        move("right")

def move(direction):
    global player_moving
    global player_direction

    if direction == "up":
        player_position[1] -= player_speed
        player_direction = "up"
        player_moving = True
    elif direction == "down":
        player_position[1] += player_speed
        player_direction = "down"
        player_moving = True
    elif direction == "left":
        player_position[0] -= player_speed
        player_direction = "left"
        player_moving = True
    elif direction == "right":
        player_position[0] += player_speed
        player_direction = "right"
        player_moving = True



