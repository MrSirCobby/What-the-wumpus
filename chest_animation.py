import pygame
import enemies
animation_speed = 8 #the number of frames to wait before switching to the next frame of animation, higher it is slower the animation
animation_frame = 0
animation_timer = 0
PLAYER_SPRITE_FS = [32, 32] #width and height of each sprite frame
 #width and height of the player sprite when scaled up
frames = []
SPRITE_SIZE = [96,96]
sprite_sheet = pygame.image.load("images/chest.png") #loading the sprite sheet

#print(sprite_sheet.get_width(), sprite_sheet.get_height())

#Cuts each frame out of the sprite sheet and scales it up
for row in range(3):
    for col in range(3):
        frame = pygame.Surface((PLAYER_SPRITE_FS[0], PLAYER_SPRITE_FS[1]), pygame.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), (col * PLAYER_SPRITE_FS[0], row * PLAYER_SPRITE_FS[1], PLAYER_SPRITE_FS[0], PLAYER_SPRITE_FS[1]))
        frame = pygame.transform.scale(frame, SPRITE_SIZE)
        frames.append(frame)

frames = frames[:7]#there are only 14 frames in the sprite sheet, so we slice the list to only include those frames

animation = {
    "closed":[0],
    "monster_open":[1,2,3],
    "chest_open":[6,7]
}



