

import os

import discord

import PIL

from PIL import Image, ImageFilter

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


#pixel code for later
#canvas = Image.open('canvas.png')
#pixelmap = canvas.load()
#pixelmap[1, 1] = (255, 255, 255)
#canvas.save('canvas.png')


client = commands.Bot(command_prefix='r/',intents=discord.Intents.all())
client.remove_command('help')
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def place(ctx, x, y, r, g, b):
  x = int(x)
  y = int(y)
  r = int(r)
  g = int(g)
  b = int(b)
  canvas = Image.open('canvas.png')
  pixelmap = canvas.load()
  pixelmap[x - 1, y - 1] = (r, g, b)
  canvas.save('canvas.png')
  canvas = Image.open('canvas.png')
  resized = canvas.resize((2048, 2048))
  resized_sharpen = resized.filter(ImageFilter.SHARPEN)
  resized_sharpen.save('resize.png')
  await ctx.send(file=discord.File('resize.png'))
@client.command()
async def display(ctx):
  await ctx.send(file=discord.File('resize.png'))
@client.command()
async def help(ctx):
  await ctx.send('``r/display : Displays the canvas. \nr/place : Places a pixel. Usage is r/place x y r g b \nr/grid : Shows the canvas with a grid in top for easier pixel placing. \n \n Made by elmemeee.``')
@client.command()
async def grid(ctx):
  canvas = Image.open('resize.png')
  canvascopy = canvas.copy()
  grid = Image.open('grid.png')
  gridcopy = grid.copy()
  gridcopy = gridcopy.convert('RGBA')
  canvascopy.paste(gridcopy, (0, 0), gridcopy)
  canvascopy.save('canvasgrid.png')
  await ctx.send(file=discord.File('canvasgrid.png'))


try:
  token = "GET YOUR OWN TOKEN" or ""
  if token == "":
    raise Exception("Please add your token")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
