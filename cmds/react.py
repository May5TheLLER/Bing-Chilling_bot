import discord
from discord.ext import commands
import random
from core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8') as jf:
    jsdata=json.load(jf)#把一長串的東西丟到json檔案裡

class react(Cog_Extension):
    @commands.command()
    async def 圖片(self,ctx):#ctx: 類似與機器人的上下文對話 當使用者輸入'['時 機器如就知道這是一個指令(參見第bot.py 第12行)
        ran_pic=random.choice(jsdata['pi'])#隨機選擇一張圖片
        pic=discord.File(ran_pic)
        await ctx.send(file=pic)

def setup(bot):
    bot.add_cog(react(bot))