# Copyright (c) 2025 deludank. All Rights Reserved.
# Stuff that usually don't fit inside of other cogs goes here

import discord
from operator import attrgetter
from discord.ext import commands

import settings

logger = settings.logging.getLogger("bot")

class Docs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        hidden="True",
        help="Generate bot documentation",
        aliases=['gd']
    )
    async def generatedoc(self, ctx):
        if ctx.message.author.id not in settings.OWNER: return
        await ctx.send(f"Generating documentation...")

        alphaSortedCMD = list()
        for command in sorted(self.bot.commands, key=attrgetter('name')):
            alphaSortedCMD.append(command)

        settings.gendocs(alphaSortedCMD)
        logger.info(f'Generated new documentation files @ {settings.gendocsPath}')
        await ctx.send(f"## :notepad_spiral: Generated docs", file=discord.File(r'logs/gendocs.html'))


async def setup(bot):
    await bot.add_cog(Docs(bot))

