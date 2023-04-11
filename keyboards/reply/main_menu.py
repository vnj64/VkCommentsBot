from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton('Добавить ключевое слово 📔'),
            KeyboardButton('Мои ключевые слова 📔'),
        ],
        [
            KeyboardButton('Профиль 📝'),
            KeyboardButton('Комментарии 📓')
        ],
        [
            KeyboardButton('access_token 🔐')
        ]
    ]
)

back_main_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton('⏪Назад')
        ]
    ]
)