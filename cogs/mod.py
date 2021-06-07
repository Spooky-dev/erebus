import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx,amount=1):
        await ctx.channel.purge(limit = amount+1)
        emb = discord.Embed(title="Messages/s Deleted")
        await ctx.send(embed=emb, delete_after=3)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason='**No Reason Provided**'):
      try:
        await member.send(f"You Have been kicked from {ctx.guild.name} for {reason}!")
      except:
        await ctx.send("The member has their DMs closed.")
        await ctx.send(f"{member.mention} has been kicked from the server")
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await member.send(f"You Have been banned from {ctx.guild.name} for {reason}!")
        await ctx.send(f"{member.mention} has been banned from the server")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                await member.send(f"You Have been Unbanned from {ctx.guild.name}!")
                return

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.author == self.client.user:
        return

      if "fuck" in message.content.lower():
        await message.channel.send('language >:(')

      if "bitch" in message.content.lower():
        await message.channel.send('language >:(')

      if "shit" in message.content.lower():
        await message.channel.send('language >:(')

def setup(client):
    client.add_cog(Moderation(client))