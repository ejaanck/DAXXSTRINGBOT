from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "23770828"))
API_HASH = getenv("API_HASH", "2d3e87f244740e5c8286591940e24cd4")

BOT_TOKEN = getenv("BOT_TOKEN", "7009082569:AAGtzM7zw0J993cLdxuAFEJaFbreYLf_Kvg")
#OWNER_ID = int(getenv("6664582540"))
OWNER_ID = int(getenv("OWNER_ID", "7149602071"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://jembutan1:1234@cluster0.w186hoa.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "thebrazzernew")
