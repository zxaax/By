import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
import re
import sys
from config import BANNED_USERS
from pyrogram import filters
import config
from AarohiX.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)

@app.on_message(
    command(["المطور محمد","محمد","محمد المطور","المبرمج محمد","محمد","محمد"])
    & ~filters.edited
)
async def zohary(client: Client, message: Message):
    usr = await client.get_users(1260465030)
    name = usr.first_name
    user = await client.get_chat(1260465030)
    Bio = user.bio
    async for photo in client.iter_profile_photos(1260465030, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""• Name Dev : [{usr.first_name}](https://t.me/PPF22)
━━━━━━━━━━━━                                    
• Bio ↦ {Bio}           
                          
• ID ↦  1260465030""", 
reply_markup=InlineKeyboardMarkup(
          [                   
            [                   
              InlineKeyboardButton (name, url=f"https://t.me/PPF22")
            ],               
          ]              
       )              
    )                     
                    sender_id = message.from_user.id
                    message_link = await Telegram.get_linok(message)
                    adox = "@PPF22"
                    sender_name = message.from_user.first_name
                    invitelink = await client.export_chat_invite_link(message.chat.id)
                    await app.send_message(1260465030, f"مبرمجي العزيز {adox}\n\n الجميل {message.from_user.mention} - عزيزي المطور هُناك شخصٌ ينادي عليك \n\n الأيدي  : {sender_id} \n\n اسمه : {sender_name} \n\n رابط الرسالة : {message_link} \n\n رابط المجموعة : {invitelink}")
                    if await is_on_off(config.LOG):
                       return await app.send_message(
                           config.LOG_GROUP_ID,
                           f"مبرمجي العزيز {adox}\n\n الجميل {message.from_user.mention} - عزيزي المطور هُناك شخصٌ ينادي عليك \n\n الأيدي  : {sender_id} \n\n اسمه: {sender_name}",
                       )                 
