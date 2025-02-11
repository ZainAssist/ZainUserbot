from telethon import events

@events.register(events.NewMessage(pattern=".unvcraid"))
async def unvcraid_handler(event):
    if event.is_private:
        await event.reply("This command only works in groups.")
        return

    if not event.sender.is_admin:
        await event.reply("You need to be an admin to use this command.")
        return

    await event.reply("VC RAID STOPPED! 🎤")
    # यहां आप VC Raid रोकने का लॉजिक जोड़ सकते हैं।
