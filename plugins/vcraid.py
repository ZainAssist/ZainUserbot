from telethon import events

@events.register(events.NewMessage(pattern=".vcraid"))
async def vcraid_handler(event):
    if event.is_private:
        await event.reply("This command only works in groups.")
        return

    if not event.sender.is_admin:
        await event.reply("You need to be an admin to use this command.")
        return

    await event.client.send_message(event.chat_id, "VC RAID STARTED! 🎤")
    for _ in range(5):  # 5 वॉइस मैसेज भेजेगा
        await event.client.send_file(event.chat_id, "voice_note.mp3")
