from telethon import events

@events.register(events.ChatAction)
async def welcome_handler(event):
    if event.user_joined:
        await event.reply(f"**Welcome to the group, {event.user.first_name}!** 👋")
