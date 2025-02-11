from telethon import events

AFK = False
AFK_REASON = ""

@events.register(events.NewMessage(pattern=".afk"))
async def afk_handler(event):
    global AFK, AFK_REASON
    AFK = True
    AFK_REASON = " ".join(event.text.split()[1:])
    await event.reply(f"I'm AFK now. Reason: {AFK_REASON} 🏃")

@events.register(events.NewMessage(incoming=True))
async def afk_listener(event):
    global AFK, AFK_REASON
    if AFK and event.is_private:
        await event.reply(f"I'm AFK. Reason: {AFK_REASON} 🏃")
