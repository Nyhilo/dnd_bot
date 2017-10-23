import json


with open("config/config.json", 'r') as cfg:
	config = json.load(cfg)

with open("config/bot_info.json", 'r') as inf:
	info = json.load(inf)

bot_token	= config["token"]
bot_name 	= config["name"]
avatar		= config["avatar"]
prefix 		= config["prefix"]

VERSION     = info["version"]
description = info["description"]