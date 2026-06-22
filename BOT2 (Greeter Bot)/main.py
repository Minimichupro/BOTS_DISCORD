import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

def init_bot():
    bot_intents = discord.Intents.default()
    bot_intents.message_content = True

    bot_client = commands.Bot(command_prefix="/", intents=bot_intents)
    return bot_client

greeter_bot = init_bot()
keyword = {
    "ping": "Pong! 🏓, Helloo!.",
    "hello": "Hi there!",
    "bye": "Hell- I mean, Bye!"
}


@greeter_bot.event
async def on_ready():
    print("Hello! Hello! Greeting is my passion!")


@greeter_bot.event
async def on_message(message):
    if message.author == greeter_bot.user:
        return
    
    user_message = message.content.lower()
    bot_replies = keyword.get(user_message)

    if bot_replies:
        await message.channel.send(bot_replies)

    if user_message == "bot":
        await message.channel.send(f"What's up, {message.author.display_name}?")

if __name__ == "__main__":
    load_dotenv()

    token = os.getenv("BOT_TOKEN")
    greeter_bot.run(token)