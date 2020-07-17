from item import Item
from player import Player
from randomizer import *
from room import Room
import os
import textwrap

# Declare all the rooms


rooms = {
        'outside': Room("Outside Cave Entrance",
                        "North of you, the cave mount beckons."),

        'foyer': Room("Foyer",
                      """Dim light filters in from the south. Dusty
                      passages run north and east."""),

        'overlook': Room("Grand Overlook",
                         """A steep cliff appears before you, falling
                         into the darkness. Ahead to the north, a light
                         flickers in the distance, but there is no way
                         across the chasm."""),

        'narrow': Room("Narrow Passage",
                       """The narrow passage bends here from west to north.
                       The smell of gold permeates the air."""),

        'treasure': Room("Treasure Chamber",
                         """You've found the long-lost treasure chamber!
                         Sadly, it has already been completely emptied by
                         earlier adventurers. The only exit is to the south."""),
        }


items = {
        'knife': Item('knife', 'A short, sharp shiv.'),
		'torch': Item('torch', 'A source of light!')
}                                   

# Create a randomized list of items as the game starts.
items = {key: adj_randomizer(DESCRIPTORS, val) for (key, val) in items.items()}

# Populate rooms with items.
rooms = {key: populate_room(room, list(items.values())) for (key, room) in rooms.items()}
print(f'Total items: {[x.name for i in rooms.values() for x in i.inventory]}')

# To do: Update room descs with item names

# Allow player to see item descs when checking inventory

# Allow player to use the 'look' command to inspect items/rooms

# Link rooms together
rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']


"""
    Overlook  Treasure
      |         |
    Foyer  -- Narrow
      |
    Outside


"""

#
# Main
#
game_loop = True
WIDTH = os.get_terminal_size()[0]
OPEN_WRAP = '\n--------------------'
CLOSE_WRAP = '--------------------\n\n'
# Make a new player object that is currently in the 'outside' room.
player1 = Player(rooms['outside'])

welcome_message = '''Welcome to the game! You are an adventurer in
search of treasure! You have an inventory which you can see with "i",
and you can "take" or "get" items. To move in a certain direction, simply
type the direction you'd like to go! You can also just use the first letter
of that direction, like typing "n" for "North". When you're done,
type 'q' to quit. Most importantly, have fun!
				   '''
welcome_message = textwrap.fill(welcome_message, WIDTH//2)
print(OPEN_WRAP)
print(welcome_message)
print(CLOSE_WRAP)
while game_loop:
    # Write a loop that:
    # * Prints the current room name
    print(f"|--     {player1.cur_room.name}     --|".center(WIDTH))
    # Prints the current description (the textwrap module might be useful here)
    for line in textwrap.wrap(player1.cur_room.desc, width=WIDTH//2):
        print(line.center(WIDTH))

    # * Waits for user input and decides what to do.
    action = input(
                   (f'What would you like to do?\n> ')).strip().lower()

    # If player tries to take or get, call method to handle command
    if action.startswith('take') or action.startswith('get'):
        print(OPEN_WRAP)
        player1 = player1.update_inventory(action)
        print(CLOSE_WRAP)

    elif action in ('i', 'inv', 'inventory'):
        print(OPEN_WRAP)
        player1.display_inventory()
        print(CLOSE_WRAP)

    # If the user enters "q", quit the game.
    elif action == 'q' or action == 'quit':
        print(OPEN_WRAP)
        print('Thanks for playing!')
        print(CLOSE_WRAP)
        game_loop = False
    else:
	    # If the user enters a cardinal direction, try to move to the room there.
	    # Print an error message if the movement isn't allowed.
        print(OPEN_WRAP)
        player1.cur_room = player1.update_room(action)
        print(CLOSE_WRAP)
        #print('--------------------\n'.rjust(WIDTH//4))
        directions = [i[0].upper() for i
                      in [*player1.cur_room.__dict__.keys()][2:]]
        print(f"Available directions are: {directions}\n")
