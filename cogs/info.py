import discord
from discord.ext import commands

import re
import datetime

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def serverinfo(self, ctx):
        """Show server information."""
        embed = discord.Embed(
            title=f"{ctx.guild.name} Server Info!",
            color=0xededed,
            timestamp=ctx.message.created_at,
        )

        roles = []
        for role in ctx.guild.roles:
            if role.name != "@everyone":
                roles.append(role.mention)
        width = 3

        boosters = [x.mention for x in ctx.guild.premium_subscribers]

        embed.add_field(name="Owner", value=f"{ctx.guild.owner.mention}", inline=False)
        embed.add_field(name="Created on", value=f"{ctx.guild.created_at.date()}")
        embed.add_field(name="Region", value=f"``{ctx.guild.region}``")
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(
            name="Verification Level", value=f"{ctx.guild.verification_level}".title()
        )
        embed.add_field(
            name="Channels",
            value="<:categories:747750884577902653>"
            + f" {len(ctx.guild.categories)}\n"
            + "<:text_channel:747744994101690408>"
            + f" {len(ctx.guild.text_channels)}\n"
            + "<:voice_channel:747745006697185333>"
            + f" {len(ctx.guild.voice_channels)}",
        )
        embed.add_field(name="Members", value=f"{ctx.guild.member_count}")
        if len(boosters) < 5:
            embed.add_field(
                name=f"Boosters ({len(boosters)})",
                value=",\n".join(
                    ", ".join(boosters[i : i + width])
                    for i in range(0, len(boosters), width)
                )
                if boosters
                else "No booster.",
            )
        else:
            embed.add_field(name=f"Boosters ({len(boosters)})", value=len(boosters))
        if len(", ".join(roles)) <= 1024:
            embed.add_field(name=f"Roles ({len(roles)})", value=", ".join(roles))
        else:
            embed.add_field(name=f"Roles", value=f"{len(roles)}")
        embed.set_footer(text=f"ID: {ctx.guild.id}")
        await ctx.reply(embed=embed)


    @commands.command()
    async def userinfo(self, ctx, member:discord.Member =  None):
        '''Displays User Information'''
        if member is None:
            member = ctx.author
            roles = [role for role in ctx.author.roles]

        else:
            roles = [role for role in member.roles]

        embed = discord.Embed(title=f"{member}'s Info!", colour=member.colour, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="User Name:",value=f'<@{member.id}>', inline=True)
        embed.add_field(name="User ID:", value=member.id, inline=True)
        embed.add_field(name="Discriminator:",value=member.discriminator, inline=True)
        embed.add_field(name="Created At:", value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=True)
        embed.add_field(name="Joined At:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=True)
        embed.add_field(name="Bot?:", value=member.bot, inline=True)
        embed.add_field(name=f"Roles [{len(roles)}]", value=" **|** ".join([role.mention for role in roles]), inline=True)
        await ctx.reply(embed=embed)
        return

    @commands.command()
    async def icon(self, ctx, member : discord.Member = None):
      """Shows a member's Icon"""
      if member is None:
            member = ctx.author

      emb = discord.Embed(title=f"{member}'s Icon!", colour=ctx.author.colour)
      emb.set_image(url=member.avatar_url)
      await ctx.reply(embed=emb)

    @commands.command()
    async def emojiinfo(self, ctx ,* ,emojiname:str):
        '''Displays Emoji Information'''
        emojiname=emojiname.replace(" ","_")
        match=re.findall(r"\b(?<!<)\w+\b",emojiname,re.I)
        emojiname=match[0].lower()
        for emoji_type in self.client.emojis:
            emoji_name=emoji_type.name.lower()
            if emoji_name == emojiname:
                emoji=emoji_type
                break
        embed = discord.Embed(title="Emoji information",colour=ctx.author.colour,timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=emoji.url)
        fields = [("Name", emoji.name, True),
        ("Emoji Preview",(emoji), True),
        ("ID",emoji.id, True),
        ("Created by", (f"{emoji.user}"), True),
        ("Created at", emoji.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
        ("Emoji Url", emoji.url, True),
        ("Emoji Guild Name", emoji.guild, True),
        ("Emoji Guild ID", emoji.guild_id, True),
        ("Bot String", f"`{emoji}`", True),
        ("Is Animated?", emoji.animated, True),
        ("Is Restricted?", len(emoji.roles), True),
        ("Can Bot use It?", emoji.is_usable(), True),
        ("Is Available?", emoji.available, True),
        ("Is Managed by Twitch?",emoji.managed, True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        await ctx.reply(embed=embed)

    @commands.command()
    async def servericon(self, ctx):
      embed = discord.Embed(
        title=ctx.guild.name,
        color = 0xededed
      )
      embed.set_image(url=ctx.guild.icon_url)

      await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def getuser(self, ctx, role: discord.Role):
      '''Get all user that has <role>'''

      emb = discord.Embed(
        title = role.name,
        description = '\n'.join(map(str, role.members)),
        color = 0xededed
      )

      await ctx.send(embed=emb)



def setup(client):
    client.add_cog(Info(client))