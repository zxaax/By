from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
import re
from AarohiX  import app as bot

mongo_url_pattern = re.compile(r'mongodb(?:\+srv)?:\/\/[^\s]+')


@bot.on_message(filters.command("فحص المونجو"))
async def mongo_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply("**↢ استخدم الأمر بشكل صحيح يا حلو")
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            # Attempt to connect to the MongoDB instance
            client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            client.server_info()  # Will cause an exception if connection fails
            await message.reply("⋙ هـذا المونجـو صالـح يمديك تستخدمه")
        except Exception as e:
            await message.reply(f"فشل في الاتصال: {e}")
    else:
        await message.reply("ما يمديك تستخدم الكود هذا")
