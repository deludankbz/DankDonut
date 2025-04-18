# Copyright (c) 2025 deludank. All Rights Reserved.
# Stuff that usually don't fit inside of other cogs goes here

import settings
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
        cmdnames = list()
        cog_names = list(self.bot.cogs)

        for x in self.bot.commands:
            divTemplate = f"""
<!-- {x.name}:{x.cog_name} -->
<div class="command-content">
<p class="name">{x.name}</p>
<div class="desc">
<p class="cog">{x.cog_name}</p>
<p class="help">{x.help}</p>
</div>
</div>
            """
            print(divTemplate)

async def setup(bot):
    await bot.add_cog(Docs(bot))

