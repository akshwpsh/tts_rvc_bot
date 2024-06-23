import discord
from discord.ext import commands
import json

# Load the config file
with open('config/config.json') as f:
    config = json.load(f)

Token = config['Token']
Prefix = config['Prefix']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=Prefix, intents=intents)

# Cog 로드



@bot.event
async def on_ready():
    await bot.load_extension("cogs.util_cog")
    print("Bot is ready")

bot.run(Token)