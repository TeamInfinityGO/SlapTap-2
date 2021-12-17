# Copyright (c) 2021 InfinityGo
# Part of:SlapTap UserBot

import asyncio
import tgcrypto
from pyrogram import Client

print("""
|| SlapTap Userbot ||

Copyright (c) 2021 InfinityGO
""")

async def pyro_str():
    print("\nPlease Enter All Required Values to Generate Pyrogram String Session for your Account! \n")
    api_id = int(input("Enter Your APP ID: "))
    api_hash = input("Enter Your API HASH: ")
    async with Client(":memory:", api_id, api_hash) as NEXAUB:
        pyro_session = await NEXAUB.export_session_string()
        session_msg = await NEXAUB.send_message("me", f"`{pyro_session}`")
        await session_msg.reply_text("Successfully Generated String Session! Thanks for trying [SlapTap Userbot](https://github.com/TeamInfinityGO/SlapTap-2) \n\n**Join @SlapTap**", disable_web_page_preview=True)
        print("\nString Session has been sent to your saved messages. Please check it. Thank You!\n")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(pyro_str())
