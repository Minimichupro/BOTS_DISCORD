import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


def init_bot():
    bot_intents = discord.Intents.default()
    bot_intents.message_content = True

    bot_client = commands.Bot(command_prefix="/", intents=bot_intents)
    return bot_client

context_bot = init_bot()


@context_bot.command()
async def server_info(ctx):
    username = ctx.author.display_name
    channel_name = ctx.channel.name
    server_name = ctx.guild.name

    await ctx.send(f"Hola {username}! Estas en el canal '{channel_name}', del servidor '{server_name}'")



if __name__ == "__main__":
    load_dotenv()

    token = os.getenv("BOT_TOKEN")
    context_bot.run(token)