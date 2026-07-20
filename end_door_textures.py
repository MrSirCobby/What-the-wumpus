import pygame
#import enemies
animation_speed = 8 #the number of frames to wait before switching to the next frame of animation, higher it is slower the animation
animation_frame = 0
animation_timer = 0
DOOR_SPRITE_FS = [32, 32] #width and height of each sprite frame
 #width and height of the player sprite when scaled up
frames = []
DOOR_SPRITE_SIZE = [156,156]
sprite_sheet = pygame.image.load("images/exit_door.png") #loading the sprite sheet

#print(sprite_sheet.get_width(), sprite_sheet.get_height())

#Cuts each frame out of the sprite sheet and scales it up
for row in range(3):
    for col in range(2):
        frame = pygame.Surface((DOOR_SPRITE_FS[0], DOOR_SPRITE_FS[1]), pygame.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), (col * DOOR_SPRITE_FS[0], row * DOOR_SPRITE_FS[1], DOOR_SPRITE_FS[0], DOOR_SPRITE_FS[1]))
        frame = pygame.transform.scale(frame, DOOR_SPRITE_SIZE)
        frames.append(frame)

frames = frames[:5]#there are only 14 frames in the sprite sheet, so we slice the list to only include those frames

animation = {
    "locked": [0],
    "open" : [1,2,3,4]

}




