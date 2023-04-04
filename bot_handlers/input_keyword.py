from aiogram import types, Dispatcher
from states.keyword_state import KeywordState


async def get_keyword(message: types.Message):
    await message.answer("Введите ключевое слово: ")
    await KeywordState.keyword.set()


def register_get_keyword(dp: Dispatcher):
    dp.register_message_handler(get_keyword, text='Добавить ключевое слово 📔')