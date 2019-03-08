import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='BlueGaming', type = 3))
    print('Siap Bos')
    

@client.command(pass_context=True)
async def hi(ctx):
    await client.say("Hello {} :joy:".format(ctx.message.author.name))

@client.command(pass_context=True)
async def echo(ctx, *,msg):
    await client.say(msg)

@client.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="Help", color=0x000000)
    embed.add_field(name="gen", value='Your account', inline=False)
    embed.set_footer(text="Get Your account {}".format(ctx.message.author.name))
    await client.say(embed=embed)

    
@client.command(pass_context=True)
async def gen(ctx):
    randomlist = ['bcs5000@live.com:123zaqccx','devgrant9@gmail.com:kipper1','owenpaine15@gmail.com:dudewolfer1','lateriss@gmail.com:Pinhead14$$','dan_jensen91@hotmail.com:fuckups134','niegsch.j@gmail.com:Finnie346643','tamsinwilson2001@gmail.com:jazzthedog','kaolakid@yahoo.com:pc198800','katje_mieke@hotmail.com:1408KILL','shahzilkhokhar@hotmail.com:Shamir007','mynameismikals@gmail.com:230811as','swiffet@gmail.com:ender2007']
    embed = discord.Embed(title="Account Minecraft", color=0x000000)
    embed.add_field(name="Your account", value=random.choice(randomlist), inline=False)
    embed.add_field(name="Published By", value="Blue Gaming#5147", inline=False)
    embed.set_footer(text="Thanks {}".format(ctx.message.author.name))
    await client.send_message(ctx.message.author, embed=embed)
    await client.send_message(ctx.message.channel, "Check Your Dms")


    
client.run(os.getenv("TOKEN"))
