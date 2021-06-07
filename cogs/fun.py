import discord
import random
import asyncio
import os
from discord.ext import commands

import random as r
from imgurpython import ImgurClient

imgur = ImgurClient("470538e04b7d269","9ba1e7b641fb219285005aed140f3a84146a5af7")

def get_embed(_title, _description, _color):
    return discord.Embed(title=_title, description=_description, color=_color)

timeout = 60*30

f = open ("response.txt", "r")
response = f.readlines()

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.author == self.client.user:
        return
      if message.author.bot: return

      if message.content.lower().startswith('e'):
        await message.channel.send('e')

      if message.content.lower().startswith('ok'):
        await message.channel.send('ok')
        
      if message.content.lower().startswith('aaa'):
        await message.channel.send('AAAAAAAAAAAAAAA')

      if message.content.lower().startswith('shut up'):
        await message.reply('no u')

      if message.content.lower().startswith('stfu'):
        await message.reply('no u')

      if message.content.lower().startswith('f'):
        await message.add_reaction('🇫')

      if message.content.lower().startswith('hallo'):
        await message.reply('HALLO!', mention_author=True)

      if message.content.lower().startswith('why'):
        await message.reply('idk', mention_author=True)

      if message.content.lower().startswith('wut'):
        await message.reply('idk', mention_author=True)

      if message.content.lower().startswith('who'):
        await message.reply('idk', mention_author=True)

      if message.content.lower().startswith('when'):
        await message.reply('idk', mention_author=True)

      if message.content.lower().startswith('how'):
        await message.reply('idk', mention_author=True)

      if message.content.lower().startswith('where'):
        await message.reply('idk', mention_author=True)

      if message.content.lower().startswith('what'):
        await message.reply('idk', mention_author=True)

      if message.content.lower().startswith('creeper'):
        await message.reply('Awww mann')

      if "<@!820618859328700416>" in message.content:
        await message.channel.send('dont ping when')

        await self.client.process_commands(message)

    @commands.command(pass_context=True, aliases = ['Mctips'])
    async def mctips(self, ctx):
      await ctx.channel.purge(limit=1)
      while True:
          await ctx.send(random.choice(response))
          await asyncio.sleep(timeout)

    @commands.command()
    @commands.is_owner()
    async def say(self, ctx, channelid:discord.TextChannel,*, message):
      await ctx.channel.purge(limit=1)
      await channelid.send(message)

    @commands.command(aliases=['eggs', 'Egg', 'Eggs'])
    async def egg(self, ctx):
        image = os.listdir('./cogs/image/')
        imgString = random.choice(image)
        path = "./cogs/image/" + imgString
        await ctx.send(file=discord.File(path))

    @commands.command()
    async def jed(self, ctx, *, message):
      await ctx.send(f'Jed {message}')

    @commands.command(aliases = ['Mctipsoff'])
    async def mctipsoff(self, ctx):
      em = discord.Embed(title='Turning off in 3...', color=0xffffff)
      emb = discord.Embed(title='2...', color=0xffffff)
      embe = discord.Embed(title='1...', color=0xffffff)
      await ctx.send(embed = em, delete_after=3)
      await asyncio.sleep(1)
      await ctx.send(embed = emb, delete_after=3)
      await asyncio.sleep(1)
      await ctx.send(embed = embe, delete_after=3)
      await asyncio.sleep(1)
      await ctx.send('https://tenor.com/Y5kV.gif')
      await asyncio.sleep(1)
      await ctx.send('<:lmaoooo:824452734673223680>')
    
    @commands.command(aliases = ['Amongus', 'AmongUs'])
    async def amongus(self, ctx):
        """Impostors can sabotage the reactor, 
        which gives Crewmates 30–45 seconds to resolve the sabotage. 
        If it is not resolved in the allotted time, The Impostor(s) will win."""


        # determining
        embed1 = discord.Embed(title = "Who's the imposter?" , description = "Find out who the imposter is, before the reactor breaks down!" , color=0xff0000)
        
        # fields
        embed1.add_field(name = 'Red' , value= '<:red:838360803068346368>' , inline=False)
        embed1.add_field(name = 'Blue' , value= '<:blue:838360803853860904>' , inline=False)
        embed1.add_field(name = 'Lime' , value= '<:lime:838360802821931008>' , inline=False)
        embed1.add_field(name = 'White' , value= '<:white:838360802771730462>' , inline=False)
        
        # sending the message
        msg = await ctx.send(embed=embed1)
        
        # emojis
        emojis = {
            'red': '<:red:838360803068346368>',
            'blue': '<:blue:838360803853860904>',
            'lime': '<:lime:838360802821931008>',
            'white': '<:white:838360802771730462>'
        }
        
        # who is the imposter?
        imposter = random.choice(list(emojis.items()))
        imposter = imposter[0]
        
        # for testing...
        print(emojis[imposter])
        
        # adding choices
        for emoji in emojis.values():
            await msg.add_reaction(emoji)
        
        # a simple check, whether reacted emoji is in given choises.
        def check(reaction, user):
            self.reacted = reaction.emoji
            return user == ctx.author and str(reaction.emoji) in emojis.values()

        # waiting for the reaction to proceed
        try: 
            reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check=check)
        
        except TimeoutError:
            # reactor meltdown - defeat
            description = "Reactor Meltdown.{0} was the imposter...".format(imposter)
            embed = get_embed("Defeat", description, discord.Color.red())
            await ctx.send(embed=embed)
        else:
            # victory
            if str(self.reacted) == emojis[imposter]:
                description = "**{0}** was the imposter...".format(imposter)
                embed = get_embed("Victory", description, discord.Color.blue())
                await ctx.send(embed=embed)

            # defeat
            else:
                for key, value in emojis.items(): 
                    if value == str(self.reacted):
                        description = "**{0}** was not the imposter...".format(key)
                        embed = get_embed("Defeat", description, discord.Color.red())
                        await ctx.send(embed=embed)
                        break

    @commands.command(name='imgur', pass_context=True)
    async def imgur(self, ctx, *text: str):
        """Allows the user to search for an image from imgur"""
        rand = r.randint(0, 29)
        if text == ():
            await ctx.send('**Please enter a search term**')
        elif text[0] != ():
            items = imgur.gallery_search(" ".join(text[0:len(text)]), advanced=None, sort='viral', window='all',page=0)
            await ctx.send(items[rand].link)

    @commands.command()
    async def uppercaselowercaseconverterthingy(self, ctx, lettercase, *, input):

      if lettercase.lower() == 'lower':
        await ctx.reply(input.lower())

      elif lettercase.lower() == 'upper':
        await ctx.reply(input.upper())

      else:
        await ctx.reply('choose between "upper" or "lower" for <lettercase>')

    @commands.command()
    @commands.is_owner()
    async def spam(self, ctx, amount:int,*, message):
      
        for i in range(amount):
            await ctx.send(f'{i}. {message}')
            i = i + 1

        await ctx.send('DONE!!!')



    

def setup(client):
    client.add_cog(Fun(client))