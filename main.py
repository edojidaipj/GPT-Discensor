from bot import Discensor
import os
from dotenv import load_dotenv

load_dotenv()
discord_token = os.environ.get("DISCORD_TOKEN")
allowed_chars = int(os.environ.get("ALLOWED_NON_JAPANESE_CHARS"))

bot = Discensor(allowed_chars = allowed_chars)
bot.run(discord_token)
