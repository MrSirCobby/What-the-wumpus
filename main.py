import pygame
import settings
import player
import rooms
import player_animation
import player_collison
import enviroment
pygame.init()

#NOTE: the players position is calculated from the top left corner of the player sprite, so if the player sprite is 96x96, the player position is 48 pixels away from the center of the player sprite

#FS means frame size, the width and height of each sprite frame [0] = width, [1] = height

#create game window
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.TITLE)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #INPUTS
    buttons_pressed = pygame.key.get_pressed() #fetches the keys pressed each frame and stores them in a list
    player.button_action(buttons_pressed) #function in player.py that adds an action to each key
  

    player_collison.player_collision()
    #STARTING THE FRAME
    screen.fill(settings.BACKGROUND_COLOUR) #starting the frame anew with a black background

    for entity in enviroment.collision_object:
        pygame.draw.rect(screen, (100, 100, 100), entity)

    #player animation
    player_image = player_animation.player_moving_animation()
    screen.blit(player_image, (settings.player_position[0]- player_animation.SPRITE_SIZE[0]//2, settings.player_position[1]- player_animation.SPRITE_SIZE[1]//2))
    #print(player.player_position) #debugging function to print the player position to the console
    pygame.draw.rect(screen, (255, 0, 0), player_collison.player_collision(), 2)
    
    pygame.display.flip()
    clock.tick(settings.FPS)
pygame.quit()