from telethon import events

@events.register(events.NewMessage(pattern=".ban"))
async def ban_handler(event):
    if event.is_group:
        if event.sender.is_admin:
            user = await event.get_reply_message()
            if user:
                await event.client.kick_participant(event.chat_id, user.sender_id)
                await event.reply(f"{user.sender.first_name} has been banned. 🚫")
            else:
                await event.reply("Reply to a user to ban them.")
        else:
            await event.reply("You need to be an admin to use this command.")
    else:
        await event.reply("This command only works in groups.")
