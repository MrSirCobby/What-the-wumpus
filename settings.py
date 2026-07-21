event_get = None
active_room = None
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
FPS = 60
player_speed = 5
player_position = [360, 620]
player_vulnerable = True
vulnerable_timer = 2000 #in milliseconds
BACKGROUND_COLOUR = (40, 40, 40)
PLAYER_SIZE = [42, 56] #width and height of the player hitbox
TITLE = "FRONTROOMS"
player_health = 100

TILE_SIZE = [SCREEN_WIDTH/8,SCREEN_HEIGHT/8]
#print(TILE_SIZE)

objects = []
key_list = []
required_keys = ["yellow", "blue", "green", "pink"]

#Torch
battery_level = 100
torch_is_active = True
game_finished = False
key_counter = 0