import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
from discord.utils import get


client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
  print("Im online")

  @client.event
  async def on_message(message):

    await client.process_commands(message)
  
  @client.command(pass_context=True)
  async def ping(ctx):
     await ctx.send(f'pong! {round(client.latency * 1000)} ms')

 
  @client.command(pass_context=True)
  async def role(ctx, role):
    
    member = ctx.message.author

    if role is None:
        await ctx.send("You have not specified a role")
    else:
        test = discord.utils.get(member.guild.roles, name=role)
        await  ctx.client.add_roles(member, test)
        await ctx.send("Role added")

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)