import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


def initialize_bot():
    bot_intents = discord.Intents.default()
    bot_intents.message_content = True

    bot_client = commands.Bot(command_prefix="/", intents=bot_intents)
    return bot_client

my_bot = initialize_bot()



@my_bot.event
async def on_ready():
    print("Login successfull!")


@my_bot.event
async def on_message(message):
    if message.author == my_bot.user:
        return
    
    if message.content.lower() == "ping":
        await message.channel.send("Pong!")

if __name__ == "__main__":
    load_dotenv()

    bot_token = os.getenv("BOT_TOKEN")
    my_bot.run(bot_token)