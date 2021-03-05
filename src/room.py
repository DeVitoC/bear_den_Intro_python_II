# Implement a class to hold room information. This should have name and
# description attributes.
from item import *
from random import random, choice

class Room:
     def __init__(self, name, description):
          self.n_to = None
          self.e_to = None
          self.s_to = None
          self.w_to = None
          self.name = name
          self.description = description
          self.stuff = self.populate_items()

     def populate_items(self):
          item_dict: Dict[str: Item] = {}
          rand_number = int(round(random() * 3))
          for i in range(rand_number):
               key, value = choice(list(item_types.items()))
               new_item = self.create_item(value)
               item_dict[new_item.name] = new_item
          return item_dict
    
     def create_item(self, item):
          item_definitions = {
               "Torch" : Torch,
               "Lamp" : Lamp,
               "Helmet" : Helmet, 
               "Chestpeice" : Chestpeice,
               "Coins" : Coins,
               "Diamond" : Diamond
          }
          
          search_item = item[0]
          this_item_type = item_definitions[search_item]
          if len(item) == 2:
               this_item = this_item_type(item[0], item[1])
          else:
               this_item = this_item_type(item[0], item[1], item[2])
          return this_item
    
    