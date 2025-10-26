import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from keep_alive import keep_alive

load_dotenv()
token = "MTQzMTkwMzkyOTQwNjU5MDk5Ng.GSCe57.EgkHhK6OPrEXN7yXHw-YF51CkBcXDPutBsuzOc"

# Logging setup
logging.basicConfig(
    level=logging.DEBUG,
    filename='discord.log',
    filemode='w',
    format='%(asctime)s:%(levelname)s:%(name)s: %(message)s',
    encoding='utf-8'
)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print("Rexander is online!")

# commands
@bot.command()
async def hello(ctx):
    await ctx.send("Heyy")

@bot.command()
async def how(ctx):
    await ctx.send("Sir it seems that you didn't have other commands yet.")

@bot.command()
async def test(ctx, *, message):
    await ctx.send(f"You said: {message}")

@bot.command()
async def writefile(ctx, filename, *, content):
    with open(f"database/{filename}", 'w') as file:
        file.write(content)
        await ctx.send(embed=discord.Embed(title=f"Successfully written **{filename}**", color=0x00ff00))

@bot.command()
async def readfile(ctx, filename):
    try:
        with open(f"database/{filename}", 'r') as file:
          content = file.read()
          await ctx.send(embed=discord.Embed(title=f"**{filename}**", description=f"```{content}```", color=0x00ff00))
    except FileNotFoundError:
        await ctx.send(embed=discord.Embed(title=f"File **{filename}** found", color=0xFF0000))

@bot.command()
async def deletefile(ctx, filename):
    if os.path.exists(f"database/{filename}"):
        os.remove(f"database/{filename}")
        await ctx.send(embed=discord.Embed(title=f"**{filename}** have been removed.", color=0x00ff00))
    else:
        await ctx.send(embed=discord.Embed(title=f"File **{filename}** found", color=0xFF0000))

@bot.command()
async def listfiles(ctx):
    files = os.listdir("database")
    if files:
        length = len(files)
        names = "\n• ".join(files)
        embed = discord.Embed(title=f"Found {length} file(s)", description=f"• {names}", color=0x00ff00)
        await ctx.send(embed=embed)
    else:
        await ctx.send(embed=discord.Embed(title="No files found", color=0xFF0000))

keep_alive()
bot.run(token)
