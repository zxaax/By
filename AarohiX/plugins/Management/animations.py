from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AarohiX import app 

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton 



@app.on_message(
    filters.command("start")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def restart(client,m):
    list = ["🧡","💚","💙","💟","💜","🖤","😻","😍","🤩","😘","😉","🥰","💘","💝","💗","❣️","ɪ","ʟᴏᴠᴇ....🙈","ʏᴏᴜ..🙊🙈","ɪ ʟᴏᴠᴇ ʏᴏᴜ......💫💞"]
    xmsg = await m.reply("❤️")
    for i in list:
     await xmsg.edit(i)
     await asyncio.sleep(0.4)
    umm = await m.reply_sticker(
"CAACAgUAAxkBAAIDG2QhN85PjxC3IZl3hYefSbz_w60-AAI-CQAC5Nr5V3U6V4xWQpckLwQ")
    await umm.delete()