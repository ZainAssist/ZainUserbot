@events.register(events.NewMessage(pattern=".purge"))
async def purge_handler(event):
    if event.is_group:
        if event.sender.is_admin:
            reply_msg = await event.get_reply_message()
            if reply_msg:
                await event.client.delete_messages(event.chat_id, list(range(reply_msg.id, event.id + 1)))
                await event.reply("Messages purged successfully. 🗑️")
            else:
                await event.reply("Reply to a message to start purging.")
        else:
            await event.reply("You need to be an admin to use this command.")
    else:
        await event.reply("This command only works in groups.")
