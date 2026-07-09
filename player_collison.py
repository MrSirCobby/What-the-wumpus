import pygame
import settings
import enviroment

def player_collision():
    #creates a rectangle that represents the players hitbox, which is used for collision detection
    global player_hitbox
    player_hitbox = pygame.Rect(settings.player_position[0] - settings.PLAYER_SIZE[0]//2, settings.player_position[1] - settings.PLAYER_SIZE[1]//2, settings.PLAYER_SIZE[0], settings.PLAYER_SIZE[1])
    return player_hitbox
    
def player_entity_check_x(dx):

    for entity in enviroment.collision_object:
        if player_hitbox.colliderect(entity):
            print(f"Collision detected on X axis! dx={dx}")
            if dx > 0:
                player_hitbox.right = entity.left
                print("Stopped moving right")
            elif dx < 0:
                player_hitbox.left = entity.right
                print("Stopped moving left")

def player_entity_check_y(dy):
    for entity in enviroment.collision_object:
        if player_hitbox.colliderect(entity):
            print(f"Collision detected on Y axis! dy={dy}")
            if dy > 0:
                player_hitbox.bottom = entity.top
                print("Stopped moving down")
            elif dy < 0:
                player_hitbox.top = entity.bottom
                print("Stopped moving up")