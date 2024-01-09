from bot.data.config import GROUP_ID
from bot.loader import bot

from aiogram import types
from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsUserSubscribed(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        user_id = message.from_user.id
        chat_member = await bot.get_chat_member(chat_id=GROUP_ID, user_id=user_id)
        if isinstance(chat_member, types.ChatMemberLeft):
            return False
        return True
