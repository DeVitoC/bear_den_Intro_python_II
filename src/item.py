from enum import Enum

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
    
##############################
### Lightsources
##############################
class Lightsource(Item):
    def __init__(self, name, description, duration):
        super().__init__(name, description)
        self.duration = duration
        self.is_on = False
        
    def on_drop(self):
        print(f"Are you sure you want to drop your source of light?")
        
class Torch(Lightsource):
    def __init__(self, name, description, duration = 20):
        super().__init__(name, description, duration)
        
class Lamp(Lightsource):
    def __init__(self, name, description, duration = 40):
        super().__init__(name, description, duration)
        
##############################
### Armor
##############################
class ArmorSlot(Enum):
    CHEST = "Chest"
    HEAD = "Head"
    
class Armor(Item):
    def __init__(self, name, description, armor_value, slot: ArmorSlot):
        super().__init__(name, description)
        self.armor_value = armor_value
        self.slot = slot
        
class Chestpeice(Armor):
    def __init__(self, name, description, armor_value, slot = ArmorSlot.CHEST):
        super().__init__(name, description, armor_value, slot)
        
class Helmet(Armor):
    def __init__(self, name, description, armor_value, slot = ArmorSlot.HEAD):
        super().__init__(name, description, armor_value, slot)
        
##############################
### Treasure
##############################

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        
class Coins(Treasure):
    def __init__(self, name, description, value):
        super().__init__(name, description, value)
        
    def __str__():
        print(f"{self.value} coins: {self.description}")
        
class Diamond(Treasure):
    def __init__(self, name, description, value):
        super().__init__(name, description, value)
        
        
item_types = {
        0 : ('Torch', 
             'a torch that can light up the darkness for 20 turns'),
        1 : ('Lamp', 
             'a lamp that can light up the darkness for 40 turns'),
        2 : ('Helmet', 
             'a helmet with minor defensive capabilities', 2),
        3 : ('Helmet', 
             'a helmet with medium defensive capabilities', 4),
        4 : ('Helmet', 
             'a helmet with major defensive capabilities', 8),
        5 : ('Chestpeice', 
             'a Chestpeice with minor defensive capabilities', 4),
        6 : ('Chestpeice', 
             'a Chestpeice with medium defensive capabilities', 8),
        7 : ('Chestpeice', 
             'a Chestpeice with major defensive capabilities', 12),
        8 : ('Coins', 
             'a pile of coins', 100),
	    9 : ('Diamond', 
          'a valuable diamond', 1000),
    }