import pygame
import settings
import chest_animation

class Enemy:
    def __init__(self, health, damage, movement_speed):
        self.health = health
        self.damage = damage
        self.speed = movement_speed
        self.position = None
    
    def set_position(self, position_x, position_y):
        self.position = [position_x, position_y]

    def move_toward_player(self):
            if self.position[0] < settings.player_position[0]:
                self.move("right")
                #self.position[0] += self.speed
            elif self.position[0] > settings.player_position[0]:
                self.move("left")
                #self.position[0] -= self.speed

            if self.position[1] < settings.player_position[1]:
                self.move("down")
                #self.position[1] += self.speed
            elif self.position[1] > settings.player_position[1]:
                self.move("up")
                #self.position[1] -= self.speed

    def move(self, direction):
        if direction == "left":
            self.position[0] -= self.speed
            #player_collison.player_entity_check_x(-settings.player_speed)
        if direction == "right":
            self.position[0] += self.speed
            #player_collison.player_entity_check_x(settings.player_speed)
        if direction == "up":
            self.position[1] -= self.speed
            #player_collison.player_entity_check_y(-settings.player_speed)
        if direction == "down":
            self.position[1] += self.speed
            #player_collison.player_entity_check_y(settings.player_speed)


    
        
    
class Slime(Enemy):
    def __init__(self, health, damage, movement_speed, sizex, sizey):
        super().__init__(self, health, damage, movement_speed)
        self.size = [sizex, sizey]
        self.player_hitbox = pygame.Rect(self.position[0] - self.size[0]//2, 
                                         self.position[1] - self.size[1]//2,
                                         self.size[0], 
                                         self.size[1])
        
class Chest_mimic(Enemy)
    def __init__(self):
        super().__init__(self)

        
        