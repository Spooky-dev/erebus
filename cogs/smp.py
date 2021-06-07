import discord
from discord.ext import commands

class SMP(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role("people that can start the server")
    
    async def smpon(self, ctx):
      await ctx.channel.purge(limit=1)
      embed = discord.Embed(title="SERVER ONLINE", description="sourswiftpog.aternos.me | 24757", color=0x15b300, timestamp=ctx.message.created_at)
      channel = self.client.get_channel(820989685139636244)
      await channel.send(embed=embed)
      print(f'\nServer turned on by {ctx.author.name}\n{ctx.message.created_at}')

    @commands.command()
    @commands.has_role("people that can start the server")
    async def smpoff(self, ctx):
      await ctx.channel.purge(limit=1)
      embed = discord.Embed(title="SERVER OFFLINE", description="sourswiftpog.aternos.me | 24757", color=0xc70000, timestamp=ctx.message.created_at)
      channel = self.client.get_channel(820989685139636244)
      await channel.send(embed=embed)
      print(f'\nServer turned off by {ctx.author.name}\n{ctx.message.created_at}')

def setup(client):
    client.add_cog(SMP(client))