from aiogram.dispatcher.filters.state import StatesGroup, State


class IdState(StatesGroup):
    telegram_id = State()
