from aiogram import types, Dispatcher
from sqlalchemy.orm import sessionmaker
from keyboards.reply.main_menu import back_main_menu
from db.get_keywords import get_keywords_list


async def check_keywords(message: types.Message):
    text = get_keywords_list()
    await message.answer(text, reply_markup=back_main_menu)


def register_checker(dp: Dispatcher):
    dp.register_message_handler(check_keywords, text='Мои ключевые слова 📔')