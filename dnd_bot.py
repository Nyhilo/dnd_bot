import setup
import discord
import os
from discord.ext.commands import Bot
import class_modules.character
from class_modules import parsers
from class_modules import character


money_parser = parsers.money_parser()
hero_parser  = parsers.hero_parser()

characters = {}
test_char = "characters/Rockheroes.json"

dnd_bot = Bot(command_prefix=setup.prefix,
              description=setup.description,
              pm_help=True)

@dnd_bot.event
async def on_ready():
	game = discord.Game(name="DnD")
	return await dnd_bot.change_presence(game=game)

@dnd_bot.command(pass_context=True)
async def hello(ctx):
	print(ctx.message.author.id)
	return await dnd_bot.send_message(ctx.message.author, "hello")



@dnd_bot.command()
async def show_attributes(*commands):
	print(*commands)
	return await dnd_bot.say("Check console")


@dnd_bot.command()
async def money(*args):
	money_parser.parse(list(args))
	return await dnd_bot.say(money_parser.handle_transactions())

@dnd_bot.command(pass_context=True)
async def hero(ctx,*args):
	author_id = ctx.message.author.id
	user = ctx.message.author

	if not author_id in characters:
		characters[author_id] = character.hero(test_char, author_id, user)

	hero_parser.parse(args)
	return await dnd_bot.say(hero_parser.handle_args(characters[author_id]))

	# return await dnd_bot.say("Strength: {}".format(characters[author_id].get_attr('Strength')))



dnd_bot.run(setup.bot_token)