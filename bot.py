import discord
from discord.ext import commands
from config import token

from discord.ext import commands
import os
import random

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah login sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send('Ini adalah echo-bot yang dibuat dengan pustaka discord.py!')

@client.command()
async def info(ctx):
    await ctx.send('''
/about - tentang bot
                  
bot ini dibuat oleh Arkan pada tahun 2025''')
    
@client.command()
async def fungsi(ctx):
    await ctx.send('''
/fungsi - fungsi bot
                  
untuk menyapa user''')
    
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)





client.run('MTM5Mzg4NzMyNDM5MTIxNTE4Ng.GB1RFu.PtyNZq3Fzq7gGogWzWI04z_-zJLnUluaKgyP4Y')
