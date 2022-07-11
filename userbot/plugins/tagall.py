

from telethon.tl.types import ChannelParticipantsAdmins

from userbot import CMD_HELP
from userbot.utils import flaming_cmd


@borg.on(flaming_cmd(pattern=r"tagall", outgoing=True))
@borg.on(flaming_cmd(pattern=r"tagall", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Plz see that msg once✨️"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, 75):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)


@borg.on(flaming_cmd(pattern=r"admin", outgoing=True))
@borg.on(flaming_cmd(pattern=r"admin", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Admins : "
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)


CMD_HELP.update(
    {
        "tagall": ".tagall\
    \nReplay any msg with .tagall nd u'll tag top 75 active mem of a grp."
    }
)
