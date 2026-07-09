import pygame
import settings
import enviroment

def update_Phitbox():
    #creates a rectangle that represents the players hitbox, which is used for collision detection
    global player_hitbox
    player_hitbox = pygame.Rect(settings.player_position[0] - settings.PLAYER_SIZE[0]//2, settings.player_position[1] - settings.PLAYER_SIZE[1]//2, settings.PLAYER_SIZE[0], settings.PLAYER_SIZE[1])
    return player_hitbox
    
def player_entity_check_x(dx):
    for entity in enviroment.collision_object:
        if player_hitbox.colliderect(entity):
            print(f"Collision detected on X axis! dx={dx}")
            if dx > 0:
<<<<<<< HEAD
                #player_hitbox.right = entity.right
                
                settings.player_position[0] = entity.left - settings.PLAYER_SIZE[0]//2
                update_Phitbox()

            elif dx < 0:
                #player_hitbox.left = entity.left
                
                settings.player_position[0] = entity.right + settings.PLAYER_SIZE[0]//2
                update_Phitbox()
=======
                player_hitbox.right = entity.left
                print("Stopped moving right")
            elif dx < 0:
                player_hitbox.left = entity.right
                print("Stopped moving left")
>>>>>>> 3f952dfe1d3ec5d54a37428288cfbda520c8cd06

def player_entity_check_y(dy):
    for entity in enviroment.collision_object:
        if player_hitbox.colliderect(entity):
            print(f"Collision detected on Y axis! dy={dy}")
            if dy > 0:
<<<<<<< HEAD
                #player_hitbox.bottom = entity.top
                
                settings.player_position[1] = entity.top - settings.PLAYER_SIZE[1]//2
                update_Phitbox()
                

            elif dy < 0:
                #player_hitbox.top = entity.bottom
                settings.player_position[1] = entity.bottom + settings.PLAYER_SIZE[1]//2
                update_Phitbox()
=======
                player_hitbox.bottom = entity.top
                print("Stopped moving down")
            elif dy < 0:
                player_hitbox.top = entity.bottom
                print("Stopped moving up")
>>>>>>> 3f952dfe1d3ec5d54a37428288cfbda520c8cd06
