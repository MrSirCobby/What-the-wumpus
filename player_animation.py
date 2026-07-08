import pygame
import player
from settings import *
#FS means frame size, the width and height of each sprite frame [0] = width, [1] = height
animation_speed = 8 #the number of frames to wait before switching to the next frame of animation, higher it is slower the animation
animation_frame = 0
animation_timer = 0
PLAYER_SPRITE_FS = [32, 32] #width and height of each sprite frame
 #width and height of the player sprite when scaled up
frames = []

sprite_sheet = pygame.image.load("images/playersprite.png") #loading the sprite sheet


#Cuts each frame out of the sprite sheet and scales it up
for row in range(4):
    for col in range(4):
        frame = pygame.Surface((PLAYER_SPRITE_FS[0], PLAYER_SPRITE_FS[1]), pygame.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), (col * PLAYER_SPRITE_FS[0], row * PLAYER_SPRITE_FS[1], PLAYER_SPRITE_FS[0], PLAYER_SPRITE_FS[1]))
        frame = pygame.transform.scale(frame, PLAYER_SIZE)
        frames.append(frame)

frames = frames[:14]#there are only 14 frames in the sprite sheet, so we slice the list to only include those frames

animation = {
    "right":[0,1,2],
    "left":[3,4,5],
    "idle":[6,7],
    "down":[8,9,10],
    "up":[11,12,13]
}


def player_moving_animation():
    global animation_frame
    global animation_timer
    if player.player_moving:
        current_animation = animation[player.player_direction]
    else:
        current_animation = animation["idle"]

    if animation_frame >= len(current_animation):
        animation_frame = 0

    animation_timer += 1

    if animation_timer >= animation_speed: #if the animation timer exceeds the animation speed, it resets the timer and moves to the next frame of animation
        animation_timer = 0
        animation_frame += 1
        if animation_frame >= len(current_animation): 
            animation_frame = 0

    return frames[current_animation[animation_frame]]