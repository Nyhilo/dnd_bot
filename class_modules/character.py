# character parser
# Read in json file, save a character 
# object in the bot

import json

class hero():
	"""
	Creates a character to reference.
	user_id is grabbed from ctx.message.author.id
	username is ctx.message.author
	char_file is the path to that user's 
	folder + filename.
	"""


	def __init__(self, char_file, user_id, username):
		with open(char_file, 'r') as cfg:
			char_info = json.load(cfg)

		self.char_file 		 = char_file
		self.user_id 		 = user_id
		self.user 		 	 = username
		self.hero_name       = char_info['characterName']
		self.hero_exp        = char_info['expPoints']
		self.hero_class      = char_info['class']
		self.hero_level      = char_info["level"]
		self.hero_background = char_info["background"]
		self.hero_race       = char_info["race"]
		self.hero_alignment  = char_info["alignment"]
		self.hero_attributes = char_info["attributes"]
		self.hero_skills     = char_info["skills"]
		self.items      	 = char_info["inventory"][0]["items"]
		self.gold			 = char_info["inventory"][0]["money"]
		self.weapons		 = char_info["inventory"][0]["weapons"]


	def get_attr(self, attribute):

		for attrs in self.hero_attributes:
			if attrs['name'] == attribute:
				return(attrs["value"])

	def get_gold(self):
		copper = self.gold['copper']
		silver = self.gold['silver']
		elec = self.gold['electrum']
		gold = self.gold['gold']
		plat = self.gold['platinum']

		return "copper: {}\nSilver: {}\nElectrum: {}\nGold: {}\nPlatinum: {}".format(copper,silver,elec,gold,plat)


	def get_uid(self):
		return self.user_id


	def mod_inv(self, remove_item=False, add_item=False, item=None, inventory='i'):
		"""
		If remove_item is True, then the
		item is removed if it exists in
		the inventory.

		If add_item is True, the item
		is added in.

		If item is None, it returns
		with a string stating no item
		was provided.
		"""

		if inventory   == 'i': inventory = self.items
		elif inventory == 'w': inventory = self.weapons

		if item is None:
			return "No item provided."
		if remove_item:
			if item in inventory:
				return "{} removed.".format(item)
			else:
				return "No such item: {}".format(item)
		if add_item:
			inventory.append(item)
			return "{} added.".format(item)		


	def mod_money(self, money="copper", amt=0, add=True):
		"""
		Add or remove money
		"""
		# TODO: Add in change calculations.
		if add:
			self.gold[money] += amt
		else:
			self.gold[money] -= amt

		return self.gold[money]


	def write_hero(self):
		"""
		Writes hero info to file
		"""
		pass
