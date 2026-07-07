import pygame
from settings import *
from player import *

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

    button_pressed = pygame.key.get_pressed()
    button_action(button_pressed)

    print(player_position)

    screen.fill((0, 0, 0))

    #player animation
    player_image = moving_animation()
    screen.blit(player_image, (player_position[0] - player_image.get_width() // 2, player_position[1] - player_image.get_height() // 2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()