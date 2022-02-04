from pyrogram import filters, Client
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from core.bot import Bot
from database.lang_utils import get_message as gm
from functions.youtube_utils import get_yt_details, download_yt_thumbnails




@Client.on_message(filters.command("start"))
async def pm_start(_, message: Message):
    bot = await Bot().get_me()
    bot_username = bot.username
    bot_name = bot.first_name
    chat_id = message.chat.id
    mention = message.from_user.mention
    user_id = message.from_user.id
    if message.chat.type == "private":
        if len(message.command) == 1:
            return await message.reply_text("[💔](https://telegra.ph/file/e01fa0ec7bb6f141fb864.jpg) **ʜᴇʏ {} !**\n\n**ɪ'ᴍ [{}](t.me/{}),**\n**ɪ ᴄᴀɴ ᴘʟᴀʏ ᴀɴʏ ᴍᴇᴅɪᴀ ɪɴ ɢʀᴏᴜᴘ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ꜰᴇᴀᴛᴜʀᴇ !**\n**ꜰɪɴᴅ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ʙʏ ᴄʟɪᴄᴋɪɴɢ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ !**".format(
          message.from_user.mention, bot_name, bot_username
          ),
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
                InlineKeyboardButton(text="😇 ᴄʜᴀɴɴᴇʟ​ 😇", url="https://t.me/DevilsHeavenMF"),
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
  )


        if len(message.command) >= 2:
            query = message.command[1]
            if query.startswith("ytinfo_"):
                link = query.split("ytinfo_")[1]
                details = get_yt_details(link)
                thumb_url = details["thumbnail"]
                thumb_file = download_yt_thumbnails(thumb_url, user_id)
                result_text = f"""
{gm(chat_id, 'track_info')}
📌 **{gm(chat_id, 'yt_title')}**: {details['title']}
🕰 **{gm(chat_id, 'duration')}**: {details['duration']}
👍 **{gm(chat_id, 'yt_likes')}**: {details['likes']}
👎 **{gm(chat_id, 'yt_dislikes')}**: {details['dislikes']}
⭐ **{gm(chat_id, 'yt_rating')}**: {details['rating']}
"""
                return await message.reply_photo(
                    thumb_file,
                    caption=result_text,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    f"🎥 {gm(chat_id, 'watch_on_yt')}",
                                    url=f"https://www.youtube.com/watch?v={details['link']}",
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    f"🗑 {gm(chat_id, 'close_btn_name')}",
                                    callback_data="close",
                                )
                            ],
                        ]
                    ),
                )
            if query.startswith("help"):
                return await message.reply(
                    gm(chat_id, "helpmusic"),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    f"{gm(chat_id, 'commands')}",
                                    url="https://telegra.ph/The-Bot-Command-11-14",
                                )
                            ]
                        ]
                    ),
                    disable_web_page_preview=True,
                )
    if message.chat.type in ["group", "supergroup"]:
        await message.reply(
            gm(chat_id, "chat_greet").format(mention, bot_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            gm(message.chat.id, "group_buttn"),
                            url=f"https://t.me/{bot_username}?start=help",
                        )
                    ]
                ],
            ),
            disable_web_page_preview=True,
        )


__cmds__ = ["start"]
__help__ = {
    "start": "help_start"
}
