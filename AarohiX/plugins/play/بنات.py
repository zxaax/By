import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AarohiX import app
import random
    

@app.on_message(command([f"رمزيات بنات", "صور"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/photo_teto1/{rl}"
    await client.send_voice(message.chat.id,url,caption="♪ 𝗝𝗢𝗜𝗡 ➧ @WX_PM  💎 .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/WX_PM")
                ],
            ]
        )
    )
