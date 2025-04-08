from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from databases.database_main import Database
from keyboards.setting_keyboard import create_inline_setting_keyboard
from lexicon.commands_lexicon import INLINE_SETTINGS_COMMANDS_LEXICON
from lexicon.main_lexicon import MAIN_COMMANDS_DESCRIPTION_LEXICON

router_standard_command = Router()


@router_standard_command.message(CommandStart())
async def start_command(message: Message, db: Database):
    duty = await db.schedule.get_all_duty_persons(session=db.session, id_chat=str(message.chat.id))
    if not duty:
        await message.answer(
            f'{MAIN_COMMANDS_DESCRIPTION_LEXICON['/start']['base']}{'\n' * 2}{MAIN_COMMANDS_DESCRIPTION_LEXICON['/start']['no_register']}',
            reply_markup=create_inline_setting_keyboard(**INLINE_SETTINGS_COMMANDS_LEXICON))
