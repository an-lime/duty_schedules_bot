from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from databases.database_main import Database
from keyboards.setting_keyboard import create_inline_duty_lists_keyboard
from lexicon.main_lexicon import MAIN_COMMANDS_DESCRIPTION_LEXICON

router_standard_command = Router()


@router_standard_command.message(CommandStart())
async def start_command(message: Message, db: Database):
    if message.chat.type == 'private':
        duty_list_all = await db.duty_lists.get_duty_list_for_current_admin(str(message.from_user.id), db.session)
        await message.answer(
            f'{MAIN_COMMANDS_DESCRIPTION_LEXICON['/start']}',
            reply_markup=create_inline_duty_lists_keyboard(duty_list_all))
