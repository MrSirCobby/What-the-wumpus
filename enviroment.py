import pygame
import wall_textures
import settings
#import enemies

interactiables = []
collision_object = []


FLOOR_TILE_SIZE = 32
FLOOR_SCALE = 3
SCALED_FLOOR_SIZE = FLOOR_TILE_SIZE * FLOOR_SCALE


#FLOOR:
frames = []
floors_sheet = pygame.image.load("images/floors.png")
for row in range(2):
    for col in range(2):
        frame = pygame.Surface((FLOOR_TILE_SIZE, FLOOR_TILE_SIZE), pygame.SRCALPHA)
        frame.blit(floors_sheet, (0, 0), (col * FLOOR_TILE_SIZE, row * FLOOR_TILE_SIZE, FLOOR_TILE_SIZE, FLOOR_TILE_SIZE))
        frame = pygame.transform.scale(frame, [SCALED_FLOOR_SIZE, SCALED_FLOOR_SIZE])
        frames.append(frame)
frames = frames[:3]#there are only 3 frames in the sprite sheet, so we slice the list to only include those frames
animation = {
    "brick":0,
    "tile":1,
    "wood":2,
}

def load_floor_sprite(type):
    current_tile = animation[type]
    return frames[current_tile]


#WALLS:
#all wall tiles are 96*96





class Wall:
    def __init__(self, grid_x, grid_y):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.mask = 0
        self.texture = None

    def get_grid_position(self):
        return [self.grid_x, self.grid_y]
    
    def get_position(self):
        self.position = [self.grid_x * settings.TILE_SIZE[0], self.grid_y * settings.TILE_SIZE[1]]
        return self.position
    

    def get_texture(self, grid):

        left  = self.check_wall(grid, self.grid_x - 1, self.grid_y)
        right = self.check_wall(grid, self.grid_x + 1, self.grid_y)
        up    = self.check_wall(grid, self.grid_x, self.grid_y - 1)
        down  = self.check_wall(grid, self.grid_x, self.grid_y + 1)

        #MASK:
        if up: 
            self.mask |= 1
        if right:
            self.mask |= 2
        if down:
            self.mask |= 4
        if left:
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










    