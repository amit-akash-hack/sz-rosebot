from dotenv import load_dotenv
from os import environ

load_dotenv("config.env")

BOT_TOKEN = environ.get("5443528866:AAGPiQvclXbRV2VlEu5sQ8CpxxfeKoJ0hfM")
API_ID = int(environ.get("18442508"))
API_HASH = environ.get("d380fa01dfabf2902e4066fd07f65074")
API_ID1 = int(environ.get("18442508"))
API_HASH1 = environ.get("d380fa01dfabf2902e4066fd07f65074")
SUDO_USERS_ID = environ.get("5348955545")
LOG_GROUP_ID = environ.get("-626111832")
BASE_DB = environ.get("BASE_")
MONGO_URL = environ.get("MONGO_URL")
ARQ_API_URL = environ.get("ARQ_API_URL")
ARQ_API_KEY = environ.get("ARQ_API_KEY")
COMMAND_PREFIXES = environ.get("COMMAND_PREFIXES")
F_SUB_CHANNEL = environ.get("F_SUB_CHANNEL")
