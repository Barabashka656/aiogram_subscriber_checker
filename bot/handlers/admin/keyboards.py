from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="Добавить статью"
            ),
            KeyboardButton(
                text="Удалить статью"
            )
        ],
        [
            KeyboardButton(
                text="Статьи"
            )
        ]
    ],
    resize_keyboard=True,
    selective=True
)
