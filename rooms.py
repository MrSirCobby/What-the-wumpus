import random
import pygame
import settings
import enviroment


class Room:
    def __init__(self):
        self.linked_rooms = []
        self.walls_list = []
        self.grid = []
        
        self.generate_grid()
        self.append_walls()
        #print(self.wall_list)

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
    
    def get_grid(self):
        return self.grid
    
    def append_walls(self):
        for x, row in enumerate(self.grid):
            for y, tile in enumerate(row):
                if tile == 1:
                    wall = enviroment.Wall(y, x)
                    self.walls_list.append(wall)
        
    def change_active(self):
        global active_room
        active_room = self

    def get_wall_list(self):
        return self.walls_list 


    def display_room(self, screen):
        for wall in self.walls_list:
            screen.blit(wall.get_texture(self.grid), (wall.get_position()[0] - settings.TILE_SIZE[0]//2,
                                    wall.get_position()[1]- settings.TILE_SIZE[1]//2))
            



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