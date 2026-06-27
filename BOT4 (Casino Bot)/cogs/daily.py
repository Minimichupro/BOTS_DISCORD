import discord
from discord.ext import commands
from discord import app_commands
from casino_logic import pick_daily
from casino_logic import daily_title_giver_jackpot
from casino_logic import daily_title_giver_loss
from casino_logic import daily_title_giver_standard
from database import update_balance
from typing import TYPE_CHECKING

# This prevents circular import errors at runtime
if TYPE_CHECKING:
    from main import Casino_Bot


class DailyCog(commands.Cog):
    def __init__(self, bot: "Casino_Bot") -> None:
        self.bot = bot


    @app_commands.command(name="daily", description="Claim your daily income")
    #@app_commands.checks.cooldown(1, 86400.0, key=lambda interaction: interaction.user.id)
    @app_commands.checks.cooldown(1, 60.0, key=lambda interaction: interaction.user.id)
    async def daily(self, interaction: discord.Interaction):
        outcome, reward, msg = pick_daily()
        
        assert self.bot.db is not None
        await update_balance(self.bot.db, interaction.user.id, reward)

        if outcome == "standard":
            title = daily_title_giver_standard()
            daily_embed = discord.Embed(
                title=title,
                description=msg,
                color=discord.Color.light_gray()
                )
            
        elif outcome == "jackpot":
            title = daily_title_giver_jackpot()
            daily_embed = discord.Embed(
                title=title,
                description=msg,
                color=discord.Color.yellow()
                )
            
        else:
            title = daily_title_giver_loss()
            daily_embed = discord.Embed(
                title=title,
                description=msg,
                color=discord.Color.red()
                )
            
        if outcome == "loss":
            daily_embed.add_field(name="📉 LOSS 📉", value=f"{reward}💵", inline=False)

        else:
            daily_embed.add_field(name="💵 PAYOUT 💵", value=f"+{reward:,}💵", inline=False)
            
        await interaction.response.send_message(embed=daily_embed)


    @daily.error
    async def daily_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError) -> None:
        if isinstance(error, app_commands.CommandOnCooldown):

            hours = int(error.retry_after // 3600)
            minutes = int((error.retry_after % 3600) // 60)
            seconds = int(error.retry_after % 60)
            
            cooldown_embed = discord.Embed(
                title="Cooldown Active!",
                description=f"You have already claimed your daily reward. Try again in **{minutes}m {seconds}s**.",
                color=discord.Color.orange()
            )
            await interaction.response.send_message(embed=cooldown_embed, ephemeral=True)
        else:
            raise error
        
async def setup(bot: Casino_Bot):
    await bot.add_cog(DailyCog(bot))