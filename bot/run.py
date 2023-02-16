import discord
from discord.ext import commands
from cogs import hello

from os import chdir
from json import loads, dumps

with open("BOTTOKEN","r") as file:
    TOKEN = file.read()

intents = discord.Intents.all()
command_prefix = "~"

bot = commands.Bot(command_prefix="~",intents=intents)
cog = [
    hello.Hello(bot)
]

@bot.event
async def on_ready():
    print(f"현재 봇이 {len(bot.guilds)}개의 서버에 접속을 성공했습니다!")
    activity = discord.Activity()
    activity.type = discord.ActivityType.listening
    activity.name = "`~help`"
    await bot.change_presence(activity=activity,status=discord.Status.online)
    for i in cog:
        await bot.add_cog(i)
    
    with open("bot\\botdata\\coins.json","r") as file:
        coins = loads(file.read())


bot.run(TOKEN)