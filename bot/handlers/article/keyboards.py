from bot.handlers.callback_datas import MenuCallback
from bot.handlers.schemas import Article

from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Pagination(CallbackData, prefix='pag'):
    action: str
    page: int

def articles_kb(articles: list[Article], page: int = 0):
    builder = InlineKeyboardBuilder()
    if len(articles) % 10 == 0:
        page_count = len(articles) // 10
    else:
        page_count = len(articles) // 10 + 1
    articles.reverse()
    for article in articles[page*10:(page+1)*10]:
        builder.button(text=article.title, url=article.link)
    builder.adjust(2)
    builder.row(
        InlineKeyboardButton(
            text='⬅️', 
            callback_data=Pagination(
                action='prev', page=page
            ).pack()
        ),
        InlineKeyboardButton(
            text=f'{page+1}/{page_count}',
            callback_data=Pagination(
                action='None', page=0
            ).pack()
        ),
        InlineKeyboardButton(
            text='➡️', 
            callback_data=Pagination(
                action='next', page=page
            ).pack()
        ),
        width=3
    )
    return builder.as_markup(resize_keyboard=True, selective=True)
    
balance_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Реферальная ссылка", 
                callback_data=MenuCallback(handler='balance', level='1').pack()
            )
        ]
    ],
    resize_keyboard=True,
    selective=True
)
