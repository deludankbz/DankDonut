# Copyright (c) 2025 deludank. All Rights Reserved.
# For network commands.

import discord, yt_dlp
from discord.ext import commands

import settings

logger = settings.logging.getLogger("bot")

class VoiceChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice = discord.utils.get(self.bot.voice_clients)
        self.queue = list()
        self.current = tuple()

    async def playNext(self, ctx) -> None:
        if not self.queue:
            await self.voice.disconnect()
            return

        url, title = self.queue.pop(0)
        self.current = (url, title)

        buffer = await discord.FFmpegOpusAudio.from_probe(url, **settings.FFMPEG_OPS, method='fallback')
        # TODO: fix this
        self.voice.play(buffer, after=lambda _: self.bot.loop.create_task(self.playNext(ctx)))
        await ctx.send(f"Now playing: **{title}**")

    @commands.command(
        help="Skips the current song.",
        pass_context=True,
    )
    async def skip(self, ctx):
        url, title = self.current

        if self.voice and self.voice.is_playing():
            self.voice.stop()
            await ctx.send(f"Skipped `{title}`")
            await self.playNext(ctx)

    @commands.command(
        help="Play music from YouTube",
        pass_context=True,
        )
    async def play(self, ctx, *, search):

        channel = ctx.author.voice.channel
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice is None or not voice.is_connected():
            await channel.connect()
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        elif voice.channel != channel: return await ctx.send("Bot is already in another voice channel.")

        async with ctx.typing():
            with yt_dlp.YoutubeDL(settings.YT_OPS) as yt:
                info = yt.extract_info(f"ytsearch:{search}", download=False)

                if 'entries' in info: info = info['entries'][0]

                url = info['url']
                title = info['title']

                self.queue.append((url, title))

                await ctx.send(f"**Added song to queue:** `{title}`")

        if not voice.is_playing(): 
            self.voice = voice
            await self.playNext(ctx)
        else: return await ctx.send("You're not in voice channel.")

async def setup(bot):
    await bot.add_cog(VoiceChat(bot))
