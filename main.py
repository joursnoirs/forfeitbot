import os
import requests
import json
import praw
import discord
from discord.ext import commands

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user)


bot = commands.Bot(command_prefix="$")

reddit = praw.Reddit(
    client_id='794223537396121610',
    client_secret=(os.getenv('CLIENT_SECRET')),
    user_agent='ForfeitBot')

#$inspire function as a test for api pulls



#boot message. WHY DOES THIS NOT WORK
@bot.command()
async def on_ready(ctx):
	print('Logged in as {0.user}'.format(bot))


@bot.command()
async def ping(ctx):
	await ctx.send('Pong!')
	await ctx.send('My ping is '+ str(bot.latency*1000)[0:6] + ' ms!')

@bot.command()
async def hello(ctx):
		await ctx.send('Hello!')

@bot.command()
async def inspire(ctx):
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " -" + json_data[0]['a']
	await ctx.send(quote)

@bot.command()
async def on_message(message):
    if message.author == bot.user:
        return


bot.run(os.getenv('TOKEN'))
