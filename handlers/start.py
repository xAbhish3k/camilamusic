from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

I am camilla Music Bot, an open-source bot that lets you play music in your Telegram groups voice chat.


To add in your group contact us at @camila_support

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Help", url="https://t.me/itsmelegend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/camila_support"
                    ),
                    InlineKeyboardButton(
                        "music userbot", url="https://t.me/camilaowner"
                    ),
                    InlineKeyboardButton(
                        "offtopic", url="https://t.me/OnlineHangout" )
                ]
              ]  
            )
         )  
            
                
                
            
          
       
        
    


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
