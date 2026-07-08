#utilises inheritance needs to incorporate polymorphism and encapsulation
import random
class Room:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_caves = []

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    
    def set_description(self, description):
        self.description = description
    def get_description(self):
        return self.description
    
    def set_linked_caves(self, linked_caves):
        self.linked_caves = linked_caves
    def get_linked_caves(self):
        return self.linked_caves


class TreasureRoom(Room):
    def __init__(self, name):
        super().__init__(name)
        self.treasure = True
        #self.treasure_type = random.choice([fuel, gold, health_potion, speed_potion])
    #stub


class MonsterRoom(Room):
    def __init__(self, name):
        super().__init__(name)
        self.monster = True
    #stub