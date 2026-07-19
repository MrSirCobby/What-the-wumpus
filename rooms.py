import random
import pygame
import settings
import floor_textures
import wall_textures
import door_animation

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
        self.is_locked = True
        self.is_open = False
        self.texture = None

        
    
    def animation_update(self):
        if self.is_locked:
            self.current_animation = door_animation.animation[(self.direction, "locked")]
        else:
            if self.is_open:
                self.current_animation = door_animation.animation[(self.direction, "open")]
            else:
                self.current_animation = door_animation.animation[(self.direction, "closed")]

        if self.animation_frame >= len(self.current_animation):
            self.animation_frame = 0

        self.animation_timer += 1

        if self.animation_timer >= door_animation.animation_speed: #if the animation timer exceeds the animation speed, it resets the timer and moves to the next frame of animation
            self.animation_timer = 0
            self.animation_frame += 1
            if self.animation_frame >= len(self.current_animation): 
                self.animation_frame = 0
        return door_animation.frames[self.current_animation[self.animation_frame]]
    

    def interact(self):
    
        if self.is_locked:
            if all(item in settings.key_list for item in settings.required_keys):
                self.is_locked = False
        else:
            if self.is_open:
                pass
            else:
                self.is_open = True


    
    
    

class Room:
    def __init__(self):
        self.linked_rooms = []
        self.walls_list = []
        self.doors_list = []
        self.grid = []
        self.room_display = pygame.Surface((settings.SCREEN_WIDTH,settings.SCREEN_WIDTH),pygame.SRCALPHA)
        self.floor_type = "brick"
        self.collision_objects = []
        self.interactables = []
        self.linked_rooms = {
            "north": None,
            "east": None,
            "south": None,
            "west": None
            }
        
        
        self.generate_grid()
        self.update_walls()
        #print(self.wall_list)

    def generate_grid(self):
        self.grid = [
    [1,1,1,1,2,1,1,1,1],
    [1,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,1],
    [2,0,0,1,0,0,0,0,2],
    [1,0,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,0,0,1],
    [1,1,1,1,2,1,1,1,1]
]   
    
    def get_grid(self):
        return self.grid
    
    def update_walls(self):
        self.walls_list = []
        self.collision_objects = []
        floor_textures.collision_object = []

        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                if tile == 1:
                    wall = Wall(x, y)
                    self.walls_list.append(wall)
                if tile == 2:
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
        
        

        for wall in self.walls_list:
            self.collision_objects.append(wall.get_hitbox())
            #enviroment.collision_object.append(hitbox)


        for door in self.doors_list:
            #self.room_display.blit(wall.get_texture(self.grid), (, ))
            pass
        for door in self.doors_list:
            self.collision_objects.append(door.get_hitbox())

    def update_room_display(self):
        for y in range(0, settings.SCREEN_HEIGHT, floor_textures.SCALED_FLOOR_SIZE):
            for x in range(0, settings.SCREEN_WIDTH, floor_textures.SCALED_FLOOR_SIZE):
                self.room_display.blit(floor_textures.load_floor_sprite(self.floor_type),(x, y))

        for wall in self.walls_list:
            # We use WALL_SPRITE_SIZE to perfectly centre the graphic over the hitbox
            draw_x = wall.get_position()[0] - wall_textures.WALL_SPRITE_SIZE[0] // 2
            draw_y = wall.get_position()[1] - wall_textures.WALL_SPRITE_SIZE[1] // 2
            self.room_display.blit(wall.get_texture(self.grid), (draw_x, draw_y))


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
            
            



class TreasureRoom(Room):
    def __init__(self, name):
        super().__init__(name)
        self.treasure = True
    #stub


class MonsterRoom(Room):
    def __init__(self, name):
        super().__init__(name)
        self.monster = True
    #stub



#room_test = Room()
#room_test.change_active()
#room_test.generate_grid()
#room_test.update_walls()
#print(active_room.get_collision_objects())