from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "23795091"))
API_HASH = getenv("API_HASH", "64a8dadb2a928e4a97e037e834d1f8db")

BOT_TOKEN = getenv("BOT_TOKEN", "7283082118:AAEmmoOO3UhxIEXgoVGJV2wiiujuOygFz0k")
OWNER_ID = int(getenv("OWNER_ID", "7283082118"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://reacode:<password>@reamusic.x7hyx2h.mongodb.net/?retryWrites=true&w=majority&appName=reamusic")
MUST_JOIN = getenv("MUST_JOIN", "NyxianNetwork")
DAXX_API = getenv("DAXX_API", "daxx-1490?api+key:free")
