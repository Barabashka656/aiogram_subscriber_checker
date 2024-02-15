from contextlib import suppress

from bot.handlers.filters import IsUserSubscribed
from bot.handlers.services import ArticleService
from bot.handlers.article.keyboards import Pagination, articles_kb

from aiogram.filters import Command
from aiogram import F, Router
from aiogram import types
from aiogram.exceptions import TelegramBadRequest

router = Router()
router.message.filter(IsUserSubscribed())
router.callback_query.filter(IsUserSubscribed())

@router.callback_query(Pagination.filter(F.action.in_(['prev', 'next'])))
async def pagination_query(query: types.CallbackQuery, callback_data: Pagination):
    page_num = int(callback_data.page)
    articles = await ArticleService.get_articles()
    if len(articles) % 10 == 0:
        page_count = len(articles) // 10
    else:
        page_count = len(articles) // 10 + 1

    if callback_data.action == 'next':
        if page_num < page_count - 1:
            page = page_num + 1
        else:
            page = 0
    else:
        if page_num > 0:
            page = page_num - 1
        else:
            page = page_count - 1
    reply_text = 'Нажмите на кнопку, чтобы перейти в статью'
    with suppress(TelegramBadRequest):
        await query.message.edit_text(
            text = reply_text,
            reply_markup=articles_kb(articles, page)
        )
    await query.answer()

@router.callback_query(Pagination.filter(F.action == 'None'))
async def pagination_none_query(query: types.CallbackQuery):
    await query.answer()

@router.message(F.text.lower() == "статьи")
@router.message(Command("articles"))
async def show_articles(message: types.Message):
    print(1)
    articles = await ArticleService.get_articles()
    print(articles)
    # return
    if not articles:
        reply_text = 'Пока нет статей'
        return await message.answer(text=reply_text)
        
    reply_text = 'Нажмите на кнопку, чтобы перейти в статью'
    await message.answer(text=reply_text, reply_markup=articles_kb(articles))
