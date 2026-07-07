import pygame
pygame.init()
global player_moving
player_moving = False
player_position = [640,360] #starting position of the player
player_speed = 2

#ANIMATION FOR PLAYER SPRITE
player_direction = "down"
sprite_sheet = pygame.image.load("images/playersprite.png")

frames = []
FRAME_SIZE = 32 #width and height of each sprite frame

#Cuts each frame out of the sprite sheet and scales it up
for row in range(4):
    for col in range(4):
        frame = pygame.Surface((FRAME_SIZE, FRAME_SIZE), pygame.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), (col * FRAME_SIZE, row * FRAME_SIZE, FRAME_SIZE, FRAME_SIZE))
        frame = pygame.transform.scale(frame, (96, 96))
        frames.append(frame)

frames = frames[:14]

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

def show(text): #used as a debug function to print text to the console
    print(text)

<<<<<<< HEAD
def player_action(buttons):
=======
def button_action(buttons):
    global player_moving
    global player_direction

    player_moving = False

>>>>>>> 18ac6ef0572c0686cbc94729af41101726dd867f
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
def moving_animation():
    global animation_frame
    global animation_timer

    if player_moving:
        current_animation = animation[player_direction]
    else:
        current_animation = animation["idle"]

    if animation_frame >= len(current_animation):
        animation_frame = 0

    animation_timer += 1

    if animation_timer >= 8:
        animation_timer = 0
        animation_frame += 1
        if animation_frame >= len(current_animation): 
            animation_frame = 0

    return frames[current_animation[animation_frame]]