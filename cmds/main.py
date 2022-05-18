import discord
from discord.ext import commands

from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jf:
    jsdata=json.load(jf)
class Main(Cog_Extension):
    # def __init__(self,bot):
    #     self.bot=bot 
    #以後在別的地方利用cog放入指令還需定義bot太麻煩了
    #所以直接開新的資料夾core裡面的classes來放定義的指令
    
    @commands.command() #@bot.command()放入cog後改名
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} [ms]' )


    @commands.command()#叫機器人在聊天頻道裡發送嵌入訊息 網路上有生成器可以使用
    async def aqours(self,ctx):
        embed=discord.Embed(title="All songs(Google drive)", url="https://reurl.cc/AK312p", description="some resource about lovelive" , color=0x0c32ed)
        embed.set_author(name="五月五日")
        embed.add_field(name="aqours(songs.LLwiki)", value="https://reurl.cc/Y93l44", inline=False)
        embed.add_field(name="aqours(songs.zh.moegirl)", value="https://reurl.cc/yQomnl", inline=True)
        #embed.set_thumbnail(url=
        await ctx.send(embed=embed)


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
        if data.message._id==971205283672113172:
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
    @commands.Cog.listener()
    async def on_message_delete(self,message):#其中的參數message只可以知道刪除的訊息以及
#原作者，故需要從審核日誌之(AuditLog)中拿取刪除訊息的人
        c=1#計數器，只讓機器人從審核日誌中抓取一個歲新的資料
        async for auditlog in message.guild.audit_logs(action=discord.AuditLogAction.message_delete):
            if c==1:
                adchannel=self.bot.get_channel(int(jsdata['Admit_channel']))#利用json將誰移除了甚麼的訊息給送到指定頻道中，而不是原地發送
                await adchannel.send(auditlog.user.name)
                c+=1
def setup(bot):
    bot.add_cog(Main(bot))