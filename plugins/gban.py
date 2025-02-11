from telethon import events

@events.register(events.NewMessage(pattern=".gban"))
async def gban_handler(event):
    if event.is_private:
        await event.reply("This command only works in groups.")
        return

    if not event.sender.is_admin:
        await event.reply("You need to be an admin to use this command.")
        return

    user = await event.get_reply_message()
    if not user:
        await event.reply("Reply to a user to globally ban them.")
        return

    # GBan लॉजिक (सभी ग्रुप्स से बैन करें)
    await event.reply(f"Globally banned {user.sender.first_name} 🚫")
    # यहां आप अपना GBan लॉजिक जोड़ सकते हैं।
