import discord
from discord.ext import commands
import config
import asyncio
import random

token = config.token

description = "I've returned to serve."
bot = commands.Bot(command_prefix = '>', description=description)

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

    print(f"@{author_name} with ID: {author_id} sent a message.")

    n = random.randint(0, 1)
        
    if n == 1 and message_string.strip()[-4:] == "lies" and author_id != bot.user.id:
        await message.channel.send("and deceit")

    # @mentions == (mention = f"<@!{author_id}>")

# ===Bot Start===

bot.run(token)
