import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from middlewares.db import DbMiddleware
from bot_handlers.start import register_start
from bot_handlers.profile import register_profile
from bot_handlers.input_keyword import register_get_keyword
from bot_handlers.add_keyword import register_add_keyword
from bot_handlers.get_keywords import register_checker
from bot_handlers.comments import register_variables_handler
from bot_handlers.add_post import register_group_add
from config import load_config
from db.tg_db import create_db_session

logger = logging.getLogger(__name__)


def register_all_middlewares(dp: Dispatcher):
    dp.setup_middleware(DbMiddleware())


def register_all_handlers(dp):
    register_start(dp)
    register_profile(dp)
    register_get_keyword(dp)
    register_add_keyword(dp)
    register_checker(dp)
    register_variables_handler(dp)
    register_group_add(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )
    config = load_config('.env')
    bot = Bot(token=config.bot.token, parse_mode='HTML')

    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config
    bot['dp'] = dp
    try:
        bot['db'] = await create_db_session(config)
        logger.info('db started')
    except Exception as e:
        logger.error(f'db can`t start cause: {e}')

    register_all_middlewares(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
        logger.info('Bot started!')
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')
