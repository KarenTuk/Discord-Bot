###############################
'''this loads the "DISCORD_TOKEN" string from the .env file'''

# import pip._vendor.certifi

from urllib.parse import quote
import random
import helpers
from ahttp import requests

from dotenv import load_dotenv
import os

from errorhandling import on_command_error

load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"] #grabs the token after loading it with load_dotenv()

###############################

import discord

from discord.ext import commands
import datetime
import json

intents = discord.Intents.default() # will require all intents by default, change this to match your bot's intents

bot = commands.Bot(
                    command_prefix=";",
                    intents=intents,
                    #help_command=  <- uncomment this if you want to write your own help command
                    )

bot.on_command_error = on_command_error

@bot.event # @bot.event attaches the function to the bot's event listener. 
async def on_ready(): #the name of the function denotes which event it listens to
    print(f"{bot.user.name} has connected to Discord!")

@bot.event
async def on_message(message : discord.Message):
    # print(message.content)
    if message.author == bot.user: #does not attempt to process any command called by the bot itself
        return
    if message.content == "Hi":
        await message.channel.send("😎👍")
    await bot.process_commands(message=message)

@bot.command()
async def pp(ctx):
    """ Create a pp in discord """
    pp_s = random.randint(0,100)
    shaft = "=" * pp_s
    await ctx.embed(title = f"8{shaft}D")

@bot.command()
async def clown(ctx: commands.Context, *, msg:str):
    """ Alternative capitalization of characters in a sentence """
    result = ""
    for x in range(len(msg)):
        if x%2==0 and msg[x].islower():
            result += (msg[x].capitalize())
        elif x%2==0 and msg[x].isupper():
            result += (msg[x].lower())
        else:
            result += (msg[x])
    await ctx.send(result) 

@bot.command()
async def cardi(ctx: commands.Context, *, msg:str):
    """ Cardi-fy a sentence"""
    okur = "U" * random.randint(1,10) + "R" * random.randint(1,10)
    await ctx.send(f"{msg} OK{okur}")

@bot.command()
async def period(ctx: commands.Context, *, msg:str):
    """ Add 'PERIODT' to the end of your message """
    await ctx.send(f"{msg}. PERIODT 💅")

@bot.command()
async def sis(ctx: commands.Context):
    await ctx.embed(title=f"🙌 Go off Sis 🙌 ")

@bot.command()
async def spread(ctx: commands.Context, *, msg:str):
    """ Spread the characters in a sentence"""
    result = ""
    for x in range(len(msg)):
        result+= " " + msg[x]
    await ctx.send(result)

@bot.command()
async def wendys(ctx:commands.Context):
    await ctx.embed(title="Ma'am, this is a Wendy's. ")

@bot.command()
async def pfp(ctx, member: discord.Member=None):
    member = member or ctx.author
    await ctx.embed(title=member, image_url=member.avatar_url)

@bot.command()
async def info(ctx, member: discord.Member=None):
    member = member or ctx.author
    await ctx.embed(title="Member info", description = f"Display name: {member.display_name}\nMember id: {member.id}\nDate created: {member.created_at.strftime('%A, %d %B %Y')}")

@bot.command()
async def date(ctx:commands.Context):
    await ctx.embed(title="Today's Date", description = datetime.datetime.today().strftime("%A, %d %B %Y"))


@bot.command()
async def kanye(ctx:commands.Context):
    data = await requests.get_json("https://api.kanye.rest/")
    if data is None:
        await ctx.embed(title = "Could not get quote")
    await ctx.embed(title = "Kanye West Quote", description = data["quote"])


@bot.command()
async def bored(ctx:commands.Context):
    data = await requests.get_json("http://www.boredapi.com/api/activity/")
    if data is None:
        await ctx.embed(title = "could not fulfill request")
    await ctx.embed(title="Random Activity", description = f'Activity: {data["activity"]}\nType: {data["type"]}\nParticipants: {data["participants"]}\nPrice: {data["price"]}\nAccesibilty Rating: {data["accessibility"]}')

@bot.command()
async def fox(ctx:commands.Context):
    data = await requests.get_json("https://randomfox.ca/floof/?ref=apilist.fun")
    if data is None:
        await ctx.embed(title = "could not fulfill request")
    await ctx.embed(title = "Random Fox Picture", image_url= data["image"])


@bot.command()
async def google(ctx:commands.Context, *, query: commands.clean_content):
    data = await requests.get_json(f"https://gurgle.nathaniel-fernandes.workers.dev/?q={quote(query)}", [])

    if len(data) == 0:
        return await ctx.embed(title = "could not fulfill request")
    await ctx.embed(image_url = data[0], footer={"text": f"search term: {query}"}, color=0x2F3136)




bot.run(TOKEN) #runs a bot with the specified [TOKEN], this connects the wrapper to your bot 