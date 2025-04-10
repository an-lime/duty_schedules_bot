from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.commands_lexicon import COMMANDS_LEXICON


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in COMMANDS_LEXICON.items()
    ]
    await bot.set_my_commands(main_menu_commands)
