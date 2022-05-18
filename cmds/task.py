#指定時間執行指令
import discord
from discord.ext import commands
from core.classes import Cog_Extension

import json,asyncio,datetime


class Task(Cog_Extension):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.counter=0#第26行 因為一分有60秒 所以到指定時間之後會執行60次 所以加計數器限制
#為甚麼要用兩次init? 首先Task是繼承位於classes.py
#的Cog_Extension 在那邊我們初始化了bot的屬性。現在
#Task類別裡包含了Cog_Extension的所有東西。就是Task
#繼承了Cog_Extension的內容。當再進行一次init初始化之後，
#原本Cog_Extension的屬性就消失了，故需要用super() (父類別初始化屬性)
        async def time_task():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(942263870381240350)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now().strftime('%H%M')
                with open('setting.json','r',encoding='utf8') as jf:
                    jsdata=json.load(jf)
                if now_time == jsdata['time'] and self.counter==0:
                    await self.channel.send('要會考了!大家加油')
                    self.counter=1
                    await asyncio.sleep(1)
                
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task=self.bot.loop.create_task(time_task())
        #self.bg_task=self.bot.loop.create_task(interval())
    
    # @commands.command()
    # async def set_channel(self,ctx,ch:int):
    #     self.channel=self.bot.get_channel(ch)
    #     await ctx.send(f'set channel:{self.channel.mention}')

    @commands.command()#讓使用者輸入指定時間
    async def set_time(self,ctx,time):
        self.counter=0
        with open('setting.json','r',encoding='utf8') as jf:
            jsdata=json.load(jf)
        jsdata['time']=time
        with open('setting.json','w',encoding='utf8') as jf:
            json.dump(jsdata,jf,indent=4)

def setup(bot):
    bot.add_cog(Task(bot))

