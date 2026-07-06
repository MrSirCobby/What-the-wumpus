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
    pygame.draw.circle(screen, (255, 255, 255), (player_position[0], player_position[1]), 30)
    pygame.display.flip()
    clock.tick(FPS)
    screen.fill((0, 0, 0))


pygame.quit()