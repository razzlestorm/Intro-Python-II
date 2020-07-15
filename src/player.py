# Write a class to hold player information, e.g. what room they are in
# currently.
import os

WIDTH = os.get_terminal_size()[0]
direction_map = {
                'n': 'North',
                'e': 'East',
                's': 'South',
                'w': 'West'
                }


class Player:
    def __init__(self, cur_room):
        self.cur_room = cur_room

    inventory = []

    def update_room(self, player_input):
        current = self.cur_room
        # Check if movement is available based on the mappiung in adv.py
        if f'{player_input}_to' in current.__dict__:
            current = current.__dict__[f'{player_input}_to']
            print((f'You move to the '
                   f'{direction_map[player_input]}.'.rjust(WIDTH//4)))

            return current
        elif player_input == 'q':
            print('Thanks for playing!'.rjust(WIDTH//4))
        else:
            print('Try moving in a direction you can see.'.rjust(WIDTH//4))
            # Unpack the key object in current, get anything after name, desc

            return current
