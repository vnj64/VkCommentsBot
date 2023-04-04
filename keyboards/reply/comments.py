from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


comments_variables = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton('Добавить пост ✍'),
            KeyboardButton('Посмотреть комментарии 📓')
        ]
    ]
)