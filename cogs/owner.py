# Only for the owner, Deludank
import settings
from discord.ext import commands
from main import startTime
from datetime import datetime

logger = settings.logging.getLogger("bot")

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    @commands.dm_only()
    async def info(self, ctx):
        await ctx.send(settings.getSysInfo())

    @commands.command(
        help="Shows who owns this bot.",
        brief="Show bot owner."
    )
    async def owner(self, ctx):
        author = ctx.message.author
        from settings import OWNER
        if author.id in OWNER:
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
    @commands.is_owner()
    async def uptime(self, ctx):
        await ctx.send(f'❕ Bot uptime is : `{datetime.utcnow() - startTime}`')

async def setup(bot):
    await bot.add_cog(Owner(bot))