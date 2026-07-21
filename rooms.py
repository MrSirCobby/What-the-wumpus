import random
import pygame
import settings
import floor_textures
import wall_textures
import door_animation
import end_door_textures
import chest_animation
import key_texture
import enemies
import player_collison
import battery
import player
import torch

class Tile_Object:
    def __init__(self, grid_x, grid_y):
        self.grid_position = [grid_x,grid_y]
        self.texture = None
        self.position = [
            self.grid_position[0] * settings.TILE_SIZE[0],
            self.grid_position[1] * settings.TILE_SIZE[1]
        ]

    def get_grid_position(self):
        return [self.grid_position[0], self.grid_position[1]]
    
    def get_position(self):
        return self.position
    
    def get_hitbox(self):
        self.hitbox = pygame.Rect(
            self.position[0] - settings.TILE_SIZE[0] // 2,
            self.position[1] - settings.TILE_SIZE[1] // 2,
            settings.TILE_SIZE[0],
            settings.TILE_SIZE[1]
        )

        return self.hitbox
    
class End_Door(Tile_Object):
    def __init__(self, grid_x, grid_y):
        super().__init__(grid_x, grid_y)

        self.is_locked = True
        self.is_open = False
        self.texture = None
        self.animation_frame = 0
        self.animation_timer = 0


        
    
    def animation_update(self):
        if self.is_locked:
            self.animation_frames = end_door_textures.animation["locked"]
        else:
            self.animation_frames = end_door_textures.animation["open"]

        self.frames = end_door_textures.frames
        self.animation_timer += 1
        #print(self.animation_timer)
        if self.animation_timer >= end_door_textures.animation_speed: #if the animation timer exceeds the animation speed, it resets the timer and moves to the next frame of animation
            self.animation_timer = 0
            if self.is_open:
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
    

    def interact(self):
        #print("door interact")
        if self.is_locked:
            if all(item in settings.key_list for item in settings.required_keys):
                self.is_locked = False
            return

        if self.is_open:
            settings.game_finished = True
        else:
            self.is_open = True

    
class Key(Tile_Object):
    def __init__(self, grid_x, grid_y,colour):
        super().__init__(grid_x, grid_y)
        self.colour = colour
        self.texture = None

    def animation_update(self):
        self.texture = key_texture.texture_list[key_texture.key_colour[self.colour]]
        return self.texture

    def interact(self):
        settings.key_list.append(self.colour)
        settings.active_room.item_list.remove(self)
        settings.active_room.interactables.remove(self)



class Wall(Tile_Object):
    def __init__(self, grid_x, grid_y):
        super().__init__(grid_x, grid_y)
        self.mask = 0
        self.texture = None

    def get_texture(self, grid):

        left  = self.check_wall(grid, self.grid_position[0] - 1, self.grid_position[1])
        right = self.check_wall(grid, self.grid_position[0] + 1, self.grid_position[1])
        up    = self.check_wall(grid, self.grid_position[0], self.grid_position[1] - 1)
        down  = self.check_wall(grid, self.grid_position[0], self.grid_position[1] + 1)

        #MASK:
        if up == False: 
            self.mask |= 1
        if right == False:
            self.mask |= 2
        if down == False:
            self.mask |= 4
        if left == False:
            self.mask |= 8
        
        self.texture = wall_textures.texture_list[wall_textures.corresponding_dict[self.mask]]
        #print(self.texture)
        return self.texture
    
    def check_wall(self, grid, x, y):
        if x < 0 or y < 0:
            return False
        if x >= len(grid[0]) or y >= len(grid):
            return False

        return grid[y][x] == 1
    

class Door(Tile_Object):
    def __init__(self, grid_x, grid_y, direction):
        super().__init__(grid_x, grid_y)
        self.direction = direction
        self.is_open = False
        self.texture = None
        self.animation_frame = 0
        self.animation_timer = 0


        
    
    def animation_update(self):
    
        
        self.animation_frames = door_animation.animation[(self.direction, "open")]

        self.frames = door_animation.frames
        self.animation_timer += 1
        #print(self.animation_timer)
        if self.animation_timer >= door_animation.animation_speed: #if the animation timer exceeds the animation speed, it resets the timer and moves to the next frame of animation
            self.animation_timer = 0
            if self.is_open:
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
    

    def interact(self):
        #print("door interact")
        
        if self.is_open:
            self.is_open = False
            change_room(self.direction)
        else:
            self.is_open = True



