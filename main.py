import pygame
import settings
import player
import rooms
import player_animation
import player_collison
import floor_textures
import enemies
import chest_animation
import torch
pygame.init()
big_font = pygame.font.Font("images/pixel_font.ttf", 28)
small_font = pygame.font.Font("images/pixel_font.ttf", 14)

#NOTE: the players position is calculated from the top left corner of the player sprite, so if the player sprite is 96x96, the player position is 48 pixels away from the center of the player sprite

#FS means frame size, the width and height of each sprite frame [0] = width, [1] = height

#create game window
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.TITLE)

#load floor sprite 


clock = pygame.time.Clock()
running = True

#Instantiate the Torch object

#Temporary test enemy instance for debugging the Mimic behavior
#test_mimic = enemies.Chest(100, 100)
#second_mimic = enemies.Chest(300,300)
#test_slime = enemies.Slime(400,400)
#second_slime = enemies.Slime(200,200)
#test_bat = enemies.Bat(300,300)
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
    
    for enemy in settings.active_room.enemy_list:
        player_collison.check_enemy_collision(enemy)

    player.check_pickup_collision()
    
    
    
    #STARTING THE FRAME



    screen.fill(settings.BACKGROUND_COLOUR) #starting the frame anew with a black background

    
    settings.active_room.display_room(screen)

    
    #DRAW PLAYER
    screen.blit(player_animation.player_moving_animation(), (settings.player_position[0]- player_animation.SPRITE_SIZE[0]//2, settings.player_position[1]- player_animation.SPRITE_SIZE[1]//2)) 
    pygame.draw.rect(screen, (255, 0, 0), player_collison.update_hitbox(), 2)
    
    #Update torch state (handles internal tracking and frame updates)
    #torch.update()
    #DRAW DARKNESS
    torch.update_torch_radius()
    torch.draw_darkness(screen)

    health_value = max(0, int(settings.player_health))
    health_text = big_font.render(f"Light Level: {health_value}", True, (255, 255, 255))
    screen.blit(health_text, (40, settings.SCREEN_HEIGHT - 60))

    controls = small_font.render("Controls: WASD to move, SPACE to interact", True, (255, 255, 255))
    screen.blit(controls, (20, settings.SCREEN_HEIGHT - 700))
    if settings.game_finished:
        end_screen = pygame.image.load("images/escaped_screen.png")
        end_screen = pygame.transform.scale(end_screen, (settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))
        screen.blit(end_screen, (0, 0))
    pygame.display.flip()
    clock.tick(settings.FPS)

