import random
from pyrogram import filters
from Waifu import Waifu, BOT_USERNAME
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from Waifu.core.strings import (music_txt, ai_txt, bass_txt, youtube_txt, 
misc_txt, broadcast_txt, checker_txt, devs_txt, instagram_txt)

TheChampu = ["https://graph.org/file/80698e4b76b1b160b5b5d.mp4", "https://graph.org/file/b8234196b088ee0e11845.mp4", "https://graph.org/file/2c454ae9e13ca07ec0cc7.mp4", "https://graph.org/file/ae5ed0cb2f0ee4ae9c15e.mp4", "https://graph.org/file/62584cef34f9a8d4427c8.mp4"] 
# ------------------------------------------------------------------------------- #

start_txt = """
**ʜᴇʟʟᴏ** {} 

**🎵✨ ɪ ᴀᴍ ʏᴏᴜʀ ᴡᴧɪғᴜ, ᴅᴇʟɪᴠᴇʀɪɴɢ ғʟᴀᴡʟᴇss ʙᴇᴀᴛs ᴡɪᴛʜ ᴢᴇʀᴏ ʟᴀɢ. ᴍᴏʀᴇ ᴛʜᴀɴ ᴀ ᴍᴜsɪᴄ ʙᴏᴛ, ɪ'ᴍ ᴛʜᴇ sʏᴍᴘʜᴏɴʏ ᴏғ ᴛʜᴇ ғᴜᴛᴜʀᴇ, ᴄᴜsᴛᴏᴍ-ᴍᴀᴅᴇ ғᴏʀ ʏᴏᴜʀ ᴍᴜsɪᴄᴀʟ ʙʟɪss. ʟᴇᴛ's ᴅɪᴠᴇ ɪɴᴛᴏ ᴀ ᴡᴏʀʟᴅ ᴡʜᴇʀᴇ ᴇᴠᴇʀʏ ɴᴏᴛᴇ ʀᴇsᴏɴᴀᴛᴇs ᴡɪᴛʜ ᴘᴇʀғᴇᴄᴛɪᴏɴ, ᴀɴᴅ ᴇᴠᴇʀʏ ʀʜʏᴛʜᴍ ɪɢɴɪᴛᴇs ʏᴏᴜʀ sᴏᴜʟ! 💖🌟.**
"""

# ------------------------------------------------------------------------------- #

button = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),    
        ],
        [
            InlineKeyboardButton("↯ ᴄᴏᴍᴍᴀɴᴅs ↯", callback_data="help_"),    
        ],
                [
            InlineKeyboardButton("☆ ᴍʏ ʙᴧʙᴇ ☆", url=f"https://t.me/TheChampu"),    
        ]
])



# ------------------------------------------------------------------------------- #

help_txt = """**
**» ˹ᴡᴧɪғᴜ˼ ᴄᴏᴏʟ ᴏʀ ᴇxᴄʟᴜsɪᴠᴇ ғᴇᴀᴛᴜʀᴇs** 
"""



# ------------------------------------------------------------------------------- #

Waifu_buttons = [              
                [
                    InlineKeyboardButton("ᴍᴜsɪᴄ", callback_data="music_"),   
                    InlineKeyboardButton("ᴀɪ", callback_data="ai_"),
                    InlineKeyboardButton("ʙᴀss", callback_data="bass_")
                ],
                [
                    InlineKeyboardButton("ʏᴏᴜᴛᴜʙᴇ", callback_data="youtube_"),   
                    InlineKeyboardButton("ᴍɪsᴄ", callback_data="misc_"),
                    InlineKeyboardButton("ʙʀᴏᴀᴅᴄᴀsᴛ", callback_data="broadcast_")
                ],
                [
                    InlineKeyboardButton("ᴄʜᴇᴄᴋᴇʀ", callback_data="checker_"),   
                    InlineKeyboardButton("ᴅᴇᴠs", callback_data="devs_"),
                    InlineKeyboardButton("ɪɴsᴛᴀɢʀᴀᴍ", callback_data="instagram_")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home_"),
                    InlineKeyboardButton("⟲ ᴄʟᴏꜱᴇ ⟳", callback_data="close_data")
                ]
                ]


back_buttons  = [[
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_"),                    
                ]]





waifu = random.choice(TheChampu)
@Waifu.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_videp(video=waifu,
                            caption=start_txt.format(message.from_user.mention),reply_markup=button)



@Waifu.on_callback_query()
async def cb_handler(client, query):
    if query.data=="home_":
        buttons =  [
            [
                InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
            [
                InlineKeyboardButton("↯ ᴄᴏᴍᴍᴀɴᴅs ↯", callback_data="help_")
            ]    
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                start_txt.format(query.from_user.mention),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


# ------------------------------------------------------------------------------- #
        
    elif query.data=="help_":        
        reply_markup = InlineKeyboardMarkup(Waifu_buttons)
        try:
            await query.edit_message_text(
                help_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
    elif query.data=="music_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                music_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="ai_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                ai_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="bass_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                bass_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="youtube_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                youtube_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
        
    elif query.data=="misc_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                misc_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


        
    elif query.data=="broadcast_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                broadcast_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="checker_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                checker_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
    elif query.data=="devs_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                devs_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass        



    elif query.data=="instagram_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                instagram_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
# ------------------------------------------------------------------------------- #

    elif query.data=="maintainer_":
            await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)

  
# ------------------------------------------------------------------------------- #
 
    elif query.data=="close_data":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass

