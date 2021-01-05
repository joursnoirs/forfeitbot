import os 
import requests
import json
import praw
import discord
import random
from random import randint 
from discord.ext import commands


#importing the redditconfig 
from redditsubconfig import REDDIT_APP_SECRET
from redditsubconfig import REDDIT_APP_ID
from redditsubconfig import REDDIT_MEME_SUBS

#boot message
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)


bot = commands.Bot(command_prefix="$")

reddit = praw.Reddit(
    client_id=REDDIT_APP_ID,
    client_secret=REDDIT_APP_SECRET,
    user_agent='ForfeitBot made by Mæx#1313')




#Letting dev know bot is online
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))





#Gives the Ping of the bot. Reminder to add uptime command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')
    await ctx.send('My ping is ' + str(bot.latency * 1000)[0:6] + ' ms! Pog!')


#Simple Hello command
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


#$inspire function as a test for api pulls
@bot.command()
async def inspire(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    await ctx.send(quote)


@bot.command()
async def inspite(ctx):
    await ctx.send('Learn to fucking spell dumbass! its $inspire!')


#requested by Dalton
@bot.command()
async def slut(ctx):
    await ctx.send('***YES DADDY!!! HARDER!!!!!***')



#########################Ideas for bot###############################
#List maker
#Sauce supplier with random numbers
#make reddit image puller
#make command to pull copypasta
#Make a $toxic command that send user to toxicjail.

@bot.command()
async def uwu(ctx):
	async with ctx.channel.typing():
  		await ctx.send(
        	'Rawr X3 *nuzzles* How are you? *pounces on you* youre so warm o3o *notices you have a bulge* someones happy! *nuzzles your necky wecky* ~murr~ hehe ;) *rubbies your bulgy wolgy* youre so big! *rubbies more on your bulgy wolgy* it doesnt stop growing .///. *kisses you and licks your neck* daddy likes ;) *nuzzle wuzzle* I hope daddy likes *wiggles butt and squirms* I wanna see your big daddy meat! *wiggles butt* I have a little itch o3o *wags tails* can you please get my itch? *put paws on your chest* nyea~ its a seven inch itch *rubs your chest* can you pwease? *squirms* pwetty pwease? :( I need to be punished *runs paws down your chest and bites lip* like, I need to be punished really good *paws on your bulge as I lick my lips* Im getting thirsty. I could go for some milk *unbuttons your pants as my eyes glow* you smell so musky ;) *licks shaft* mmmmmmmmmmmmmmmmmmm so musky ;) *drools all over your cawk* your daddy meat. I like. Mister fuzzy balls. *puts snout on balls and inhales deeply* oh my gawd. Im so hard *rubbies your bulgy wolgy* *licks balls* punish me daddy nyea~ *squirms more and wiggles butt* I9/11 lovewas an yourinside muskyjob goodness *bites lip* please punish me *licks lips* nyea~ *suckles on your tip* so good *licks precum off your cock* salty goodness~ *eyes roll back and goes balls deep*' )




@bot.command()
async def meme(ctx,  subreddit: str = ""):
		async with ctx.channel.typing():
				reddit = praw.Reddit(
				client_id=REDDIT_APP_ID,
				client_secret=REDDIT_APP_SECRET,
				user_agent="ForfeitBot by Mæx#1313 v1.0")
				
				sub_to_pick = REDDIT_MEME_SUBS[random.randint(1,17)]
				
				limit=randint(3, 25)
				post_to_pick = reddit.subreddit(sub_to_pick).hot(limit=limit)
				await ctx.send('This post came from ' + ((post_to_pick).url))
				await ctx.send(next(post_to_pick).url)
	
							###Might allow to not pick sticky##
			#post_to_pick = next(x for x in reddit.subreddit(sub_to_pick).hot() if not x.stickied)


				#if reddit:
				#	print('banana')
						#working
				#	chosen_subreddit = REDDIT_MEME_SUBS[0]
				#	if subreddit:
				#				#checks if sub is in approved list
				#			if subreddit in REDDIT_MEME_SUBS:
				#					chosen_subreddit = subreddit

				#	submission = reddit.subreddit(chosen_subreddit).hot()

				#	post_to_pick = random.randint(1, 10)
				#	for i in range(0, post_to_pick):
					#	submission = next(x for x in submission if not x.stickied)
					#await ctx.send(submission.url)
				
			#	else:
			#			await ctx.send('The bot has encountered a hiccup. Please contact @Mæx#1313')

@bot.command()
async def daddy(ctx):
	async with ctx.channel.typing():
    
		await ctx.send('Daddy 👨 touches ✋ my 👧 thicc ass 🍑He 👨tells me 👧Im a pretty lass Puts his penis 🍆 in ➡️🍑⬅️ my butt 🤤😫😥Oh my god, Im such a slut! 💃💦Mommy 👩 sees 👀😲 us, and shes mad 😡😠😤Im sorry 😓😔hun, the sex 🍑🍆💦 was bad!👎🔚Mommy pulls out ⬆️ guns 🔫 akimbo 🔫👩🔫Because she hates 😲😠 her little bimbo 👧The Cummies 💦 are dripping ⬇️💧from my hole 🍑I cant 🙅 stop working 😩😫💪 on Daddys 👨 pole 💈😫Mommy 👩 shoots 🔫, her shots all miss 😂Daddy 👨 and I 👩 share a special ☄️ kiss 💋One ☝️ round left 👈, Mommy 👩 takes the gun 🔫She rests 💤 the barrel 🛢️ on her tongue 👅Goodbye 👋 world 🌍, and goodbye 👋 cheater! 👨I hope youre happy ☺️😄 with your stupid 📖🚫 wife 👩 beater! 👊The gun 🔫 goes bang 💥, Mommy 👩 dies 💀☠️⚰️But we 👨👧 dont 🚫 care, Daddy 👨 just sighs 🌬️😤No 🚫 thoughts 💭 in her 👩 head 💆, no 🚫blood 💉 in her heart➡️♥️⬅️That stupid 📖🚫whore 💃 cant 🚫tear us apart. 💖💕💓')

@bot.command()
async def homie(ctx):
	async with ctx.channel.typing():
		await ctx.send('Yo my homeslice breadslice dawg with butter and salsa my friend, what the hizzle is up with ur dizzle, brodawgio, I dont mean to be unhip, but if you keep this up i may have to get not so dorky with u my friendly amigo of brohominess. It would be most unpleasant and not at all cash money to partake in this kind of un-excellent behavior, but by golly, you seem to leave me with no other option in this fresh turn of happenstance homie-frendo would you like that I would not like to have to get undorky with you, but gosh diddly heckin darn, i find this is a most un-radical, non-groovy, totally unsexy situation I find myself in with you, my bestest of amigofriendlydudes')

@bot.command()
async def owo(ctx):
    await ctx.send('*𝓌𝒶𝓉𝓈 𝒹𝒾𝓈?*ღ(O꒳Oღ)')
    await ctx.send('*𝓃𝓊𝓏𝓏𝓁𝑒𝓈 𝓎𝑜𝓊*(。O⁄ ⁄ω⁄ ⁄ O。)')


#I actually don't know if this does anything lmao
@bot.command()
async def on_message(message):
    if message.author == bot.user:
        return


bot.run(os.getenv('TOKEN'))
