import os
import pygame
import settings


class Battery:
    def __init__(self, grid_x, grid_y):
        self.grid_position = [grid_x, grid_y]
        self.position = [
            self.grid_position[0] * settings.TILE_SIZE[0] + settings.TILE_SIZE[0] // 2,
            self.grid_position[1] * settings.TILE_SIZE[1] + settings.TILE_SIZE[1] // 2
        ]
        self.texture = None
        self._load_texture()

    def _load_texture(self):
        try:
            image_path = os.path.join("images", "battery.png")
            self.texture = pygame.image.load(image_path).convert_alpha()
            size = max(24, int(settings.TILE_SIZE[0] * 0.5))
            self.texture = pygame.transform.scale(self.texture, (size, size))
        except pygame.error:
            self.texture = pygame.Surface((24, 24), pygame.SRCALPHA)
            pygame.draw.rect(self.texture, (255, 215, 0), (2, 2, 20, 20))
            pygame.draw.rect(self.texture, (255, 255, 255), (8, 4, 8, 16), 2)

    def animation_update(self):
        return self.texture

    def get_position(self):
        return self.position

    def get_hitbox(self):
        size = max(20, int(settings.TILE_SIZE[0] * 0.5))
        return pygame.Rect(
            self.position[0] - size // 2,
            self.position[1] - size // 2,
            size,
            size
        )

    def get_draw_position(self):
        if self.texture is None:
            return self.position
        return (
            self.position[0] - self.texture.get_width() // 2,
            self.position[1] - self.texture.get_height() // 2
        )

    def interact(self):
        settings.battery_level = min(100, settings.battery_level + 30)
        settings.player_health = min(100, settings.player_health + 30)
        settings.pickup_message_timer = 120

        if settings.active_room is not None:
            if self in settings.active_room.item_list:
                settings.active_room.item_list.remove(self)
            if self in settings.active_room.interactables:
                settings.active_room.interactables.remove(self)
