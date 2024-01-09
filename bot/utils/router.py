from bot.handlers.admin.router import router as admin_router
from bot.handlers.start.router import router as start_router
from bot.handlers.article.router import router as article_router
from bot.handlers.error.router import router as error_router

from aiogram import Dispatcher


def setup_routers(dp: Dispatcher):
    dp.include_routers(
        admin_router,
        article_router,
        start_router,
        error_router
    )
