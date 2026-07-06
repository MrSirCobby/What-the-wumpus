import pygame
pygame.init()
global player_moving
player_moving = False
player_position = [640,360] #starting position of the player
player_speed = 10 

def show(text): #used as a debug function to print text to the console
    print(text)

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
    if direction == "up":
        player_position[1] -= player_speed
        player_moving = True
    elif direction == "down":
        player_position[1] += player_speed
        player_moving = True
    elif direction == "left":
        player_position[0] -= player_speed
        player_moving = True
    elif direction == "right":
        player_position[0] += player_speed
        player_moving = True
    else:
        player_moving = False


def moving_animation():
    if player_moving:
        # code for moving animation
        pass
    else:
        # code for idle animation
        pass
