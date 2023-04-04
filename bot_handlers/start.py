from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.reply.main_menu import main_menu


async def start(message: types.Message, state: FSMContext):
    is_state = await state.get_state()
    if is_state:
        await state.finish()

    text = [
        "Спасибо, что выбрали нас!",
        "Выберите в меню, что хотите сделать."
    ]

    await message.answer('\n'.join(text), reply_markup=main_menu)


async def back_main(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Главное меню', reply_markup=main_menu)


def register_start(dp: Dispatcher):
    dp.register_message_handler(start, Command(['start']), state='*')
    dp.register_message_handler(back_main, state='*', text='⏪Назад')
