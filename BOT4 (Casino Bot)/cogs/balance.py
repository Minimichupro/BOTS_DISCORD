import discord
from discord.ext import commands
from discord import app_commands
from database import get_balance
from casino_logic import balance_insult_giver_broke
from casino_logic import balance_insult_giver_poor
from casino_logic import balance_insult_giver_mid
from casino_logic import balance_insult_giver_sugar_daddy
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Casino_Bot


class BalanceCog(commands.Cog):
    def __init__(self, bot: "Casino_Bot"):
        self.bot = bot


    @app_commands.command(name="balance", description="Show your own balance")
    async def show_balance(self, interaction: discord.Interaction):
        assert self.bot.db is not None
        balance = await get_balance(self.bot.db, interaction.user.id)

        if balance <= 0:
            insult_description = balance_insult_giver_broke()

        elif 0 < balance < 1000:
            insult_description = balance_insult_giver_poor()

        elif 1000 <= balance < 2500:
            insult_description = balance_insult_giver_mid()

        elif balance >= 2500:
            insult_description = balance_insult_giver_sugar_daddy()


        balance_embed= discord.Embed(
            title=f"💰 BALANCE 💰",
            description=insult_description,
            color=discord.Color.green(),
            timestamp=discord.utils.utcnow()
            )
        
        balance_embed.set_thumbnail(url=interaction.user.display_avatar.url)

        balance_embed.add_field(name="💰 Current Balance", value=f"`${balance:,}`", inline=False)

        await interaction.response.send_message(embed=balance_embed)

async def setup(bot: Casino_Bot):
    await bot.add_cog(BalanceCog(bot))