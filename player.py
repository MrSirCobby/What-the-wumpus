import pygame
import settings
import player_collison
import floor_textures
import math
#import rooms
#pygame.init()
global player_moving
player_moving = False
 #starting position of the player
interactiable_radius = 100


player_direction = "down" #starting direction of the player sprite


def button_action(buttons):
    global player_moving
    global player_direction
    if buttons[pygame.K_w] or buttons[pygame.K_s] or buttons[pygame.K_a] or buttons[pygame.K_d]:
        if buttons[pygame.K_a]:
            player_direction = ("left")
            move("left")
        if buttons[pygame.K_d]:
            player_direction = ("right")
            move("right")
        if buttons[pygame.K_w]:
            player_direction = ("up")
            move("up")
        if buttons[pygame.K_s]:
            player_direction = ("down")
            move("down")
        player_moving = True
    else:
        player_moving = False
    for event in settings.event_get:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                check_interactables()
                
        
        #print("space")


def check_interactables():
    for entity in settings.active_room.get_interactiables:
        dx = settings.player_position[0] - entity.get_position()[0]
        dy = settings.player_position[1] - entity.get_position()[1]
        distance = math.sqrt(dx**2 + dy**2)
        if distance <= interactiable_radius:
            entity.interact()

def move(direction):
    global player_moving
    global player_direction

    
    if direction == "left":
        settings.player_position[0] -= settings.player_speed
        player_collison.player_entity_check_x(-settings.player_speed)
    if direction == "right":
        settings.player_position[0] += settings.player_speed
        player_collison.player_entity_check_x(settings.player_speed)
    if direction == "up":
        settings.player_position[1] -= settings.player_speed
        player_collison.player_entity_check_y(-settings.player_speed)
    if direction == "down":
        settings.player_position[1] += settings.player_speed
        player_collison.player_entity_check_y(settings.player_speed)

def check_health():
    if settings.player_health <= 0:
        #player dead
        print("player dead")
