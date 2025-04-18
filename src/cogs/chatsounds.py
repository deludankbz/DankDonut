# Copyright (c) 2025 deludank. All Rights Reserved.
# For network commands.

import glob, discord
from discord.ext import commands

import settings

logger = settings.logging.getLogger("bot")

class ChatSounds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(
        help="Plays the selected ChatSound in voicechat on which the author is connected.",
        pass_context=True,
        aliases=["ab"]
        )
    async def abobinha(self, ctx, soundname):
        """ This enters the ctx.message.author.voice.channel, plays a selected sound and quits. """

        soundfiles = glob.glob(f"{settings.CHATSOUNDS_DIR}*")

        if soundname == "list":
            return await ctx.send(f"""{soundfiles}""")

        if ctx.author.voice:
            channel = ctx.message.author.voice.channel

            for sound in soundfiles:
                # NOTE: this trick will only work for linux paths
                if soundname == sound.split('/')[-1][:-4]:
                    voice_client = await channel.connect()
                    voice_client.play(discord.FFmpegPCMAudio(source=sound))


    @commands.command(
        help="Joins the same voice channel on which the author is connected",
        hidden=True, 
        pass_context=True,
        aliases=["j"]
    )
    async def join(self, ctx):
        """ Joins a voice channel """

        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            return await channel.connect()


    @commands.command(
        help="If connected to a voice channel; the bot will exit the current voice channel",
        hidden=True,
        aliases=["q"]
    )
    async def quit(self, ctx):
        """ Quits a voice channel """

        voice = ctx.message.guild.voice_client
        await voice.disconnect()

async def setup(bot):
    await bot.add_cog(ChatSounds(bot))
