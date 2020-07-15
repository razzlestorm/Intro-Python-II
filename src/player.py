# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, cur_room):
		self.cur_room = cur_room

	inventory = []

	def update_room(self, player_input):
		current = self.cur_room
		# Check if movement is available based on the mappiung in adv.py
		if player_input in current.__dict__:
			current = current.__dict__[player_input]
			print(f'You move to the {player_input[0].upper()}.')
			return current

		else:
			print('Try moving in a direction you can see.')
			return current
