from discord.ext import commands
import discord

class ErrorHandler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      if isinstance(error,commands.MissingPermissions):
        emb = discord.Embed(title="You can't do that" ,colour=0xff0000)
        await ctx.reply(embed=emb, delete_after=3)
        
      elif isinstance(error,commands.MissingRequiredArgument):
        emb = discord.Embed(title="Please enter the required arguments. Do `_help {command}`" ,colour=0xff0000)
        await ctx.reply(embed=emb, delete_after=3)

      elif isinstance(error, commands.CommandNotFound):
        emb = discord.Embed(title="Command not Found" ,colour=0xff0000)
        await ctx.reply(embed=emb, delete_after=3)

      elif isinstance(error, commands.MemberNotFound):
        emb = discord.Embed(title="Member not Found" ,colour=0xff0000)
        await ctx.reply(embed=emb, delete_after=3)

      elif isinstance(error,commands.CommandInvokeError):
        emb = discord.Embed(title="there was an error trying to execute that command!" ,colour=0xff0000)
        await ctx.reply(embed=emb, delete_after=3)

        raise error

      elif isinstance(error,commands.MissingRole):
        emb = discord.Embed(title="You can't do that" ,colour=0xff0000)
        await ctx.reply(embed=emb, delete_after=3)

      elif isinstance(error,commands.ChannelNotFound):
        emb = discord.Embed(title="Can't Find Channel" ,colour=0xff0000)
        await ctx.reply(embed=emb, delete_after=3)

      elif isinstance(error,commands.RoleNotFound):
        emb = discord.Embed(title="Can't Find Role" ,colour=0xff0000)
        await ctx.reply(embed=emb, delete_after=3)

      elif isinstance(error,commands.NotOwner):
        emb = discord.Embed(title="YOY CANT DO THAT, YOY NOT MY MWASTER UWU" ,colour=0xff0000)
        await ctx.reply(embed=emb, delete_after=3)

      else:
        raise error
        
      

def setup(client):
    client.add_cog(ErrorHandler(client))