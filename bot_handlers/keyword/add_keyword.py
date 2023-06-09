from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from keyboards.reply.main_menu import back_main_menu
from models.keywords import Keyword
from states.keyword_state import KeywordState


async def add_keyword(message: types.Message, state: FSMContext):
    await state.update_data(keyword=str(message.text).split())
    data = await state.get_data()
    word = f"{data['keyword']}"
    session_maker = message.bot.get('db')
    if len(word) < 2:
        await message.answer(f"Ваше ключевое слово: {data['keyword']}. Я запомнил.", reply_markup=back_main_menu)
        await Keyword.add_keyword(session_maker=session_maker, telegram_id=message.from_user.id, keyword=word)
    else:
        await message.answer(f"Ваши ключевые слова: {data['keyword']}. Я запомнил.", reply_markup=back_main_menu)
        await Keyword.add_keyword(session_maker=session_maker, telegram_id=message.from_user.id, keyword=word)
    await state.finish()


def register_add_keyword(dp: Dispatcher):
    dp.register_message_handler(add_keyword, state=KeywordState.keyword)
