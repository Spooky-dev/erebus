from discord.ext import commands
import random
import discord
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

from PIL import Image
from io import BytesIO
import aiohttp

import asyncio



class General(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.client.ses = aiohttp.ClientSession()
    

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready me master')

        print(discord.__version__)
        print('------')

        print('Servers connected to:')
        for guild in self.client.guilds:
            print(guild.name)

        DiscordComponents(self.client)
        
    @commands.command(aliases=['Ping'])
    async def ping(self, ctx):
        await ctx.reply(f'Pong! `{round(self.client.latency * 1000)}ms`')

    @commands.command(aliases=['Colorcodes', 'ColorCodes'])
    async def colorcodes(self, ctx):
      embed=discord.Embed(title="Minecraft Color Codes", description="Black §0\nDark Blue §1\nDark Green §2\nDark Aqua §3\nDark Red §4\nDark Purple §5\nGold §6\nGray §7\nDark Gray §8\nBlue §9\nGreen §a\nAqua §b\nRed §c\nLight Purple §d\nYellow §e\nWhite §f\n\nReset §r\nItalic §o\nBold §l\nRandom Symbols §k", color=0xffffff)
      await ctx.reply(embed=embed)

    @commands.command(aliases=['hallo', 'HALLO'])
    async def Hallo(self, ctx):
      variable = ["Hallo","HALLLOOOOOOOOOOOOOOOOOO!","Hey!","HIIIIIIIIIIII!!!!!","hi uwu"]
      await ctx.reply(f"{random.choice(variable)}", mention_author=True)

    @commands.command(aliases=['seed', 'Seeds', 'Seed'])
    async def seeds(self, ctx):
        emb = discord.Embed(title="Seeds")
        emb.add_field(name="New SSG Seed:", value="564030617", inline = False)
        emb.add_field(name="Bastion SSG Seed:", value="376166226", inline = False)
        emb.add_field(name="Old SSG Seed:", value="-27383160", inline = False)
        emb.add_field(name="Beta SSG Seed:", value="-23209558", inline = False)
        emb.add_field(name="1.5 Seed:", value="-1804478546", inline = False)
        emb.add_field(name="Enter Nether NS Seed:", value="-609243055", inline = False)
        emb.add_field(name="Enter Nether WS Seed:", value="319296525", inline = False)
        emb.add_field(name="All Woods 0.9.0:", value="8634814", inline = False)
        emb.add_field(name="All Woods Pre 0.9.0:", value="1867476839", inline = False)
        emb.add_field(name="All Woods 1.16+:", value="-453960600", inline = False)
        emb.add_field(name="All Dyes Seed:", value="-1652834985", inline = False)
        emb.add_field(name="Obtain Secondary Dyes:", value="1226473653", inline = False)
        emb.add_field(name="Obtain Primary Dyes:", value=" -1652834985", inline = False)

        await ctx.channel.send(embed=emb)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx, title, * , message):
      '''Sends a Message through an Embed\nPut quotation marks for words that are more than a word'''
      await ctx.channel.purge(limit=1)
      emb = discord.Embed(title=title, description=message, colour=ctx.author.colour)
      emb.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=emb)

    @commands.command()
    @commands.is_owner()
    async def purrplecat(self, ctx):
      await ctx.reply('https://open.spotify.com/playlist/4TliGt63npSjodq6oH24pc?si=ddea9d78e23347e7')

    @commands.command()
    async def button(self, ctx):
      await ctx.send(
          "Content",
          components=[
              Button(style=ButtonStyle.blue, label="Blue"),
              Button(style=ButtonStyle.red, label="Red"),
              Button(style=ButtonStyle.URL, label="url", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
          ],
      )

      res = await self.client.wait_for("button_click")
      if res.channel == ctx.channel:
          await res.respond(
              type=InteractionType.ChannelMessageWithSource,
              content=f'{res.component.label} clicked'
          )

    @commands.command(aliases=['calc'])
    async def calculate(self, ctx, number_1, operation, number_2):

      if operation == '+':
        sum = float(number_1) + float(number_2)
        await ctx.reply(f'Sum: **{sum}**')

      elif operation == '-':
        difference = float(number_1) - float(number_2)
        await ctx.reply(f'Difference: **{difference}**')

      elif operation == '*':
        product = float(number_1) * float(number_2)
        await ctx.reply(f'Product: **{product}**')

      elif operation == '/':
        qoutient = float(number_1) / float(number_2)
        await ctx.reply(f'Qoutient: **{qoutient}**')

      else:
        emb = discord.Embed(
          title='Syntax Error',
          color=0xff0000,
          inline=False
        )

        emb.add_field(
          name= 'Addition:',
          value= '**+**',
          inline=False
        )
        emb.add_field(
          name= 'Subtraction:',
          value= '**-**',
          inline=False
        )
        emb.add_field(
          name= 'Multiplication:',
          value= '*****',
          inline=False
        )
        emb.add_field(
          name= 'Division:',
          value= '**/**',
          inline=False
        )
        await ctx.reply(embed=emb)

    @commands.command()
    async def rotate(self, ctx, url: str, degrees: int):
      async with self.client.ses.get(url) as r:
        if r.status in range(200, 299):
          img = Image.open(BytesIO(await r.read()), mode='r')
          img_rotated = img.rotate(angle=degrees)
          b = BytesIO()
          img_rotated.save(b, format=f'{img.format}')
          b_im = b.getvalue()
          file = discord.File(filename=f'rotated.{img.format}', fp=BytesIO(b_im))

          embed = discord.Embed(title=f'Rotated Image to {degrees}')
          embed.set_image(url=f'attachment://rotated.{img.format}')

          await ctx.channel.trigger_typing()
          await asyncio.sleep(2)

          await ctx.send(embed = embed, file = file)

        else:
          await ctx.send(f'Error. Response: {r.status}')

    @commands.command()
    async def scale(self, ctx, url: str):
      async with self.client.ses.get(url) as r:
          if r.status in range(200, 299):

            img = Image.open(BytesIO(await r.read()), mode='r')
            size = (300, 300)
            img_scaled = img.resize((size), Image.NEAREST)
            b = BytesIO()
            img_scaled.save(b, format=f'{img.format}')
            b_im = b.getvalue()
            file = discord.File(filename=f'scaled.{img.format}', fp=BytesIO(b_im))

            embed = discord.Embed(title='Scaled!')
            embed.set_image(url=f'attachment://scaled.{img.format}')

            await ctx.channel.trigger_typing()
            await asyncio.sleep(2)

            await ctx.send(embed = embed, file = file)

          else:
            await ctx.send(f'Error. Response: {r.status}')

def setup(client):
    client.add_cog(General(client))