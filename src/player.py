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

    inventory = {}

    def update_room(self, player_input):
        current = self.cur_room
        # Check if movement is available based on the mappiung in adv.py
        if f'{player_input}_to' in current.__dict__:
            current = current.__dict__[f'{player_input}_to']
            print((f'You move to the '
                   f'{direction_map[player_input]}.'))

            return current
        else:
            print('Try typing a direction or valid command'.rjust(WIDTH//4))
            # Unpack the key object in current, get anything after name, desc

            return current

    def update_inventory(self, player_input):
        item = player_input.split(' ')[1:]
        if any(word in item for item in self.cur_room.inventory):
            print(f"You take the {' '.join(item)} and put it in your pack.")
            self.inventory[' '.join(item)] += 1
            return self
        else:
            print(f"You look around for a "
			      f"{' '.join(item)}, but don't see that.")
            return self

    def display_inventory(self):
        if not self.inventory:
            print("You do not have anything in your inventory!")
        else:
            print('Your inventory contains the following:')
            for k, v in self.inventory:
                print(f'{v} {x}\n')
        return self
