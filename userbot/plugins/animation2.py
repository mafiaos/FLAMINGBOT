import asyncio
from collections import deque

from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import flaming_cmd, sudo_cmd, edit_or_reply

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Black Lightning"


@borg.on(flaming_cmd(pattern=r"lul$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("ππ€£ππ€£ππ€£"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(flaming_cmd(pattern=r"nothappy$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("πβΉοΈπβΉοΈπβΉοΈπ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(flaming_cmd(outgoing=True, pattern="clock$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("πππππππππππ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(flaming_cmd(pattern=r"muah$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("πππππ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(flaming_cmd(pattern="heart$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("β€οΈπ§‘πππππ€"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(flaming_cmd(pattern="gym$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("πβπβπ€Έβπβπβπ€Έβπβπβπ€Έβ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(flaming_cmd(pattern=f"earth$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("ππππππππ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(flaming_cmd(outgoing=True, pattern="moon$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("ππππππππ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(flaming_cmd(pattern=r"candy$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("π¦π§π©πͺππ°π§π«π¬π­"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(flaming_cmd(pattern=f"smoon$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 101)
    await event.edit("smoon..")
    animation_chars = [
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@borg.on(flaming_cmd(pattern=f"tmoon$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 117)
    await event.edit("tmoon")
    animation_chars = [
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


@borg.on(flaming_cmd(pattern=f"clown$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.50
    animation_ttl = range(0, 16)
    animation_chars = [
        "COMMAND CREATE BY @Sur_vivor",
        "π€‘οΈ",
        "π€‘π€‘",
        "π€‘π€‘π€‘",
        "π€‘π€‘π€‘π€‘",
        "π€‘π€‘π€‘π€‘π€‘",
        "π€‘π€‘π€‘π€‘π€‘π€‘",
        "π€‘π€‘π€‘π€‘π€‘",
        "π€‘π€‘π€‘π€‘",
        "π€‘π€‘π€‘",
        "π€‘π€‘",
        "π€‘",
        "You",
        "You Are",
        "You Are A",
        "You Are A Clown π€‘",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 16])


@borg.on(flaming_cmd(pattern=f"human$", outgoing=True))
@borg.on(sudo_cmd(pattern="human$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(16)
    event = await edit_or_reply(event, "human...")
    animation_chars = [
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬π\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬πβ¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬πβ¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬πβ¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬πβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
        "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 16])


@borg.on(flaming_cmd(pattern=f"music$", outgoing=True))
@borg.on(sudo_cmd(pattern="music$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "starting player...")
    animation_chars = [
        "β¬€β¬€β¬€ 81% β β β β β β β β β β β β β β β β β β β `βοΈ`\n\nβ β β β β [Music Player](t.me/flaming_support_group)\n\nβ β β β **Now Playing:shape of u**\n\n**00:00** β±β±β±β±β±β±β±β±β±β± **00:10**\n\nβ β β β β `π` `β?οΈ` `βͺοΈ` `βΆοΈ` `β©οΈ` `β­οΈ`\n\n**β Next Song:** __Alan Walker - Alone.__\n\nβ β β β **β Device: I Fone XXX**",
        "β¬€β¬€β¬€ 81% β β β β β β β β β β β β β β β β β β β `βοΈ`\n\nβ β β β β [Music Player](t.me/flaming_support_group)\n\nβ β β β **Now Playing:shape of u**\n\n**00:01** β°β±β±β±β±β±β±β±β±β± **00:10**\n\nβ β β β β `π` `β?οΈ` `βͺοΈ` `βΈοΈ` `β©οΈ` `β­οΈ`\n\n**β Next Song:** __Alan Walker - Alone.__\n\nβ β β β **β Device: Ifone XXX**",
        "β¬€β¬€β¬€ 81% β β β β β β β β β β β β β β β β β β β `βοΈ`\n\nβ β β β β [Music Player](t.me/flaming_support_group)\n\nβ β β β **Now Playing:shape of u**\n\n**00:02** β°β°β±β±β±β±β±β±β±β± **00:10**\n\nβ β β β β `π` `β?οΈ` `βͺοΈ` `βΈοΈ` `β©οΈ` `β­οΈ`\n\n**β Next Song:** __Alan Walker - Alone.__\n\nβ β β β **β Device: Ifone XXX**",
        "β¬€β¬€β¬€ 81% β β β β β β β β β β β β β β β β β β β `βοΈ`\n\nβ β β β β [Music Player](t.me/flaming_support_group)\n\nβ β β β **Now Playing:shape of u**\n\n**00:03** β°β°β°β±β±β±β±β±β±β± **00:10**\n\nβ β β β β `π` `β?οΈ` `βͺοΈ` `βΈοΈ` `β©οΈ` `β­οΈ`\n\n**β Next Song:** __Alan Walker - Alone.__\n\nβ β β β **β Device: Ifone XXX**",
        "β¬€β¬€β― 80% β β β β β β β β β β β β β β β β β β β `βοΈ`\n\nβ β β β β [Music Player](t.me/flaming_support_group)\n\nβ β β β **Now Playing:shape of u**\n\n**00:04** β°β°β°β°β±β±β±β±β±β± **00:10**\n\nβ β β β β `π` `β?οΈ` `βͺοΈ` `βΈοΈ` `β©οΈ` `β­οΈ`\n\n**β Next Song:** __Alan Walker - Alone.__\n\nβ β β β **β Device: Ifone XXX**",
        "β¬€β¬€β― 80% β β β β β β β β β β β β β β β β β β β `βοΈ`\n\nβ β β β β [Music Player](t.me/flaming_support_group)\n\nβ β β β **Now Playing:shape of u**\n\n**00:05** β°β°β°β°β±β±β±β±β±β± **00:10**\n\nβ β β β β `π` `β?οΈ` `βͺοΈ` `βΈοΈ` `β©οΈ` `β­οΈ`\n\n**β Next Song:** __Alan Walker - Alone.__\n\nβ β β β **β Device: Ifone XXX**",
        "β¬€β¬€β― 80% β β β β β β β β β β β β β β β β β β β `βοΈ`\n\nβ β β β β [Music Player](t.me/flaming_support_group)\n\nβ β β β **Now Playing:shape of u**\n\n**00:06** β°β°β°β°β°β°β±β±β±β± **00:10**\n\nβ β β β β `π` `β?οΈ` `βͺοΈ` `βΈοΈ` `β©οΈ` `β­οΈ`\n\n**β Next Song:** __Alan Walker - Alone.__\n\nβ β β β **β Device: Ifone XXX**",
        "β¬€β¬€β― 80% β β β β β β β β β β β β β β β β β β β `βοΈ`\n\nβ β β β β [Music Player](t.me/flaming_support_group)\n\nβ β β β **Now Playing:shape of u**\n\n**00:07** β°β°β°β°β°β°β°β±β±β± **00:10**\n\nβ β β β β `π` `β?οΈ` `βͺοΈ` `βΈοΈ` `β©οΈ` `β­οΈ`\n\n**β Next Song:** __Alan Walker - Alone.__\n\nβ β β β **β Device: Ifone XXX**",
        "β¬€β¬€β― 80% β β β β β β β β β β β β β β β β β β β `βοΈ`\n\nβ β β β β [Music Player](t.me/flaming_support_group)\n\nβ β β β **Now Playing:shape of u**\n\n**00:08** β°β°β°β°β°β°β°β°β±β± **00:10**\n\nβ β β β β `π` `β?οΈ` `βͺοΈ` `βΈοΈ` `β©οΈ` `β­οΈ`\n\n**β Next Song:** __Alan Walker - Alone.__\n\nβ β β β **β Device: Ifone XXX**",
        "β¬€β¬€β― 80% β β β β β β β β β β β β β β β β β β β `βοΈ`\n\nβ β β β β [Music Player](t.me/flaming_support_group)\n\nβ β β β **Now Playing:shape of u**\n\n**00:09** β°β°β°β°β°β°β°β°β°β± **00:10**\n\nβ β β β β `π` `β?οΈ` `βͺοΈ` `βΈοΈ` `β©οΈ` `β­οΈ`\n\n**β Next Song:** __Alan Walker - Alone.__\n\nβ β β β **β Device: Ifone XXX**",
        "β¬€β¬€β― 80% β β β β β β β β β β β β β β β β β β β `βοΈ`\n\nβ β β β β [Music Player](t.me/flaming_support_group)\n\nβ β β β **Now Playing:shape of u**\n\n**00:10** β°β°β°β°β°β°β°β°β°β° **00:10**\n\nβ β β β β `π` `β?οΈ` `βͺοΈ` `βΊοΈ` `β©οΈ` `β­οΈ`\n\n**β Next Song:** __Alan Walker - Alone.__\n\nβ β β β **β Device: Ifone XXX**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@borg.on(flaming_cmd(pattern=f"squ$", outgoing=True))
@borg.on(sudo_cmd(pattern="squ$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(
        event, "βββββββββββββββββββββ \n  \nβββββββββββββββββββββ"
    )
    await asyncio.sleep(1)
    await event.edit("βββββββββββββββββββββ \n \tβ \nβββββββββββββββββββββ")
    await asyncio.sleep(1)
    await event.edit("βββββββββββββββββββββ \n β \tβ \nβββββββββββββββββββββ")
    await asyncio.sleep(1)
    await event.edit("βββββββββββββββββββββ \n β β β \nβββββββββββββββββββββ")
    await asyncio.sleep(1)
    await event.edit("βββββββββββββββββββββ \n β β β β \nβββββββββββββββββββββ")
    await asyncio.sleep(1)
    await event.edit("βββββββββββββββββββββ \n β β β β β \nβββββββββββββββββββββ")
    await asyncio.sleep(1)
    await event.edit("βββββββββββββββββββββ \n β β β β β β \nβββββββββββββββββββββ")
    await asyncio.sleep(1)
    await event.edit("βββββββββββββββββββββ \n β β β β β β β \nβββββββββββββββββββββ")
    await asyncio.sleep(1)
    await event.edit("βββββββββββββββββββββ \n β β β β β β β β \nβββββββββββββββββββββ")
    await asyncio.sleep(1)
    await event.edit(
        "βββββββββββββββββββββ \n β β β β β β β β β \nβββββββββββββββββββββ"
    )
    await asyncio.sleep(1)
    await event.edit(
        "βββββββββββββββββββββ \n β β β β β β β β β β \nβββββββββββββββββββββ"
    )
    await asyncio.sleep(1)
    await event.edit(
        "βββββββββββββββββββββ \n β β β β β β β β β β β \nβββββββββββββββββββββ"
    )
    await asyncio.sleep(1)
    await event.edit(
        "βββββββββββββββββββββ \n β β β β β β β β β β β β \nβββββββββββββββββββββ"
    )
    await asyncio.sleep(1)
    await event.edit(
        "βββββββββββββββββββββ \n β β β β β β β β β β β β β \nβββββββββββββββββββββ"
    )
    await asyncio.sleep(1)
    await event.edit(
        "βββββββββββββββββββββ \n β β β β β β β β β β β β β β \nβββββββββββββββββββββ"
    )
    await asyncio.sleep(6)


@borg.on(flaming_cmd(outgoing=True, pattern="kiler( (.*)|$)"))
@borg.on(sudo_cmd(pattern="kiler( (.*)|$)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    if not name:
        name = "die"
    animation_interval = 0.7
    animation_ttl = range(8)
    event = await edit_or_reply(event, f"**Ready Commando **__{DEFAULTUSER}....")
    animation_chars = [
        "οΌ¦ο½ο½ο½ο½ο½ο½ο½",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/οΉ\_\n (?`_Β΄)\n <,οΈ»β¦β€β ? - \n _/οΉ\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/οΉ\_\n (?`_Β΄)\n  <,οΈ»β¦β€β ? - -\n _/οΉ\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/οΉ\_\n (?`_Β΄)\n <,οΈ»β¦β€β ? - - -\n _/οΉ\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/οΉ\_\n (?`_Β΄)\n<,οΈ»β¦β€β ? - -\n _/οΉ\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/οΉ\_\n (?`_Β΄)\n <,οΈ»β¦β€β ? - \n _/οΉ\_\n",
        f"__**Commando **__{DEFAULTUSER}         \n\n_/οΉ\_\n (?`_Β΄)\n  <,οΈ»β¦β€β ? - -\n _/οΉ\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/οΉ\_\n (?`_Β΄)\n <,οΈ»β¦β€β ? - - - {name}\n _/οΉ\_\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])



CMD_HELP.update(
    {
     "animation2": "`.lul`\
     \n**USAGE**: Laughing Animation.\
     \n\nanimation2: .nothappy\
     \n**USAGE**: Sad Animation plugin.\
     \nanimation2: `.killer` `username\
     \n**USAGE**: Killing input user.\
     \n\nanimation2: `.squ`\
     \n**USAGE**: Cool Animation plugin.\
     \n\nanimation2: `.music`\
     \n**USAGE**:  Cool Music Player Animation"
     
    }
)
