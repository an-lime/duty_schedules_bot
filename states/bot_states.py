from aiogram.fsm.state import StatesGroup, State


class BotStates(StatesGroup):
    set_pair = State()
    set_title_pair_list = State()
