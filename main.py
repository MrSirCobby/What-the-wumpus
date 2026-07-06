import pygame, sys
from settings import *
from player import *
from rooms import *
pygame.init()

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)


clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0)) #resets the screen to black every frame

    button_pressed = pygame.key.get_pressed() #sets button_pressed to all keys that are pressed
    player_action(button_pressed) #determines the players action based on the buttons pressed
    #print(player_position) debugging line to print the players position to the console


    pygame.draw.circle(screen, (255, 255, 255), (player_position[0], player_position[1]), 30) #placeholder for the player, draws a white circle at the players position
    
    


    pygame.display.update()
    clock.tick(FPS)
    




pygame.quit()