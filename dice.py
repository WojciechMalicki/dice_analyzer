from random import randint

class Dice():
	"""symulowanie rzutu kostką"""
	def __init__(self, num_sides=6):
		"""Domyślnie K6"""
		self.num_sides = num_sides
		
	def roll(self):
		"""Rzut kością"""
		return randint(1, self.num_sides)