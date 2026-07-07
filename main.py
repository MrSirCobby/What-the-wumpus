import pygame, sys
from settings import *
from player import *
<<<<<<< HEAD
from rooms import *
=======

>>>>>>> 18ac6ef0572c0686cbc94729af41101726dd867f
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
<<<<<<< HEAD
    screen.fill((0, 0, 0)) #resets the screen to black every frame

    button_pressed = pygame.key.get_pressed() #sets button_pressed to all keys that are pressed
    player_action(button_pressed) #determines the players action based on the buttons pressed
    #print(player_position) debugging line to print the players position to the console


    pygame.draw.circle(screen, (255, 255, 255), (player_position[0], player_position[1]), 30) #placeholder for the player, draws a white circle at the players position
    
    


    pygame.display.update()
    clock.tick(FPS)
    


=======

    button_pressed = pygame.key.get_pressed()
    button_action(button_pressed)

    print(player_position)

    screen.fill((0, 0, 0))
>>>>>>> 18ac6ef0572c0686cbc94729af41101726dd867f

    #player animation
    player_image = moving_animation()
    screen.blit(player_image, (player_position[0] - player_image.get_width() // 2, player_position[1] - player_image.get_height() // 2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()