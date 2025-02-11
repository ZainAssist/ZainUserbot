from telethon import events

@events.register(events.NewMessage(pattern=".clone"))
async def clone_handler(event):
    if event.is_private:
        await event.reply("This command only works in groups.")
        return

    user = await event.get_reply_message()
    if not user:
        await event.reply("Reply to a user to clone their profile.")
        return

    await event.client(UpdateProfileRequest(
        first_name=user.sender.first_name,
        last_name=user.sender.last_name,
        about=user.sender.about
    ))
    await event.reply(f"Cloned {user.sender.first_name}'s profile! 👤")
