from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from keyboards.inline.comments import comment_methods, add_post, check_comments
from keyboards.reply.main_menu import back_main_menu
from states.comment_state import CommentState
from models.post import Post

from api_handlers.checker import comments_getter


async def get_post_variables(message: types.Message):
    await message.answer("Что хотите сделать?", reply_markup=comment_methods)


async def add_group(callback: types.CallbackQuery):
    await callback.message.answer("Введите group_id: ")
    await CommentState.group_id.set()


async def return_group_id(message: types.Message, state: FSMContext):
    await state.update_data(group=message.text)
    await message.answer("Теперь введите post_id")
    await CommentState.next()


async def all_rdy(message: types.Message, state: FSMContext):
    await state.update_data(post=message.text)
    data = await state.get_data()
    session_maker = message.bot.get('db')

    await message.answer(comments_getter(f"{data['group']}", f"{data['post']}"), reply_markup=back_main_menu)
    await Post.add_post_info(session_maker=session_maker, telegram_id=message.from_user.id,
                             owner_id=data['group'], post_id=data['post'])
    await state.finish()


async def get_cmnts(callback: types.CallbackQuery):
    session_maker = callback.bot.get('db')
    comments = await Post.get_post_info(session_maker=session_maker, telegram_id=callback.from_user.id)
    for comment in comments:
        await callback.message.answer(comments_getter(comment[0], comment[1]))


def register_group_add(dp: Dispatcher):
    dp.register_message_handler(get_post_variables, text='Комментарии 📓')
    dp.register_callback_query_handler(add_group, add_post.filter())
    dp.register_message_handler(return_group_id, state=CommentState.group_id)
    dp.register_message_handler(all_rdy, state=CommentState.post_id)
    dp.register_callback_query_handler(get_cmnts, check_comments.filter())
