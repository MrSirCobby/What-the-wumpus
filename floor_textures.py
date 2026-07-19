import pygame
import wall_textures
import settings
#import enemies

#interactiables = []
#collision_object = []


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















    