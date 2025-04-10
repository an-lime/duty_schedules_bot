from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message

from databases.database_main import Database
from handlers.main_commands_handler import start_command
from services.validator import validate_pair
from states.bot_states import BotStates

router_other_command = Router()


@router_other_command.callback_query(F.data == 'create_duty_list', StateFilter(default_state))
async def create_duty_list(callback: CallbackData, state: FSMContext):
    await state.set_state(BotStates.set_pair)
    await callback.message.edit_text(
        f'''
Введите список дежурящих в формате:\n
Фамилия1 Фамилия2,
Фамилия3 Фамилия4
        ''')


@router_other_command.message(StateFilter(BotStates.set_pair))
async def set_pair(message: Message, state: FSMContext):
    pairs = validate_pair(message.text)
    await state.update_data(pairs=pairs)
    await state.set_state(BotStates.set_title_pair_list)
    await message.answer('Отправьте название списка:')


@router_other_command.message(StateFilter(BotStates.set_title_pair_list))
async def set_title_pair_list(message: Message, state: FSMContext, db: Database):
    await state.update_data(title=message.text)
    await state.update_data(admins=message.from_user.id)
    await db.duty_lists.add_pair(await state.get_data(), db.session)
    await state.clear()
    await state.set_state(default_state)
    await message.answer('Готово!')
    await start_command(message=message, db=db)
