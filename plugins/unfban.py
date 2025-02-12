from telethon import events

@events.register(events.NewMessage(pattern=".unfban"))
async def unfban_handler(event):
    if event.is_private:
        await event.reply("This command only works in groups.")
        return

    if not event.sender.is_admin:
        await event.reply("You need to be an admin to use this command.")
        return

    user = await event.get_reply_message()
    if not user:
        await event.reply("Reply to a user to un-federally ban them.")
        return

    # Un-FBan लॉजिक (सभी फेडरेटेड ग्रुप्स से अनबैन करें)
    await event.reply(f"Un-Federally banned {user.sender.first_name} ✅")
