import pygame
import settings
import chest_animation
import slime_animation
import bat_animation
import math
#import floor_textures
debug = False

mimic_health = 100
mimic_damage = 10
mimic_speed = 1.5
mimic_size = [40, 30]
mimic_detection_radius = 120
#player collision is moved to player_collision.p

slime_health = 60
slime_damage = 10
slime_speed = 2
slime_size = [30,25]
slime_detection_radius = 150

bat_health = 20
bat_damage = 5
bat_speed = 3
bat_size = [20, 20]
bat_detection_radius = 110


ENEMY_LIST = []

class Object:
    def __init__(self, positionx, positiony, sizex, sizey):
        self.position = [positionx,positiony]
        self.size = [sizex, sizey]
        settings.objects.append(self)

    def set_position(self, position_x, position_y):
        self.position = [position_x, position_y]

    def get_position(self):
        return self.position
    

    def get_size(self):
        return self.size
    
    def update_hitbox(self):
        self.hitbox = pygame.Rect(self.position[0] - self.size[0]//2, 
                                  self.position[1] - self.size[1]//2,
                                  self.size[0], 
                                  self.size[1])
        
    def return_hitbox(self):
        self.update_hitbox()
        return self.hitbox 

class Enemy(Object):
    def __init__(self, positionx, positiony, sizex, sizey):
        super().__init__(positionx,positiony,sizex,sizey)
        self.health = None
        self.damage = None
        self.speed = 2
        self.moving = False
        self.detection_radius = None
        self.animation_frame = 0
        self.animation_timer = 0
        ENEMY_LIST.append(self)
        
    def get_damage(self):
        return self.damage
    
    def set_speed(self, new_speed):
        self.speed = new_speed
    
    
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
        for entity in settings.active_room.get_collision_objects():
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
        for entity in settings.active_room.get_collision_objects():
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
    def __init__(self, positionx, positiony):
        super().__init__(positionx, positiony, slime_size[0],slime_size[1])
        self.health = slime_health
        self.damage = slime_damage
        self.speed = slime_speed
        self.detection_radius = slime_detection_radius

    def animation_update(self):
        if self.moving == True:
            self.current_animation = slime_animation.animation["moving"]
        else:
            self.current_animation = slime_animation.animation["idle"]

        if self.animation_frame >= len(self.current_animation):
            self.animation_frame = 0

        self.animation_timer += 1

        if self.animation_timer >= slime_animation.animation_speed: #if the animation timer exceeds the animation speed, it resets the timer and moves to the next frame of animation
            self.animation_timer = 0
            self.animation_frame += 1
            if self.animation_frame >= len(self.current_animation): 
                self.animation_frame = 0
        return slime_animation.frames[self.current_animation[self.animation_frame]]
    
    def display_animation(self,screen):
        screen.blit(self.animation_update(), (self.get_position()[0]-slime_animation.SLIME_SPRITE_SIZE[0]//2,
                                    self.get_position()[1]-slime_animation.SLIME_SPRITE_SIZE[1]//2))
        
class Bat(Enemy):
    def __init__(self, positionx, positiony):
        super().__init__(positionx, positiony, bat_size[0], bat_size[1])
        self.health = bat_health
        self.damage = bat_damage
        self.speed = bat_speed
        self.detection_radius = bat_detection_radius

    def animation_update(self):
        self.current_animation = bat_animation.animation["flapping"]

        if self.animation_frame >= len(self.current_animation):
            self.animation_frame = 0

        self.animation_timer += 1

        if self.animation_timer >= bat_animation.animation_speed: #if the animation timer exceeds the animation speed, it resets the timer and moves to the next frame of animation
            self.animation_timer = 0
            self.animation_frame += 1
            if self.animation_frame >= len(self.current_animation): 
                self.animation_frame = 0
        return bat_animation.frames[self.current_animation[self.animation_frame]]
    
    def display_animation(self,screen):
        screen.blit(self.animation_update(), (self.get_position()[0]-bat_animation.BAT_SPRITE_SIZE[0]//2,
                                    self.get_position()[1]-bat_animation.BAT_SPRITE_SIZE[1]//2))



class Mimic(Enemy):
    def __init__(self, positionx, positiony):
        super().__init__(positionx, positiony, mimic_size[0], mimic_size[1])
        self.health = mimic_health
        self.damage = mimic_damage
        self.speed = mimic_speed
        
        

        self.detection_radius = mimic_detection_radius
    def animation_update(self):
        if self.moving == True:
            self.current_animation = chest_animation.animation["monster_open"]
        else:
            self.current_animation = chest_animation.animation["closed"]

        if self.animation_frame >= len(self.current_animation):
            self.animation_frame = 0

        self.animation_timer += 1

        if self.animation_timer >= chest_animation.animation_speed: #if the animation timer exceeds the animation speed, it resets the timer and moves to the next frame of animation
            self.animation_timer = 0
            self.animation_frame += 1
            if self.animation_frame >= len(self.current_animation): 
                self.animation_frame = 0
        return chest_animation.frames[self.current_animation[self.animation_frame]]
    
    def display_animation(self,screen):
        screen.blit(self.animation_update(), (self.get_position()[0]-chest_animation.CHEST_SPRITE_SIZE[0]//2,
                                    self.get_position()[1]-chest_animation.CHEST_SPRITE_SIZE[1]//2))
    
class Chest(Object):
    def __init__(self, position_x, position_y):
        super().__init__(position_x,position_y, mimic_size[0],mimic_size[1])
        print("using enemies.py chest class")
        self.open = False
        settings.active_room.interactiables_append(self)
        self.animation_frame = 0
        self.animation_timer = 0


    def open_chest(self):
        self.open = True
        #print("chest open")
        #stub
    
    def close_chest(self):
        self.open = False
        self.__class__ = Mimic
        Mimic.__init__(self, self.position[0],self.position[1])
        settings.active_room.interactiables_remove(self)
        #print("close chest")
    
    def interact(self):
        if self.open:
            self.close_chest()
            #print("close chest")
        else:
            self.open_chest()
            #print("chest opening")

    
    def check_in_range(self):
        return False
    
    def animation_update(self):
        
        self.animation_frames = chest_animation.animation["chest_open"]
        self.frames = chest_animation.frames
        self.animation_timer += 1

        if self.animation_timer >= chest_animation.animation_speed: #if the animation timer exceeds the animation speed, it resets the timer and moves to the next frame of animation
            self.animation_timer = 0
            if self.open:
                self.animation_frame += 1
            else:
                self.animation_frame -= 1
            #print("update animation")


        if self.animation_frame >= len(self.animation_frames):
            self.animation_frame = len(self.animation_frames)-1
        if self.animation_frame < 0:
            self.animation_frame = 0
        #print(self.animation_frame)
        return self.frames[self.animation_frames[self.animation_frame]]
    
    def display_animation(self,screen):
        screen.blit(self.animation_update(), (self.get_position()[0]-chest_animation.CHEST_SPRITE_SIZE[0]//2,
                                    self.get_position()[1]-chest_animation.CHEST_SPRITE_SIZE[1]//2))
    

        
        
        