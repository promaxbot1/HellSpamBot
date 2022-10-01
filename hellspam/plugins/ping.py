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
        message = await e.client.send_message(e.chat_id, "𝐑ᴜᴋᴋᴋ 𝐉ᴀᴀ 𝐆ᴀᴀɴᴅᴜ👀🤣💦")
        after = datetime.now()
        ms = (after - before).microseconds / 1000
        await e.client.edit_message(message, f"𓆩𝐔𝐑𝐀𝐍𝐈𝐔𝐌𓆪 ✘ 𝐒𝐏𝐀𝐌║⚡                           🇵𝐎𝐍𝐆🥀🍫  {ms}                             𝙂𝘼𝘼𝙉𝘿𝙐 𝙒𝘼𝙇𝘼 𝙓 𝙎𝙋𝘼𝙈 😈💦𝙅𝙊                                                𝐌𝐚𝐬𝐭𝐞𝐫- @aa_raha_hu_ruk")
