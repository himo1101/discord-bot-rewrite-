#coding: utf-8
#必要なモジュールをインストール
import discord 
import traceback
from discord.ext import commands

#コグとして読み込むファイルを格納
LOAD_FILE = [
    'cog.ct'
]

class TestBot(commands.Bot):
    def __init__(self, cmd_prefix):

        super().__init__(cmd_prefix)
        #コグ(LOAD_FILE)を一つずつ読み込む
        for c in LOAD_FILE:
            try:
                self.load_extension(c)
            
            #読み込むときにエラーが出たら表示
            except Exception:
                traceback.print_exc()

    #BOTが起動したら呼び出される処理
    async def on_ready(self):
        print('ログインしました。')
        print(self.user.name)


if __name__ == '__main__':
    #BOTのPrefixを定義
    bot = TestBot(cmd_prefix = '$')
    #実行
    bot.run('NTgwNjk4MDEzMDUyMTc0MzM2.XOUfMQ.DIr9J0ltN7VVOunpfechAVIEWek')
