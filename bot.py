import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json','r',encoding='utf8') as jf:
    jsdata=json.load(jf)#把一長串的東西丟到json檔案裡

intents=discord.Intents.default()#新版本
intents.members=True#新版本
bot=commands.Bot(command_prefix='[',intents=intents)

@bot.event#機器人的事件
async def on_ready():
    print('Bing Chilling機器人 is online')#bot上線
#已經放入event的cog資料夾裡面了
# #成員加入訊息
# @bot.event
# async def on_member_join(member):
#     cha=bot.get_channel(int(jsdata['wellcome_cannel']))#把訊息發送到指定聊天頻道(歡迎)
#     await cha.send(F'{member} 加入了:)!')#有人加入了 傳送訊息在該頻道

# #成員離開訊息
# @bot.event
# async def on_member_remove(member):
#     cha=bot.get_channel(int(jsdata['leave_cannel']))#把訊息發送到指定聊天頻道(離開)
#     await cha.send(F'{member} 離開了:(')#有人離開了 傳送訊息在該頻道

#已經放入了react的cog資料夾裡面了
# @bot.command()
# async def ping(ctx):
#     await ctx.send(f'{round(bot.latency*1000)} [ms]' )
# #從我的電腦檔案中傳送圖片訊息

# @bot.command()
# async def 圖片(ctx):#ctx: 類似與機器人的上下文對話 當使用者輸入'['時 機器如就知道這是一個指令(參見第10行)
#     ran_pic=random.choice(jsdata['pi'])#隨機選擇一張圖片
#     pic=discord.File(ran_pic)
#     await ctx.send(file=pic)

@bot.command()
async def load(ctx, extension):
    bot.load_extension[f'cmds.{extension}']
    await ctx.send[f'Loaded {extension} done.']

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension[f'cmds.{extension}']
    await ctx.send[f'UnLoaded {extension} done.']

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension[f'cmds.{extension}']
    await ctx.send[f'ReLoaded {extension} done.']



for filename in os.listdir('./cmds'):
    if filename.endswith('.py'): #檔名為.py才導入 
        bot.load_extension(f'cmds.{filename[:-3]}')#把導入後檔名的.py去掉

if __name__=='__main__': 
    bot.run(jsdata['token'])#執行機器人 'token' 是此機器人的執行金鑰(完整的放在json裡)

