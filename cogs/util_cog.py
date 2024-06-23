import discord
from discord.ext import commands
from utils.util_etts import get_etts
from utils.util_gtts import get_gtts
from utils.rvc import get_rvc


class UtilCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tts_settings = {}

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice:
            await ctx.author.voice.channel.connect()
            await ctx.send("음성 채널에 접속했습니다.")
        else:
            await ctx.send("먼저 음성 채널에 접속해 주세요.")

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("음성 채널에서 나갔습니다.")
        else:
            await ctx.send("음성 채널에 접속해 있지 않습니다.")

    @commands.command()
    async def setTTS(self, ctx, tts_type):
        if tts_type not in ['gtts', 'etts']:
            await ctx.send("TTS 유형이 잘못되었습니다. 'gtts' 또는 'etts' 중에서 선택하세요.")
            return

        self.tts_settings[ctx.channel.id] = tts_type
        await ctx.send(f"TTS type for this channel has been set to {tts_type}.")

    @commands.command()
    async def tts(self, ctx, *, message):
        if ctx.channel.id not in self.tts_settings:
            self.tts_settings[ctx.channel.id] = 'etts'

        tts_type = self.tts_settings[ctx.channel.id]
        if tts_type == 'gtts':
            await get_gtts(message, ctx.channel.id)
        elif tts_type == 'etts':
            await get_etts(message, ctx.channel.id)
        get_rvc(tts_type, ctx.channel.id)
        source = discord.FFmpegPCMAudio(f"utils/rvc_output/{ctx.channel.id}_output.wav")
        ctx.voice_client.play(source)


async def setup(bot):
    await bot.add_cog(UtilCog(bot))


