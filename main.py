import os
import time
from cmd_cllaback import *
import logging
from pyrogram import *
import requests
from progress import progress
from conf import Config
from pyrogram import Client, filters, idle
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)



APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN

   
OC_GoFiles_Files = Client(
    "GofileUploader",
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


@OC_GoFiles_Files.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@OC_GoFiles_Files.on_message(filters.private & filters.media & ~filters.sticker)
async def main(client, message):
    status = await message.reply("π«ππππππππππ ππππ π­πππ π»π π΄π πΊπππππ...")
    now = time.time()
    file =await OC_GoFiles_Files.download_media(message,progress=progress,progress_args=("**ππππππ πΏπππππππ πππππππ, πΏπππππ ππππ !**\n**πα΄π€ πα΄α΄α΄ α΄Ιͺα΄α΄ πΈα΄α΄α΄Κα΄ΙͺΙ΄Ι’ πα΄α΄Κ π½ΙͺΚα΄π€ πΙͺα΄’α΄** \n\n**α΄α΄α΄:** ", status,now))
    krakenapi = requests.get(url="https://krakenfiles.com/api/server/available").json()
    krakenxurl = krakenapi['data']['url']
    krakentoken = krakenapi['data']['serverAccessToken']
    params = {'serverAccessToken': krakentoken}
    headers = {'X-AUTH-TOKEN': 'YjdiNDVjNWVjODUwNDE1YTvA3SwQLNGO0Yw0wo6YyaBPk4CcXFVEg3KFozUxaBaJ'}
    files = {'file': open(file, 'rb')}
    krakenupload = requests.post(krakenxurl, files=files, data=params).json()
    krakenlink = krakenupload['data']['url']
    await status.delete()
    os.remove(file)

    output = f"""
<u>**πππ ΖΖΤΌΠ Ζ²Ζ€ΤΌΖ ΖΖΠΖ Ζ¬Ζ  ΖΖ ΖΖΤΌΠ ππ**</u>


βββββββββββββββββ

**π¦ Download Page:**

βββββββββββββββββ
 
 {krakenlink}

βββββββββββββββββ

βββββββββββββββββ


π· πππππππππ : βοΈβοΈππΉπ?π· ππΈπ­π? ππ?πΏπΌ βοΈβοΈ"""

    await message.reply(output, disable_web_page_preview=True)



@OC_GoFiles_Files.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    else:
        await update.message.delete()


OC_GoFiles_Files.start()
print("""GoFileBot Is Started!
π· πππππππππ : βοΈβοΈππΉπ?π· ππΈπ­π? ππ?πΏπΌ βοΈβοΈ
Send me any media file, I will upload it to Gofile.io and give the download link
""")
idle()
