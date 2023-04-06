from aiogram import types, Dispatcher
from models.keywords import Keyword


async def check_keywords(message: types.Message):
    session_maker = message.bot.get('db')
    keywords = await Keyword.get_keyword(session_maker=session_maker, telegram_id=message.from_user.id)
    lst = [keyword[0] for keyword in keywords]
    await message.answer('\n'.join(lst))


def register_checker(dp: Dispatcher):
    dp.register_message_handler(check_keywords, text='Мои ключевые слова 📔')