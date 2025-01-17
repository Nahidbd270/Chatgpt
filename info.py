# ©️biisal jai shree krishna 😎
from os import environ
from dotenv import load_dotenv

load_dotenv()

API_ID = environ.get("API_ID" , "19234664")
API_HASH = environ.get("API_HASH" , "29c2f3b3d115cf1b0231d816deb271f5")
BOT_TOKEN = environ.get("BOT_TOKEN" , "7586293548:AAGW_s5sCKKAoAfnEsKE7P0TWIVrjjKwg2U")
ADMIN = int(environ.get("ADMIN" , "8058281460"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1002340194683"))
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002491365982")
MONGO_URL = environ.get("MONGO_URL" , "mongodb+srv://mofajir580:mofajir580@cluster0.nqum3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1002309821556")
)
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
