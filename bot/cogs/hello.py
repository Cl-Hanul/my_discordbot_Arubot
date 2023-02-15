import discord
from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="hello")
    async def hello(self, ctx: commands.Context):
        await ctx.send("hi!")

if __name__ == "__main__":
    print("이것은 Cog 입니다\nrun코드에서 실행해주세요!")