import discord
from discord.ext import commands
from discord import app_commands
# slot spins returns: slot_display, prize_mult, bet * prize_mult
from casino_logic import slot_spin
from casino_logic import insult_giver
from database import get_balance
from database import update_balance



class CommandBot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @app_commands.command(name="slots", description="Play the slots minigame")
    async def slots(self, interaction: discord.Interaction, bet: int):
        user_balance = await get_balance(interaction.user.id)

        if user_balance == 0:
            insult = insult_giver()
            
            await interaction.response.send_message(insult, ephemeral=True)
            return
        
        if bet > user_balance:
            await interaction.response.send_message(f"Even the slot machine is laughing at you. You requested a ${bet} spin but your broke ass only has ${user_balance}.", ephemeral=True)
            return
        
        if bet <= 0:
            await interaction.response.send_message(f"Error: Zero testosterone detected. A ${bet} bet is not allowed in this establishment.", ephemeral=True)
            return

        display, mult, prize = slot_spin(bet)
        net_payout = prize - bet
        await update_balance(user_id=interaction.user.id, amount=net_payout)

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
        
        formatted_display = " | ".join(display)

        casino_embed.add_field(name="Roll", value=formatted_display, inline=True)
        casino_embed.add_field(name="Multiplier", value=f"{mult}", inline=True)

        if net_payout > 0:
            casino_embed.add_field(name="Payout", value=f"+{net_payout}💵", inline=True)
        else:
            casino_embed.add_field(name="Payout", value=f"{net_payout}💵", inline=True)


        await interaction.response.send_message(embed=casino_embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(CommandBot(bot))