from telethon import events

@events.register(events.NewMessage(pattern=".info"))
async def info_handler(event):
    user = await event.get_sender()
    info_text = f"""
    **User Info:**
    - Name: {user.first_name}
    - Username: {user.username}
    - ID: {user.id}
    """
    await event.reply(info_text)
