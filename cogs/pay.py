import discord
from discord.ext import commands
from discord import app_commands
from database import get_balance
from database import update_balance
from typing import TYPE_CHECKING

# This prevents circular import errors at runtime
if TYPE_CHECKING:
    from main import Casino_Bot

class PayCog(commands.Cog):
    def __init__(self, bot: "Casino_Bot"):
        self.bot = bot

    @app_commands.command(name="pay", description="Pay others off your balance")
    async def pay(self, interaction: discord.Interaction, usuario: discord.User, payment: int):

        payer_id = interaction.user.id
        creditor_id = usuario.id
        
        if usuario.bot:
            await interaction.response.send_message("No puedes pagar a un bot.", ephemeral=True)
            return
        
        elif payer_id == creditor_id:
            await interaction.response.send_message("No puedes pagarte a ti mismo.", ephemeral=True)
            return

        assert self.bot.db is not None
        user_balance = await get_balance(self.bot.db, interaction.user.id)

        if payment > user_balance:
            await interaction.response.send_message("No puede pagar")

        elif payment <= user_balance:
            await update_balance(self.bot.db, user_id=usuario.id, amount=payment)
            await update_balance(self.bot.db, user_id=interaction.user.id, amount=-payment)
            await interaction.response.send_message(f"Has pagado {payment} a {usuario.display_name}")


async def setup(bot: Casino_Bot):
    await bot.add_cog(PayCog(bot))