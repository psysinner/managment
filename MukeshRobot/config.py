import os
from dotenv import load_dotenv
import ast

# Load environment variables from .env file
load_dotenv()

class Config(object):
    LOGGER = os.getenv("LOGGER", "True") == "True"
    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH", "")
    TOKEN = os.getenv("TOKEN", "")
    OWNER_ID = os.getenv("OWNER_ID")

    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "")
    START_IMG = os.getenv("START_IMG", "")
    EVENT_LOGS = ast.literal_eval(os.getenv("EVENT_LOGS", "()"))
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    CASH_API_KEY = os.getenv("CASH_API_KEY", "")
    TIME_API_KEY = os.getenv("TIME_API_KEY", "")

    BL_CHATS = ast.literal_eval(os.getenv("BL_CHATS", "[]"))
    DRAGONS = ast.literal_eval(os.getenv("DRAGONS", "[]"))
    DEV_USERS = ast.literal_eval(os.getenv("DEV_USERS", "[]"))
    DEMONS = ast.literal_eval(os.getenv("DEMONS", "[]"))
    TIGERS = ast.literal_eval(os.getenv("TIGERS", "[]"))
    WOLVES = ast.literal_eval(os.getenv("WOLVES", "[]"))

    ALLOW_CHATS = os.getenv("ALLOW_CHATS", "True") == "True"
    ALLOW_EXCL = os.getenv("ALLOW_EXCL", "True") == "True"
    DEL_CMDS = os.getenv("DEL_CMDS", "True") == "True"
    INFOPIC = os.getenv("INFOPIC", "True") == "True"
    LOAD = ast.literal_eval(os.getenv("LOAD", "[]"))
    NO_LOAD = ast.literal_eval(os.getenv("NO_LOAD", "[]"))
    STRICT_GBAN = os.getenv("STRICT_GBAN", "True") == "True"
    TEMP_DOWNLOAD_DIRECTORY = os.getenv("TEMP_DOWNLOAD_DIRECTORY", "./")
    WORKERS = int(os.getenv("WORKERS", "8"))

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
