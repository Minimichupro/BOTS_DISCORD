import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from database import init_db

def init():
    bot_intents = discord.Intents.default()
    bot_intents.message_content = True

    bot_client = commands.Bot(command_prefix="/", intents=bot_intents)
    return bot_client

Casino_Bot = init()

@Casino_Bot.event
async def on_ready():
    await init_db()
    await Casino_Bot.load_extension('cogs.slots')
    await Casino_Bot.load_extension('cogs.balance')

    test_guild = discord.Object(id=1314969646989971466)
    Casino_Bot.tree.copy_global_to(guild=test_guild)

    await Casino_Bot.tree.sync(guild=test_guild)
    await Casino_Bot.tree.sync()

    print("Ready to gamble!")

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN') or ""

Casino_Bot.run(TOKEN)