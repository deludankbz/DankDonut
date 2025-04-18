# Copyright (c) 2025 deludank. All Rights Reserved.
# For network commands.
import discord
import requests
import random 
from discord.ext import commands

import settings

logger = settings.logging.getLogger("bot")

@commands.guild_only()
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    async def makeRequest(self, ctx, num):
        numFactUrl = f"http://numbersapi.com/{num}"
        resp = requests.get(numFactUrl)
        if resp.status_code == 200:
            # returns a list
            text = resp.text
            embed=discord.Embed(title="😎 please die", color=0x1874ec)
            embed.add_field(name="", value=f"```{text}```", inline=True)
            embed.set_footer(text=f"🌐 Source : http://numbersapi.com/")
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"🙄 BRO CHILL THE FUCK OUT; that number is too high :shamrock:")


    # TODO: Fix not being able to fetch an user's avatar if he's outside of the current guild.
    @commands.command(
        help="Shows the user avatar.",
        brief="Get user avatar."
    )
    async def avatar(self, ctx, user: discord.Member = None):
        if user != None: msgAuthor = user
        else: msgAuthor = ctx.message.author
        embed=discord.Embed(title=f"{msgAuthor.name}'s avatar", url=f"{msgAuthor.avatar.url}", color=0x794fee)
        embed.set_image(url=msgAuthor.avatar.url)
        embed.set_footer(text="DankDonut")
        await ctx.send(f"{ctx.message.author.mention}")
        await ctx.send(embed=embed)


    @commands.command(
        help="Shows a random fact",
        brief="Get a random fact.",
        aliases=['rf', 'randomf', 'randf']
    )
    async def randomfact(self, ctx):
        randFactUrl = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
        resp = requests.get(randFactUrl)
        if resp.status_code == 200:
            # returns a list
            text, source = resp.json()["text"], resp.json()["source_url"]
            embed=discord.Embed(title="😎 fuck you", color=0x1874ec)
            embed.add_field(name="", value=f"```{text}```", inline=True)
            embed.set_footer(text=f"🌐 Source : {source}")
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"🙄 Sorry, mistakes were made. You")


    @commands.command(
        help="Shows a random fact",
        brief="Get a random fact.",
        aliases=['nf', 'numf', 'numberfact']
    )
    async def numfact(self, ctx, numArg: int):
        await self.makeRequest(ctx, numArg)

    # @commands.command(
    #     help="Search a term in Urban",
    #     brief="???",

    # )
    async def urban(self, ctx, *term):
        termLenght = len(term)
        formatedTerm = ' '.join(term)
        if termLenght > 0:
            await ctx.send(f"✅ Term: `{formatedTerm}`")
        else: await ctx.send(f"❌ Few arguments: `{termLenght}` were given")

    @numfact.error
    async def clearErr(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument): await self.makeRequest(ctx, random.randint(0, 100))

async def setup(bot):
    await bot.add_cog(Fun(bot))
