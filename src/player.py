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

    # Laboriously checks room for any word in player's input, then adds to inv
    def add_to_inventory(self, player_input):
        item = player_input.split(' ')[1:]
        condition = [word for word in item]
        if any([x for x in condition
                if x in str([i.name for i in self.cur_room.inventory])]):
            for word in condition:
                for i in self.cur_room.inventory:
                    if word in i.name:
                        print((f'You take the {i.name}'
                               f' and put it in your pack.'))
                        if self.inventory.get(i) is not None:
                            self.inventory[i] += 1
                            self.cur_room.inventory.remove(i)
                            self.cur_room.desc = self.cur_room.desc.replace(
                                         f' You see a {i.name}'
                                         f' on the ground.', '', 1)
                        else:
                            self.inventory[i] = 0
                            self.inventory[i] += 1
                            self.cur_room.inventory.remove(i)
                            self.cur_room.desc = self.cur_room.desc.replace(
                                  f' You see a {i.name} on the ground.', '', 1)
            return self
        else:
            print(f"You look around for a "
                  f"{' '.join(item)}, but don't see that.")
            return self

    def remove_from_inventory(self, player_input):
        item = player_input.split(' ')[1:]
        condition = [word for word in item]
        if any([x for x in condition
               if x in str([i.name for i in self.inventory])]):
            for word in condition:
                for i in self.inventory.copy():
                    if word in i.name:
                        print(f"You let the {i.name} fall to the ground")
                        if self.inventory[i] > 1:
                            self.inventory[i] -= 1
                            self.cur_room.inventory.append(i)
                            self.cur_room.desc += (f' You see a {i.name}'
                                                   f' on the ground.')
                        else:
                            del self.inventory[i]
                            self.cur_room.inventory.append(i)
                            self.cur_room.desc += (f' You see a {i.name}'
                                                   f' on the ground.')
            return self
        else:
            print(f"You rummage around in your pack for a "
                  f"{' '.join(item)}, but don't see that.")
            return self

    # Displays number of items in inventory
    def display_inventory(self):
        if not self.inventory:
            print("You do not have anything in your inventory!")
        else:
            print('Your inventory contains the following:')
            for k, v in self.inventory.items():
                print(f'{v} {k.name}\n')
        return self
