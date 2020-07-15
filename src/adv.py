from player import Player
from room import Room
import os
import textwrap

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer",
 					 """Dim light filters in from the south. Dusty
					  passages run north and east."""),

    'overlook': Room("Grand Overlook",
 					 """A steep cliff appears before you, falling
					  into the darkness. Ahead to the north, a light
					  flickers in the distance, but there is no way
 					  across the chasm."""),

    'narrow':   Room("Narrow Passage",
					"""The narrow passage bends here from west to north. "
					 The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber",
					 """You've found the long-lost treasure chamber!
					 Sadly, it has already been completely emptied by
					 earlier adventurers. The only exit is to the south."""),
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

# Make a new player object that is currently in the 'outside' room.
player1 = Player(room['outside'])

while game_loop:
# Write a loop that:
# * Prints the current room name
	print(f"|--     {player1.cur_room.name}     --|".center(WIDTH))
# * Prints the current description (the textwrap module might be useful here).
	for line in textwrap.wrap(player1.cur_room.desc, width=WIDTH//2):
		print(line.center(WIDTH))

# * Waits for user input and decides what to do.
	action = input('Which direction would you like to move? ').lower()
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
	print('------------------- '.rjust(WIDTH//4))
	player1.cur_room = player1.update_room(action)
	print('-------------------\n'.rjust(WIDTH//4))
	if action == 'q':
		game_loop = False
	else:
		directions = [i[0].upper() for i
					  in [*player1.cur_room.__dict__.keys()][2:]]
		print(f"Available directions are: {directions}")
#
# If the user enters "q", quit the game.
