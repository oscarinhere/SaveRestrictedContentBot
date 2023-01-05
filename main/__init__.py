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
SESSION = config("BQA9Y_REpkS_FsgjEfTb4lR48IOYyyFG7WQSvV65mpZrbYL_LUBXxItE-SZ9Itw-ToFHiYDO8kpUommdWUsUw_-DCt3kaZInxAc0uRhjsvrAr0dT5lf0uG1gRsDK6YQL-6DAm5WK3klTh3P8GyP-tohk-JxD3-Cr3UK2JgJqn1jVH_7W8oYuOhIwNicxRTRDKe2dSXY79WpQy-oaTuYW7kE3KlFzO4c6QnqaujFewSd0L8F_tHQWXJQph4LoHGY0tlvBptYFT9U7AETzgvej5KE6HFVjePqCdKpvQerXZiMYg3T_PoC3sILUcPG2oOYnIsOj9IXvgftSwqHKQPTs0blJdgQptQA", default=None)
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
