import pygame
#import enemies
collision_object = []
side_walls = [
    pygame.Rect(0, 0, 20, 700)#left wall
    ,pygame.Rect(20, 0, 700, 20)#top wall
    ,pygame.Rect(700, 20, 20, 700)#right wall
    ,pygame.Rect(0,700,700,20)
    #test walls
]

for entity in side_walls:
    collision_object.append(entity)

interactiables = []



    