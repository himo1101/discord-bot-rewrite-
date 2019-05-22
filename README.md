# discord-bot-rewrite-雑解説

これは簡単にPythonでBOTを作るためのコードです

まずあなたは、Python3.7xをダウンロードする必要があります。  
[Python](https://www.python.org/downloads/release/python-373/)
これは私の開発環境のPython3.7.3のインストーラーが公開されてるページのURLです  
そしてインストールします  
次にcmdを開き
```python -m pip install -U pip```  
と入力しpipをアップグレードしてください  
そして、終わったら
```python -m pip install -U discord.py[voice]```
と入力してください。ボイスサポート付きのdiscord.pyを最新バージョンでインストールします。

そして私が置いてる`test.py`を開いてトークンを貼り付けてください
```このトークンがあるとBOTにログインできます。逆に言えばこのトークンを流出させてしまうと貴方のBOTが悪用されかねません。
必ずトークンは何があっても流出させないでください。
```

そしてcmdに`test.py`をD&Dして実行できます。
