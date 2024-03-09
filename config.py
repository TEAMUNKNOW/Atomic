from os import getenv


API_ID = int(getenv("API_ID", "20837006"))
API_HASH = getenv("API_HASH", "b7c5f5ea03b19b1687cddf9eceaf69aa")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "6399386263"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
MONGO_URL = getenv("MONGO_URL", "")
SESSION_STRING = getenv("SESSION_STRING", "")


