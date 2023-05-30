from pyrogram import Client, filters
import time
from HydraUB import Hydra as HS

@HS.on_message(filters.command("hack", prefixes="."))
def hack(client, message):
    animation_interval = 3
    animation_chars = [
        "`Connecting To Hacked Private Server...`",
        "`Target Selected.`",
        "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
        "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Hacking... 84%\n█████████████████████▒▒▒▒ `",
        "`Hacking... 100%\n█████████HACKED███████████ `",
        "`Targeted Account Hacked...\n\nPay 69$ To Remove this hack..`"
    ]
    
    with HS.send_message(message.chat.id, "Hacking..") as msg:
        for i in range(len(animation_chars)):
            time.sleep(animation_interval)
            msg.edit(animation_chars[i])


