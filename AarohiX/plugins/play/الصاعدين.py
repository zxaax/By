from pyrogram import filters, Client
from AarohiX import app
import asyncio
import config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import VideoChatEnded, Message
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AarohiX.core.call import Dil
from AarohiX.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)


@app.on_message(filters.regex("^مين في الكول$"))
async def strcall(client, message):
    assistant = await group_assistant(Dil, message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("https://graph.org/file/217aac5f9cd2b05f7ba5a.mp4"), stream_type=StreamType().pulse_stream)
        text = "~ الموجودين بالكول :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k = 0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut = "~ فاتح المايك "
            else:
                mut = "~ قافل المايك "
            user = await client.get_users(participant.user_id)
            k += 1
            text += f"{k} ~ {user.mention} {mut}\n"
        text += f"\n~ عددهم : {len(participants)}\n️"  

        # إضافة زر شفاف في الأسفل
        inline_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("- قناة البوت . ", url=config.SUPPORT_CHAT)],
        ])      

        await message.reply(f"{text}", reply_markup=inline_keyboard)
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"- ماكو شي مشتغل")
    except TelegramServerError:
        await message.reply(f"- حدث خطأ.")
    except AlreadyJoinedError:
        text = "~ الصاعدين :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k = 0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut = "~ جاي يمسلت "
            else:
                mut = "~ ساد المايك "
            user = await client.get_users(participant.user_id)
            k += 1
            text += f"{k} ~ {user.mention} {mut}\n"
        text += f"\n~ عددهم : {len(participants)}\n️"

        # إضافة زر شفاف في الأسفل
        inline_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("- قناة البوت . ", url=config.SUPPORT_CHAT)],
        ])
        await message.reply(f"{text}", reply_markup=inline_keyboard)



@app.on_message(command(['ز','زوجني']))
def iddd(client:Client, message:Message):
    chat_id = message.chat.id
    if chat_id in iddof:
         return
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}]( tg://openmessage?user_id={random_member.user.id} )"
    random_message = random.choice([
        f"• اخترت لك هذا الشخص \n {random_member_mention} \n 🙈♥️",
        f"• اخترت لك هذا الشخص \n {random_member_mention} \n **"
    ])
