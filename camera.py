import settings

class camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
    
    def update(self, player_x, player_y):
        #center the camera on the player
        self.x = player_x - self.width // 2
        self.y = player_y - self.height // 2
    
    def apply(self, x, y):
        return (x - self.x, y - self.y)
    
    def apply_rect(self, rect):
        return rect.move(-self.x, -self.y)