from aiogram import types, Dispatcher

from models.post import Post
from api_handlers.checker import comments_getter


async def get_comments(message: types.Message):
    session_maker = message.bot.get('db')
    comments = await Post.get_post_info(session_maker=session_maker, telegram_id=message.from_user.id)
    for i in comments:
        await message.answer(comments_getter(i[0], i[1]))


def register_get_comments(dp: Dispatcher):
    dp.register_message_handler(get_comments, text='Посмотреть комментарии 📓')
