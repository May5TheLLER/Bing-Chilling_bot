from genericpath import commonprefix

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl

from core.classes import Cog_Extension


class Music(Cog_Extension):
    
    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("使用者不在頻道")

        channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await channel.connect()
            vc = ctx.voice_clients
            await vc.stop()
        else:
            await ctx.voice_client.moveto(channel)



    @commands.command()
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()
        
    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        vc =  ctx.voice_client
        YDL_OPTIONS = {'format':"bestaudio"}
        FFMPEG_OPTIONS = {'before_options':"-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",'options':"-vn"}
        #其實以上兩行我看不懂原理，只知道很多開發者的寫法都一樣，我想是某種參數之類的。
    
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info =ydl.extract_info(url,download=False)
            url2 = info["formats"][0]["url"]
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            vc.play(source)
            #vc.play(discord.FFmpegPCMAudio(executable="D:\\ffmpeg\\bin", source=url2, **FFMPEG_OPTIONS))
            #vc.play(discord.FFmpegPCMAudio(executable="D:\\ffmpeg\\bin", source=(await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS))
            #做play (播放)功能時感覺有點超出了我的能力範圍(連看都看不懂)，不過我統整了多位開發者的程式寫法，在中發現一些相似之處。從44行到47行都是是我嘗試各種看似邏輯
#           相同的寫法，最終有一種順利執行了(第44、45行)





    @commands.command()
    async def pause(self,ctx):
        vc = ctx.voice_client
        if vc.is_playing():
            await vc.pause()
            await ctx.send("pause")
        else:
            await ctx.send("no audio playing")

    @commands.command()
    async def resume(self,ctx):
        vc = ctx.voice_client
        if vc.is_paused():
            await vc.resume()
            await ctx.send("resume")
        else:
            await ctx.send("no audio paused.")

    @commands.command()
    async def stop(self,ctx):
        vc = ctx.voice_client
        await vc.stop()

def setup(bot):
    bot.add_cog(Music(bot))