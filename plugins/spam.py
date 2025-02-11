from telethon import events

@events.register(events.NewMessage(pattern=".spam"))
async def spam_handler(event):
    if event.is_private:
        await event.reply("This command only works in groups.")
        return

    if not event.sender.is_admin:
        await event.reply("You need to be an admin to use this command.")
        return

    try:
        count = int(event.text.split()[1])
        message = " ".join(event.text.split()[2:])
        for _ in range(count):
            await event.client.send_message(event.chat_id, message)
    except:
        await event.reply("Usage: .spam <count> <message>")
