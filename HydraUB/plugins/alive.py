"""
This Telegram Userbot is provided "as is" without warranty of any kind, either express or implied. The author(s) and/or distributor(s) of this Userbot shall not be liable for any damages arising from the use of this Userbot.

By using this Userbot, you agree to the terms and conditions set forth in this license. If you do not agree to these terms and conditions, do not use this Userbot.

This Userbot may be used by anyone, provided that credit is given to Hyper Speed™.

The author(s) and/or distributor(s) reserve the right to modify or discontinue this Userbot at any time without notice.

All rights reserved to Hyper Speed™.
"""
import time 
import random 
import asyncio
from config import HANDLER, OWNER_ID, HS
from pyrogram import filters, __version__ as pyrover
from HydraUB import get_readable_time, StartTime
from HydraUB import Hydra as HS




@HS.on_message(filters.command("alive",prefixes=HANDLER) & filters.user("5965055071"))
async def alive(_, message):
    name = (await HS.get_me()).first_name
    await message.edit("Lᴏᴀᴅɪɴɢ HʏᴅʀᴀUB")
    await asyncio.sleep(3)
    await message.delete()
    alive = await message.reply_animation(HS, caption="")
    await alive.edit_caption(f"Hello Master **{name}**,\nYou Are Using HydraUserBot V-7 And Your Current Pyrogram Version Is {pyrover}!")


@HS.on_message(filters.command("ping",prefixes=HANDLER) & filters.user(OWNER_ID))
async def ping(_, message):
     start_time = time.time()
     end_time = time.time()
     ping_time = round((end_time - start_time) * 1000, 3)
     uptime = get_readable_time((time.time() - StartTime))
     await message.edit(f"👾 **System Uptime & Ping**\n=> 🔔 **Ping**: {ping_time}\n=> ⬆️ **Uptime**: {uptime}")

