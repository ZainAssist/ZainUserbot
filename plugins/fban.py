from telethon import events

@events.register(events.NewMessage(pattern=".fban"))
async def fban_handler(event):
    if event.is_private:
        await event.reply("This command only works in groups.")
        return

    if not event.sender.is_admin:
        await event.reply("You need to be an admin to use this command.")
        return

    user = await event.get_reply_message()
    if not user:
        await event.reply("Reply to a user to federally ban them.")
        return

    # FBan लॉजिक (सभी फेडरेटेड ग्रुप्स से बैन करें)
    await event.reply(f"Federally banned {user.sender.first_name} 🚫")
    # यहां आप अपना FBan लॉजिक जोड़ सकते हैं।
