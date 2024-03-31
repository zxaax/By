import requests
import random
from AarohiX import app
from AarohiX.misc import SUDOERS
from pyrogram import *
from pyrogram.types import *
from pyrogram.types import Message
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram import filters


#<<<<<<<<<<<<<AdminXFilter>>>>>>>>>>>>>#     

async def admin_filter_f(filt, client, message):
    return (
        not message.edit_date
        and await admin_check(message)
    )

admin_filter = filters.create(func=admin_filter_f, name="AdminFilter")

async def admin_check(message: Message) -> bool:
    if not message.from_user:
        return False

    if message.chat.type not in [ChatType.SUPERGROUP, ChatType.CHANNEL]:
        return False

    if message.from_user.id in [
        777000,
        1087968824,
    ]:
        return True

    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    check_status = await client.get_chat_member(chat_id=chat_id, user_id=user_id)
    if check_status.status not in [
        ChatMemberStatus.OWNER,
        ChatMemberStatus.ADMINISTRATOR
    ]:
        return False
    else:
        return True


#<<<<<<<<<<<<<AdminXFilter>>>>>>>>>>>>>#     


Adisa_text = [
    "وخر من هنا.",
    "شتبي؟",
    "هلا",
    "لبيه",
    "أطلق من يناديني",
    "مشغول",
    "كم مرة قلت لك مشغول؟",
    "✨🕊️ هلا وغلا",
    "لبيـه 🤍",
    "هلا فيك",
    "كم مرة ناديتني؟",
]

strict_txt = [
    "لا أستطيع أن أقيد ضد أعزائي",
    "are you serious i am not restrict to my friends",
    "fuck you bsdk k mai apne dosto ko kyu kru",
    "hey stupid admin ",
    "ha ye phele krlo maar lo ek dusre ki gwaand",
    "i can't hi is my closest friend",
    "i love him please don't restict this user try to usertand ",
]

ban = ["حظر", "boom"]
unban = ["الغاء الحظر",]
mute = ["كتم", "silent", "shut"]
unmute = ["الغاء الكتم", "speak", "free"]
kick = ["طرد", "out", "nikaal", "nikal"]
promote = ["رفع مشرف", "رفع رئيس"]
demote = ["تنزيل مشرف", "lelo"]
group = ["المجموعة"]
channel = ["القناة"]

# ========================================= #

@app.on_message(filters.command(["فهد", "فهود"], prefixes=["a", "A"]) & admin_filter)
async def restriction_app(app: app, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    if len(message.text) < 2:
        return await message.reply(random.choice(Adisa_text))
    bruh = message.text.split(maxsplit=1)[1]
    data = bruh.split(" ")

    if reply:
        user_id = reply.from_user.id
        for banned in data:
            print(f"أبشر {banned}")
            if banned in ban:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await message.reply("OK, Ban kar diya madrchod ko sala Chutiya tha !")

        for unbanned in data:
            print(f"أبشر {unbanned}")
            if unbanned in unban:
                await app.unban_chat_member(chat_id, user_id)
                await message.reply(f"Ok, aap bolte hai to unban kar diya")

        for kicked in data:
            print(f"present {kicked}")
            if kicked in kick:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await app.unban_chat_member(chat_id, user_id)
                    await message.reply("get lost! bhga diya bhosdi wale ko")

        for muted in data:
            print(f"present {muted}")
            if muted in mute:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                else:
                    permissions = ChatPermissions(can_send_messages=False)
                    await message.chat.restrict_member(user_id, permissions)
                    await message.reply(f"muted successfully! Disgusting people.")

        for unmuted in data:
            print(f"present {unmuted}")
            if unmuted in unmute:
                permissions = ChatPermissions(can_send_messages=True)
                await message.chat.restrict_member(user_id, permissions)
                await message.reply(f"هاه، حسنًا يا سيدي!")

        for promoted in data:
            print(f"present {promoted}")
            if promoted in promote:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=False,
                    can_pin_messages=True,
                    can_promote_members=False,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                ))
                await message.reply("↢ أبشر رفعته مُشرف .")

        for demoted in data:
            print(f"present {demoted}")
            if demoted in demote:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=False,
                    can_delete_messages=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=False,
                    can_manage_video_chats=False,
                ))
                await message.reply("↢ أبشر نزلته من الإشراف .")
