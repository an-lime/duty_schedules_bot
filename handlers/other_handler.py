from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message

from databases.database_main import Database
from services.validator import validate_pair
from states.bot_states import BotStates

router_other_command = Router()


@router_other_command.callback_query(F.data == 'set_pair', StateFilter(default_state))
async def set_pair(callback: CallbackData, state: FSMContext):
    await state.set_state(BotStates.set_pair)
    await callback.message.edit_text(
        f'''
Введите список дежурящих в формате:\n
Фамилия1 Фамилия2,
Фамилия3 Фамилия4
        ''')


@router_other_command.message(StateFilter(BotStates.set_pair))
async def set_pair(message: Message, state: FSMContext, db: Database):
    await message.answer("чек консоль")
    await db.schedule.add_pair(id_chat=str(message.chat.id), pairs=validate_pair(message.text), session=db.session)
    await state.set_state(default_state)
