from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config

@app.on_message(
    command(["اوامر", "الاوامر"])
)
async def mmmezat(client, message):
    await message.reply_text(
        f"""مرحبًا بك عزيزي {message.from_user.mention} في بوت فهد\nللحصول على الأوامر راسل البوت 🤍.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "للدخول للبوت", url=f"https://t.me/FH4FBot"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- مسح .", callback_data="close"
                    ),
                ],
            ]
        ),
    )

@app.on_message(
    command(["المطور", "السورس", "المصنع"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/3c4a1eb0ceac848e26bc8.jpg",
        caption="• Name Bot ↦ فهد \n ━━━━━━━━━━━━ \n • Dev ↦  مُحمـد 🇵🇸. \n • Bio ↦ أشعر بالفخر لأني مسلم، ولغـتي اللغـة العربيـة 🕌 - @Tepthon ، @PPYNY #فلسطين_حُرة 🇵🇸 .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مُحمـد 🇵🇸", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        " تحديثـات فهد 🇵🇸🤍 .", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )
