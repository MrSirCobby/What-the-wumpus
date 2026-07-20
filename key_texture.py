import pygame
import settings

KEY_SPRITE_FS = [32, 32] #width and height of each sprite frame
 #width and height of the player sprite when scaled up
texture_list = []

KEY_SPRITE_SIZE = [64,64]
sprite_sheet = pygame.image.load("images/keys.png") #loading the sprite sheet
#print(sprite_sheet.width, sprite_sheet.height)
#print(sprite_sheet.width,sprite_sheet.height)

#Cuts each frame out of the sprite sheet and scales it up
for row in range(2):
    for col in range(2):
        frame = pygame.Surface((KEY_SPRITE_FS[0], KEY_SPRITE_FS[1]), pygame.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), (col * KEY_SPRITE_FS[0], row * KEY_SPRITE_FS[1], KEY_SPRITE_FS[0], KEY_SPRITE_FS[1]))
        frame = pygame.transform.scale(frame, KEY_SPRITE_SIZE)
        texture_list.append(frame)

texture_list = texture_list[:4]#there are only 14 frames in the sprite sheet, so we slice the list to only include those frames

key_colour = {
    "yellow" : (0),
    "blue" : (1),
    "green" : (2),
    "pink" : (3)
}