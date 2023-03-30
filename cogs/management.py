from time import sleep
import discord
import settings
from discord.ext import commands

logger = settings.logging.getLogger("bot")

class Management(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx):
        await ctx.send(f"✅ Cleanning the channel : `#{ctx.channel}` in 5 seconds.")
        sleep(5)
        await ctx.channel.purge()
        await ctx.send(f"✅ `#{ctx.channel}` Cleaned.")
        await ctx.channel.purge()

    @clear.error
    async def clearErr(ctx, error): 
        if isinstance(error, commands.MissingPermissions()): await ctx.send(f"❌ Can't clear a channel. You are not an Admin.")
    

    @commands.command(
            help="Delete X amount of messages. Maximum of 25",
            brief="Delete messages."
        )
    async def delete(self, ctx, amount=None):
        channel = ctx.message.channel
        try:
            i_Amount = int(amount)
            if i_Amount < 25:
                await ctx.send(f"✅ Deleting last `{i_Amount}` messages.")
                sleep(2)
                async for message in channel.history(limit=i_Amount + 2):
                    sleep(0.5)
                    await message.delete()
            else:
                await ctx.send(f"❌ Can't delete more than 25 messages.")
        except Exception:
            await ctx.send(f"❌ {amount} needs to be a number!")

async def setup(bot):
    await bot.add_cog(Management(bot))