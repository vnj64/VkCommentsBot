from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from config import load_config

from states.comment_state import CommentState
from keyboards.reply.comments import comments_variables

config = load_config('.env')


async def check_comments(message: types.Message):
    await message.answer("Выберите действие: ", reply_markup=comments_variables)


async def add_group(message: types.Message):
    await message.answer("Введите owner_id: ")
    await CommentState.group_id.set()


async def add_post(message: types.Message, state: FSMContext):
    await state.update_data(group=message.text)
    await message.answer("Отлично! Теперь введите post_id: ")
    await CommentState.next()


async def add_count(message: types.Message, state: FSMContext):
    await state.update_data(post=message.text)
    await message.answer("Прелестно. Осталось ввести count: ")
    await CommentState.next()


async def get_comments(message: types.Message, state: FSMContext):
    await state.update_data(count=message.text)
    data = await state.get_data()
    await message.answer(data['group'], data['post'], data['count'])
    await state.finish()


def register_comments(dp: Dispatcher):
    dp.register_message_handler(check_comments, text="Комментарии 📓")
    dp.register_message_handler(add_group, text='Добавить пост ✍️')
    dp.register_message_handler(add_post, state=CommentState.group_id)
    dp.register_message_handler(add_count, state=CommentState.post_id)
    dp.register_message_handler(get_comments, state=CommentState.count)
