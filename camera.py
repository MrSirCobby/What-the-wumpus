import settings
class camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
    
    def update_camera(self):
        #center the camera on the player
        self.x = settings.player_position[0] - self.width // 2
        self.y = settings.player_position[1] - self.height // 2
    
    def apply(self, x, y):
        return (x - self.x, y - self.y)
    
    def apply_rect(self, rect):
        return rect.move(-self.x, -self.y)