import discord
from discord.ext import commands
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
  print ("Ready!")

@client.command()
async def hello(ctx):
  await ctx.send(f"Hello {ctx.author.mention}!")

client.run("token")