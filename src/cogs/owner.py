# ^}Copyright (c) 2025 deludank. All Rights Reserved.

import os
from discord.ext import commands
from main import startTime
from datetime import datetime

import settings

logger = settings.logging.getLogger("bot")
class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # NOTE: @commands.is_owner() doesn't work
    @commands.command(
        help="Show bot's machine info."
    )
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


    @commands.command(
        help="Show's the bot uptime.", 
        brief="Show bot uptime."
    )
    async def uptime(self, ctx):
        author = ctx.message.author
        if author in settings.OWNER:
            # TODO: Format the uptime to XX days, YY hours and zz minutes
            await ctx.send(f'❕ Bot uptime is : `{datetime.now() - startTime}`')


    @commands.command(
        help="Full bot reload."
    )
    async def reload(self, ctx, arg = None):
        author = ctx.message.author
        if author.id in settings.OWNER: 
            os.system("clear")
            if arg == "update": settings.update()
            await ctx.send("Restarting and updating bot ..." if arg != None else "Restarting bot ...")
            logger.info("Restarting and updating bot." if arg != None else "Restarting bot.")
            settings.restart()


async def setup(bot): await bot.add_cog(Owner(bot))
