import os
from dotenv import find_dotenv, load_dotenv
import json

load_dotenv(find_dotenv())

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

GROUP_ID = os.getenv('GROUP_ID')

ADMINS = json.loads(os.getenv('ADMINS'))

DATABASE_URL = 'sqlite+aiosqlite:///bot/data/database.db'