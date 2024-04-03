import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["","اوامري"])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/e0e39b327dac30ee715dc.jpg",
        caption=f"""**- أوامر التشغيل اتبع مايلي
        
 [— — — — — — — — — —](https://te.legra.ph/file/e0e39b327dac30ee715dc.jpg)
◇︰ تشغيل أو شغل : لبدء تشغيل السورة أو الأنشودة الإسلامية

◇︰ بينج : لقياس سرعة النت في البوت .

◇︰ كتم : لكتم السورة أو الأنشودة

◇︰ الغاء كتم : لإلغاء كتم السورة أو الأنشودة

◇︰ تخطي : لتخطي السورة أو الأنشودة الحالية .

◇︰ ايقاف : لإيقاف تشغيل السورة أو الأنشودة الحالية .**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/Tepthon"),
                    InlineKeyboardButton(
                        "‹ الدعم ›", url=f"https://t.me/Tepthon_Help"),
                ],
                [
                   InlineKeyboardButton(
                        "‹ المطور ›", url=f"https://t.me/PPF22"),
                ],       
            ]
        ),
    )

@app.on_message(
    command(["","اوامر التفعيل"])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/e0e39b327dac30ee715dc.jpg",
        caption=f"""**
- أوامر التفعيل اتبع ما يلي :

— — — — — — — — — —

↫ أضف البوت إلى مجموعتك
↫ ارفعه مُشرِفًا
↫ سيتم انضمام الحساب المساعد تلقائيًا
↫ أرسل تشغيل + اسم السورة أو الأنشودة
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/Tepthon"),
                    InlineKeyboardButton(
                        "‹ الدعم ›", url=f"https://t.me/Tepthon_Help"),
                ],
                [
                   InlineKeyboardButton(
                        "‹ المطور ›", url=f"https://t.me/PPF22"),
                ],       
            ]
        ),
    )

@app.on_message(
    command(["","اوامر اضافية"])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/e0e39b327dac30ee715dc.jpg",
        caption=f"""**
-  أوامر إضافيـة :
 — — — — — — — — — — 

- ( فيلم ) فيلم كامل عشوائي

- ( متحركة ) متحركات عشوائيه مميزة

- ( اقتباسات ) اقتباس بالصورة جميل

- ( اسمي ) لعرض اسمك الكامل

- ( ايدي ) لعرض معلوماتك

- ( تاك ) لعمل تاك جماعي في المجموعة

- لو خيروك ↫ لعبة لو خيروك

- كت تويت ↫ لعبة كت تويت عشوائي 

- ذكاء اصطناعي ↫ اكتب ذكاء اصطناعي + سؤالك 

- سكرين ↫ /سكرين + الرابط

- وضع وصف ↫ لوضع وصف للمجموعة بالرد

- وضع صورة ↫ لوضع صورة للمجموعة بالرد

- وضع اسم ↫ لوضع اسم للمجموعة بالرد

- تلاوات ↫ لسماع آيات من القرآن الكريم

- حظر ↫ لحظر العضو بالرد

- كتم ↫ لكتم العضو بالرد

- صورة ↫ لجلب صورة عشوائية

- فحص مونجو ↫ فحص كود المونجو 

- تلجراف ميديا ↢ لجلب رابط الصورة .

— — — — — — — — — — — — — —**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/Tepthon"),
                    InlineKeyboardButton(
                        "‹ الدعم ›", url=f"https://t.me/Tepthon_Help"),
                ],
                [
                   InlineKeyboardButton(
                        "‹ المطور ›", url=f"https://t.me/PPF22"),
                ],       
            ]
        ),
    )
