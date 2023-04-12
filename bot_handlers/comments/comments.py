from aiogram import types, Dispatcher

from keyboards.reply.comments import comments_variables


async def check_variables(message: types.Message):
    await message.answer("Что хотите сделать?", reply_markup=comments_variables)


def register_variables_handler(dp: Dispatcher):
    dp.register_message_handler(check_variables, text="Комментарии 📓")
