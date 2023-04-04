from aiogram.dispatcher.filters.state import State, StatesGroup


class CommentState(StatesGroup):
    group_id = State()
    post_id = State()
    count = State