from aiogram.fsm.state import StatesGroup, State

class AdminState(StatesGroup):
    add_title = State()
    add_link = State()
    delete_article = State()
