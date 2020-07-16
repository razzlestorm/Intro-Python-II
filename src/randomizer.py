import random

DESCRIPTORS = ['dazzling',
               'glittering',
			   'glistening',
			   'shiny',
			   'glowing',
			   'darkened',
			   ]

def adj_randomizer(desc_list, itemobj):
	itemobj.name = f'{random.choice(desc_list)} ' + itemobj.name
	return itemobj

def populate_room(room, itemlist):
    if random.random() > 0.5:
        item = random.choice(itemlist)
        room.inventory.append(item)
        print(f'{item.name} in {room.name}')
        #print(f'{item.name} in {room.name}')
        return room
    else:
        print(f'Nothing added to {room.name}')
        return room
