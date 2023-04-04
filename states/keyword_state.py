from aiogram.dispatcher.filters.state import State, StatesGroup


class KeywordState(StatesGroup):
    keyword = State()
