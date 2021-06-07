from discord.ext import commands
import discord

err_color = discord.Color.red()
color = 0x0da2ff

note = '**NOTE:** UUIDs are already generated. There is no need to change them.'

class Packs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['UUID', 'Uuid'])
    async def uuid(self, ctx):
      await ctx.send('Hallo, sorry this command no longer exists. You can Invite **Pack-Man** to your servers, Pack-Man is Discord Bot that has this command\nInvite Link: https://github.com/Spooky-dev/pack-man')

    @commands.command(aliases=['Manifest'])
    async def manifest(self, ctx):
      await ctx.send('Hallo, sorry this command no longer exists. You can Invite **Pack-Man** to your servers, Pack-Man is Discord Bot that has this command\nInvite Link: https://github.com/Spooky-dev/pack-man')

def setup(client):
    client.add_cog(Packs(client))