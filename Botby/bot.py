import discord
from discord.ext import commands
import config
import asyncio
import random

token = config.token
cp = ">"

description = "I've returned to serve."
bot = commands.Bot(command_prefix = cp, description=description)

# ===Setup===

bot.remove_command("help")

@bot.event
async def on_ready():
    print('Logged in successfully!')
    print(f"Name: {bot.user.name}")
    print(f"ID: {bot.user.id}")
    print('----------------------')

# ===Basic Commands===

@bot.command()
async def help(ctx):
    """This function does does not help"""
    await ctx.send("No.")

'''@bot.command()
async def command(ctx, *, command):
    await ctx.send("No.")'''

# ===Automatic Responses===

@bot.event
async def on_message(message):
    author_name = message.author.name
    author_id = message.author.id

    message_string = message.content.lower()

    if message_string.strip()[0] == cp:
        print(f"@{author_name} with ID: {author_id} sent a command.")
    else:
        print(f"@{author_name} with ID: {author_id} sent a message.")
  
    if message_string.strip()[-4:] == "lies" and author_id != bot.user.id:
        await message.channel.send("and deceit")

    if message_string.strip()[-11:] == "nukes ready" and author_id != bot.user.id:
        await message.channel.send("it's time boys")
        
    n = random.randint(1, 100)
    if n == 69 and author_id == 420348710095159317:
        await message.channel.send("Kaitlyn is a furry, change my mind.")

    # @mentions == (mention = f"<@!{author_id}>")

    await bot.process_commands(message)

# ===Bot Start===

bot.run(token)
