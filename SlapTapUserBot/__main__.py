# Copyright (c) 2021 Itz-fork
# Part of: Nexa-Userbot
import asyncio

from pyrogram import idle
from nexa_userbot import NEXAUB
from nexa_userbot.modules import *
from nexa_userbot.core.startup_checks import check_or_set_log_channel, check_arq_api


async def main_startup():
    print("""
|| SlapTap Userbot ||

Copyright (c) 2021 InfinityGO
"""
    )
    await NEXAUB.start()
    # Check or set log channel id
    log_channel_id = await check_or_set_log_channel()
    # Check if arq api is available else it'll obtain a one
    await check_arq_api()
    try:
        await NEXAUB.send_message(chat_id=log_channel_id[1], text="`SlapTap Userbot is alive!`")
    except:
        print("WARNING: There was an error while creating the LOG CHANNEL please add a one manually!")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(main_startup())
