from aiogram.dispatcher.filters.state import State, StatesGroup


class TokenState(StatesGroup):
    token = State()
