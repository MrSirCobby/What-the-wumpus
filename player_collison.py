import pygame
from settings import *
import player

def player_collision():
    #creates a rectangle that represents the players hitbox, which is used for collision detection
    player_hitbox = pygame.Rect(player.player_position[0], player.player_position[1], PLAYER_SIZE[0], PLAYER_SIZE[1])
    return player_hitbox
    
