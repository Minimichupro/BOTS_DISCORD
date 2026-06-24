import discord
from discord.ext import commands
from discord import app_commands
from database import get_balance
from casino_logic import balance_insult_giver_broke
from casino_logic import balance_insult_giver_poor
from casino_logic import balance_insult_giver_mid
from casino_logic import balance_insult_giver_sugar_daddy


class BalanceCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @app_commands.command(name="balance", description="Show your own balance")
    async def show_balance(self, interaction: discord.Interaction):
        balance = await get_balance(interaction.user.id)

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

async def setup(bot: commands.Bot):
    await bot.add_cog(BalanceCog(bot))