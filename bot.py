import discord
from validation import validate_massage_by_chatgpt


class GPTDiscensor(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        super().__init__(intents = intents)

    async def on_message(self, message):
        # 自分のメッセージは無視する
        if message.author == self.user:
            return

        # メッセージをログに出力する
        # 例： "user_name(user_id): message"
        print(f"{message.author.name}({message.author.id}): {message.content}")

        # ChatGPTを使ってメッセージを検証する
        result = await validate_massage_by_chatgpt(message = message.content)

        if result is False:
            # メッセージを削除する
            await message.delete()

            # メッセージを削除したことをログに出力する
            print(f"{message.author.name}({message.author.id}): {message.content} is deleted.")

            # メッセージを削除したことをメンション付きで通知する
            alert_message = "あなたのメッセージは削除されました。"
            await message.channel.send(f"{message.author.mention}{alert_message}")
