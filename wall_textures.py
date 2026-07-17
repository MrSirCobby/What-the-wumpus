import pygame
WALL_SPRITE_FS = [32, 32] #width and height of each sprite frame
 #width and height of the player sprite when scaled up
texture_list = []
WALL_SPRITE_SIZE = [96,96]
sprite_sheet = pygame.image.load("images/wall.png") #loading the sprite sheet
#print(sprite_sheet.width,sprite_sheet.height)
#print(sprite_sheet.get_width(), sprite_sheet.get_height())

#Cuts each frame out of the sprite sheet and scales it up
for row in range(4):
    for col in range(4):
        frame = pygame.Surface((WALL_SPRITE_FS[0], WALL_SPRITE_FS[1]), pygame.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), (col * WALL_SPRITE_FS[0], row * WALL_SPRITE_FS[1], WALL_SPRITE_FS[0], WALL_SPRITE_FS[1]))
        frame = pygame.transform.scale(frame, WALL_SPRITE_SIZE)
        texture_list.append(frame)

texture_list = texture_list[:16]#there are only 14 frames in the sprite sheet, so we slice the list to only include those frames

#not_used = {
    #[0,1,3,5,6,7,9,15]#top
    #[0,1,4,5,11,12,14,15] #right
    #[0,2,3,4,5,6,10,11]#bottom
    #[0,1,2,3,4,7,8,14]#left



corresponding_dict = {
    0:13
    ,1:9
    ,2:12
    ,3:15
    ,4:10
    ,5:6
    ,6:11
    ,7:5
    ,8:8
    ,9:7
    ,10:14
    ,11:1
    ,12:3
    ,13:2
    ,14:4
    ,15:0
}