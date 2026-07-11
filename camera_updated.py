import pygame
def set_camera(width, height):
        global camera_x
        global camera_y
        global camera_width
        global camera_height
        camera_width = width
        camera_height = height
        camera_x = 0
        camera_y = 0
    
def update_camera(updated_x, updated_y):
    #center the camera on the player
    global camera_x
    global camera_y
    camera_x = updated_x - camera_width // 2
    camera_y = updated_y - camera_height // 2
    
def apply(x, y):
        return (x - camera_x, y - camera_y)
    
def apply_rect(rect):
        return rect.move(-camera_x, -camera_y)