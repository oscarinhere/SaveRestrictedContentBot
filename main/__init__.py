#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("21332328", default=None, cast=int)
API_HASH = config("a2215944df845b4f64b4e8b7c71c84ac", default=None)
BOT_TOKEN = config("5983735642:AAGFowFBm435ql_hIT9dodMgHUliMfh1TCo", default=None)
SESSION = config("BQBwXa4roLlYuv6K6ixfeqVBbhn8QrAjYRo4YL48UBxGE-ASrW-H5b7pnb9R55wx0jmY1r5GzriMoRMBCGqNkO9koXYYNkNHw5eAdvs6E94gjTwQL42ddeOmJ69YQfHpAUgZaF8neSIvCvFqreHxgXI_rVyjJdxxVOk1GJtK5HhZGrUs1tzFXGCSPt31gAGaT7NLuckITnK24s5YGU4C6w_IA8ZyzLEOvEC6AMT1K6RNKv7IDG53vOg_ozEQLH8_xmzHYcm0l_P4btvKa-4tbnlzFol8n7oDiOQkF7E_J871RTDJ_xxHOVTQkK6h_BBy4xmvoW7t84XGxcHYgnk0K1upVD1k3AA", default=None)
FORCESUB = config("genkpetirinfo", default=None)
AUTH = config("2062576370", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
