import random
import pygame
import settings
import enviroment



class Room:
    def __init__(self):
        self.linked_rooms = []
        self.walls = []
        self.grid = []
        self.wall_list = []
        
        self.generate_grid()
        self.append_walls()
        print(self.wall_list)

    def generate_grid(self):
        self.grid = [
    [1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,1],
    [1,0,0,1,0,2,0,0,1],
    [1,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,1,0,1],
    [1,0,3,0,0,0,1,0,1],
    [1,0,0,0,0,0,0,4,1],
    [1,1,1,1,1,1,1,1,1]
]
    def append_walls(self):
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                if tile == 1:
                    self.wall_list.append(pygame.Rect(x - settings.wall_size[0], 
                                                                   y - settings.wall_size[1],
                                                                    settings.wall_size[0],
                                                                    settings.wall_size[1]))



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



room_test = Room()