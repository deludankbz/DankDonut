# For network commands.
import discord

from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(help="??", brief="???")
    async def owner(self, ctx):
        author = ctx.message.author
        from settings import OWNER
        if author.id == OWNER:
            await ctx.send(f"🥰 Hi {author}, you own me!")
        else:
            await ctx.send(f"😑 Sorry {author}, but you're not my owner.")

    @commands.command(help="??", brief="???")
    async def urban(self, ctx, *term):
        termLenght = len(term)
        formatedTerm = ' '.join(term)
        if termLenght > 0:
            await ctx.send(f"✅ Term: `{formatedTerm}`")
        else: await ctx.send(f"❌ Few arguments: `{termLenght}` were given")

async def setup(bot):
    await bot.add_cog(Fun(bot))