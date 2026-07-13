import pygame
import enemies
from enemies import Mimic
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


class Chest(Mimic):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.open = False

        interactiables.append(self)

    def interact(self):
        if self.open:
            self.close_chest
        else:
            self.open_chest

    def open_chest(self):
        print("chest open")
        #stub
    
    def close_chest(self, position_x, position_y):
        self = enemies.Mimic(position_x, position_y)

    def return_hitbox(self):
        return pygame.Rect(-1000,-1000,0,0)
    