import pygame
from settings import *
from player import *
from rooms import *
pygame.init()

#FS means frame size, the width and height of each sprite frame [0] = width, [1] = height

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    buttons_pressed = pygame.key.get_pressed() #fetches the keys pressed each frame and stores them in a list
    button_action(buttons_pressed) #function in player.py that adds an action to each key

    #print(player_position) #debugging function to print the player position to the console

    screen.fill(BACKGROUND_COLOUR) #starting the frame anew with a black background

    #player animation
    player_image = player_moving_animation()
    screen.blit(player_image, (player_position[0] - player_image.get_width() // 2, player_position[1] - player_image.get_height() // 2))

    pygame.display.flip()
    clock.tick(FPS)
    animation_timer += 1
pygame.quit()