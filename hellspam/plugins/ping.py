# If you are kanging this, make sure to give credits else you are gay no doubt in that..!!!


from hellspam import *
from hellspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5
from telethon import events
from datetime import datetime

@SpamBot1.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot2.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot3.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot4.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot5.on(events.NewMessage(incoming=True, pattern='/ping'))
async def ping(e):
    if e.sender_id in MY_USERS:
        before = datetime.now()
        message = await e.client.send_message(e.chat_id, "𝙎𝘼𝘽𝙃𝙍𝙍𝙍 𝙍𝙃𝘼𝙆 𝙉𝘼 𝙇𝙊𝘿𝙐")
        after = datetime.now()
        ms = (after - before).microseconds / 2000
        await e.client.edit_message(message, f"👅👅🇺𝗥𝗔𝗡𝗜𝗨𝗠  ✘  🇸𝗣𝗔𝗠 /n {ms} /n 𝐓𝐀𝐈𝐘𝐀𝐑𝐑𝐑 𝐇𝐎𝐎 𝐉𝐀𝐀 𝐆𝐀𝐀𝐍𝐃𝐔🤣🎉  ")
