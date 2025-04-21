# Copyright (c) 2025 deludank. All Rights Reserved.
# Stuff that usually don't fit inside of other cogs goes here

import settings
from operator import attrgetter
from discord.ext import commands

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
        await ctx.send(f"Generating documentation...")
        cmdnames = list()
        cog_names = list(self.bot.cogs)


        alphaSortedCMD = list()
        for command in sorted(self.bot.commands, key=attrgetter('name')):
            alphaSortedCMD.append(command)

        settings.gendocs(alphaSortedCMD)
        logger.info(f'Generated new documentation files @ {settings.gendocsPath}')


async def setup(bot):
    await bot.add_cog(Docs(bot))

