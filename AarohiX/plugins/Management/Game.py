from pyrogram import Client, enums, filters
import asyncio
from AarohiX import app

from pyrogram.handlers import MessageHandler


@app.on_message(filters.command("حجر النرد"))
async def dice(bot, message):
    x=await bot.send_dice(message.chat.id)
    m=x.dice.value
    await message.reply_text(f"مرحبًـا 👋 {message.from_user.mention} مستواك هو : {m}",quote=True)
  
@app.on_message(filters.command("سهم"))
async def dart(bot, message):
    x=await bot.send_dice(message.chat.id, "🎯")
    m=x.dice.value
    await message.reply_text(f"مرحبًـا 👋 {message.from_user.mention} مستواك هو : {m}",quote=True)

@app.on_message(filters.command("باسكت_بول"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🏀")
    m=x.dice.value
    await message.reply_text(f"مرحبًـا 👋 {message.from_user.mention} مستواك هو : {m}",quote=True)
@app.on_message(filters.command("الفوز_بالجائزة_الكبرى"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎰")
    m=x.dice.value
    await message.reply_text(f"مرحبًـا 👋 {message.from_user.mention} مستواك هو : {m}",quote=True)
@app.on_message(filters.command("بولنج"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎳")
    m=x.dice.value
    await message.reply_text(f"مرحبًـا 👋 {message.from_user.mention} مستواك هو : {m}",quote=True)
@app.on_message(filters.command("كرة_القدم"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "⚽")
    m=x.dice.value
    await message.reply_text(f"مرحبًـا 👋 {message.from_user.mention} مستواك هو : {m}",quote=True)
__help__ = """
 ↢الألعاب مع الإيموجيات
/حجر النرد - Dice 🎲
/سهم - Dart 🎯
/باسكت_بول - Basket Ball 🏀
/بولنج - Bowling Ball 🎳
/بولنج القدم - Football ⚽
/الفوز_بالجائزة_الكبرى - Spin slot machine 🎰
 """

__mod_name__ = "Dɪᴄᴇ"
