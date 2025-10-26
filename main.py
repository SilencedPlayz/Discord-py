import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

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

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online sir.")

bot.run(token)