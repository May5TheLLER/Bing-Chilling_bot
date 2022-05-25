import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jf:
    jsdata=json.load(jf)#把一長串的東西丟到json檔案裡

class Event(Cog_Extension):
    #成員加入訊息
    @commands.Cog.listener()#@bot.event改名
    async def on_member_join(self,member):
        cha=self.bot.get_channel(int(jsdata['welcome_channel']))#把訊息發送到指定聊天頻道(歡迎)
        await cha.send(F'{member} 加入了:)!')#有人加入了 傳送訊息在該頻道

    #成員離開訊息
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        cha=self.bot.get_channel(int(jsdata['leave_channel']))#把訊息發送到指定聊天頻道(離開)
        await cha.send(F'{member} 離開了:(')#有人離開了 傳送訊息在該頻道
    
    #關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword=['醉了','彬彬']
        if msg.content in keyword:#當輸入的訊息裡有包含keyword在裡面的話
            await msg.channel.send('那個彬彬就是遜啦')#在使用者輸入的頻道裡回覆「那個彬彬就是遜啦」
        
        if msg.content.endswith('太遜了'):#當輸入的訊息結尾包含「太遜了」的話
            await msg.channel.send('那個彬彬就是遜啦')#在使用者輸入的頻道裡回覆「那個彬彬就是遜啦」
            ran_pic=random.choice(jsdata['bing'])#隨機選擇一張圖片
            pic=discord.File(ran_pic)
            await msg.channel.send(file=pic)
def setup(bot):
    bot.add_cog(Event(bot))