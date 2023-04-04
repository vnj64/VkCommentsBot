import datetime

from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from models.users import User


class DbMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ['error', 'update']

    async def pre_process(self, obj, data, *args):
        session_maker = obj.bot.get('db')
        date = datetime.datetime.now()
        user = await User.get_user(session_maker=session_maker, telegram_id=obj.from_user.id)
        if not user:
            user = await User.add_user(
                session_maker,
                telegram_id=obj.from_user.id,
                fullname=obj.from_user.full_name,
                username=obj.from_user.username,
                date=date
            )
        await User.update_username_fullname(session_maker=session_maker, telegram_id=obj.from_user.id,
                                            username=obj.from_user.username, fullname=obj.from_user.full_name)
        data['user'] = data