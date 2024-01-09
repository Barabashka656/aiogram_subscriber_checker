from bot.data.config import ADMINS
from bot.handlers.admin.states import AdminState
from bot.handlers.services import ArticleService, UserService
from bot.loader import bot
from bot.handlers.admin.keyboards import admin_kb
from bot.handlers.article.keyboards import articles_kb

from aiogram.enums import ContentType
from aiogram import F, Router
from aiogram import types
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext   



router = Router()
router.message.filter(F.from_user.id.in_(ADMINS))

@router.message(CommandStart())
async def admin(message: types.Message):
    await message.answer('Выберите действие', reply_markup=admin_kb)
    await UserService.new_user(message.from_user.id)

@router.message(AdminState.delete_article, F.content_type == ContentType.TEXT)
async def admin(message: types.Message, state: FSMContext):
    reply_text = await ArticleService.delete_article(message.text)
    await message.answer(reply_text, reply_markup=admin_kb)
    await state.clear()

@router.message(AdminState.add_link)
async def admin(message: types.Message, state: FSMContext):
    await message.answer('Введите заголовок статьи')
    await state.update_data(link=message.text)
    await state.set_state(AdminState.add_title)

@router.message(AdminState.add_title)
async def admin(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    is_article_added = await ArticleService.add_article(message.text, user_data.get('link'))
    if not is_article_added:
        reply_text = 'Статья с таким заголовком или ссылкой уже есть'
        await message.answer(reply_text, reply_markup=admin_kb)

    users = await UserService.get_all_users()
    articles = await ArticleService.get_articles()
    for user in users:
        await bot.send_message(
            chat_id=user.user_id, 
            text='Добавлена новая статья', 
            reply_markup=articles_kb(articles)
        )
    await state.clear()

@router.message(StateFilter(None), F.text == 'Добавить статью')
async def admin(message: types.Message, state: FSMContext):
    await message.answer('Введите ссылку на статью')
    await state.set_state(AdminState.add_link)
    
@router.message(StateFilter(None), F.text == 'Удалить статью')
async def admin(message: types.Message, state: FSMContext):
    await message.answer('Введите ссылку или заголовок статьи')
    await state.set_state(AdminState.delete_article) 
