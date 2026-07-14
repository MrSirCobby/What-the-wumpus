import pygame

animation_speed = 8 #the number of frames to wait before switching to the next frame of animation, higher it is slower the animation
animation_frame = 0
animation_timer = 0
SLIME_SPRITE_FS = [32, 32] #width and height of each sprite frame
 #width and height of the player sprite when scaled up
frames = []
SLIME_SPRITE_SIZE = [64,64]
sprite_sheet = pygame.image.load("images/slime.png") #loading the sprite sheet

#print(sprite_sheet.get_width(), sprite_sheet.get_height())
print(sprite_sheet.width,sprite_sheet.height)
#Cuts each frame out of the sprite sheet and scales it up
for row in range(2):
    for col in range(2):
        frame = pygame.Surface((SLIME_SPRITE_FS[0], SLIME_SPRITE_FS[1]), pygame.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), (col * SLIME_SPRITE_FS[0], row * SLIME_SPRITE_FS[1], SLIME_SPRITE_FS[0], SLIME_SPRITE_FS[1]))
        frame = pygame.transform.scale(frame, SLIME_SPRITE_SIZE)
        frames.append(frame)

frames = frames[:3]#there are only 14 frames in the sprite sheet, so we slice the list to only include those frames

animation = {
    "idle":[0],
    "moving":[0,1,2]

}



