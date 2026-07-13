import pygame
import settings
import chest_animation
import math
import enviroment
debug = False

mimic_health = 100
mimic_damage = 10
mimic_speed = 1.5
mimic_size = [40, 30]
#player collision is moved to player_collision.py

detection_radius = 150

ENEMY_LIST = []

class Enemy:
    def __init__(self, positionx, positiony, sizex, sizey):
        self.health = None
        self.damage = None
        self.speed = 2
        self.position = [positionx,positiony]
        self.size = [sizex, sizey]
        self.moving = False
        self.detection_radius = detection_radius
        ENEMY_LIST.append(self)
    
    def set_position(self, position_x, position_y):
        self.position = [position_x, position_y]

    def get_position(self):
        return self.position
    
    def get_size(self):
        return self.size
    
    def get_damage(self):
        return self.damage
    
    def set_speed(self, new_speed):
        self.speed = new_speed
    
    def update_hitbox(self):
        self.hitbox = pygame.Rect(self.position[0] - self.size[0]//2, 
                                  self.position[1] - self.size[1]//2,
                                  self.size[0], 
                                  self.size[1])

    def return_hitbox(self):
        self.update_hitbox()
        return self.hitbox    
    
    def update_movement(self):
        if self.check_in_range():
            self.move_toward_player()
        else: 
            self.moving = False
        return


    def check_in_range(self):
        dx = settings.player_position[0] - self.position[0]
        dy = settings.player_position[1] - self.position[1]

        distance = math.sqrt(dx**2 + dy**2)
        if debug:
            if distance <= self.detection_radius == True:
                print("in range")
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
            self.entity_collision_x(-self.speed)
            #player_collison.player_entity_check_x(-settings.player_speed)
        if direction == "right":
            self.position[0] += self.speed
            self.entity_collision_x(self.speed)
            #player_collison.player_entity_check_x(settings.player_speed)
        if direction == "up":
            self.position[1] -= self.speed
            self.entity_collision_y(-self.speed)
            #player_collison.player_entity_check_y(-settings.player_speed)
        if direction == "down":
            self.position[1] += self.speed
            self.entity_collision_y(self.speed)
            #player_collison.player_entity_check_y(settings.player_speed)
        self.moving = True
    
    def is_moving(self):
        return self.moving
    
    def entity_collision_x(self, dx):
        self.update_hitbox()
        for entity in enviroment.collision_object:
            if self.hitbox.colliderect(entity):
                if debug:
                    print(f"Collision detected on X axis! dx={dx}")
                
                if dx > 0:
                    self.position[0] = entity.left - self.size[0]//2
                    #player_hitbox.right = entity.left
                    if debug:
                        print("Stopped moving right")
                elif dx < 0:
                    self.position[0] = entity.right + self.size[0]//2
                    #player_hitbox.left = entity.right
                    if debug:
                        print("Stopped moving left")


    def entity_collision_y(self, dy):
        self.update_hitbox()
        for entity in enviroment.collision_object:
            if self.hitbox.colliderect(entity):
                if debug:
                    print(f"Collision detected on Y axis! dy={dy}")
                if dy > 0:
                    self.position[1] = entity.top - self.size[1]//2
                    #player_hitbox.bottom = entity.top
                    if debug:
                        print("Stopped moving down")
                elif dy < 0:
                    self.position[1] = entity.bottom + self.size[1]//2
                    #player_hitbox.top = entity.bottom
                    if debug:
                        print("Stopped moving up")


    
        
    
class Slime(Enemy):
    def __init__(self, positionx, positiony, sizex, sizey):
        super().__init__(positionx, positiony, sizex, sizey)
        self.health = None
        self.damage = None
        self.speed = 2

class Mimic(Enemy):
    def __init__(self, positionx, positiony):
        super().__init__(positionx, positiony, mimic_size[0], mimic_size[1])
        self.health = mimic_health
        self.damage = mimic_damage
        self.speed = mimic_speed

    def animation_update(self):
        if self.moving == True:
            current_animation = chest_animation.animation["monster_open"]
        else:
            current_animation = chest_animation.animation["closed"]

        if chest_animation.animation_frame >= len(current_animation):
            chest_animation.animation_frame = 0

        chest_animation.animation_timer += 1

        if chest_animation.animation_timer >= chest_animation.animation_speed: #if the animation timer exceeds the animation speed, it resets the timer and moves to the next frame of animation
            chest_animation.animation_timer = 0
            chest_animation.animation_frame += 1
            if chest_animation.animation_frame >= len(current_animation): 
                chest_animation.animation_frame = 0

        return chest_animation.frames[current_animation[chest_animation.animation_frame]]
    
class Chest():
    def __init__(self, position_x, position_y):
        self.open = False
        self.position = [position_x, position_y]
        self.size = mimic_size
        enviroment.interactiables.append(self)

    def update_hitbox(self):
        self.hitbox = pygame.Rect(self.position[0] - self.size[0]//2, 
                                  self.position[1] - self.size[1]//2,
                                  self.size[0], 
                                  self.size[1])

    def return_hitbox(self):
        self.update_hitbox()
        return self.hitbox  

    def open_chest(self):
        self.open = True
        #print("chest open")
        #stub
    
    def close_chest(self):
        self.open = False
        self = Mimic(self.position[0], self.position[1])
    
    def interact(self):
        if self.open:
            self.close_chest()
            #print("close chest")
        else:
            self.open_chest()
            #print("chest opening")

    
    def check_in_range(self):
        return False
    
    def mimic_animation_update(self):
        if self.open == True:
            current_animation = chest_animation.animation["chest_open"]
        else:
            current_animation = chest_animation.animation["closed"]

        if chest_animation.animation_frame >= len(current_animation):
            chest_animation.animation_frame = 0

        chest_animation.animation_timer += 1

        if chest_animation.animation_timer >= chest_animation.animation_speed: #if the animation timer exceeds the animation speed, it resets the timer and moves to the next frame of animation
            chest_animation.animation_timer = 0
            chest_animation.animation_frame += 1
            if chest_animation.animation_frame >= len(current_animation): 
                chest_animation.animation_frame = 0

        return chest_animation.frames[current_animation[chest_animation.animation_frame]]
            
        
        
        