from bot.data.config import ADMINS

from aiogram import F, Router
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import ErrorEvent, Message


router = Router()

@router.error(
        ExceptionTypeFilter(Exception), 
        F.update.message.as_("message"),
        F.update.message.from_user.id.in_(ADMINS)
    )
async def handle_my_custom_exception(event: ErrorEvent, message: Message):
    await message.answer(text=str(event.exception))

@router.error(ExceptionTypeFilter(Exception), F.update.message.as_("message"))
async def handle_my_custom_exception(event: ErrorEvent, message: Message):
    reply_text='произошла ошибка'
    await message.answer(text=reply_text)

@router.error()
async def error_handler(event: ErrorEvent):
    pass
