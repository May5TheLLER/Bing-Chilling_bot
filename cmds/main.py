import discord
from discord.ext import commands

from core.classes import Cog_Extension#繼承 Cog_Extension 中的類別
import random
import json

with open('setting.json','r',encoding='utf8') as jf:
    jsdata=json.load(jf)
class Main(Cog_Extension): #繼承Cog_Extension的類別之外還繼承了定義的屬性(bot)
    # def __init__(self,bot):
    #     self.bot=bot 
    #以後在別的地方利用cog放入指令還需定義bot太麻煩了
    #所以直接開新的資料夾core裡面的classes來放定義的指令
    
    @commands.command() #@bot.command()放入cog後要改名為@commands.command() 不然會出錯
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} [ms]' )


    @commands.command()#叫機器人在聊天頻道裡發送嵌入訊息 網路上有生成器可以使用
    async def aqours(self,ctx):
        embed=discord.Embed(title="All songs(Google drive)", url="https://reurl.cc/AK312p", description="some resource about aqours", color=0x0055ff)
        embed.set_author(name="五月五日")
        embed.set_thumbnail(url="https://preview.redd.it/5z1rz73sz9o21.png?width=3845&format=png&auto=webp&s=6bc7f3cc9eecddcfe20a84cfc70ecb4b17b1558d")
        embed.add_field(name="aqours(songs.LLwiki)", value="https://reurl.cc/Y93l44", inline=True)
        embed.add_field(name="aqours(songs.zh.moegirl)", value="https://reurl.cc/yQomnl", inline=True)
        embed.add_field(name="official", value="https://reurl.cc/8oXXRd", inline=True)
        embed.add_field(name="stop(oficial)", value="https://reurl.cc/RreeoG", inline=True)
        embed.add_field(name="Recommended shop", value="Gamers Shop, Animate,Amazone.jp", inline=True)
        embed.set_footer(text=":)")
        await ctx.send(embed=embed)

#隨機組隊
    @commands.command()
    async def RandSquad(self,ctx):
        online=[]
        role = discord.utils.get(ctx.guild.roles, name="R6自訂")
        for mem in ctx.guild.members:
            if mem.bot==False and role in mem.roles:
                online.append(mem.name)
        RandOnline=random.sample(online,k=10)

        for sq in range(2):
            l=random.sample(RandOnline,k=5)
            await ctx.send(l)
            print(l)
            for n in l:
                RandOnline.remove(n)
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        await ctx.send(error)
#新增貼圖後判斷是否為指定貼圖 是的話給予身分組
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):
        if data.message_id==971205283672113172:
            if str(data.emoji)=='<:R6CustomGame:968671628437368862>':
                guild=self.bot.get_guild(data.guild_id)
                # rolesforemoji = discord.utils.get(guild.member.roles, name="R6自訂")
                R6CustomGame=guild.get_role(968670199890993263)
                await data.member.add_roles(R6CustomGame)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,data):
        if data.message._id==971205283672113172:
            if str(data.emoji)=='<:R6CustomGame:968671628437368862>':
                guild=self.bot.get_guild(data.guild_id)
                user=guild.get_member(data.user_id)
                R6CustomGame=guild.get_role(968670199890993263)
                #await data.member.remove_roles(R6CustomGame)
                #本以為改成remove就可以順利運作 但查詢後發現只能用在add上
                await user.remove_roles(R6CustomGame)

def setup(bot):
    bot.add_cog(Main(bot))
