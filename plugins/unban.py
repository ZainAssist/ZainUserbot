from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

@events.register(events.NewMessage(pattern=".unban"))
async def unban_handler(event):
    if event.is_group:
        if event.sender.is_admin:
            user = await event.get_reply_message()
            if user:
                banned_rights = ChatBannedRights(
                    until_date=None,
                    send_messages=False,
                )
                await event.client(EditBannedRequest(event.chat_id, user.sender_id, banned_rights))
                await event.reply(f"{user.sender.first_name} has been unbanned. ✅")
            else:
                await event.reply("Reply to a user to unban them.")
        else:
            await event.reply("You need to be an admin to use this command.")
    else:
        await event.reply("This command only works in groups.")
