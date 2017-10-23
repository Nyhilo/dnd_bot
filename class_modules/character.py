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
			char_file = json.load(cfg)

		self.user_id = user_id
		self.user = username
		self.hero_name       = char_file['characterName']
		self.hero_exp        = char_file['expPoints']
		self.hero_class      = char_file['class']
		self.hero_level      = char_file["level"]
		self.hero_background = char_file["background"]
		self.hero_race       = char_file["race"]
		self.hero_alignment  = char_file["alignment"]
		self.hero_attributes = char_file["attributes"]
		self.hero_skills     = char_file["skills"]


	def get_attr(self, attribute):

		for attrs in self.hero_attributes:
			if attrs['name'] == attribute:
				return(attrs["value"])

	def get_uid(self):
		return self.user_id