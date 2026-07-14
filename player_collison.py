import pygame
import settings
import enviroment
debug = False
damage_tick =0
def update_hitbox():
    #creates a rectangle that represents the players hitbox, which is used for collision detection
    global player_hitbox
    player_hitbox = pygame.Rect(settings.player_position[0] - settings.PLAYER_SIZE[0]//2,
                                 settings.player_position[1] - settings.PLAYER_SIZE[1]//2, 
                                 settings.PLAYER_SIZE[0], 
                                 settings.PLAYER_SIZE[1])
    return player_hitbox
    

def check_enemy_collision(enemy):
    global damage_tick
    if settings.player_vulnerable:
        if player_hitbox.colliderect(enemy.return_hitbox()):
            settings.player_health -= enemy.get_damage()
            damage_tick = pygame.time.get_ticks()
            settings.player_vulnerable = False
            #change player appearance here
    
    
    if (pygame.time.get_ticks() - damage_tick) > settings.vulnerable_timer:
        settings.player_vulnerable = True







def player_entity_check_x(dx):
    global debug
    update_hitbox()
    for entity in enviroment.collision_object:
        if player_hitbox.colliderect(entity):
            if debug:
                print(f"Collision detected on X axis! dx={dx}")
            if dx > 0:
                settings.player_position[0] = entity.left - settings.PLAYER_SIZE[0]//2
                #player_hitbox.right = entity.left
                if debug:
                    print("Stopped moving right")
            elif dx < 0:
                settings.player_position[0] = entity.right + settings.PLAYER_SIZE[0]//2
                #player_hitbox.left = entity.right
                if debug:
                    print("Stopped moving left")


def player_entity_check_y(dy):
    global debug
    update_hitbox()
    for entity in enviroment.collision_object:
        if player_hitbox.colliderect(entity):
            if debug:
                print(f"Collision detected on Y axis! dy={dy}")
            if dy > 0:
                settings.player_position[1] = entity.top - settings.PLAYER_SIZE[1]//2
                #player_hitbox.bottom = entity.top
                if debug:
                    print("Stopped moving down")
            elif dy < 0:
                settings.player_position[1] = entity.bottom + settings.PLAYER_SIZE[1]//2
                #player_hitbox.top = entity.bottom
                if debug:
                    print("Stopped moving up")
