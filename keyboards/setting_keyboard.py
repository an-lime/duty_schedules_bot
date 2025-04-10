from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_inline_setting_keyboard(lexicon: dict[str:], *args: str, width: int = 1,
                                   **kwargs: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    if args:
        for button in args:
            buttons.append(
                InlineKeyboardButton(
                    text=lexicon[
                        button] if button in lexicon else button,
                    callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text, callback_data=button))

    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()


def create_inline_duty_lists_keyboard(duty_list_all) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='Создать список', callback_data='create_duty_list')]

    for duty_list in duty_list_all:
        buttons.append(InlineKeyboardButton(text=duty_list.title, callback_data=f"show_duty_list_{duty_list.id}"))

    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()
