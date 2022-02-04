from pyrogram import filters, Client
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from core.bot import Bot
from database.lang_utils import get_message as gm
from functions.youtube_utils import get_yt_details, download_yt_thumbnails

bot = Bot()


@Client.on_message(filters.command("start"))
async def pm_start(_, message: Message):
    bot_username = (await bot.get_me()).username
    bot_name = (await bot.get_me()).first_name
    chat_id = message.chat.id
    mention = message.from_user.mention
    user_id = message.from_user.id
    if message.chat.type == "private":
        if len(message.command) == 1:
            await message.reply_sticker("CAACAgUAAx0CZIiVngACOsth_WQtWVQhHeIMyg9IKsGTXtr7GwACaAUAAoMOOFZMrCdgPGw4nSME")
            await message.reply_photo(
                photo=f"https://telegra.ph/file/053f99956ccee8416b8f7.jpg",
                caption=f"""**💔 ʜᴇʏ {message.from_user.mention} !

ɪ'ᴍ [{bot_name}](t.me/{bot_username}),
ɪ ᴄᴀɴ ᴘʟᴀʏ ᴀɴʏ ᴍᴇᴅɪᴀ ɪɴ ɢʀᴏᴜᴘ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ꜰᴇᴀᴛᴜʀᴇ !
ꜰɪɴᴅ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ʙʏ ᴄʟɪᴄᴋɪɴɢ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ !
━━━━━━━━━━━━━━━━━━━**""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton( 
                   text="😅 ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ ​😅", url=f"https://t.me/{bot_username}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(text="🤔 ʜᴇʟᴘ​ 🤔", callback_data="cbhelp"),
                InlineKeyboardButton(
                    text="💕 ᴍᴀɪɴᴛᴀɪɴᴇʀ 💕​", url="https://t.me/anonymous_was_bot"
                ),
            ],
            [
                InlineKeyboardButton(text="😇 ᴄʜᴀɴɴᴇʟ​ 😇", url=config.CHANNEL_LINK),
                InlineKeyboardButton(
                    text="💔 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ​💔", url="https://t.me/DevilsHeavenMF"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🙄 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🙄​", url="https://t.me/DevilsHeavenMF",
                )
            ],
        ]
    )



__cmds__ = ["start"]
__help__ = {
    "start": "help_start"
}
