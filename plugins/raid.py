from telethon import events

@events.register(events.NewMessage(pattern=".raid"))
async def raid_handler(event):
    if event.is_private:
        await event.reply("This command only works in groups.")
        return

    if not event.sender.is_admin:
        await event.reply("You need to be an admin to use this command.")
        return

    user = await event.get_reply_message()
    if not user:
        await event.reply("Reply to a user to start raid.")
        return

    for _ in range(10):  # 10 मैसेज भेजेगा
        await event.client.send_message(event.chat_id, f"RAID! {user.sender.first_name} 🚀")
