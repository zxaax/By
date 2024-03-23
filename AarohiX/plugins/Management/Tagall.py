import asyncio
from pyrogram.enums import ChatType, ChatMemberStatus
from AarohiX import app
from pyrogram import filters
from AarohiX.utils.admin_check import admin_filter



SPAM_CHATS = []


@app.on_message(filters.command("تاج",prefixes="")) & filters.group & admin_filter)
async def tag_all_users(_,message): 
    replied = message.reply_to_message  
    if len(message.command) < 2 and not replied:
        await message.reply_text("**قم بالرد على رسالة أو اعمل ريبلي للنص**") 
        return                  
    if replied:
        SPAM_CHATS.append(message.chat.id)      
        usernum= 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id): 
            if message.chat.id not in SPAM_CHATS:
                break       
            usernum += 5
            usertxt += f" [{m.user.first_name}](tg://user?id={m.user.id})"
            if usernum == 1:
                await replied.reply_text(usertxt)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try :
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]
        
        SPAM_CHATS.append(message.chat.id)
        usernum= 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):       
            if message.chat.id not in SPAM_CHATS:
                break 
            usernum += 1
            usertxt += f" [{m.user.first_name}](tg://user?id={m.user.id})"
            if usernum == 5:
                await app.send_message(message.chat.id,f'{text}\n{usertxt}')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""                          
        try :
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass        
           
@app.on_message(filters.command("تعطيل التاج",prefixes="")) & ~filters.private)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try :
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass   
        return await message.reply_text("**تم ايقاف التاج بنجاح ✅**")     
                                     
    else :
        await message.reply_text("**تم الانتهاء بالفعل 🤸‍♂️.**")  
        return       
