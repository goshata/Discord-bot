import discord
from discord.ext import commands
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
  print ("Ready!")

@client.command()
async def hello(ctx):
  await ctx.send(f"Hello {ctx.author.mention}!")

async def kick(ctx, member : discord.Member, *, reason=None):
  await ctx.send(f"{ctx.author.mention} kicked {member.mention}")
  await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await ctx.send(f"{ctx.author.mention} banned {member.mention}")
  await member.ban(reason=reason)

client.run("token")