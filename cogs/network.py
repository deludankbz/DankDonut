# For network commands.
from discord.ext import commands

class Network(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Get bot's ping in ms", brief="Simple Ping.")
    async def ping(self, ctx):
        await ctx.send(f"🏓 In `{str(self.bot.latency)[:4]} ms`.")

async def setup(bot):
    await bot.add_cog(Network(bot))