from SafoneAPI import SafoneAPI
from AarohiX import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
api = SafoneAPI()

@app.on_message(filters.command(["استخراج فيزا", "فيزا"], [".", "!", "/", " "]))
async def gen_cc(client, message):
    if len(message.command) < 2:
        return await message.reply_text("↢ دزلي البين مع الأمر..")

    try:
        await message.delete()
    except:
        pass

    aux = await message.reply_text("جاري الاستخراج ...")
    bin = message.text.split(None, 1)[1]

    if len(bin) < 6:
        return await aux.edit("بين خاطئ...")

    try:
        resp = await api.ccgen(bin, 10)
        cards = resp.liveCC

        regenerate_button = InlineKeyboardButton(
            "إعادة الاستخراج¹", callback_data=f"regenerate_{bin}"
        )
        keyboard = InlineKeyboardMarkup([[regenerate_button]])

        await aux.edit(
            f"""
↢بعض الفيزات المفحوصـة ✅ :

╭✠╼━━━━━━❖━━━━━━━✠╮ 

{cards[0]}\n{cards[1]}\n{cards[2]}
{cards[3]}\n{cards[4]}\n{cards[5]}
{cards[6]}\n{cards[7]}\n{cards[8]}
{cards[9]}\n
╰✠╼━━━━━━❖━━━━━━━✠╯

⦿ البين : `{resp.results[0].bin}`
⦿ مدة الاستخراج : {resp.took}\n\n @Tepthon""",
            reply_markup=keyboard,
        )

    except Exception as e:
        return await aux.edit(f"خطأ: {e}.")

@app.on_callback_query(filters.regex(r"regenerate_"))
async def regenerate_cc(client, callback_query):
    bin_to_regenerate = callback_query.data.split("_")[1]

    try:
        resp = await api.ccgen(bin_to_regenerate, 10)
        cards = resp.liveCC

        await callback_query.edit_message_text(
            f"""
↢بعض الفيزات المفحوصـة ✅ :

╭✠╼━━━━━━❖━━━━━━━✠╮ 

{cards[0]}\n{cards[1]}\n{cards[2]}
{cards[3]}\n{cards[4]}\n{cards[5]}
{cards[6]}\n{cards[7]}\n{cards[8]}
{cards[9]}\n
╰✠╼━━━━━━❖━━━━━━━✠╯

⦿ البين : `{resp.results[0].bin}`
⦿ مدة الاستخراج : {resp.took}\n\n @Tepthon""",
        )

    except Exception as e:
        await callback_query.edit_message_text(f"Error: {e}.")
    
