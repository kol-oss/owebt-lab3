from telegram import InlineKeyboardButton
from app.enums.callbacks import CallbackData


def create_button(name: str, callback_data: CallbackData) -> list[InlineKeyboardButton]:
    return [InlineKeyboardButton(name, callback_data=callback_data.value)]
