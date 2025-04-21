# Copyright (c) 2025 deludank. All Rights Reserved.

# TODO:
#   show:
#      show metrics like ping etc... 

import os, discord
from discord.ext import commands
from donut import startTime
from datetime import datetime

import settings

# NOTE: @commands.is_owner() doesn't work

logger = settings.logging.getLogger("bot")

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help="Show bot's server specs."
    )
    async def info(self, ctx):
        if ctx.message.author.id not in settings.OWNER: return
        await ctx.send(settings.getSysInfo())


    @commands.command(
        help="Shows server info, logs and latency.",
        brief="Shows useful information",
        aliases=["s"]
    )
    async def show(self, ctx):
        author = ctx.message.author

        if author.id in settings.OWNER:
            await ctx.send(f"## :computer: System info {settings.getSysInfo()}")
            await ctx.send(f"## :notepad_spiral: Info logs about the bot", file=discord.File(r'logs/infos.log'))
            await ctx.send(f"### :ping_pong: Latency `{str(self.bot.latency)[:4]} ms`")


    @commands.command(
        help="Shows who owns this bot. Useless",
        brief="Show bot owner."
    )
    async def owner(self, ctx):
        author = ctx.message.author

        if author.id in settings.OWNER: await ctx.send(f"🥰 Hi {author}, you own me!")
        else: await ctx.send(f"😑 Sorry {author}, but you're not my owner.")


    @commands.command(
        help="Show's the bot repo at GitHub",
        brief="Bot repo."
    )
    async def repo(self, ctx):
        # TODO: turn repo link into a settings var
        await ctx.send(f"❕ DankDonut repo availble at :\nhttps://github.com/deludankbz/DankDonut")


    @commands.command(
        help="Show's the bot uptime.", 
        brief="Show bot uptime."
    )
    async def uptime(self, ctx):
        if ctx.message.author.id not in settings.OWNER: return
        # TODO: Format uptime to XX days, YY hours and ZZ minutes
        await ctx.send(f'❕ Bot uptime is : `{datetime.now() - startTime}`')


    @commands.command(
        help="Full bot reload.",
        aliases=['r']
    )
    async def reload(self, ctx, arg = None):
        if ctx.message.author.id not in settings.OWNER: return
        os.system("clear")
        if arg == "update": settings.update()
        await ctx.send("Restarting and updating bot ..." if arg is not None else "Restarting bot ...")
        logger.info("Restarting and updating bot." if arg is not None else "Restarting bot.")
        settings.restart()

    @commands.command(
        help="Sets the bot version. Doesn't work yet lmao",
        aliases=['sv', 'sver']
    )
    async def setversion(self, ctx, newVer = None) -> None:
        if ctx.message.author.id not in settings.OWNER: return
        oldVer = settings.VER

        if newVer is not None:
            settings.VER = newVer
            logger.info("settings.VER changed! :: from {oldVer} to {newVer}")
            await ctx.send(f":exclamation: Changing version: `{oldVer} -> {newVer}`")

        else: await ctx.send(f":exclamation: Current version: `{settings.VER}`")

async def setup(bot): await bot.add_cog(Owner(bot))
