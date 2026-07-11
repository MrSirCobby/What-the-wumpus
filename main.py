import pygame
import settings
import player
import rooms
import player_animation
import player_collison
import enviroment
import camera_updated
import enemies
pygame.init()

#NOTE: the players position is calculated from the top left corner of the player sprite, so if the player sprite is 96x96, the player position is 48 pixels away from the center of the player sprite

#FS means frame size, the width and height of each sprite frame [0] = width, [1] = height

#create game window
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.TITLE)

#load floor sprite 
floor_frame = rooms.load_floor_sprite()

clock = pygame.time.Clock()
running = True

test_slime = enemies.Enemy(100, 2, 100, 100, 30, 30)

#camera
camera_updated.set_camera(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #INPUTS
    buttons_pressed = pygame.key.get_pressed() #fetches the keys pressed each frame and stores them in a list
    player.button_action(buttons_pressed) #function in player.py that adds an action to each key


    player_collison.update_hitbox()
    
    #update camera to follow player
    camera_updated.update_camera(settings.player_position[0], settings.player_position[1])
    
    #STARTING THE FRAME
    screen.fill(settings.BACKGROUND_COLOUR) #starting the frame anew with a black background

    #draw tiled floor with camera offset
    floor_size = rooms.SCALED_FLOOR_SIZE
    #calculate the starting tile position based on camera
    start_x = int(camera_updated.camera_x // floor_size) * floor_size # the cordante of the tile the topleft corner of the frame is on
    start_y = int(camera_updated.camera_y // floor_size) * floor_size
    #draw floor tiles starting from the calculated position and extending beyond the screen size to ensure coverage
    for x in range(start_x - floor_size, start_x + settings.SCREEN_WIDTH + floor_size * 2, floor_size):
        for y in range(start_y - floor_size, start_y + settings.SCREEN_HEIGHT + floor_size * 2, floor_size):
            adjusted_pos = camera_updated.apply(x, y)
            screen.blit(floor_frame, adjusted_pos)

    # Draw walls with camera offset
    for entity in enviroment.collision_object:
        adjusted_wall = camera_updated.apply_rect(entity)
        #print(entity)
        pygame.draw.rect(screen, (100, 100, 100), adjusted_wall)


    #player animation
    player_image = player_animation.player_moving_animation()
    player_screen_pos = camera_updated.apply(settings.player_position[0], settings.player_position[1]) #this function takes the players position and applies the camera offset to it, so that the player is drawn in the correct position on the screen
    screen.blit(player_image, (player_screen_pos[0]- player_animation.SPRITE_SIZE[0]//2, player_screen_pos[1]- player_animation.SPRITE_SIZE[1]//2)) 
    #print(player.player_position) #debugging function to print the player position to the console


    
    # Draw player hitbox with camera offset
    hitbox_adjusted = camera_updated.apply_rect(player_collison.update_hitbox())
    pygame.draw.rect(screen, (255, 0, 0), hitbox_adjusted, 2)

    hitbox_adjusted = camera_updated.apply_rect(test_slime.update_hitbox())
    pygame.draw.rect(screen, (255, 0, 0), hitbox_adjusted, 2)

    
    pygame.display.flip()
    clock.tick(settings.FPS)
pygame.quit()