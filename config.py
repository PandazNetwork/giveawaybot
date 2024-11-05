import os
import dotenv

if os.path.exists("vars.env"):
    load_dotenv("vars.env")
else:
    load_dotenv()  
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_URI = os.getenv("DB_URI")
DB_NAME = os.getenv("DB_NAME")
ADMIN_IDS = [int(admin_id) for admin_id in os.getenv("ADMIN_IDS", "").split()]
