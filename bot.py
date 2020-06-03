import discord
from discord.ext import commands
import os
import json

def get_prefix(client, message):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = get_prefix)
token = "token"

@client.event
async def on_guild_join(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'a!'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    
    prefixes.pop(str(guild.id))

    with open('prefixes.joson', 'w') as f:
        json.dump(prefixes, f, indent = 4)
        
@client.command()
async def setprefix(ctx, prefix):
    @has_permissions(administrator=True)
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f"Prefixed changed to {prefix}")
    
client.run(token)
