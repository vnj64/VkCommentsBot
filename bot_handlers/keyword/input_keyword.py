from aiogram import types, Dispatcher

from keyboards.reply.main_menu import back_main_menu
from states.keyword_state import KeywordState


async def get_keyword(message: types.Message):
    await message.answer("Введите ключевые слова через пробел: ", reply_markup=back_main_menu)
    await KeywordState.keyword.set()


def register_get_keyword(dp: Dispatcher):
    dp.register_message_handler(get_keyword, text='Добавить ключевое слово 📔', state='*')
