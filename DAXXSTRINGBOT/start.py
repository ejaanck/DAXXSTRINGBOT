from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𝖧𝐞𝐲 {msg.from_user.mention},

{me2},
𝗔𝗱𝗮𝗹𝗮𝗵 𝗕𝗼𝘁 𝘂𝗻𝘁𝘂𝗸 𝗺𝗲𝗺𝗯𝘂𝗮𝘁 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻.
𝗢𝘄𝗻𝗲𝗿  : [FAKEBOT](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖤 𝖲𝖳𝖱𝖨𝖭𝖦", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("CHANNEL", url="https://t.me/stayheresay"),
                    InlineKeyboardButton("GRUP", url="https://t.me/jaaxkucsupport")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
