import os
from dotenv import load_dotenv

load_dotenv()

# Credentials
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
STRING_SESSION = os.getenv("STRING_SESSION", "")

# Owner & Support details
OWNER_ID = int(os.getenv("OWNER_ID", "0"))  # Dev button ke liye user id
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/your_channel")  # Channel button link

# Images/Graphics URLs
START_IMG = os.getenv("START_IMG", "https://telegra.ph/file/default_start.jpg")
THUMB_IMG = os.getenv("THUMB_IMG", "https://telegra.ph/file/default_thumb.jpg")
