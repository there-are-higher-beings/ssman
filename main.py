name = ('ssman'.upper())
version = '1.0.0'

print(
	f"""
	{name} {version}
	Copyright (c) .wncry#4617
	Licensed under the GNU AGPL 3.0
	"""
)

import discord
import time
import random
from discord.ext import commands

client = commands.Bot(command_prefix = ["~E~"])

@client.event
async def on_ready():
	print("Connected to Discord at " + time.ctime())
	perms = discord.Permissions(11264)
	print("Invite link: {}".format(discord.utils.oauth_url(client.user.id, perms)))

	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="you sleep"))
	print('\n:::\n')

ping_responses = ['stop', 'stap', 'really?', 'can you not?', 'bruh wth', 'i will kick you', '<https://bfy.tw/PFhi>']

@client.listen('on_message')
async def idk(message):
	msg = message.content.lower()
	if message.author == client.user:
		return

	if msg.startswith('/speak '):
		await message.delete()
		await message.channel.send(message.content[7:])

	if client.user.mentioned_in(message):
		time.sleep(1)
		await message.channel.send(random.choice(ping_responses))

client.run('TOKEN')
