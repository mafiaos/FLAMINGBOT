
from telethon import events
from userbot.utils import flaming_cmd
from userbot import CMD_HELP
@borg.on(flaming_cmd(pattern=r"repo", outgoing=True))
async def hapy(event):
     a="REPO [FLAMING REPO](https://github.com/ITS-FLAMINGBOT/FLAMINGBOT)"
     await event.edit(a)
