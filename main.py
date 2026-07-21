import math
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
objective_font = pygame.font.Font("images/pixel_font.ttf", 18)

#NOTE: the players position is calculated from the top left corner of the player sprite, so if the player sprite is 96x96, the player position is 48 pixels away from the center of the player sprite

#FS means frame size, the width and height of each sprite frame [0] = width, [1] = height

#create game window
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.TITLE)

#load death screen image
dead_screen_image = pygame.image.load("images/died.png")
dead_screen_image = pygame.transform.scale(dead_screen_image, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

#load floor sprite 

def get_restart_button_rect():
    return pygame.Rect(settings.SCREEN_WIDTH // 2 - 120, settings.SCREEN_HEIGHT - 140, 240, 60)

#this function draws the restart button on the screen and returns the button's rectangle for collision detection
def draw_restart_button(screen):
    button_rect = get_restart_button_rect()
    pygame.draw.rect(screen, (220, 55, 55), button_rect, border_radius=12)
    pygame.draw.rect(screen, (255, 255, 255), button_rect, width=3, border_radius=12)
    label = big_font.render("Play Again", True, (255, 255, 255))
    label_x = button_rect.centerx - label.get_width() // 2
    label_y = button_rect.centery - label.get_height() // 2
    screen.blit(label, (label_x, label_y))
    return button_rect

#this function draws the interaction prompt above the closest interactable entity if the player is within range
def draw_interaction_prompt(screen):
    prompt_font = pygame.font.Font("images/pixel_font.ttf", 16)
    closest_interactable = None
    closest_distance = float("inf")

    for entity in settings.active_room.get_interactables():
        if not hasattr(entity, "get_position"):
            continue
        if isinstance(entity, rooms.Key):
            continue

        dx = settings.player_position[0] - entity.get_position()[0]
        dy = settings.player_position[1] - entity.get_position()[1]
        distance = math.sqrt(dx**2 + dy**2)

        if distance <= player.interactiable_radius and distance < closest_distance:
            closest_distance = distance
            closest_interactable = entity
    #if the closest interactable is within range, draw the prompt above it
    if closest_interactable is not None:
        x, y = closest_interactable.get_position()
        if isinstance(closest_interactable, rooms.End_Door):
            collected_keys = len(set(settings.key_list))
            prompt_text = prompt_font.render(f"{collected_keys}/{len(settings.required_keys)} keys", True, (255, 255, 255))
        else:
            prompt_text = prompt_font.render("Double Tap SPACE", True, (255, 255, 255))
        text_width = prompt_text.get_width()
        text_height = prompt_text.get_height()

        if hasattr(closest_interactable, "get_size"):
            size_x, size_y = closest_interactable.get_size()
            anchor_y = y - max(24, size_y // 2 + 6)
        else:
            anchor_y = y - 40

        prompt_x = x - text_width // 2
        prompt_y = anchor_y - text_height

        prompt_x = max(8, min(prompt_x, settings.SCREEN_WIDTH - text_width - 8))
        prompt_y = max(8, min(prompt_y, settings.SCREEN_HEIGHT - text_height - 8))

        screen.blit(prompt_text, (prompt_x, prompt_y))


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
    restart_button_rect = None

    for event in settings.event_get:
        if event.type == pygame.QUIT:
            running = False
        if settings.player_health <= 0 and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            restart_button_rect = get_restart_button_rect()
            if restart_button_rect.collidepoint(event.pos):
                rooms.reset_game_state()
                continue

    if not running:
        break

    #INPUTS
    if settings.player_health > 0:
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
    if settings.player_health > 0:
        screen.blit(player_animation.player_moving_animation(), (settings.player_position[0]- player_animation.SPRITE_SIZE[0]//2, settings.player_position[1]- player_animation.SPRITE_SIZE[1]//2)) 
    #pygame.draw.rect(screen, (255, 0, 0), player_collison.update_hitbox(), 2)
    
    #Update torch state (handles internal tracking and frame updates)
    if settings.player_health > 0:
        torch.update_torch_radius()
    torch.draw_darkness(screen)
    draw_interaction_prompt(screen)

    health_value = max(0, int(settings.player_health))
    health_text = big_font.render(f"Light Level: {health_value}", True, (255, 255, 255))
    screen.blit(health_text, (40, settings.SCREEN_HEIGHT - 60))

    collected_keys = len(set(settings.key_list))
    keys_needed = max(0, len(settings.required_keys) - collected_keys)

    if settings.game_finished:
        objective_lines = [
            "Objective: You escaped!",
            "Press QUIT to exit the game."
        ]
    elif collected_keys >= len(settings.required_keys):
        objective_lines = [
            "Objective: The exit is open!",
            "Walk through the exit door to escape."
        ]
    else:
        objective_lines = [
            "Objective: Find the 4 coloured keys.",
            f"Progress: {collected_keys}/{len(settings.required_keys)} keys found"
        ]

    objective_box_y = 20
    for index, line in enumerate(objective_lines):
        objective_text = objective_font.render(line, True, (255, 255, 255))
        screen.blit(objective_text, (20, objective_box_y + index * 26))

    controls = small_font.render("Controls: WASD to move, SPACE to interact", True, (255, 255, 255))
    screen.blit(controls, (400, settings.SCREEN_HEIGHT - 700))
    if settings.game_finished:
        end_screen = pygame.image.load("images/escaped_screen.png")
        end_screen = pygame.transform.scale(end_screen, (settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))
        screen.blit(end_screen, (0, 0))
    #player health check
    if settings.player_health <= 0:
        #display death screen
        screen.blit(dead_screen_image, (0, 0))
        draw_restart_button(screen)
    pygame.display.flip()
    clock.tick(settings.FPS)

