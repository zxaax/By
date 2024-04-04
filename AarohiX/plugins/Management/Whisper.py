from AarohiX import app as bot
from config import BOT_USERNAME
from pyrogram import filters
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton
)

whisper_db = {}

switch_btn = InlineKeyboardMarkup([[InlineKeyboardButton("ابدأ بالهمس", switch_inline_query_current_chat="")]])

async def _whisper(_, inline_query):
    data = inline_query.query
    results = []
    
    if len(data.split()) < 2:
        mm = [
            InlineQueryResultArticle(
                title="↢ همسـة",
                description=f"@{BOT_USERNAME} [ USERNAME | ID ] [ TEXT ]",
                input_message_content=InputTextMessageContent(f"↢ الاستخدام :\n\n@{BOT_USERNAME} [ الاسم المستخدم | الأيدي ] [ النص ]"),
                thumb_url="https://te.legra.ph/file/70872d57cab08aa096a04.jpg",
                reply_markup=switch_btn
            )
        ]
    else:
        try:
            user_id = data.split()[0]
            msg = data.split(None, 1)[1]
            user = await _.get_users(user_id)
            
            whisper_btn = InlineKeyboardMarkup([[InlineKeyboardButton("❥ Wʜɪsᴘᴇʀ", callback_data=f"fdaywhisper_{inline_query.from_user.id}_{user.id}")]])
            one_time_whisper_btn = InlineKeyboardMarkup([[InlineKeyboardButton("☞ Oɴᴇ-Tɪᴍᴇ Wʜɪsᴘᴇʀ", callback_data=f"fdaywhisper_{inline_query.from_user.id}_{user.id}_one")]])
            
            mm = [
                InlineQueryResultArticle(
                    title="همسـة",
                    description=f" {user.first_name}!",
                    input_message_content=InputTextMessageContent(f"↢أرسلت همسة لـ {user.first_name}.\n\n اكتب رسالتك/Sᴇɴᴛᴇɴᴄᴇ."),
                    thumb_url="https://te.legra.ph/file/70872d57cab08aa096a04.jpg",
                    reply_markup=whisper_btn
                ),
                InlineQueryResultArticle(
                    title="➤ Oɴᴇ-Tɪᴍᴇ Wʜɪsᴘᴇʀ",
                    description=f"Sᴇɴᴅ A Oɴᴇ-Tɪᴍᴇ Wʜɪsᴘᴇʀ Tᴏ {user.first_name}!",
                    input_message_content=InputTextMessageContent(f"☞ Yᴏᴜ Aʀᴇ Sᴇɴᴅɪɴɢ A Oɴᴇ-Tɪᴍᴇ Wʜɪsᴘᴇʀ Tᴏ {user.first_name}.\n\nTʏᴘᴇ Uʀ Mᴇssᴀɢᴇ/Sᴇɴᴇᴛᴇɴᴄᴇ."),
                    thumb_url="https://te.legra.ph/file/70872d57cab08aa096a04.jpg",
                    reply_markup=one_time_whisper_btn
                )
            ]
            
            whisper_db[f"{inline_query.from_user.id}_{user.id}"] = msg
        except Exception as e:
            mm = [
                InlineQueryResultArticle(
                    title="⦿ Wʜɪsᴘᴇʀ ⦿",
                    description="Iɴᴠᴀʟɪᴅ Usᴇʀɴᴀᴍᴇ ᴏʀ Iᴅ!",
                    input_message_content=InputTextMessageContent("معرف أو أيدي غير صالح!"),
                    thumb_url="https://te.legra.ph/file/70872d57cab08aa096a04.jpg",
                    reply_markup=switch_btn
                )
            ]
    
    results.append(mm)
    return results



@bot.on_callback_query(filters.regex(pattern=r"همسة_(.*)"))
async def whispes_cb(_, query):
    data = query.data.split("_")
    from_user = int(data[1])
    to_user = int(data[2])
    user_id = query.from_user.id
    
    if user_id not in [from_user, to_user, 5465943450]:
        try:
            await _.send_message(from_user, f"{query.from_user.mention} Is Tʀʏɪɴɢ Tᴏ Oᴘᴇɴ Uʀ Wʜɪsᴘᴇʀ.")
        except Unauthorized:
            pass
        
        return await query.answer("الهمسة ليست لك 𖣘︎", show_alert=True)
    
    search_msg = f"{from_user}_{to_user}"
    
    try:
        msg = whisper_db[search_msg]
    except:
        msg = "𖣘︎ خطأ!\n\nهمستك محذوفة من قاعدة البيانات!"
    
    SWITCH = InlineKeyboardMarkup([[InlineKeyboardButton("Gᴏ Iɴʟɪɴᴇ ➻", switch_inline_query_current_chat="")]])
    
    await query.answer(msg, show_alert=True)
    
    if len(data) > 3 and data[3] == "one":
        if user_id == to_user:
            await query.edit_message_text("➤ تمت قراءة الهمسة!\n\nاضغط على الزر أدناه لإرسال همسة!", reply_markup=SWITCH)


async def in_help():
    answers = [
        InlineQueryResultArticle(
            title="⦿ همسـة ⦿",
            description=f"@Alone_Dil_bot [USERNAME | ID] [TEXT]",
            input_message_content=InputTextMessageContent(f"**الاستخدام :**\n\n@Alone_Dil_bot (Target Username or ID) (Your Message).\n\n**Example:**\n@Alone_Dil_bot @username I Wanna Phuck You"),
            thumb_url="https://te.legra.ph/file/70872d57cab08aa096a04.jpg",
            reply_markup=switch_btn
        )
    ]
    return answers


@bot.on_inline_query()
async def bot_inline(_, inline_query):
    string = inline_query.query.lower()
    
    if string.strip() == "":
        answers = await in_help()
        await inline_query.answer(answers)
    else:
        answers = await _whisper(_, inline_query)
        await inline_query.answer(answers[-1], cache_time=0)
                                               
