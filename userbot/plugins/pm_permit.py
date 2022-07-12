

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import io
import os

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

import userbot.plugins.sql_helper.pmpermit_sql as flaming_sql
from userbot import ALIVE_NAME, bot
from userbot.thunderconfig import Config
from var import Var
FLAMINGUSER = str(ALIVE_NAME) if ALIVE_NAME else "Userbot"
from userbot.utils import flaming_cmd

FLAMING_WRN = {}
FLAMING_REVL_MSG = {}

FLAMING_PROTECTION = Config.FLAMING_PRO

SPAM = os.environ.get("SPAM", None)
if SPAM is None:
    HMM_LOL = "5"
else:
    HMM_LOL = SPAM

FLAMING_PM = os.environ.get("FLAMING_PM", None)
if FLAMING_PM is None:
    CUSTOM_FLAMING_PM_PIC = "https://te.legra.ph/file/655a5de5e0232d5d8e62b.jpg"
else:
    CUSTOM_FLAMING_PM_PIC = FLAMING_PM
FUCK_OFF_WARN = f"**Blocked You As You Spammed {FLAMINGUSER}'s DM\n\n **IDC**"




OVER_POWER_WARN = (
    f"**Hello Sir Im Here To Protect {FLAMINGUSER} Dont Under Estimate Me I Am Very Powerful😂😂  **\n\n"
    f"`My Master {FLAMINGUSER} is Busy Right Now !` \n"
    f"{FLAMINGUSER} Is Very Busy Why Came Please Lemme Know Choose Your Deasired Reason"
    f"**Btw Dont Spam Or Get Banned** 😂😂 \n\n"
    f"**{CUSTOM_FLAMING_PM_PIC}**\n"
)

