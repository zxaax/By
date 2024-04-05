from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AarohiX import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/Tepthon":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("Tepthon", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/Tepthon".isalpha():
                link = "https://t.me/Tepthon"
            else:
                chat_info = await bot.get_chat("Tepthon")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙عذرًا عزيزي ↫ {msg.from_user.mention} \n⌯︙عـليك الاشـتࢪاك في قنـاة البـوت أولًا\n⌯︙قناة البوت : @Tepthon .\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("تحديثات فهد 🇵🇸", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat @Tepthon !")
      
