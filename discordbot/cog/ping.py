import discord
from discord.ext import commands

class Tc(commands.Cog):
    #BOTをインスタンス化
    def __init__(self, bot):
        self.bot = bot

    #コマンドの処理
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')

#cogとして登録
def setup(bot):
    bot.add_cog(Tc(bot))
