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

            if dx > 0:
                player_hitbox.right = entity.left

            elif dx < 0:
                player_hitbox.left = entity.right

def player_entity_check_y(dy):
    for entity in enviroment.collision_object:
        if player_hitbox.colliderect(entity):

            if dy > 0:
                player_hitbox.bottom = entity.top

            elif dy < 0:
                player_hitbox.top = entity.bottom