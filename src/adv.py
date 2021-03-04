from room import Room
from player import Player
from item import *

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Lightsourse("Torch", "A simple lightsource", 15)]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Armor("LeatherArmor", "A simple set of Leather Armor", 3)]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Lightsourse("Torch", "A simple lightsource", 15), Armor("Plate Armor", "A shiny set of Plate Armor", 10)]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("What is your character's name? ")
player = Player(player_name, room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(f"Welcome {player.name}! Can you find find the treasure room in this dungeon?")

possible_commands = """
"q" = quit
"n" or "move north" = move north
"e" or "move east" = move east 
"s" or "move south" = move south
"w" or "move west" = move west
"i" or "inspect room" = inspect room
"get [item]" = pick up the item
"drop [item]" = drop the item
"view inventory" = view items in inventory
"""

while True: 
    print(f"You are in the {player.current_room.name}")
    inp = input("Enter a command (h = help): ")
    commands = inp.split(" ")
    if len(commands) == 1:
        if commands[0].lower() == "q":
            break
        elif commands[0].lower() == "n":
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
            else:
                print("There is no room to the north")
        elif commands[0].lower() == "e":
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
            else:
                print("There is no room to the east")
        elif commands[0].lower() == "s":
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
            else:
                print("There is no room to the south")
        elif commands[0].lower() == "w":
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
            else:
                print("There is no room to the west")
        elif commands[0].lower() == "h":
            print(possible_commands)
        elif commands[0].lower() == "i":
            if player.current_room.stuff == []:
                print("There is nothing in this room.")
            else:
                for item in player.current_room.stuff:
                    print(item)  
    else:
        if commands[1].lower() == "north":
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
            else:
                print("There is no room to the north")
        elif commands[1].lower() == "east":
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
            else:
                print("There is no room to the east")
        elif commands[1].lower() == "south":
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
            else:
                print("There is no room to the south")
        elif commands[1].lower() == "west":
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
            else:
                print("There is no room to the west")
        elif commands[0].lower() == "inspect":
            if player.current_room.stuff == []:
                print("There is nothing in this room.")
            else:
                for item in player.current_room.stuff:
                    print(item)
        elif commands[0].lower() == "get":
            for item in player.current_room.stuff:
                if item.name == commands[1]:
                    player.inventory.append(item)
                    player.current_room.stuff.remove(item)
                    item.on_take()
        elif commands[0].lower() == "drop":
            for item in player.inventory:
                if item.name == commands[1]:
                    player.inventory.remove(item)
                    player.current_room.stuff.append(item)
                    item.on_drop()
        elif commands[0].lower() == "view":
            if player.inventory == []:
                print("You have no items")
            else:
                for item in player.inventory:
                    print(item)
    
