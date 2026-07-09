import pygame
import settings
import player_collison
import enviroment
pygame.init()
global player_moving
player_moving = False
 #starting position of the player

player_direction = "down" #starting direction of the player sprite


def button_action(buttons):
    global player_moving
    global player_direction
    if buttons[pygame.K_w] or buttons[pygame.K_s] or buttons[pygame.K_a] or buttons[pygame.K_d]:
        if buttons[pygame.K_w]:
            player_direction = ("up")
            move("up")
        if buttons[pygame.K_s]:
            player_direction = ("down")
            move("down")
        if buttons[pygame.K_a]:
            player_direction = ("left")
            move("left")
        if buttons[pygame.K_d]:
            player_direction = ("right")
            move("right")
        player_moving = True
    else:
        player_moving = False


def move(direction):
    global player_moving
    global player_direction

    if direction == "up":
        settings.player_position[1] -= settings.player_speed
        player_collison.player_entity_check_y(settings.player_speed)
    elif direction == "down":
        settings.player_position[1] += settings.player_speed
        player_collison.player_entity_check_y(settings.player_speed)
    elif direction == "left":
        settings.player_position[0] -= settings.player_speed
        player_collison.player_entity_check_x(settings.player_speed)
    elif direction == "right":
        settings.player_position[0] += settings.player_speed
        player_collison.player_entity_check_x(settings.player_speed)



