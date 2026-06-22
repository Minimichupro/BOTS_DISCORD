import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

def create_bot_instance():
    # Setup the intents (permissions) the bot requires
    bot_intents = discord.Intents.default()
    bot_intents.message_content = True  # Allows the bot to read message text

    # Initialize the bot with a prefix and the defined intents
    bot_client = commands.Bot(command_prefix="!", intents=bot_intents)
    return bot_client

# Instantiate the bot
bot = create_bot_instance()

@bot.event
async def on_ready():
    # This event fires when the bot successfully connects to Discord
    print(f"Success! Logged in as {bot.user}")

@bot.event
async def on_message(message):
    # This event fires whenever a message is sent in a visible channel
    
    # Ignore messages sent by the bot itself to prevent infinite loops
    if message.author == bot.user:
        return

    # A simple responder check
    if message.content.lower() == "ping":
        await message.channel.send("Pong!")

if __name__ == "__main__":
    # Load the environment variables from your .env file
    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN")
    
    # Start the bot using the token
    bot.run(bot_token)