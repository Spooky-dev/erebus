import discord
from discord.ext import commands
import os
import keep_alive

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="_", intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="something", url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
                
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

keep_alive.keep_alive()
client.run(os.getenv('TOKEN'))