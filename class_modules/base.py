import random
import math

class base_roller():
	
	def __init__(self, dice_amt=1, dice_sides=20):
		self.dice_amt = dice_amt
		self.sides = dice_sides

	def roll(self):
		return random.randint(1,self.sides)

	def handle_rolls(self, type_of_roll=None):
		"""
		The multi roll function will handle anything 
		that needs to be rolled, whether for advantage, 
		disadvantage, or neither. If for advantage, 
		it will return the greater of the two numbers, 
		else it will return the lesser of the two.

		Valid strings for type_of_roll are 'adv' and 'dis'
		for advantage and disadvantage respectively, and 
		None for no special rolling.
		"""

		if type_of_roll is None:
			return self.roll()
		elif type_of_roll == "adv":
			return max(self.roll(), self.roll())
		elif type_of_roll == "dis":
			return max(self.roll(), self.roll())
		else:
			return "Unknown roll type"

	def stealth_roll(self):
		"""
		Basically an advantage roll. Doing a 
		multi roll here. This function is 
		purely for ease of understanding.
		"""
		return handle_rolls("adv")

	def damage_roll(self, type_of_roll=None):
		"""
		Handles damage calculation
		"""
		damage = []
		for i in range(self.dice_amt):
			damage.append(self.handle_rolls(type_of_roll))
		return sum(damage)
