import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from yt_dlp import YoutubeDL
from pytgcalls.types import MediaStream

# main.py se hum apna PyTgCalls ka instance import kar rahe hain
from main import call 

# Extreme Fast yt-dlp Settings (ZERO DOWNLOAD)
YDL_OPTIONS = {
    'format': 'bestaudio/best',
    'quiet': True,
    'no_warnings': True,
    'skip_download': True,  # Yahi wo magic hai jo file download nahi hone dega
    'simulate': True,       # Sirf link extract karega
    'geo_bypass': True,
    'extract_flat': False,
    'nocheckcertificate': True,
}

@Client.on_message(filters.command("play") & filters.group)
async def play_command(client: Client, message: Message):
    # Check karna ki user ne gaane ka naam likha hai ya nahi
    if len(message.command) < 2:
        return await message.reply_text("๏ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴍᴇ ᴀ sᴏɴɢ ɴᴀᴍᴇ ᴏʀ ʟɪɴᴋ ᴛᴏ ᴘʟᴀʏ.")
    
    query = message.text.split(None, 1)[1]
    
    # Fast response indicator
    processing_msg = await message.reply_text("⚡ ᴘʀᴏᴄᴇssɪɴɢ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ...")

    try:
        # Run yt-dlp in a separate thread so it doesn't block the bot
        def get_stream_url():
            with YoutubeDL(YDL_OPTIONS) as ydl:
                # ytsearch: lagane se wo direct youtube par search karega
                info = ydl.extract_info(f"ytsearch:{query}", download=False)
                if 'entries' in info:
                    info = info['entries'][0]
                return info['url'], info['title'], info['duration']

        loop = asyncio.get_event_loop()
        stream_url, title, duration = await loop.run_in_executor(None, get_stream_url)

        # PyTgCalls ke through directly VC me push karna
        await call.play(
            message.chat.id,
            MediaStream(stream_url)
        )

        # Success message format bilkul tumhare reference jaisa
        play_text = f"""
➲ **sᴛᴀʀᴛᴇᴅ sᴛʀᴇᴀᴍɪɴɢ** 🎵

▶️ **ᴛɪᴛʟᴇ :** {title}
⏱️ **ᴅᴜʀᴀᴛɪᴏɴ :** {duration} sᴇᴄᴏɴᴅs
👤 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
"""
        await processing_msg.edit_text(play_text)

    except Exception as e:
        # Error handling ko clean rakha hai taaki crash na ho
        await processing_msg.edit_text(f"❌ ʏᴛ-ᴅʟᴘ ᴇʀʀᴏʀ: {str(e)[:100]}...\n\nᴛʀʏ ᴀɴᴏᴛʜᴇʀ ǫᴜᴇʀʏ.")
      
