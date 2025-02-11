from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

@events.register(events.NewMessage(pattern=".mute"))
async def mute_handler(event):
    if event.is_group:
        if event.sender.is_admin:
            user = await event.get_reply_message()
            if user:
                banned_rights = ChatBannedRights(
                    until_date=None,
                    send_messages=True,
                )
                await event.client(EditBannedRequest(event.chat_id, user.sender_id, banned_rights))
                await event.reply(f"{user.sender.first_name} has been muted. 🔇")
            else:
                await event.reply("Reply to a user to mute them.")
        else:
            await event.reply("You need to be an admin to use this command.")
    else:
        await event.reply("This command only works in groups.")
