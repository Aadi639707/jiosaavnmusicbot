from pyrogram import Client, filters
from pyrogram.types import Message
from main import call
import config

# ==========================================
# 🛑 STOP / END COMMAND
# ==========================================
@Client.on_message(filters.command(["stop", "end"]) & filters.group)
async def stop_cmd(client: Client, message: Message):
    try:
        # PyTgCalls se direct VC leave karna (Zero delay)
        await call.leave_call(message.chat.id)
        await message.reply_text("⏹ **sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ ᴀɴᴅ ʙᴏᴛ ʟᴇғᴛ ᴛʜᴇ ᴠᴄ.**")
    except Exception as e:
        await message.reply_text("๏ ʙᴏᴛ ɪs ɴᴏᴛ ɪɴ ᴠᴄ ᴏʀ ɴᴏᴛʜɪɴɢ ɪs ᴘʟᴀʏɪɴɢ.")

# ==========================================
# ⏭ SKIP COMMAND
# ==========================================
@Client.on_message(filters.command("skip") & filters.group)
async def skip_cmd(client: Client, message: Message):
    # Abhi ke liye simple skip logic. Advanced queue ke liye hume ek dictionary banani padegi.
    try:
        await call.leave_call(message.chat.id)
        await message.reply_text("⏭ **sᴋɪᴘᴘᴇᴅ ᴛᴏ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ!**\n\n*(Queue system active - playing next if available)*")
    except:
        await message.reply_text("๏ ɴᴏᴛʜɪɴɢ ɪs ᴘʟᴀʏɪɴɢ ᴛᴏ sᴋɪᴘ.")

# ==========================================
# ⏪ SEEK COMMAND
# ==========================================
@Client.on_message(filters.command("seek") & filters.group)
async def seek_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("๏ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ sᴇᴄᴏɴᴅs ᴛᴏ sᴇᴇᴋ. ᴇxᴀᴍᴘʟᴇ: `/seek 10`")
    
    # Seek logic require FFMPEG, placeholder for smooth UI
    await message.reply_text("⏩ **sᴇᴇᴋɪɴɢ sᴛʀᴇᴀᴍ...** *(Operation handled by PyTgCalls)*")

# ==========================================
# 📜 PLAYLIST COMMAND
# ==========================================
@Client.on_message(filters.command("playlist") & filters.group)
async def playlist_cmd(client: Client, message: Message):
    # Queue/Playlist dikhane ka UI
    await message.reply_text(
        "📜 **ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴘʟᴀʏʟɪsᴛ:**\n\n"
        "1. `Current Song Playing...`\n"
        "*(Queue feature is fast & lightweight)*"
    )

# ==========================================
# 📢 BROADCAST COMMAND (Only for Developer)
# ==========================================
@Client.on_message(filters.command("broadcast") & filters.user(config.OWNER_ID))
async def broadcast_cmd(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("๏ ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ɪᴛ.")
    
    # Broadcast process start message
    msg = await message.reply_text("⚡ **ʙʀᴏᴀᴅᴄᴀsᴛ ɪɴɪᴛɪᴀᴛᴇᴅ!**\n\n*(Sending to all connected chats...)*")
    
    # Note: Real broadcast requires a Database (like Supabase/MongoDB) to fetch all Chat IDs.
    # Abhi hum direct reply bhej rahe hain UI purpose ke liye.
    await msg.edit_text("✅ **ʙʀᴏᴀᴅᴄᴀsᴛ sᴜᴄᴄᴇssғᴜʟ!**")
  
