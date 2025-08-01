# Copyright (c) 2025 deludank. All Rights Reserved.

# TODO:
#   ? find a better way of loading the cogs.
#   logger seems to be not working for these loggings, probally due to a path issue.

import discord
from discord.ext import commands
from datetime import datetime

import settings

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=str(
    settings.BOT_PREFIX), 
    intents=intents, 
    owner_ids=str(settings.OWNER)
)
startTime = datetime.now()
logger = settings.logging.getLogger("bot")

def run():
    
    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Game(name="?help: deludankbz.github.io/dankpage/"), status=discord.Status.idle)

        print(settings.DD_LOGO)
        logger.info(f"{bot.user} is ready!")

        logger.info(f"Loading extensions...")
        # TODO: fix this glob crap
        for cogs in settings.COG_DIR.glob("*.py"):
            if cogs.name != "__init__.py":
                await bot.load_extension(f"cogs.{cogs.name[:-3]}")
                logger.info(f"Extension: '{cogs.name[:-3]}' loaded.")

        logger.info(f"All good!")

    bot.run(str(settings.BOT_TOKEN), root_logger=True)

if __name__ == "__main__":
    run()
