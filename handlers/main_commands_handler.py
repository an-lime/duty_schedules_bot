from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from databases.database_main import Database
from lexicon.main_lexicon import MAIN_COMMANDS_LEXICON

router_standard_command = Router()


@router_standard_command.message(CommandStart())
async def start_command(message: Message, db: Database):
    duty = await db.schedule.get_all_duty_persons(session=db.session, id_chat=str(message.chat.id))
    if not duty:
        await message.answer(
            f'{MAIN_COMMANDS_LEXICON['/start']['base']}{'\n' * 2}{MAIN_COMMANDS_LEXICON['/start']['no_register']}')
