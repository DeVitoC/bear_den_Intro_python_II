class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f'{self.name}'
    
    def on_take(self):
        print(f"You have picked up: {self.name}")
        
    def on_drop(self):
        print(f"You have dropped: {self.name}")
    
class Lightsourse(Item):
    def __init__(self, name, description, duration):
        super().__init__(name, description)
        self.duration = duration
        self.is_on = False
        
    def on_drop(self):
        print(f"Are you sure you want to drop your source of light?")
        
class Armor(Item):
    def __init__(self, name, description, armor_value):
        super().__init__(name, description)
        self.armor_value = armor_value