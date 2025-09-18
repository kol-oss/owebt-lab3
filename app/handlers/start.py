from telegram import InlineKeyboardMarkup, Update
from telegram.constants import ParseMode

from app.enums.callbacks import CallbackData
from app.utils.keyboard import create_button


def create_start_menu() -> InlineKeyboardMarkup:
    keyboard = [
        create_button("Student", CallbackData.STUDENT_INFO),
        create_button("Technologies", CallbackData.TECHNOLOGIES),
        create_button("Contacts", CallbackData.CONTACTS),
        create_button("Prompt", CallbackData.AI_PROMPT),
    ]

    return InlineKeyboardMarkup(keyboard)


async def handle_start(update: Update, context):
    menu = create_start_menu()

    await update.message.reply_text(
        "<b>Welcome</b>\nPlease select command:",
        reply_markup=menu,
        parse_mode=ParseMode.HTML,
    )
