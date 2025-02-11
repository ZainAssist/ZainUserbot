from telethon import events

@events.register(events.NewMessage(pattern=".help"))
async def help_handler(event):
    help_text = """
    **ZainUserBot Commands:**
    - `.ping`: Check bot's ping.
    - `.welcome`: Welcomes new users.
    - `.help`: Show this help message.
    - `.info`: Get user info.
    - `.ban`: Ban a user (Admin only).
    - `.mute`: Mute a user (Admin only).
    - `.unban`: Unban a user (Admin only).
    - `.purge`: Delete messages (Admin only).
    - `.afk`: Set AFK status.
    - `.weather`: Get weather info.
    """
    await event.reply(help_text)
