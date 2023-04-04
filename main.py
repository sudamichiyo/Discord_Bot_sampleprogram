import discord
import os
from dotenv import load_dotenv
load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        # メッセージを書いた人がBotなら処理終了
        if message.author.bot:
            return
        channel = message.channel 
        if message.content == '仕事終わった':
            await channel.send('お疲れ様')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['DISCORD_TOKEN'])