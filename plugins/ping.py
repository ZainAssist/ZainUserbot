from telethon import events

@events.register(events.NewMessage(pattern=".ping"))
async def ping_handler(event):
    await event.reply("**Pong!** 🏓")
