import discord
import asyncio
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command-prefix='.')

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Zypox"))


@client.command(pass_context=True)
async def livecounter(ctx):
	while True:
		author = ctx.message.author
		guild = ctx.message.guild
		print('- ', author, '-> LiveCounter-Command')
		members = 0
		for member in guild.members:
			print(' --> ',member)
			members = members + 1
		file = open('channel_id.txt', 'r')
		channelid = file.read()
		print(' + Channel ID Config: ', channelid)
		VoiceChannel = client.get_channel(569875375149023232)
		await VoiceChannel.edit(name='Mitglieder: {}'.format(members))


client.run("NTY5NTI5MDQ2NDU1ODEyMDk2.XLx9yA.Y7Kmoka0NaTjvKHsly-MU5p7bGU")