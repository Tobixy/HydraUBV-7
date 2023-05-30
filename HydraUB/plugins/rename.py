from HydraUB import Hydra as HS
from config import OWNER_ID, HANDLER
import os
from pyrogram import filters


async def FileType(message):
    if message.document:
        type = message.document.mime_type
        return ["txt" if type == "text/plain" else type.split("/")[1]][0]
    elif message.photo:
          return "jpg"
    elif message.animation:
          return message.animation.mime_type.split("/")[1]
    elif message.video:
         return message.video.mime_type.split("/")[1]
    else:
         return False

@HS.on_message(filters.command("rename",prefixes=HANDLER) & filters.user(OWNER_ID))
async def rename(_, message):
    try:
       filename = message.text.split(None,1)[1]
    except:
        name = "HS"
        try:
          if (await FileType(message=message.reply_to_message)) != False:
               filetype = await FileType(message=message.reply_to_message)
        except Exception as e:
               return await message.reply_text(f"Error: `{e}`")
        filename = "{name}.{filetype}".format(name=name, filetype=filetype)
    msg = await message.reply_text("⬇️ File has downloading...")
    path = await message.reply_to_message.download(file_name=filename)
    thumb_id = "./HydraUB/Helper/tf.jpg"
    await msg.edit_text("⬆️ File has uplaoding")
    await message.reply_document(document=path, thumb=thumb_id)
    await msg.delete()
    os.remove(path)
    return 
    
    
    
