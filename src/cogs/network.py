# Copyright (c) 2025 deludank. All Rights Reserved.
# For network commands.

import settings
from discord.ext import commands

logger = settings.logging.getLogger("bot")

class Network(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help="Get bot's ping in ms",
        brief="Simple Ping."
    )
    async def ping(self, ctx):
        await ctx.send(f"🏓 In `{str(self.bot.latency)[:4]} ms`.")


async def setup(bot):
    await bot.add_cog(Network(bot))
