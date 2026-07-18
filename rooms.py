import random
import pygame
import settings
import enviroment
import wall_textures

class Wall:
    def __init__(self, grid_x, grid_y):
        self.grid_position = [grid_x,grid_y]
        self.mask = 0
        self.texture = None
        self.position = [
            self.grid_position[0] * settings.TILE_SIZE[0],
            self.grid_position[1] * settings.TILE_SIZE[1]
        ]

    def get_grid_position(self):
        return [self.grid_position[0], self.grid_position[1]]
    
    def get_position(self):
        return self.position
    

    def get_texture(self, grid):

        left  = self.check_wall(grid, self.grid_position[0] - 1, self.grid_position[1])
        right = self.check_wall(grid, self.grid_position[0] + 1, self.grid_position[1])
        up    = self.check_wall(grid, self.grid_position[0], self.grid_position[1] - 1)
        down  = self.check_wall(grid, self.grid_position[0], self.grid_position[1] + 1)

        #MASK:
        if up == False: 
            self.mask |= 1
        if right == False:
            self.mask |= 2
        if down == False:
            self.mask |= 4
        if left == False:
            self.mask |= 8
        
        self.texture = wall_textures.texture_list[wall_textures.corresponding_dict[self.mask]]
        #print(self.texture)
        return self.texture
    
    def check_wall(self, grid, x, y):
        if x < 0 or y < 0:
            return False
        if x >= len(grid[0]) or y >= len(grid):
            return False

        return grid[y][x] == 1
    
    def get_hitbox(self):
        self.hitbox = pygame.Rect(
            self.position[0] - settings.TILE_SIZE[0] // 2,
            self.position[1] - settings.TILE_SIZE[1] // 2,
            settings.TILE_SIZE[0],
            settings.TILE_SIZE[1]
        )

        return self.hitbox
    

class Room:
    def __init__(self):
        self.linked_rooms = []
        self.walls_list = []
        self.grid = []
        self.wall_display = pygame.Surface((settings.SCREEN_WIDTH,settings.SCREEN_WIDTH),pygame.SRCALPHA)
        self.collision_objects = []
        
        self.generate_grid()
        self.update_walls()
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
    
    def update_walls(self):
        self.walls_list = []
        self.collision_objects = []
        enviroment.collision_object = []

        for x, row in enumerate(self.grid):
            for y, tile in enumerate(row):
                if tile == 1:
                    wall = Wall(y, x)
                    self.walls_list.append(wall)
        
        for wall in self.walls_list:
            # We use WALL_SPRITE_SIZE to perfectly centre the graphic over the hitbox
            draw_x = wall.get_position()[0] - wall_textures.WALL_SPRITE_SIZE[0] // 2
            draw_y = wall.get_position()[1] - wall_textures.WALL_SPRITE_SIZE[1] // 2
            
            self.wall_display.blit(wall.get_texture(self.grid), (draw_x, draw_y))
        
        for wall in self.walls_list:
            self.collision_objects.append(wall.get_hitbox())
            #enviroment.collision_object.append(hitbox)

    def change_active(self):
        global active_room
        active_room = self


    def get_wall_list(self):
        return self.walls_list 
    
    def get_collision_objects(self):
        return self.collision_objects



    def display_room(self, screen):
        screen.blit(self.wall_display, (0,0))
            
            



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
room_test.change_active()
room_test.generate_grid()
room_test.update_walls()
print(active_room.get_collision_objects())