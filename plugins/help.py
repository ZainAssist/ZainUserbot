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
    - `.raid`: Start a raid on a user.
    - `.spam`: Spam messages.
    - `.replyraid`: Start a reply raid.
    - `.vcraid`: Start a voice chat raid.
    - `.fakehack`: Fake hack a user.
    - `.gban`: Globally ban a user (Admin only).
    - `.ungban`: Un-globally ban a user (Admin only).
    - `.weather`: Get weather info.
    """
    await event.reply(help_text)
