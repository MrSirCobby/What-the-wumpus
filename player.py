import pygame
from settings import *
pygame.init()
global player_moving
player_moving = False
player_position = [640,360] #starting position of the player


#ANIMATION FOR PLAYER SPRITE
player_direction = "down" #starting direction of the player sprite
sprite_sheet = pygame.image.load("images/playersprite.png") #loading the sprite sheet


frames = []
PLAYER_SPRITE_FS = [32, 32] #width and height of each sprite frame
PLAYER_SIZE = [96, 96] #width and height of the player sprite when scaled up
#Cuts each frame out of the sprite sheet and scales it up
for row in range(4):
    for col in range(4):
        frame = pygame.Surface((PLAYER_SPRITE_FS[0], PLAYER_SPRITE_FS[1]), pygame.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), (col * PLAYER_SPRITE_FS[0], row * PLAYER_SPRITE_FS[1], PLAYER_SPRITE_FS[0], PLAYER_SPRITE_FS[1]))
        frame = pygame.transform.scale(frame, PLAYER_SIZE)
        frames.append(frame)

frames = frames[:14]#there are only 14 frames in the sprite sheet, so we slice the list to only include those frames

#stores the frame numbers for each animation
animation = {
    "right":[0,1,2],
    "left":[3,4,5],
    "idle":[6,7],
    "down":[8,9,10],
    "up":[11,12,13]
}

animation_frame = 0
animation_timer = 0
animation_speed = 8 #the number of frames to wait before switching to the next frame of animation, higher it is slower the animation

def button_action(buttons):
    if buttons[pygame.K_w]:
        move("up")
    if buttons[pygame.K_s]:
        move("down")
    if buttons[pygame.K_a]:
        move("left")
    if buttons[pygame.K_d]:
        move("right")

def move(direction):
    global player_moving
    global player_direction

    if direction == "up":
        player_position[1] -= player_speed
        player_direction = "up"
        player_moving = True
    elif direction == "down":
        player_position[1] += player_speed
        player_direction = "down"
        player_moving = True
    elif direction == "left":
        player_position[0] -= player_speed
        player_direction = "left"
        player_moving = True
    elif direction == "right":
        player_position[0] += player_speed
        player_direction = "right"
        player_moving = True

#ANIMATION FOR PLAYER
def player_moving_animation():
    global animation_frame
    global animation_timer

    if player_moving:
        current_animation = animation[player_direction] #assigns a list to current_animation based on the direction the player is moving and the corresonding frames of animation
    else:
        current_animation = animation["idle"] #same but if the player is not moving, it assigns the idle animation

    if animation_frame >= len(current_animation): #resets the animation frame if it exceeds the number of frames in the current animation
        animation_frame = 0


    if animation_timer >= animation_speed: #if the animation timer exceeds the animation speed, it resets the timer and moves to the next frame of animation
        animation_timer = 0
        animation_frame += 1
        if animation_frame >= len(current_animation): 
            animation_frame = 0

    return frames[current_animation[animation_frame]]