from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.commands_lexicon import INLINE_SETTINGS_COMMANDS_LEXICON


def create_inline_setting_keyboard(*args: str, width: int = 1, **kwargs: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    if args:
        for button in args:
            buttons.append(
                InlineKeyboardButton(
                    text=INLINE_SETTINGS_COMMANDS_LEXICON[
                        button] if button in INLINE_SETTINGS_COMMANDS_LEXICON else button,
                    callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text, callback_data=button))

    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()
