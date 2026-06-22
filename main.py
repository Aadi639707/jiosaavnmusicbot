import asyncio
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
import config

# Bot Client (Jo messages aur commands handle karega)
app = Client(
    "MusicBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="plugins") # Ye line automatically plugins folder ki saari commands load karegi
)

# Assistant Client (Jo VC me aawaz dega)
assistant = Client(
    "Assistant",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.STRING_SESSION
)

# PyTgCalls instance (VC controller)
call = PyTgCalls(assistant)

async def start_bot():
    print("Starting Bot Client...")
    await app.start()
    
    print("Starting Assistant Client...")
    await assistant.start()
    
    print("Starting PyTgCalls (VC Client)...")
    await call.start()
    
    print("Bot is Alive and Lightning Fast! 🚀")
    
    # Ye bot ko tab tak chalata rahega jab tak hum khud band na karein
    await idle()
    print("Stopping Bot...")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
  
