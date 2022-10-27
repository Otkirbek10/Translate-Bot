from aiogram.dispatcher.filters.state import State,StatesGroup


class Translate(StatesGroup):
    lang = State()
    trans = State()
    voice = State()