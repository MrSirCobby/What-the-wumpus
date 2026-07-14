import pygame
#import enemies

FLOOR_TILE_SIZE = 32
FLOOR_SCALE = 3
SCALED_FLOOR_SIZE = FLOOR_TILE_SIZE * FLOOR_SCALE


collision_object = []
side_walls = [
    pygame.Rect(0, 0, 20, 700)#left wall
    ,pygame.Rect(20, 0, 700, 20)#top wall
    ,pygame.Rect(700, 20, 20, 700)#right wall
    ,pygame.Rect(0,700,700,20)#bottom wall
    #test walls
]

class Wall():
    def __init__():
        pass

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



for entity in side_walls:
    collision_object.append(entity)

interactiables = []



    