from telegram import InlineKeyboardMarkup, Update
from telegram.constants import ParseMode

from app.enums.callbacks import CallbackData
from app.enums.params import ContextParams
from app.utils.keyboard import create_button
from app.handlers.start import create_start_menu


def create_back_menu() -> InlineKeyboardMarkup:
    keyboard = [
        create_button("Back", CallbackData.BACK),
    ]

    return InlineKeyboardMarkup(keyboard)


async def on_student_info(query, context):
    await query.edit_message_text(
        text="Khozhainov Mykola, group IM-21",
        reply_markup=create_back_menu(),
    )


async def on_technologies(query, context):
    await query.edit_message_text(
        text="<b>Technologies:</b> Java, WEB",
        reply_markup=create_back_menu(),
        parse_mode=ParseMode.HTML,
    )


async def on_contacts(query, context):
    await query.edit_message_text(
        text="Phone number: 050-669-69-40\nEmail: kolyakhozhajinov@gmail.com",
        reply_markup=create_back_menu(),
        parse_mode=ParseMode.HTML,
    )


async def on_prompt(query, context):
    await query.edit_message_text(
        text="Please enter your prompt:",
        reply_markup=create_back_menu(),
    )

    context.user_data[ContextParams.MESSAGE_ID.value] = query.message.message_id
    context.user_data[ContextParams.CHAT_ID.value] = query.message.chat_id

    context.user_data[ContextParams.PROMPT_EXPECTED.value] = True


async def on_back(query, context):
    context.user_data[ContextParams.PROMPT_EXPECTED.value] = False
    await query.edit_message_text(
        text="<b>Welcome</b>\nPlease select command:",
        reply_markup=create_start_menu(),
        parse_mode=ParseMode.HTML,
    )


async def handle_menu(update: Update, context):
    query = update.callback_query
    await query.answer()

    data = query.data
    if data == CallbackData.STUDENT_INFO.value:
        await on_student_info(query, context)
    elif data == CallbackData.TECHNOLOGIES.value:
        await on_technologies(query, context)
    elif data == CallbackData.CONTACTS.value:
        await on_contacts(query, context)
    elif data == CallbackData.AI_PROMPT.value:
        await on_prompt(query, context)
    elif data == CallbackData.BACK.value:
        await on_back(query, context)
