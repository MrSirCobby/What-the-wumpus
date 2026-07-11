import settings
class camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
    
    def update_camera(self, updated_x, updated_y):
        #center the camera on the player
        self.x = updated_x - self.width // 2
        self.y = updated_y - self.height // 2
    
    def apply(self, x, y):
        return (x - self.x, y - self.y)
    
    def apply_rect(self, rect_x, rect_y, rect_width, rect_height):
        return (rect_x - self.x, rect_y - self.y, rect_width, rect_height)