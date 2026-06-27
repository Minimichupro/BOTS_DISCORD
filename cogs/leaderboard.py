import discord
from discord import app_commands
from discord.ext import commands
from database import get_top_players
from typing import TYPE_CHECKING

# This prevents circular import errors at runtime
if TYPE_CHECKING:
    from main import Casino_Bot


class CasinoLeaderboard(commands.Cog):
    def __init__(self, bot: "Casino_Bot"):
        self.bot = bot

    
    @app_commands.command(name="leaderboard", description="Displays the top wealthiest players in the server.")
    async def show_leaderboard(self, interaction: discord.Interaction):
        
        await interaction.response.defer()
        
        assert self.bot.db is not None
        top_players = await get_top_players(self.bot.db, limit=5)

        if not top_players:
            error_embed = discord.Embed(
                description="⚠️ **The casino vault is currently empty. Start playing to build the leaderboard!**",
                color=discord.Color.red()
            )
            await interaction.followup.send(embed=error_embed)
            return
        
        rank_medals = {1: "🥇", 2: "🥈", 3: "🥉", 4: "🔹", 5: "🔹"}
        leaderboard_lines = []

        for index, (user_id, balance) in enumerate(top_players, start=1):
            cached_user = self.bot.get_user(user_id)
            
            if not cached_user:
                try:
                    cached_user = await self.bot.fetch_user(user_id)
                except discord.NotFound:
                    cached_user = None

            username = cached_user.name if cached_user else f"User_{user_id}"

            formatted_balance = f"{balance:,}"
            medal = rank_medals.get(index, "🔹")

            rank_line = f"{medal} **#{index}** | `{username}` — **{formatted_balance}** coins"
            leaderboard_lines.append(rank_line)

        leaderboard_text = "\n".join(leaderboard_lines)

        leaderboard_embed = discord.Embed(
            title="🏆 CASINO HIGH-ROLLERS LEADERBOARD 🏆",
            description=leaderboard_text,
            color=discord.Color.gold()
            )
        
        if interaction.guild:
            leaderboard_embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon.url if interaction.guild.icon else None)

        leaderboard_embed.set_footer(text=f"Requested by {interaction.user.name} • Live Global Rankings", icon_url=interaction.user.display_avatar.url)


        await interaction.followup.send(embed=leaderboard_embed)


async def setup(bot: Casino_Bot):
    await bot.add_cog(CasinoLeaderboard(bot))