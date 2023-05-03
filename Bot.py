import discord
import Boardgame
import re
import yaml
from tabulate import tabulate

with open('token.yml', 'r') as yml:
    config = yaml.safe_load(yml)
TOKEN = config['token']
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
	if message.author.bot:
		return
	id = "<@1002461482132455464>"
	content = message.content
	text = re.sub(id, '', content)
	if  (id in message.content) & (not len(text) == 0):
		bg = Boardgame.BoardGame
		id = bg.getIdFromText(text)
		if(not id is None):
			title = bg.getGameTitle(id)
			data1 = tabulate(bg.getData1(id),tablefmt='simple',showindex=False)
			data2 = tabulate(bg.getData2(id),tablefmt='simple',showindex=False)
			await message.channel.send(title)
			await message.channel.send(data1)
			await message.channel.send(data2)
		else:
			await message.channel.send("データが存在しません")

client.run(TOKEN)