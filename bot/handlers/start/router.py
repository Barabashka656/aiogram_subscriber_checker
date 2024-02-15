from aiogram.exceptions import TelegramBadRequest
from bot.data.config import ADMINS, GROUP_ID
from bot.handlers.filters import IsUserSubscribed
from bot.handlers.services import UserService
from bot.loader import bot

from aiogram import F, Router
from aiogram import types
from aiogram.filters import KICKED, ChatMemberUpdatedFilter, CommandObject, CommandStart
from aiogram.fsm.context import FSMContext   


router = Router()
router.message.filter()
    
@router.message(CommandStart(), IsUserSubscribed())
async def start(message: types.Message):
    print(message.from_user.id)
    await UserService.new_user(message.from_user.id)
    reply_text = "Напишите 'статьи' или /articles,\nчтобы прочитать статьи"
    await message.answer(reply_text)

@router.message(CommandStart())
async def start(message: types.Message):
    print(message.from_user.id)
    await UserService.new_user(message.from_user.id)
    reply_text = f"Подпишитесь на группу {GROUP_ID}, чтобы увидеть статьи\n" + \
        "а потом введите команду /start"
    await message.answer(reply_text)

@router.my_chat_member(
    ChatMemberUpdatedFilter(member_status_changed=KICKED)
)
async def user_blocked_bot(event: types.ChatMemberUpdated):
    await UserService.deactivate_user(event.from_user.id)

