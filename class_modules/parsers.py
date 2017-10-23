import argparse

class money_parser():
	"""
	This handles any money related commands.
	The following commands can be passed into it.


	Removal commands
	-c, --copper-r X   :: Remove X copper from player
	-s, --silver-r X   :: Remove X Silver from plater
	-g, --gold-r   X   :: Remove X Gold from player
	-p, --platinum-r X :: Remove X Platinum from player

	Addition commands
	+c, ++copper X   :: Give X copper to player
	+s, ++silver X   :: Give X silver to player
	+g, ++gold X     :: Give X gold to player
	+p, ++platinum X :: Give X platinum to player

	Misc options
	-n, --note "Note here" :: Add a note to the transaction. 
							  Must include quotation marks.
	-l, --list             :: Display current gold
	"""

	def __init__(self):
		self.parser = argparse.ArgumentParser(prefix_chars="-+")


		self.parser.add_argument("-l", "--list", help="List player's gold", action="store_true")
		self.parser.add_argument("-n", "--note", help="Add a note to transaction", type=str, metavar="", nargs='*')
		self.parser.add_argument("-c", "--copper_r", help="Remove coppers", type=int, metavar="")
		self.parser.add_argument("-s", "--silver_r", help="Remove silvers", type=int, metavar="")
		self.parser.add_argument("-g", "--gold_r", help="Remove gold", type=int, metavar="")
		self.parser.add_argument("-p", "--platinum_r", help="Remove platinum", type=int, metavar="")
		self.parser.add_argument("+c", "++copper", help="Add coppers", type=int, metavar="")
		self.parser.add_argument("+s", "++silver", help="add silvers", type=int, metavar="")
		self.parser.add_argument("+g", "++gold", help="Add gold", type=int, metavar="")
		self.parser.add_argument("+p", "++platinum", help="Add platinum", type=int, metavar="")


	def parse(self, arg_list):


		# Current issues with parser that needs looking at:
		#   - Passing in a str instead of an int will cause
		#     a ValueError exception. Putting this in a try
		#     except clause will catch the exception, but 
		#     while trying to handle that exception, another
		#     one will occur. While handling the second one,
		#     another exception will occur and cause the 
		#     entire program to die. 
		#     Example problem command: .money -c p 
		self.args = self.parser.parse_args(arg_list)
			

	def handle_transactions(self):
		"""
		Simple if statements to check the arguments
		passed in.
		"""


		returned_info = []

		# Anyone with ideas on how to shorten these if statements?
		if self.args.copper_r:		
			returned_info.append("Removed {} cp".format(self.args.copper_r))
		
		if self.args.silver_r:		
			returned_info.append("Removed {} sp".format(self.args.silver_r))
		
		if self.args.gold_r:
			returned_info.append("Removed {} gp".format(self.args.gold_r))
		
		if self.args.platinum_r:
			returned_info.append("Removed {} plat".format(self.args.platinum_r))
		
		if self.args.copper:
			returned_info.append("Added {} cp".format(self.args.copper))
		
		if self.args.silver:
			returned_info.append("Added {} sp".format(self.args.silver))
		
		if self.args.gold:
			returned_info.append("Added {} gp".format(self.args.gold))

		if self.args.platinum:
			returned_info.append("Added {} plat".format(self.args.platinum))

		if self.args.note:
			returned_info.append("Transaction note: {}".format(" ".join(self.args.note)))

		if self.args.list:
			returned_info.append("You have \u221e monies")

		return "\n".join(returned_info)

class hero_parser():
	"""
	Hero handler

	Attribute Modifying


	"""

	def __init__(self):

		self.parser = argparse.ArgumentParser(prefix_chars="-+")
		self.parser.add_argument("-m", "--modify", help="Lower an attribute or remove an item")
		self.parser.add_argument("-a", "--attr", help="Display an attribute", type=str, metavar="", nargs="*")
		self.parser.add_argument("-i", "--inv_r", help="Display inventory/remove item", type=str, metavar="", nargs="*")
		self.parser.add_argument("+i", "++inv", help="Display inventory/add item", type=str, metavar="", nargs="*")

	def parse(self, arg_list):

		self.args = self.parser.parse_args(arg_list)

	def handle_args(self, hero_object):

		returned_info = []
		attributes = {"str" : "Strength", "dex" : "Dexterity",
					  "con" : "Constitution", "int" : "Intelligence",
					  "wis" : "Wisdom", "cha" : "Charisma"}


		try:
			if self.args.attr:
				for i in self.args.attr:
						attr = attributes[i]
						returned_info.append("{} :: {}".format(attr, hero_object.get_attr(attr)))


			if self.args.inv_r:
				inv_item = " ".join(self.args.inv_r)
				if self.args.inv_r[0] == "list":
					returned_info.append("Inventory items: {}".format(hero_object.items))
					returned_info.append("Inventory weapons: {}".format(hero_object.weapons))

				elif hero_object.mod_inv(remove_item=True, item=inv_item):
					returned_info.append("{} removed.".format(inv_item))

			if self.args.inv:
				inv_item = " ".join(self.args.inv)
				if self.args.inv[0] == "list":
					returned_info.append("Inventory items: {}".format(hero_object.items))
					returned_info.append("Inventory weapons: {}".format(hero_object.weapons))

				elif hero_object.mod_inv(add_item=True, item=inv_item):
					returned_info.append("{} added.".format(inv_item))


			return "\n".join(returned_info)

		except KeyError as e:
			print(e)
			return "Incorrectly formatted attribute.\nTry cha, con, dex, int, str, or wis"

		
