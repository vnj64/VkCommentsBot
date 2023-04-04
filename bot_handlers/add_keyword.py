from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from keyboards.reply.main_menu import back_main_menu
from states.keyword_state import KeywordState


async def add_keyword(message: types.Message, state: FSMContext):
    await state.update_data(keyword=message.text)
    data = await state.get_data()
    await message.answer(f"Ваше ключевое слово: {data['keyword']}. Я запомнил.", reply_markup=back_main_menu)
    await state.finish()


def register_add_keyword(dp: Dispatcher):
    dp.register_message_handler(add_keyword, state=KeywordState.keyword, )
