import pygame

animation_speed = 8 #the number of frames to wait before switching to the next frame of animation, higher it is slower the animation
animation_frame = 0
animation_timer = 0
BAT_SPRITE_FS = [32, 32] #width and height of each sprite frame
 #width and height of the player sprite when scaled up
frames = []
BAT_SPRITE_SIZE = [64,64]
sprite_sheet = pygame.image.load("images/bat.png") #loading the sprite sheet


#print(sprite_sheet.get_width(), sprite_sheet.get_height())
#print(sprite_sheet.width,sprite_sheet.height)
#Cuts each frame out of the sprite sheet and scales it up
for row in range(2):
    for col in range(2):
        frame = pygame.Surface((BAT_SPRITE_FS[0], BAT_SPRITE_FS[1]), pygame.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), (col * BAT_SPRITE_FS[0], row * BAT_SPRITE_FS[1], BAT_SPRITE_FS[0], BAT_SPRITE_FS[1]))
        frame = pygame.transform.scale(frame, BAT_SPRITE_SIZE)
        frames.append(frame)

frames = frames[:4]
animation = {
    "flapping":[0,1,2,3],


}
