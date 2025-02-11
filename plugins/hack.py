from telethon import events

@events.register(events.NewMessage(pattern=".hack"))
async def hack_handler(event):
    user = await event.get_reply_message()
    if not user:
        await event.reply("Reply to a user to fake hack them.")
        return

    await event.reply("Hacking... 💻")
    await event.reply("Hack complete! 🔓")
