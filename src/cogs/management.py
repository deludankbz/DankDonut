# Copyright (c) 2025 deludank. All Rights Reserved.
from time import sleep
import discord
import settings
from discord.ext import commands

logger = settings.logging.getLogger("bot")


# TODO:
#       Add user check to confimr purge 


class Management(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help="Clears an entire channel",
        brief="Clears a channel",
        aliases=['prg']
        )
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def purge(self, ctx):
        await ctx.send(f"✅ Cleanning the channel : `#{ctx.channel}` in 5 seconds.")
        sleep(5)
        await ctx.channel.purge()

    @purge.error
    async def clearDM(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage): await ctx.send(f"❌ You can't clear a DM. dummy")



    @commands.command(
        help="Delete X amount of messages. Maximum of 25.",
        brief="Delete messages.", aliases=['del']
        )
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def delete(self, ctx, amount: int = 0):
        channel = ctx.message.channel
        if amount > 250:
            await ctx.send(f"That's too many messages!")
            return

        await ctx.send(f"✅ Deleting last `{amount}` messages.")
        async for message in channel.history(limit=amount + 2): await message.delete()

    @delete.error
    async def delDM(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage): await ctx.send(f"❌ You cannot delete DM messages.")



async def setup(bot):
    await bot.add_cog(Management(bot))