FLAMING_STOP_EMOJI = (
    "✋"
)
if Var.PRIVATE_GROUP_ID is not None:
    @bot.on(events.NewMessage(outgoing=True))
    async def flaming_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not flaming_sql.is_approved(chat.id):
                if not chat.id in FLAMING_WRN:
                    flaming_sql.approve(chat.id, "outgoing")
                    bruh = "Auto-approved bcuz outgoing 😄😄"
                    rko = await borg.send_message(event.chat_id, bruh)
                    await asyncio.sleep(3)
                    await rko.delete()  

    @borg.on(flaming_cmd(pattern="(a|approve)"))
    async def block(event):
        if event.fwd_from:
            return
        replied_user = await borg(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chats = await event.get_chat()
        if event.is_private:
            if not flaming_sql.is_approved(chats.id):
                if chats.id in FLAMING_WRN:
                    del FLAMING_WRN[chats.id]
                if chats.id in FLAMING_REVL_MSG:
                    await FLAMING_REVL_MSG[chats.id].delete()
                    del FLAMING_REVL_MSG[chats.id]
                flaming_sql.approve(chats.id, f"Wow lucky You {FLAMINGUSER} Approved You")
                await event.edit(
                    "Approved to pm [{}](tg://user?id={})".format(firstname, chats.id)
                )
                await asyncio.sleep(3)
                await event.delete()

    @borg.on(flaming_cmd(pattern="block$"))
    async def flaming_approved_pm(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chat = await event.get_chat()
        if event.is_private:
            if flaming_sql.is_approved(chat.id):
                flaming_sql.disapprove(chat.id)
            await event.edit("Blocked [{}](tg://user?id={})".format(firstname, chat.id))
            await asyncio.sleep(2)
            await event.client(functions.contacts.BlockRequest(chat.id))
            await event.delete()

            
    @borg.on(flaming_cmd(pattern="(da|disapprove)"))
    async def flaming_approved_pm(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chat = await event.get_chat()
        if event.is_private:
            if flaming_sql.is_approved(chat.id):
                flaming_sql.disapprove(chat.id)
            await event.edit("Disapproved [{}](tg://user?id={})".format(firstname, chat.id))
            await asyncio.sleep(2)
            await event.edit(
                    "Disapproved User [{}](tg://user?id={})".format(firstname, chat.id)
                )
            await event.delete()

    

    @borg.on(flaming_cmd(pattern="listapproved$"))
    async def flaming_approved_pm(event):
        if event.fwd_from:
            return
        approved_users = flaming_sql.get_all_approved()
        PM_VIA_LIGHT = f"♥‿♥ {FLAMINGUSER} Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    PM_VIA_LIGHT += f"♥‿♥ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    PM_VIA_LIGHT += (
                        f"♥‿♥ [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            PM_VIA_LIGHT = "no Approved PMs (yet)"
        if len(PM_VIA_LIGHT) > 4095:
            with io.BytesIO(str.encode(PM_VIA_LIGHT)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(PM_VIA_LIGHT)

    @bot.on(events.NewMessage(incoming=True))
    async def flaming_new_msg(flaming):
        if flaming.sender_id == bot.uid:
            return

        if Var.PRIVATE_GROUP_ID is None:
            return

        if not flaming.is_private:
            return

        flaming_chats = flaming.message.message
        chat_ids = flaming.sender_id

        flaming_chats.lower()
        if OVER_POWER_WARN == flaming_chats:
            # flaming should not reply to other flaming
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await bot.get_entity(flaming.sender_id)
        if chat_ids == bot.uid:
            # don't log Saved Messages
            return
        if sender.bot:
            # don't log bots
            return
        if sender.verified:
            # don't log verified accounts
            return
        if FLAMING_PROTECTION == "NO":
            return
        if flaming_sql.is_approved(chat_ids):
            return
        if not flaming_sql.is_approved(chat_ids):
            # pm permit
            await flaming_goin_to_attack(chat_ids, flaming)

    async def flaming_goin_to_attack(chat_ids, flaming):
        if chat_ids not in FLAMING_WRN:
            FLAMING_WRN.update({chat_ids: 0})
        if FLAMING_WRN[chat_ids] == 3:
            lemme = await flaming.reply(FUCK_OFF_WARN)
            await asyncio.sleep(3)
            await flaming.client(functions.contacts.BlockRequest(chat_ids))
            if chat_ids in FLAMING_REVL_MSG:
                await FLAMING_REVL_MSG[chat_ids].delete()
            FLAMING_REVL_MSG[chat_ids] = lemme
            flaming_msg = ""
            flaming_msg += "#Some Retards 😑\n\n"
            flaming_msg += f"[User](tg://user?id={chat_ids}): {chat_ids}\n"
            flaming_msg += f"Message Counts: {FLAMING_WRN[chat_ids]}\n"
            # flaming_msg += f"Media: {message_media}"
            try:
                await flaming.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=lightn_msg,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True,
                )
                return
            except BaseException:
                  await  flaming.edit("Something Went Wrong")
                  await asyncio.sleep(2) 
            return

        # Inline
        flamingusername = Var.TG_BOT_USER_NAME_BF_HER
        FLAMING_L = OVER_POWER_WARN.format(
        FLAMINGUSER, FLAMING_STOP_EMOJI, FLAMING_WRN[chat_ids] + 1, HMM_LOL
        )
        flaming_hmm = await bot.inline_query(flamingusername, FLAMING_L)
        new_var = 0
        yas_ser = await flaming_hmm[new_var].click(flaming.chat_id)
        FLAMING_WRN[chat_ids] += 1
        if chat_ids in FLAMING_REVL_MSG:
           await FLAMING_REVL_MSG[chat_ids].delete()
        FLAMING_REVL_MSG[chat_ids] = yas_ser



@bot.on(events.NewMessage(incoming=True, from_users=(1232461895)))
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not flaming_sql.is_approved(chats.id):
            flaming_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, "**Alert! My dev 𝕶𝖗𝖎𝖘𝖍𝖓𝖆😎 is here. **"
            )
            print("Krishna is here")


@bot.on(
    events.NewMessage(incoming=True, from_users=(1311769691))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not flaming_sql.is_approved(chats.id):
            flaming_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, f"**Good To See You @flaming_AI. How Can I Disapprove You Come In Sir**😄😄"
            )
            print("Dev Here")
       
@bot.on(
    events.NewMessage(incoming=True, from_users=(798271566))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not flaming_sql.is_approved(chats.id):
            flaming_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, f"**Good To See You @flaming_AI. How Can I Disapprove You Come In Sir**😄😄"
            )               
            print("Dev Here")
            
@bot.on(
    events.NewMessage(incoming=True, from_users=(2146145623))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not flaming_sql.is_approved(chats.id):
            flaming_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, f"**MY DEV!!DEAR COMRADE IS HERE...HOW CAN I DISAPPROVE.... AUTO APPROVED**😄😄"
            )               
            print("DEAR COMRADE IS HERE")            
@bot.on(
    events.NewMessage(incoming=True, from_users=(1908955228))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not flaming_sql.is_approved(chats.id):
            flaming_sql.approve(chats.id, "`Yo Developer @CYBER_RISHISUPERYO,felling op to see u⚡🙂🙃😉`")
            await borg.send_message(
                chats, f"RISHISUPERYO IZ HERE😎,HOW CAN I DISAPPROVE YOU OP BEYBLADER😎 U ARE ALWAYS ALLOWED IN PM😎\n @Cosmic_Rishisuperyo iz here😎\n so auto approved must🌈 "
            )               
            print("`RISHISUPERYO OP IZ HERE ⚡`")            
@bot.on(
    events.NewMessage(incoming=True, from_users=(1754865180))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not flaming_sql.is_approved(chats.id):
            flaming_sql.approve(chats.id, "`Alert: @flaming_AI`")
            await borg.send_message(
                chats, f"`⚠️Alert: @flaming_AI is Here ⚠️`."
            )               
            print("`Paramatin7 Spotted`")   
@bot.on(
    events.NewMessage(incoming=True, from_users=(1435941875))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not flaming_sql.is_approved(chats.id):
            flaming_sql.approve(chats.id, "`⚠️Alert: @flaming_AI is Here ⚠️`")
            await borg.send_message(
                chats, f"Welcome Sir please let me know how may i help you."
            )               
            print("`MR.CRACKER IS HERE`")   
@bot.on(
    events.NewMessage(incoming=True, from_users=(2021388501))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not flaming_sql.is_approved(chats.id):
            flaming_sql.approve(chats.id, "`⚠️Alert: Moi Dev is Here ⚠️`")
            await borg.send_message(
                chats, f"Welcome Sir please let me know how may i help you."
            )               
            print("`My DEV IS HERE...AUTO APPROVED`")   
