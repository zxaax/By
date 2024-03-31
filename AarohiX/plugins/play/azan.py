import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from AarohiX import app
import random
from datetime import datetime
import requests
import pytz
from AarohiX.core.call import Dil
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AarohiX.core.call import Dil
from AarohiX.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
from pyrogram.errors import (
    ChatAdminRequired,
    UserAlreadyParticipant,
    UserNotParticipant,
)

tz = pytz.timezone('Asia/Amman')

chat = []

@app.on_message(filters.text & ~filters.private, group = 20)
async def azaan(c, msg):
  if msg.text == "تفعيل تنبيه الصلاة":
    if msg.chat.id in chat:
      return await msg.reply_text("**⋙ الآذان مفعل من قبـل**")
    else:
      chat.append(msg.chat.id)
      return await msg.reply_text("**⋙ أبشـر فعلت الآذان**")
  elif msg.text == "تعطيل الاذان":
    if msg.chat.id in chat:
      chat.remove(msg.chat.id)
      return await msg.reply_text("**⋙ تم تعطيـل الآذان في هـذه المُحادثـة**")
    else:
      return await msg.reply_text("**⋙ تنبيـه الآذان غير مُفعـل أصـلًا .**")
      
async def kill():
  for i in chat:
    await Anon.force_stop_stream(i)


async def play(i):
  assistant = await group_assistant(Anon,i)
  file_path = "AarohiX/assets/azan.m4a"
  stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
  try:
      await assistant.join_group_call(
           i,
           stream,
           stream_type=StreamType().pulse_stream,
      )
  except NoActiveGroupCall:
    try:
        await Anon.join_assistant(i,i)
    except Exception as e:
       await app.send_message(i,f"{e}")
  except TelegramServerError:
    await app.send_message(i,"خطأ في سيرفرات التليجـرام")
  except AlreadyJoinedError:
    await kill()
    try:
        await assistant.join_group_call(
           i,
           stream,
           stream_type=StreamType().pulse_stream,
        )
    except Exception as e:
        await app.send_message(i,f"{e}")
    
           
       

def prayer_time():
   try:
       prayer = requests.get(f"http://api.aladhan.com/timingsByAddress?address=Amman&method=4&school=0")
       prayer = prayer.json()
       fajr = datetime.strptime(prayer['data']['timings']['Fajr'], '%H:%M').strftime('%H:%M')
       dhuhr = datetime.strptime(prayer['data']['timings']['Dhuhr'], '%H:%M').strftime('%H:%M')
       asr = datetime.strptime(prayer['data']['timings']['Asr'], '%H:%M').strftime('%H:%M')
       maghrib = datetime.strptime(prayer['data']['timings']['Maghrib'], '%H:%M').strftime('%H:%M')
       isha = datetime.strptime(prayer['data']['timings']['Isha'], '%H:%M').strftime('%H:%M')
       if datetime.now(tz).strftime('%H:%M') == fajr:
         return "الفجر"
       elif datetime.now(tz).strftime('%H:%M') == dhuhr:
         return "الظهر"
       elif datetime.now(tz).strftime('%H:%M') == asr:
         return "العصر"
       elif datetime.now(tz).strftime('%H:%M') == maghrib:
         return "المغرب"
       elif datetime.now(tz).strftime('%H:%M') == isha:  
         return "العشاء"
   except Exception as e:
       asyncio.sleep(5)
       print(e)  
#لالالالا
#حقوق_هلال

async def azkar():
  while not await asyncio.sleep(2):
    if prayer_time():
     prayer = prayer_time()
     await kill()
     for i in chat:
       await app.send_message(i, f"**⋙ حـان الآن موعـد آذان {prayer) في الأردن 🕌**")
       await play(i)
     await asyncio.sleep(174)
     await kill()
#@z0hary
     
