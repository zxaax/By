from SafoneAPI import SafoneAPI
from pyrogram import *
from pyrogram.types import *
from AarohiX import app

api = SafoneAPI()

@app.on_message(filters.command(["bin", "ccbin", "bininfo"], [".", "!", "/"]))
async def check_ccbin(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "<b>↢ وين البين كيف أجيبلك معلوماته وما أعرف شو البين؟</b>"
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("<b>جاري التحقق ...</b>")
    bin = message.text.split(None, 1)[1]
    if len(bin) < 6:
        return await aux.edit("<b>❌ بين خاطئ❗...</b>")
    try:
        resp = await api.bininfo(bin)
        await aux.edit(f"""
<b> صالح ✃ </b>

<b>🏦 ʙᴀɴᴋ➪</b> <tt>{resp.bank}</tt>
<b>💳 ʙɪɴ➪</b> <tt>{resp.bin}</tt>
<b>🏡 ᴄɴ➪</b> <tt>{resp.country}</tt>
<b>🌐 ғʟᴀɢ➪</b> <tt>{resp.flag}</tt>
<b>🧿 ɪsᴏ➪</b> <tt>{resp.iso}</tt>
<b>⏳ ʟᴇᴠᴇʟ➪</b> <tt>{resp.level}</tt>
<b>🔴 ᴘʀᴇᴘᴀɪᴅ➪</b> <tt>{resp.prepaid}</tt>
<b>🆔 ᴛʏᴘᴇ➪</b> <tt>{resp.type}</tt>
<b>ℹ️ ᴠᴇɴᴅᴏʀ➪</b> <tt>{resp.vendor}</tt>"""
        )
    except:
        return await aux.edit(f"""
🚫 لم يتم التعرف على بن. الرجاء إدخال رقم تعريف شخصي صالح.""")
