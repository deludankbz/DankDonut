# For network commands.
import discord
import settings
from discord.ext import commands

logger = settings.logging.getLogger("bot")

@commands.guild_only()
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Add *args, so the user can

    # Fix not being able to fetch an user's avatar if he's outside of
    # the current guild.
    @commands.command(
        help="Shows the user avatar.",
        brief="Get user avatar."
    )
    async def avatar(self, ctx, user: discord.Member = None):
        if user != None:
            msgAuthor = user
        else:
            msgAuthor = ctx.message.author
        embed=discord.Embed(title=f"{msgAuthor.name}'s avatar", url=f"{msgAuthor.avatar.url}", color=0x794fee)
        embed.set_image(url=msgAuthor.avatar.url)
        embed.set_footer(text="DankDonut")
        await ctx.send(f"{ctx.message.author.mention}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Search a term in Urban",
        brief="???"
    )
    async def urban(self, ctx, *term):
        termLenght = len(term)
        formatedTerm = ' '.join(term)
        if termLenght > 0:
            await ctx.send(f"✅ Term: `{formatedTerm}`")
        else: await ctx.send(f"❌ Few arguments: `{termLenght}` were given")

async def setup(bot):
    await bot.add_cog(Fun(bot))