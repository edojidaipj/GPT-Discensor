import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")
discord_token = os.environ.get("DISCORD_TOKEN")
