# Copyright (c) 2025 deludank. All Rights Reserved.
# Only for the owner, deludank
from discord.ext import commands
from main import startTime
from datetime import datetime

import settings

logger = settings.logging.getLogger("bot")

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # NOTE: @commands.is_owner() doesn't work
    @commands.command()
    @commands.dm_only()
    async def info(self, ctx):
        author = ctx.message.author
        if author.id in settings.OWNER:
            await ctx.send(settings.getSysInfo())

    @commands.command(
        help="Shows who owns this bot.",
        brief="Show bot owner."
    )
    async def owner(self, ctx):
        author = ctx.message.author
        if author.id in settings.OWNER:
            await ctx.send(f"🥰 Hi {author}, you own me!")
        else:
            await ctx.send(f"😑 Sorry {author}, but you're not my owner.")

    @commands.command(
        help="Show's the bot repo at GitHub",
        brief="Bot repo."
    )
    async def repo(self, ctx):
        await ctx.send(f"❕ DankDonut repo availble at :\nhttps://github.com/deludankbz/DankDonut")

    # TODO: Format the uptime to XX days, YY hours and zz minutes
    @commands.command(help="Show's the bot uptime.", brief="Show bot uptime.")
    async def uptime(self, ctx):
        author = ctx.message.author
        if author.id in settings.OWNER:
            await ctx.send(f'❕ Bot uptime is : `{datetime.now() - startTime}`')

    @commands.command()
    @commands.dm_only()
    async def restart(self, ctx):
        author = ctx.message.author
        if author.id in settings.OWNER:
            print("HUUUUUH????")
            self.bot.close()            

async def setup(bot):
    await bot.add_cog(Owner(bot))
