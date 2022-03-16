import discord
from discord.ext import commands

from core.classes import Cog_Extension
class Main(Cog_Extension):
    # def __init__(self,bot):
    #     self.bot=bot 
    #以後在別的地方利用cog放入指令還需定義bot太麻煩了!
    #所以直接開新的資料夾core裡面的classes來放定義的指令
    
    @commands.command() #@bot.command()放入cog後改名
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} [ms]' )


    @commands.command()#叫機器人在聊天頻道裡發送嵌入訊息 網路上有生成器可以使用
    async def embed(self,ctx):
        embed=discord.Embed(title="all songs", url="https://reurl.cc/AK312p", description="(google drive)")
        embed.add_field(name="aqours(songs.LLwiki)", value="https://reurl.cc/Y93l44", inline=False)
        embed.add_field(name="aqours(songs.zh.moegirl)", value="https://reurl.cc/yQomnl", inline=True)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Main(bot))