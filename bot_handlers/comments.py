from aiogram import types, Dispatcher

from keyboards.reply.comments import comments_variables


async def check_comments(message: types.Message):
    await message.answer("Выберите действие: ", reply_markup=comments_variables)


def register_comments(dp: Dispatcher):
    dp.register_message_handler(check_comments, text="Комментарии 📓")
