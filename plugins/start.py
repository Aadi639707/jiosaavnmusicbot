from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import config

# Small-caps font format with dynamic variables
START_TEXT = """
ʜᴇʏ {user_name}, 🥀

๏ ᴛʜɪs ɪs {bot_name} ♪ [ ɴᴏ ᴀᴅs ]™ !

➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.

๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.
"""

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    # Bot aur User ka naam fetch kar rahe hain
    bot = await client.get_me()
    bot_name = bot.first_name
    user_name = message.from_user.first_name
    
    # Text me naam inject karna
    text = START_TEXT.format(user_name=user_name, bot_name=bot_name)
    
    # Developer ID link create karna
    dev_link = f"tg://user?id={config.OWNER_ID}"
    
    # Buttons setup exactly as requested
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("+ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ +", url=f"https://t.me/{bot.username}?startgroup=true")
            ],
            [
                InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_menu")
            ],
            [
                InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ ↗️", url=dev_link),
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ ↗️", url=config.SUPPORT_CHAT)
            ]
        ]
    )
    
    # Image ke sath message send karna
    await message.reply_photo(
        photo=config.START_IMG,
        caption=text,
        reply_markup=buttons
    )

# Ek simple ping command check karne ke liye ki bot zinda hai ya nahi
@Client.on_message(filters.command("ping"))
async def ping_cmd(client: Client, message: Message):
    await message.reply_text("PONG! 🚀 Bot is running fast.")
  
