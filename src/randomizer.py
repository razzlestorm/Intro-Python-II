from colorama import Fore, Style
import random

DESCRIPTORS = ['dazzling',
               'glittering',
               'glistening',
               'shiny',
               'glowing',
               'enchanted', ]

COLORS = [Fore.RED,
          Fore.GREEN,
          Fore.YELLOW,
          Fore.BLUE,
          Fore.MAGENTA,
          Fore.CYAN,
          Fore.WHITE]


# This adds a color to the descriptor words of an item's name.
def adj_randomizer(desc_list, itemobj):
    color = random.choice(COLORS)
    itemobj.name = (f'{color}{random.choice(desc_list)} '
                    f'{Style.RESET_ALL}' + itemobj.name)
    return itemobj


# Called once at the start of the game to populate the dungeon.
def populate_room(room, itemlist):
    if random.random() > 0.5:
        item = random.choice(itemlist)
        room.inventory.append(item)
        print(f'{item.name} in {room.name}')
        update_string = f' You see a {item.name} on the ground.'
        room.desc += update_string
        return room
    else:
        print(f'Nothing added to {room.name}')
        return room
