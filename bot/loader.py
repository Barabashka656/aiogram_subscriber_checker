from bot.data.config import TELEGRAM_API_TOKEN

from aiogram import Bot
from aiogram import Dispatcher


bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher()
