import pygame
CHEST_SPRITE_FS = [32, 32] #width and height of each sprite frame
 #width and height of the player sprite when scaled up
frames = []
CHEST_SPRITE_SIZE = [64,64]
sprite_sheet = pygame.image.load("images/wall.png") #loading the sprite sheet
print(sprite_sheet.width,sprite_sheet.height)
#print(sprite_sheet.get_width(), sprite_sheet.get_height())

#Cuts each frame out of the sprite sheet and scales it up
for row in range(3):
    for col in range(3):
        frame = pygame.Surface((CHEST_SPRITE_FS[0], CHEST_SPRITE_FS[1]), pygame.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), (col * CHEST_SPRITE_FS[0], row * CHEST_SPRITE_FS[1], CHEST_SPRITE_FS[0], CHEST_SPRITE_FS[1]))
        frame = pygame.transform.scale(frame, CHEST_SPRITE_SIZE)
        frames.append(frame)

frames = frames[:7]#there are only 14 frames in the sprite sheet, so we slice the list to only include those frames

animation = {
    "closed":[0],
    "monster_open":[1,2,3],
    "chest_open":[4,5,6]
}