import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from AarohiX import app

# ------------------------------------------------------------------------------- #

chatQueue = []

stopProcess = False

# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["مسح الحسابات المحذوفة","تنظيف"]))
async def remove(client, message):
  global stopProcess
  try: 
    try:
      sender = await app.get_chat_member(message.chat.id, message.from_user.id)
      has_permissions = sender.privileges
    except:
      has_permissions = message.sender_chat  
    if has_permissions:
      bot = await app.get_chat_member(message.chat.id, "self")
      if bot.status == ChatMemberStatus.MEMBER:
        await message.reply("**↢ كيف أمسح الحسابات المحذوفة وما معي صلاحية حظر الأعضاء؟")  
      else:  
        if len(chatQueue) > 30 :
          await message.reply("↢ أنا مستعد للعمل، عيد المحاولة.")
        else:  
          if message.chat.id in chatQueue:
            await message.reply("↢ التنظيف يجري بالفعل..")
          else:  
            chatQueue.append(message.chat.id)  
            deletedList = []
            async for member in app.get_chat_members(message.chat.id):
              if member.user.is_deleted == True:
                deletedList.append(member.user)
              else:
                pass
            lenDeletedList = len(deletedList)  
            if lenDeletedList == 0:
              await message.reply("↢ما فيه حسابات محذوفة.")
              chatQueue.remove(message.chat.id)
            else:
              k = 0
              processTime = lenDeletedList*1
              temp = await app.send_message(message.chat.id, f"↢ عدد الحسابات المحذوفة {lenDeletedList} تم إزالة جميع الحسابات المحذوفة\n↢ الوقت المُستغرق : {processTime} ثانية.")
              if stopProcess: stopProcess = False
              while len(deletedList) > 0 and not stopProcess:   
                deletedAccount = deletedList.pop(0)
                try:
                  await app.ban_chat_member(message.chat.id, deletedAccount.id)
                except Exception:
                  pass  
                k+=1
                await asyncio.sleep(10)
              if k == lenDeletedList:  
                await message.reply(f"**↢ تم حذف الحسابات المحذوفة.")  
                await temp.delete()
              else:
                await message.reply(f"↢ تم حذف {k} حساب محذوف من هذه المجموعة")  
                await temp.delete()  
              chatQueue.remove(message.chat.id)
    else:
      await message.reply("↢ ما يمديك تستخدم هالأمر أنت مو مُشرف")  
  except FloodWait as e:
    await asyncio.sleep(e.value)                               
        

# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["الادمنية","الأدمنية"]))
async def admins(client, message):
  try: 
    adminList = []
    ownerList = []
    async for admin in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
      if admin.privileges.is_anonymous == False:
        if admin.user.is_bot == True:
          pass
        elif admin.status == ChatMemberStatus.OWNER:
          ownerList.append(admin.user)
        else:  
          adminList.append(admin.user)
      else:
        pass   
    lenAdminList= len(ownerList) + len(adminList)  
    text2 = f"**ɢʀᴏᴜᴘ sᴛᴀғғ - {message.chat.title}**\n\n"
    try:
      owner = ownerList[0]
      if owner.username == None:
        text2 += f"↢ المالك\n└ {owner.mention}\n\n↢ الأدمنية\n"
      else:
        text2 += f"↢ المالك\n└ @{owner.username}\n\n↢ الأدمنية\n"
    except:
      text2 += f"↢المالك\n└ <i>Hidden</i>\n\n↢ الأدمنية\n"
    if len(adminList) == 0:
      text2 += "└ <i>↢المشرفين المخفيين</i>"  
      await app.send_message(message.chat.id, text2)   
    else:  
      while len(adminList) > 1:
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"├ {admin.mention}\n"
        else:
          text2 += f"├ @{admin.username}\n"    
      else:    
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"└ {admin.mention}\n\n"
        else:
          text2 += f"└ @{admin.username}\n\n"
      text2 += f"↢ عدد الأدمنيـة**: {lenAdminList}"  
      await app.send_message(message.chat.id, text2)           
  except FloodWait as e:
    await asyncio.sleep(e.value)       

# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("البوتات"))
async def bots(client, message):  
  try:    
    botList = []
    async for bot in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BOTS):
      botList.append(bot.user)
    lenBotList = len(botList) 
    text3  = f"**↢ قائمة البوتات - {message.chat.title}**\n\n↢ البوتات\n"
    while len(botList) > 1:
      bot = botList.pop(0)
      text3 += f"├ @{bot.username}\n"    
    else:    
      bot = botList.pop(0)
      text3 += f"└ @{bot.username}\n\n"
      text3 += f"↢ عدد البوتات : {lenBotList}"  
      await app.send_message(message.chat.id, text3)
  except FloodWait as e:
    await asyncio.sleep(e.value)
    
# ------------------------------------------------------------------------------- #
