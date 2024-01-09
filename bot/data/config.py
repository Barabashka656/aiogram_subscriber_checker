import os
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

DATABASE_URL = 'sqlite+aiosqlite:///bot/data/database.db'

GROUP_ID = '@promokoddavinci'

ADMINS = [462206848]
