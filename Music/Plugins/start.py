import asyncio
from time import time
from datetime import datetime
from Music import BOT_USERNAME
from Music.config import UPDATES_CHANNEL, ZAID_SUPPORT
from Music.MusicUtilities.helpers.filters import command
from Music.MusicUtilities.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/31a1aaad8469d8bdb2380.jpg",
        caption=f"""**يتيح لك تشغيل الموسيقى والفيديو في المجموعات من خلال المكالمات الجديدة في تيلجرام 🎶!..
  💡 تعلم طريقة تشغيلي واوامر التحكم بي عن طريق الضغط علي زر  » 📚 الاوامر!  ...
💞  تم برمجة البوت بواسطة [「 ســــافو ص دلــــتـــا × 」](t.me/s_a_s_a_3li) 
Powered By [「 ســــافو ص دلــــتـــا × 」](t.me/s_a_s_a_3li) ...
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضغط لـ اضافتي لمجموعتك ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "الاوامر..📚", url=f"https://t.me/DEV_SAVO/28"
                    ),
                    InlineKeyboardButton(
                        "البشمبرمج..😺♥", url="https://t.me/s_a_s_a_3li"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📢 قناة السـورس", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "جروب الدعم 🇮🇳", url=f"https://t.me/D_E_V_S_A_V_O"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/سورس", f"السورس","سورس"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/07abf620f2429032f1a90.jpg",
        caption=f"""شكرًا لإضافتي إلى الدردشة  ، لأي استفسار يمكنك الانضمام إلى مجموعات الدعم الخاصة بنا 🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 انضم هنا 💞", url=f"https://t.me/D_E_V_S_A_V_O")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "سورس", f"سورس","السورس"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/31a1aaad8469d8bdb2380.jpg",
        caption=f"""هنا يوزر المبرمج لو حابب تتواصل معاه ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " البشمبرمج ⚒️", url=f"https://t.me/s_a_s_a_3li")
                ]
            ]
        ),
    )
