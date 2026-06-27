import os
import aiosqlite
import discord
from discord.ext import commands
from dotenv import load_dotenv
from database import init_db

class Casino_Bot(commands.Bot):
    def __init__(self):
        bot_intents = discord.Intents.default()
        bot_intents.message_content = True

        super().__init__(command_prefix="/", intents=bot_intents)
        self.db = None


    async def setup_hook(self):
        
        self.db = await aiosqlite.connect("casino.db")
        await init_db(self.db)

        await self.load_extension('cogs.slots')
        await self.load_extension('cogs.balance')
        await self.load_extension('cogs.daily')
        await self.load_extension('cogs.leaderboard')

        test_guild = discord.Object(id=1314969646989971466)
        self.tree.copy_global_to(guild=test_guild)

        await self.tree.sync(guild=test_guild)
        #await self.tree.sync()

        print("Ready to gamble!")


        async def close(self):
            if self.db is not None:
                await self.db.close()
                print("Database connection closed safely.")
        
            await super().close()

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN') or ""


if __name__ == "__main__":
    casino_bot = Casino_Bot()
    casino_bot.run(TOKEN)