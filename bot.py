import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding='utf8') as jf:
    jsdata=json.load(jf)#把一長串的東西丟到json檔案裡

intents=discord.Intents.default()#新版本
intents.members=True#新版本
bot=commands.Bot(command_prefix='[',intents=intents)

@bot.event#機器人的事件
async def on_ready():
    print('Bing Chilling機器人 is online')#上線

#成員加入訊息
@bot.event
async def on_member_join(member):
    cha=bot.get_channel(int(jsdata['wellcome_cannel']))#把訊息發送到指定聊天頻道(歡迎)
    await cha.send(F'{member} 加入了:)!')

#成員離開訊息
@bot.event
async def on_member_remove(member):
    cha=bot.get_channel(int(jsdata['leave_cannel']))#把訊息發送到指定聊天頻道(離開)
    await cha.send(F'{member} 離開了:(')

#從我的電腦檔案中傳送圖片訊息
@bot.command()
async def image(ctx):#ctx: 類似與機器人的上下文對話 當使用者輸入'['時 機器如就知道這是一個指令(參見第10行)
    pic=discord.File(jsdata['pic'])
    await ctx.send(pic)

bot.run(jsdata['token'])#執行機器人 token 是此機器人的執行金鑰(完整的放在json裡)

