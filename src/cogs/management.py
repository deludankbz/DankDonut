from time import sleep
import discord
import settings
from discord.ext import commands

logger = settings.logging.getLogger("bot")

# TODO: fix command.error() boilerplate
# ? how do i fix this shit???

class Management(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Add user check to confimr purge 
    @commands.command(
        help="Clears an entire channel",
        brief="Clears a channel"
        )
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def clear(self, ctx):
        await ctx.send(f"✅ Cleanning the channel : `#{ctx.channel}` in 5 seconds.")
        sleep(5)
        await ctx.channel.purge()
        await ctx.send(f"✅ `#{ctx.channel}` Cleaned.")
        sleep(5)
        await ctx.channel.purge()

    @commands.command(
        help="Delete X amount of messages. Maximum of 25.",
        brief="Delete messages.", aliases=['del']
        )
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def delete(self, ctx, amount=None):
        channel = ctx.message.channel
        try:
            i_Amount = int(amount)
            # TODO: custom command to set i_Amount
            if i_Amount <= 25:
                await ctx.send(f"✅ Deleting last `{i_Amount}` messages.")
                sleep(2)
                async for message in channel.history(limit=i_Amount + 2):
                    sleep(0.5)
                    await message.delete()
            else:
                await ctx.send(f"❌ Can't delete more than 25 messages.")
        except Exception:
            await ctx.send(f"❌ {amount} needs to be a number!")
    
    # note: don't call classes that raise an error
    @clear.error
    async def clearErr(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage): await ctx.send(f"❌ You cannot clear a DM.")

    @delete.error
    async def clearErr(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage): await ctx.send(f"❌ You cannot delete messages from a DM.")

async def setup(bot):
    await bot.add_cog(Management(bot))