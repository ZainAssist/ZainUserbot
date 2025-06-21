from .. import SUDOERS
from pyrogram.types import *
from traceback import format_exc
from typing import Callable


def sudo_user_only(func: Callable) -> Callable:
    async def decorator(client, message: Message):
        if message.from_user.id in SUDOERS:
            return await func(client, message)
        
    return decorator


def cb_wrapper(func):
    async def wrapper(bot, cb):
        from .. import bot
        users = SUDOERS
        if cb.from_user.id not in users:
            await cb.answer(
                "❎ You Are Not A Sudo User❗",
                cache_time=0,
                show_alert=True,
            )
        else:
            try:
                await func(bot, cb)
            except Exception:
                print(format_exc())
                await cb.answer(
                    f"❎ Something Went Wrong, Please Check Logs❗..."
                )

    return wrapper


def inline_wrapper(func):
    async def wrapper(bot, query):
        from .. import bot
        users = SUDOERS
        if query.from_user.id not in users:
            try:
                button = [
                    [
                        InlineKeyboardButton(
                            "💥 Deploy Zain Userbot ✨",
                            url=f"https://github.com/ZainAssist/ZainUserbot"
                        )
                    ]
                ]
                await bot.answer_inline_query(
                    query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultPhoto(
                                photo_url=f"https://envs.sh/ElG.jpg",
                                title="🥀 Zain Userbot ✨",
                                thumb_url=f"https://envs.sh/ElG.jpg",
                                description=f"🌷 Deploy Your Own ZainUserbot 🌿...",
                                caption=f"<b>🥀 Welcome › To › Zain 🌷\n✅ Userbot v2.0 ✨...</b>",
                                reply_markup=InlineKeyboardMarkup(button),
                            )
                        )
                    ],
                )
            except Exception as e:
                print(str(e))
                await bot.answer_inline_query(
                    query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultArticle(
                                title="",
                                input_message_content=InputTextMessageContent(
                                    f"||**🥀 Please, Deploy Your Own Zain Userbot❗...\n\nRepo:** <i>https://github.com/ZainAssist/ZainUserbot/</i>||"
                                ),
                            )
                        )
                    ],
                )
            except Exception as e:
                print(str(e))
                pass
        else:
           return await func(bot, query)

    return wrapper
