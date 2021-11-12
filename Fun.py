import discord
from discord.ext import commands
import random
import os
import requests
import json
import aiohttp

def get_quote():
	res = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(res.text)
	quote = json_data[0]['q'] + " - " + json_data[0]['a']
	return quote

class Fun(commands.Cog, name='Fun'):
  """le help Fun"""
  def __init__(self, bot):
    self.bot = bot
    self.dagpi_headers = {
  'Authorization': 'MTYyODkyNDMwMg.Q5sOQkbg0TFsSCQUCcXXaZuKLKDdjUt2.a70cabc168ca2fc0'
}
  
  
  @commands.command(description="random quote", brief='random quote')
  @commands.cooldown(1, 8, commands.BucketType.user)
  async def quote(ctx):
    quote = get_quote()
    await ctx.reply(quote)
  
  @commands.command(description="random dank memes", brief='random dank memes')
  @commands.cooldown(1, 8, commands.BucketType.user)
  async def dankmeme(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://meme-api.herokuapp.com/gimme/dankmemes') as r:
        res = await r.json()
    name = res['title']
    url = res['url']
    link = res['postLink']
    embed = discord.Embed(color = discord.colour.Color.green(), timestamp=ctx.message.created_at, description=f"[{name}]({link})")
    embed.set_image(url=url)
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)
  
  @commands.command(description="r/woosh", brief='r/woosh')
  @commands.cooldown(1, 8, commands.BucketType.user)
  async def rwoosh(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://meme-api.herokuapp.com/gimme/woosh') as r:
        res = await r.json()
    name = res['title']
    url = res['url']
    link = res['postLink']
    embed = discord.Embed(color = discord.colour.Color.green(), timestamp=ctx.message.created_at, description=f"[{name}]({link})")
    embed.set_image(url=url)
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)
  
  @commands.command(description="random wholesome memes", brief='random wholesome memes', aliases=['wsmeme'])
  @commands.cooldown(1, 8, commands.BucketType.user)
  async def wholesomememe(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://meme-api.herokuapp.com/gimme/wholesomememes') as r:
        res = await r.json()
    name = res['title']
    url = res['url']
    link = res['postLink']
    embed = discord.Embed(color = discord.colour.Color.green(), timestamp=ctx.message.created_at, description=f"[{name}]({link})")
    embed.set_image(url=url)
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)
  
  @commands.command(description="random memes", brief='random memes')
  @commands.cooldown(1, 8, commands.BucketType.user)
  async def meme(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://meme-api.herokuapp.com/gimme/memes') as r:
        res = await r.json()
    name = res['title']
    url = res['url']
    link = res['postLink']
    embed = discord.Embed(color = discord.colour.Color.green(), timestamp=ctx.message.created_at, description=f"[{name}]({link})")
    embed.set_image(url=url)
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)
  
  @commands.command(description="r/cursedcomments", brief='r/cursedcomments', aliases=['ccomments'])
  @commands.cooldown(1, 8, commands.BucketType.user)
  async def cursedcomments(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://meme-api.herokuapp.com/gimme/cursedcomments') as r:
        res = await r.json()
    name = res['title']
    url = res['url']
    link = res['pos']    
    embed = discord.Embed(color = discord.colour.Color.green(), timestamp=ctx.message.created_at, description=f"[{name}]({link})")
    embed.set_image(url=url)
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)

  @commands.cooldown(1, 8, commands.BucketType.user)
  async def susrate(self, ctx, member: discord.Member = None):
    member = ctx.author
    zeroto100 = random.randint(0, 100)
    embedVar = discord.Embed(color=0xff0000, timestamp=ctx.message.created_at)
    embedVar.add_field(name=f"{member}'s sus rate",
                      value=f"{member} is {zeroto100}% sus")
    embedVar.set_footer(text=f"Requested by {ctx.author.name}")
    await ctx.reply(embed=embedVar)


def setup(client):
  client.add_cog(Fun(client))
