import discord
from discord.ext import commands
from discord import app_commands
#slot spins returns: slot_display, prize_mult, bet * prize_mult
from casino_logic import slot_spin


class CommandBot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @app_commands.command(name="slots", description="Play the slots minigame")
    async def slots(self, interaction: discord.Interaction, bet: int):
        display, mult, prize = slot_spin(bet)

        if mult == 3:
            casino_embed = discord.Embed(
                title=f"💰 YOU WON! 💰",
                description="See? Gambling IS a viable career choice! Go tell your parents.",
                color=discord.Color.green()
                )
        
        elif mult == 1.5:
            casino_embed = discord.Embed(
                title=f"✨ NOT BAD! ✨",
                description="Quick, hide it before the government tries to tax it!",
                color=discord.Color.gold()
                )
        
        else:
            casino_embed = discord.Embed(
                title=f"💸 WIPED OUT! 💸",
                description="Quick question... how attached are you to having TWO fully functioning kidneys?",
                color=discord.Color.red()
                )
            

        casino_embed.add_field(name="Roll", value=display, inline=True)
        casino_embed.add_field(name="Multiplier", value=f"{mult}", inline=True)
        casino_embed.add_field(name="Payout", value=f"+{prize}💵", inline=True)

        await interaction.response.send_message(embed=casino_embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(CommandBot(bot))