import discord
import settings
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=settings.BOT_PREFIX, intents=intents)

logger = settings.logging.getLogger("bot")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle)
    print(settings.DD_LOGO)
    logger.info(f"{bot.user} is ready!")
    
    # ! Only use cogs for commands
    logger.info(f"Loading extensions...")
    for cogs in settings.COG_DIR.glob("*.py"):
        if cogs.name != "__init__.py":
            await bot.load_extension(f"cogs.{cogs.name[:-3]}")
            logger.info(f"Extension: '{cogs.name[:-3]}' loaded.")
    
    logger.info(f"All good!")

bot.run(settings.BOT_TOKEN, root_logger=True)

