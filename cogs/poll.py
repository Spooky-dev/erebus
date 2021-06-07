import discord
from discord.ext import commands

class Poll(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Poll Cog Ready!')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def poll(self, ctx, title, *options):
        '''Put quotation marks for words that are more than a word'''
        await ctx.channel.purge(limit=1)
        emojiLetters = [
            "\N{REGIONAL INDICATOR SYMBOL LETTER A}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER B}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER C}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER D}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER E}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER F}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER G}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER H}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER I}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER J}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER K}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER L}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER M}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER N}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER O}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER P}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER Q}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER R}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER S}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER T}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER U}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER V}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER W}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER X}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER Y}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER Z}",
        ]

        options = list(options)
        for i in range(len(options)):
            options[i] = f"{emojiLetters[i]}  {options[i]}"
        embed = discord.Embed(
            title=title, description="\n".join(options), color=ctx.author.colour
        )
        message = await ctx.send(embed=embed)
        for i in range(len(options)):
            await message.add_reaction(emojiLetters[i])

    @commands.command()
    async def quickpoll(self, ctx, *, question):
      '''A yes and no poll'''
      await ctx.channel.purge(limit=1)
      message = await ctx.send(f'**{question}**')
      await message.add_reaction('👍')
      await message.add_reaction('👎')

def setup(client):
    client.add_cog(Poll(client))