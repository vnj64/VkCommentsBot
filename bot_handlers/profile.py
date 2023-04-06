from aiogram import types, Dispatcher
from keyboards.reply.main_menu import back_main_menu


async def generate_profile_text(user_id: int, username: str):
    text = f"""
        🔑 ID: {user_id}\n👤 Никнейм: {f'@{username}' if username else 'Отсутствует'}
    """

    return text


async def profile(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    text = await generate_profile_text(user_id=user_id, username=username)

    await message.answer(text, reply_markup=back_main_menu)


def register_profile(dp: Dispatcher):
    dp.register_message_handler(profile, text='Профиль 📝')
