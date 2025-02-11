from telethon import events

@events.register(events.NewMessage(pattern=".dreplyraid"))
async def dreplyraid_handler(event):
    if event.is_private:
        await event.reply("This command only works in groups.")
        return

    if not event.sender.is_admin:
        await event.reply("You need to be an admin to use this command.")
        return

    user = await event.get_reply_message()
    if not user:
        await event.reply("Reply to a user to start delete reply raid.")
        return

    for _ in range(10):  # 10 रिप्लाई मैसेज भेजेगा और डिलीट करेगा
        msg = await event.client.send_message(event.chat_id, "REPLY RAID! 🔥", reply_to=user.id)
        await msg.delete()
