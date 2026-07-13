import pygame
import settings


class Torch:
    #Torch class to manage the player's torchlight effect and battery level
    def __init__(self, x, y):
        self.position = [x, y]
        self.is_active = True
       
        self.battery_level = 100.0
        self.light_radius = 275 #The radius of the torch light circle (increase for a larger view)
       
        #sprite Sheet for torch.png
        self.TORCH_SPRITE_FS = [32, 16]   #Individual frame size
        self.TORCH_SPRITE_SIZE = [64, 32] #Upscaled scale
        self.frames = []
       
        #fade effect
        self.ambient_color = (10, 10, 10)
        self.light_mask = self._create_gradient_light()
       
    def _create_gradient_light(self):
        #generates a pre-rendered surface containing the smooth radial fade
        mask_size = self.light_radius * 2
        light_surface = pygame.Surface((mask_size, mask_size))
        light_surface.fill(self.ambient_color)
       
        for radius in range(self.light_radius, 0, -1):
            factor = 1.0 - (radius / self.light_radius)
            color_val = int(self.ambient_color[0] + (255 - self.ambient_color[0]) * factor)
            color = (color_val, color_val, color_val)
           
            pygame.draw.circle(
                light_surface,
                color,
                (self.light_radius, self.light_radius),
                radius
            )
        return light_surface


    def update(self):
        pass


    def draw_darkness(self, screen):
        #create darkness surface
        darkness = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
       
        #Fill surface with colour
        darkness.fill(self.ambient_color)
       
        #centre the pre-rendered gradient onto the player
        mask_x = int(settings.player_position[0]) - self.light_radius
        mask_y = int(settings.player_position[1]) - self.light_radius
       
        #Draw a circle of light around the player position
        darkness.blit(self.light_mask, (mask_x, mask_y))
       
        screen.blit(darkness, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
