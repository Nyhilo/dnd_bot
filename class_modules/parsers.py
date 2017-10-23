import argparse

class money_parser():
	"""
	This handles any money related commands.
	The following commands can be passed into it.


	Removal commands
	-c, --copper_r X   :: Remove X copper from player
	-s, --silver_r X   :: Remove X Silver from player
	-e, --electrum_r X :: Remove X Electrum from player
	-g, --gold_r X     :: Remove X Gold from player
	-p, --platinum_r X :: Remove X Platinum from player

	Addition commands
	+c, ++copper X   :: Give X copper to player
	+s, ++silver X   :: Give X silver to player
	+e, ++electrum X :: Give X electrum to player
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
		self.parser.add_argument("-e", "--electrum_r", help="Remove electrum", type=int, metavar="")
		self.parser.add_argument("-g", "--gold_r", help="Remove gold", type=int, metavar="")
		self.parser.add_argument("-p", "--platinum_r", help="Remove platinum", type=int, metavar="")
		self.parser.add_argument("+c", "++copper", help="Add coppers", type=int, metavar="")
		self.parser.add_argument("+s", "++silver", help="add silvers", type=int, metavar="")
		self.parser.add_argument("+e", "++electrum", help="add electrum", type=int, metavar="")
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
			

	def handle_transactions(self, hero_object):
		"""
		Simple if statements to check the arguments
		passed in.
		"""


		returned_info = ["Money for {}\n".format(hero_object.user)]

		# Anyone with ideas on how to shorten these if statements?
		if self.args.copper_r:
			returned_info.append("Copper remaining: {}".format(hero_object.mod_money(money='copper', amt=self.args.copper_r, add=False)))
		
		if self.args.silver_r:		
			returned_info.append("Silver remaining: {}".format(hero_object.mod_money(money='silver', amt=self.args.silver_r, add=False)))

		if self.args.electrum_r:
			returned_info.append("Electrum remaining: {}".format(hero_object.mod_money(money='electrum', amt=self.args.electrum_r, add=False)))
		
		if self.args.gold_r:
			returned_info.append("Gold remaining: {}".format(hero_object.mod_money(money='gold', amt=self.args.gold_r, add=False)))
		
		if self.args.platinum_r:
			returned_info.append("Platinum remaining: {}".format(hero_object.mod_money(money='platinum', amt=self.args.platinum_r, add=False)))
		
		if self.args.copper:
			returned_info.append("Copper remaining: {}".format(hero_object.mod_money(money='copper', amt=self.args.copper, add=True)))
		
		if self.args.silver:
			returned_info.append("Silver remaining: {}".format(hero_object.mod_money(money='silver', amt=self.args.silver, add=True)))

		if self.args.electrum:
			returned_info.append("Electrum_remaining: {}".format(hero_object.mod_money(money="electrum", amt=self.args.electrum, add=True)))

		if self.args.gold:
			returned_info.append("Gold remaining: {}".format(hero_object.mod_money(money='gold', amt=self.args.gold, add=True)))

		if self.args.platinum:
			returned_info.append("Platinum remaining: {}".format(hero_object.mod_money(money='platinum', amt=self.args.platinum, add=True)))

		if self.args.note:
			# TODO: Save notes with character. 
			#       Maybe a separate 'transaction log'?
			returned_info.append("Transaction note: {}".format(" ".join(self.args.note)))

		if self.args.list:
			returned_info.append(hero_object.get_gold())

		return "\n".join(returned_info)

class hero_parser():
	"""
	Hero handler

	Removal Commands

	-i, --inv_r X	:: remove item. "list" will show all items. 
	-w, --wep_r X	:: remove weapon. "list" will show all weapons.

	Addition commands

	+i, ++inv X		:: Add item. "list" will show all items.
	+w, ++wep X		:: Add weapon. "list" will show all weapons.

	"""

	def __init__(self):

		self.parser = argparse.ArgumentParser(prefix_chars="-+")
		self.parser.add_argument("-a", "--attr", help="Display an attribute", type=str, metavar="", nargs="*")
		self.parser.add_argument("-i", "--inv_r", help="Display inventory/remove item", type=str, metavar="", nargs="*")
		self.parser.add_argument("+i", "++inv", help="Display inventory/add item", type=str, metavar="", nargs="*")
		self.parser.add_argument("-w", "--wep_r", help="Display weapons/remove weapon", type=str, metavar="", nargs="*")
		self.parser.add_argument("+w", "++wep", help="Display weapons/add weapon", type=str, metavar="", nargs="*")

	def parse(self, arg_list):

		# This suffers from the same problem as the
		# parser money_parser.parse().
		# Also needs fixin.
		self.args = self.parser.parse_args(arg_list)

	def handle_args(self, hero_object):

		returned_info = ["Info for {}:\n".format(hero_object.user)]
		attributes = {"str" : "Strength", "dex" : "Dexterity",
					  "con" : "Constitution", "int" : "Intelligence",
					  "wis" : "Wisdom", "cha" : "Charisma"}



		# This below needs condensing.
		try:
			if self.args.attr:
				for i in self.args.attr:
						attr = attributes[i]
						returned_info.append("{} :: {}".format(attr, hero_object.get_attr(attr)))


			if self.args.inv_r:
				inv_item = " ".join(self.args.inv_r)
				if self.args.inv_r[0] == "list":
					returned_info.append("Inventory items: {}".format(hero_object.items))

				else:	
					returned_info.append(hero_object.mod_inv(remove_item=True, item=inv_item))

			if self.args.inv:
				inv_item = " ".join(self.args.inv)
				if self.args.inv[0] == "list":
					returned_info.append("Inventory items: {}".format(hero_object.items))

				else:
					returned_info.append(hero_object.mod_inv(add_item=True, item=inv_item))

			if self.args.wep_r:
				weapon = " ".join(self.args.wep_r)
				if self.args.wep_r[0] == "list":
					returned_info.append("Weapons: {}".format(hero_object.weapons))
				else:
					returned_info.append(hero_object.mod_inv(remove_item=True, item=weapon, inventory='w'))

			if self.args.wep:
				weapon = " ".join(self.args.wep)
				if self.args.wep[0] == "list":
					returned_info.append("Weapons: {}".format(hero_object.weapons))
				else:
					returned_info.append(hero_object.mod_inv(add_item=True, item=weapon, inventory='w'))

			return "\n".join(returned_info)

		except KeyError as e:
			print(e)
			return "Incorrectly formatted attribute.\nTry cha, con, dex, int, str, or wis"

		