class Chest(enemies.Object):
    def __init__(self, grid_x, grid_y):
        super().__init__(grid_x * settings.TILE_SIZE[0],grid_y * settings.TILE_SIZE[1], enemies.mimic_size[0],enemies.mimic_size[1])
        self.open = False
        self.animation_frame = 0
        self.animation_timer = 0
        self.grid_position = [grid_x,grid_y]


    def open_chest(self):
        self.open = True
        #print("chest open")
        #stub
    
    def close_chest(self):
        self.open = False
        self.__class__ = enemies.Mimic
        enemies.Mimic.__init__(self, self.position[0]+self.size[0]//2,self.position[1]+self.size[1]//2)
        settings.active_room.enemy_list.append(self)
        settings.active_room.interactables.remove(self)
        settings.active_room.item_list.remove(self)
        #print("close chest")
    
    def interact(self):
        if self.open:
            self.close_chest()
            #print("close chest")
        else:
            self.open_chest()
            batt = battery.Battery(self.grid_position[0],self.grid_position[1])
            settings.active_room.item_list.append(batt)
            settings.active_room.interactables.append(batt)
            #print("chest opening")

    
    #def check_in_range(self):
        #return False
    
    def animation_update(self):
        #print(self.animation_timer)
        self.animation_frames = chest_animation.animation["chest_open"]
        self.frames = chest_animation.frames
        self.animation_timer += 1
        

        if self.animation_timer >= chest_animation.animation_speed: #if the animation timer exceeds the animation speed, it resets the timer and moves to the next frame of animation
            self.animation_timer = 0
            if self.open:
                self.animation_frame += 1
                #print("plus 1")
            else:
                self.animation_frame -= 1
                #print("minus 1")
            #print("update animation")


        if self.animation_frame >= len(self.animation_frames):
            self.animation_frame = len(self.animation_frames)-1
        if self.animation_frame < 0:
            self.animation_frame = 0
        #print(self.animation_frame)
        return self.frames[self.animation_frames[self.animation_frame]]
    

    def display_animation(self,screen):
        self.animation_update
        screen.blit(self.animation_update(), (self.get_position()[0]-chest_animation.CHEST_SPRITE_SIZE[0]//2,
                                    self.get_position()[1]-chest_animation.CHEST_SPRITE_SIZE[1]//2))
    #UNUSED ^^^^
    



class Room:
    def __init__(self):
        self.linked_rooms = []
        self.walls_list = []
        self.doors_list = []
        self.room_display = pygame.Surface((settings.SCREEN_WIDTH,settings.SCREEN_WIDTH),pygame.SRCALPHA)
        self.floor_type = "brick"
        self.collision_objects = []
        self.interactables = []
        self.enemy_list = []
        self.item_list = []
        self.load_room()
        
        
        
        #print(self.wall_list)

 
    
    def get_grid(self):
        return self.grid
    
    def load_room(self):
        self.walls_list = []
        self.collision_objects = []
        self.doors_list = []
        self.interactables = []
        self.item_list = []
        self.enemy_list = []
    

        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                if tile == 1: #WALLS
                    wall = Wall(x, y)
                    self.walls_list.append(wall)
                    #print("wall made")
                if tile == 2: #DOORS
                    if y == 0:
                        direction = "north"
                    if x == 8:
                        direction = "east"
                    if y == 8:
                        direction = "south"
                    if x == 0:
                        direction = "west"
                    door = Door(x,y, direction)
                    self.doors_list.append(door)
                if tile == 3: #CHEST
                    chest = Chest(x,y)
                    self.interactables.append(chest)
                    self.item_list.append(chest)
                if tile == 4:#SLIME
                    slime = enemies.Slime(x*settings.TILE_SIZE[0],y*settings.TILE_SIZE[1])
                    self.enemy_list.append(slime)
                if tile == 5:#BAT
                    bat = enemies.Bat(x*settings.TILE_SIZE[0], y * settings.TILE_SIZE[1])
                    self.enemy_list.append(bat)
                if tile == 6:#KEY
                    colour = settings.required_keys[settings.key_counter]
                    settings.key_counter += 1
                    if settings.key_counter > 3:
                        settings.key_counter = 3
                    key = Key(x,y,colour)
                    self.item_list.append(key)
                    self.interactables.append(key)
                if tile == 7: #END DOOR
                    end_door = End_Door(x,y)
                    self.doors_list.append(end_door)
                

        

        for wall in self.walls_list:
            self.collision_objects.append(wall.get_hitbox())
            #enviroment.collision_object.append(hitbox)
        
        for door in self.doors_list:
            self.interactables.append(door)
            self.collision_objects.append(door.get_hitbox())




    def update_room_display(self):
        #self.update_room()
        self.room_display.fill(settings.BACKGROUND_COLOUR)
        #FLOOR
        for y in range(0, settings.SCREEN_HEIGHT, floor_textures.SCALED_FLOOR_SIZE):
            for x in range(0, settings.SCREEN_WIDTH, floor_textures.SCALED_FLOOR_SIZE):
                self.room_display.blit(floor_textures.load_floor_sprite(self.floor_type),(x, y))
        
        #WALLS
        for wall in self.walls_list:
            # We use WALL_SPRITE_SIZE to perfectly centre the graphic over the hitbox
            draw_x = wall.get_position()[0] - wall_textures.WALL_SPRITE_SIZE[0] // 2
            draw_y = wall.get_position()[1] - wall_textures.WALL_SPRITE_SIZE[1] // 2
            self.room_display.blit(wall.get_texture(self.grid), (draw_x, draw_y))

        #DOORS
        for door in self.doors_list:
            #print("door animation update")
            self.room_display.blit(door.animation_update(),
                                   (door.get_position()[0] - door_animation.DOOR_SPRITE_SIZE[0]//2,
                                    door.get_position()[1] - door_animation.DOOR_SPRITE_SIZE[1]//2))
        
        #ITEMS
        for item in self.item_list:
            texture = item.animation_update()
            if hasattr(item, "get_draw_position"):
                draw_x, draw_y = item.get_draw_position()
            else:
                draw_x, draw_y = item.get_position()
            self.room_display.blit(texture, (draw_x, draw_y))

        #ENEMIES
        for enemy in self.enemy_list:
            enemy.display_animation(self.room_display)



    def change_active(self):
        settings.active_room = self

    def get_wall_list(self):
        return self.walls_list 
    
    def get_collision_objects(self):
        return self.collision_objects
    
    def append_interactables(self, interactable):
        self.interactables.append(interactable)
    
    def get_interactables(self):
        return self.interactables

    def display_room(self, screen):
        self.update_room_display()
        screen.blit(self.room_display, (0,0))
            
            
class Spawn_Room(Room):
    def __init__(self):
        self.grid = [
    [1,1,1,1,2,1,1,1,1],
    [1,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,1],
    [2,0,1,0,0,0,1,0,2],
    [1,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,1],
    [1,1,1,1,2,1,1,1,1]
]
        super().__init__()
           



class Treasure_Room(Room):
    def __init__(self):
        self.grid = [
    [1,1,1,1,2,1,1,1,1],
    [1,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,1],
    [2,0,1,0,3,0,1,0,2],
    [1,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,1],
    [1,1,1,1,2,1,1,1,1]
] 
        super().__init__()
          

    

class Key_Room(Room):
    def __init__(self):
        self.grid = [
    [1,1,1,1,2,1,1,1,1],
    [1,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,0,0,6,0,0,0,1],
    [2,0,1,1,0,0,1,0,2],
    [1,0,0,4,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1],
    [1,1,1,1,2,1,1,1,1]
] 
        super().__init__()
          

class Monster_Room(Room):
    def __init__(self):
        self.grid = [
    [1,1,1,1,2,1,1,1,1],
    [1,0,0,0,0,0,0,0,1],
    [1,0,5,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,1],
    [2,0,1,1,0,0,1,0,2],
    [1,0,1,0,4,0,1,0,1],
    [1,0,1,0,0,0,1,0,1],
    [1,4,0,0,0,0,0,0,1],
    [1,1,1,1,2,1,1,1,1]
]  
        super().__init__()
        
        

class Maze_Room(Room):
    def __init__(self):
        self.grid = [
    [1,1,1,1,2,1,1,1,1],
    [1,0,0,0,0,1,1,0,1],
    [1,0,1,0,1,3,1,0,1],
    [1,0,0,0,0,0,1,0,1],
    [2,0,1,1,1,0,1,0,2],
    [1,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,1],
    [1,1,1,1,2,1,1,1,1]
]  
        super().__init__()
        
        

class End_Room(Room):
    def __init__(self):
        self.grid = [
    [1,1,1,1,7,1,1,1,1],
    [1,0,1,0,0,0,1,0,1],
    [1,0,0,0,1,0,0,0,1],
    [1,1,0,0,0,0,0,1,1],
    [2,0,0,0,1,0,0,0,2],
    [1,1,0,0,0,0,0,1,1],
    [1,0,0,0,1,0,0,0,1],
    [1,0,1,0,0,0,1,0,1],
    [1,1,1,1,2,1,1,1,1]
]  
        super().__init__()
        










rooms = {
    (0, 0): Spawn_Room(),
    (1, 0): Treasure_Room(),
    (2, 0): Monster_Room(),
    (3, 0): End_Room(),

    (0, 1): Monster_Room(),
    (1, 1): Key_Room(),
    (2, 1): Maze_Room(),
    (3, 1): Treasure_Room(),

    (0, 2): Key_Room(),
    (1, 2): Maze_Room(),
    (2, 2): Monster_Room(),
    (3, 2): Key_Room(),

    (0, 3): Treasure_Room(),
    (1, 3): Monster_Room(),
    (2, 3): Maze_Room(),
    (3, 3): Key_Room(),
}


current_room_position = (0, 0)
settings.active_room = rooms[current_room_position]
#print(settings.active_room.walls_list)

def reset_game_state():
    global current_room_position
    global rooms

    settings.objects = []
    settings.key_list = []
    settings.required_keys = ["yellow", "blue", "green", "pink"]
    settings.key_counter = 0
    settings.game_finished = False
    settings.player_health = 100
    settings.player_position = [settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2]
    settings.player_vulnerable = True
    settings.vulnerable_timer = 2000
    player.player_moving = False
    player.player_direction = "down"
    torch.torch_light_radius = 300
    enemies.ENEMY_LIST = []

    rooms = {
        (0, 0): Spawn_Room(),
        (1, 0): Treasure_Room(),
        (2, 0): Monster_Room(),
        (3, 0): End_Room(),

        (0, 1): Monster_Room(),
        (1, 1): Key_Room(),
        (2, 1): Maze_Room(),
        (3, 1): Treasure_Room(),

        (0, 2): Key_Room(),
        (1, 2): Maze_Room(),
        (2, 2): Monster_Room(),
        (3, 2): Key_Room(),

        (0, 3): Treasure_Room(),
        (1, 3): Monster_Room(),
        (2, 3): Maze_Room(),
        (3, 3): Key_Room(),
    }

    current_room_position = (0, 0)
    settings.active_room = rooms[current_room_position]


def change_room(direction):
    global current_room_position
    settings.player_vulnerable = True
    x, y = current_room_position

    if direction == "north":
        new_position = (x, y - 1)

    elif direction == "south":
        new_position = (x, y + 1)

    elif direction == "east":
        new_position = (x + 1, y)

    elif direction == "west":
        new_position = (x - 1, y)


    if new_position in rooms:
        current_room_position = new_position
        settings.active_room = rooms[new_position]
        if direction == "north":
            settings.player_position = [360, 640]
        if direction == "east":
            settings.player_position = [80,360]
        if direction == "south":
            settings.player_position = [360,80]
        if direction == "west":
            settings.player_position = [640,360]
