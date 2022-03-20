import asyncio
from Music import client as USER
from Music import BOT_USERNAME
from Music.config import OWNER_ID
from Music import ASSNAME, ASSUSERNAME
from Music.MusicUtilities.helpers.decorate import authorized_users_only, sudo_users_only, errors
from Music.MusicUtilities.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant


@Client.on_message(
    command(["انضم", f"دخول"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
@errors
async def join_group(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "• **ليـس لدي صلحيه:**\n\n» ❌ __اضافه مستخدمين__",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Zaid2_Assistant"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"🛑 Flood Wait Error 🛑 \n\n** ❌ {ASSNAME}(@{ASSUSERNAME}) couldn't join your group due to heavy join requests for userbot**"
            "\n\n**or add assistant manually to your Group and try again**",
        )
        return
    await message.reply_text(
        f"✅ **جيـت يعم هتشغل اي ؟**",
    )


@Client.on_message(
    command(["غادر", f"userbotleave"]) & filters.group & ~filters.edited
)
@authorized_users_only
async def leave_group(client, message):
    try:
        await USER.send_message(message.chat.id, "✅ خـلاص يعـم هطلع بكرامتي ،، سلااام")
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            "❌ **userbot couldn't leave your group, may be floodwaits.**\n\n**» or manually kick userbot from your group**"
        )

        return


@Client.on_message(command(["مغادره", f"leaveall@{BOT_USERNAME}"]))
@sudo_users_only
async def leave_all(client, message):
    if message.from_user.id not in OWNER_ID:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **userbot** leaving all chats !")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"Userbot leaving all group...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        except:
            failed += 1
            await lol.edit(
                f"Userbot leaving...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"✅ Left from: {left} chats.\n❌ Failed in: {failed} chats."
    )
