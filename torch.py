import pygame
import settings


    
    
torch_light_radius = 275 #The radius of the torch light circle (increase for a larger view)
minimum_torch_radius = 70



#fade effect
torch_ambient_color = (10, 10, 10)

def update_torch_radius():
    global torch_light_radius
    torch_light_radius = max(settings.player_health * 2.5, minimum_torch_radius)
    if settings.player_health <= 0:
        torch_light_radius = 0
    
def create_gradient_light():
    #generates a pre-rendered surface containing the smooth radial fade
    mask_size = torch_light_radius* 2
    light_surface = pygame.Surface((mask_size, mask_size))
    light_surface.fill(torch_ambient_color)
    
    for radius in range(int(torch_light_radius), 0, -1):
        factor = 1.0 - (radius / torch_light_radius)
        color_val = int(torch_ambient_color[0] + (255 - torch_ambient_color[0]) * factor)
        color = (color_val, color_val, color_val)
        
        pygame.draw.circle(
            light_surface,
            color,
            (torch_light_radius, torch_light_radius),
            radius
        )
    return light_surface


def update():
    pass


def draw_darkness(screen):
    #create darkness surface
    darkness = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    
    #Fill surface with colour
    darkness.fill(torch_ambient_color)
    
    #centre the pre-rendered gradient onto the player
    mask_x = int(settings.player_position[0]) - torch_light_radius
    mask_y = int(settings.player_position[1]) - torch_light_radius
    
    #Draw a circle of light around the player position
    darkness.blit(create_gradient_light(), (mask_x, mask_y))
    
    screen.blit(darkness, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
