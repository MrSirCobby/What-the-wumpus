import pygame
import settings
import chest_animation
import math

mimic_health = 100
mimic_damage = 10
detection_radius = 40


class Enemy:
    def __init__(self, health, damage, positionx, positiony, sizex, sizey):
        self.health = health
        self.damage = damage
        self.speed = 2
        self.position = [positionx,positiony]
        self.size = [sizex, sizey]
        self.moving = False
        self.detection_radius = detection_radius
    
    def set_position(self, position_x, position_y):
        self.position = [position_x, position_y]
    
    def set_speed(self, new_speed):
        self.speed = new_speed
    
    def update_hitbox(self):
        self.hitbox = pygame.Rect(self.position[0] - self.size[0]//2, 
                                  self.position[1] - self.size[1]//2,
                                  self.size[0], 
                                  self.size[1])

    def return_hitbox(self):
        return self.hitbox    
    
    def update(self):
        if self.check_in_range():
            self.move_toward_player
        else: 
            self.is_moving = False
        return


    def check_in_range(self):
        dx = settings.player_position[0] - self.position[0]
        dy = settings.player_position[1] - self.position[1]

        distance = math.sqrt(dx**2 + dy**2)

        return distance <= self.detection_radius

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
        self.moving = True
    
    def is_moving(self):
        return self.moving


    
        
    
class Slime(Enemy):
    def __init__(self, health, damage, movement_speed, sizex, sizey):
        super().__init__(self, health, damage, movement_speed,sizex, sizey)
        
        
        
        
        