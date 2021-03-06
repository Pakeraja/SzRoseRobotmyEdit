from Rose import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from Rose.utils.lang import *


fbuttons = InlineKeyboardMarkup(
        [
        [
            InlineKeyboardButton(
                text="ð§¡sá´Éªá´á´á´Ê á´á´á´á´sð§¡", url="https://t.me/groot_network"
            ),
            InlineKeyboardButton(
                text="ðÒá´É´É´Ê É¢ÉªÒsð", url="https://t.me/rjbr0"
            )
        ], 
        [
            InlineKeyboardButton(
                text="ðá´á´Êá´É¢á´ É¢Êá´á´á´sð", url="https://t.me/telugulittleworld"
            ),
            InlineKeyboardButton(
                text="ðá´á´Êá´É¢á´ á´á´á´á´Êsð", url="https://t.me/telugucoders"
            )
        ], 
        [
            InlineKeyboardButton(
                text="ðá´á´¡É´á´Êð", url="https://t.me/mynameisgroot"
            )
        ], 
        [
            InlineKeyboardButton("Â« Back", callback_data='startcq')
        ]
        ]
)

keyboard =InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="ð±ð· English", callback_data="languages_en"
            ),
            InlineKeyboardButton(
                text="ð±ð° à·à·à¶à·à¶½", callback_data="languages_si"
            )
        ],
        [
            InlineKeyboardButton(
                text="ð®ð³ à¤¹à¤¿à¤¨à¥à¤¦à¥", callback_data="languages_hi"
            ),
            InlineKeyboardButton(
                text="ð®ð¹ Italiano", callback_data="languages_it"
            )
        ],
        [
            InlineKeyboardButton(
                text="ð®ð³ à°¤à±à°²à±à°à±", callback_data="languages_ta"
            ),
            InlineKeyboardButton(
                text="ð®ð© Indonesia", callback_data="languages_id"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ð¦ðª Ø¹Ø±Ø¨Ù", callback_data="languages_ar"
            ),
            InlineKeyboardButton(
                text="ð®ð³ à´®à´²à´¯à´¾à´³à´", callback_data="languages_ml"
            ), 
        ],
        [
            InlineKeyboardButton(
                text="ð²ð¼ chichewa", callback_data="languages_ny"
            ), 
            InlineKeyboardButton(
                text="ð©ðª german", callback_data="languages_ge"
            ), 
        ], 
        [  
            InlineKeyboardButton("Â« Back", callback_data='startcq')
        ]
    ]
)

@app.on_callback_query(filters.regex("_langs"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    user = CallbackQuery.message.from_user.mention
    await app.send_message(
        CallbackQuery.message.chat.id,
        text= "The list of available languages:",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()
    
@app.on_callback_query(filters.regex("_about"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=_["menu"],
        reply_markup=fbuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()

