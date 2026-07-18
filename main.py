import pygame
import settings
import player
import rooms
import player_animation
import player_collison
import enviroment
import enemies
import chest_animation
import torch
pygame.init()

#NOTE: the players position is calculated from the top left corner of the player sprite, so if the player sprite is 96x96, the player position is 48 pixels away from the center of the player sprite

#FS means frame size, the width and height of each sprite frame [0] = width, [1] = height

#create game window
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.TITLE)

#load floor sprite 
floor_frame = enviroment.load_floor_sprite("brick")

clock = pygame.time.Clock()
running = True

#Instantiate the Torch object

#Temporary test enemy instance for debugging the Mimic behavior
#test_mimic = enemies.Chest(100, 100)
#second_mimic = enemies.Chest(300,300)
#test_slime = enemies.Slime(400,400)
#second_slime = enemies.Slime(200,200)
test_room = rooms.Room()
test_room.change_active()
test_room.update_walls()
while running:
    settings.event_get = pygame.event.get()
    for event in settings.event_get:
        if event.type == pygame.QUIT:
            running = False
    #INPUTS
    buttons_pressed = pygame.key.get_pressed() #fetches the keys pressed each frame and stores them in a list
    player.button_action(buttons_pressed) #function in player.py that adds an action to each key

    #UPDATE HIBOXES:
    for enemy in enemies.ENEMY_LIST:
        enemy.update_movement()
        enemy.update_hitbox()
    
    player_collison.update_hitbox()
    
    for enemy in enemies.ENEMY_LIST:
        player_collison.check_enemy_collision(enemy)
    
    
    
    #STARTING THE FRAME
    screen.fill(settings.BACKGROUND_COLOUR) #starting the frame anew with a black background

    for y in range(0, settings.SCREEN_HEIGHT, enviroment.SCALED_FLOOR_SIZE):
        for x in range(0, settings.SCREEN_WIDTH, enviroment.SCALED_FLOOR_SIZE):
            screen.blit(floor_frame, (x, y))

    test_room.display_room(screen)
    # Draw WALLS
    #for wall in enviroment.collision_object:
       # pygame.draw.rect(screen, (250, 100, 100), wall)
    





    #DRAW ENEMIES
    for enemy in enemies.ENEMY_LIST:
        enemy.display_animation(screen)
        pygame.draw.rect(screen, (255, 0, 0), enemy.return_hitbox(), 2)


    #DRAW INTERACTABLES
    for entity in enviroment.interactiables:
        entity.display_animation(screen)
        pygame.draw.rect(screen, (255, 0, 0), entity.return_hitbox(), 2)

    #wprint(enemies.ENEMY_LIST)
    
    #DRAW PLAYER
    screen.blit(player_animation.player_moving_animation(), (settings.player_position[0]- player_animation.SPRITE_SIZE[0]//2, settings.player_position[1]- player_animation.SPRITE_SIZE[1]//2)) 
    pygame.draw.rect(screen, (255, 0, 0), player_collison.update_hitbox(), 2)
    
    #Update torch state (handles internal tracking and frame updates)
    #torch.update()
    #DRAW DARKNESS
    torch.update_torch_radius()
    torch.draw_darkness(screen)

    
    pygame.display.flip()
    clock.tick(settings.FPS)
pygame.quit()