import random
import pygame

FLOOR_TILE_SIZE = 32
FLOOR_SCALE = 4
SCALED_FLOOR_SIZE = FLOOR_TILE_SIZE * FLOOR_SCALE

def load_floor_sprite():
    wall_floor_sheet = pygame.image.load("images/wall_floor.png")
    floor_frame = pygame.Surface((FLOOR_TILE_SIZE, FLOOR_TILE_SIZE), pygame.SRCALPHA)
    floor_frame.blit(wall_floor_sheet, (0, 0), (0, FLOOR_TILE_SIZE, FLOOR_TILE_SIZE, FLOOR_TILE_SIZE))  # Extract frame 1

    #scale floor size
    floor_frame = pygame.transform.scale(floor_frame, (SCALED_FLOOR_SIZE, SCALED_FLOOR_SIZE))
    return floor_frame

class Room:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_caves = []

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    
    def set_description(self, description):
        self.description = description
    def get_description(self):
        return self.description
    
    def set_linked_caves(self, linked_caves):
        self.linked_caves = linked_caves
    def get_linked_caves(self):
        return self.linked_caves


class TreasureRoom(Room):
    def __init__(self, name):
        super().__init__(name)
        self.treasure = True
    #stub


class MonsterRoom(Room):
    def __init__(self, name):
        super().__init__(name)
        self.monster = True
    #stub