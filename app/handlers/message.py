from telegram import Update
from telegram.constants import ParseMode
from groq import Groq

from dotenv import load_dotenv
import os

from app.enums.params import ContextParams
from app.handlers.menu import create_back_menu

load_dotenv()

chatbot = Groq(api_key=os.getenv("AI_API_KEY"))
model = os.getenv("AI_MODEL")


def send_prompt(message: str) -> str:
    chat_completion = chatbot.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model=model,
    )

    return chat_completion.choices[0].message.content


async def on_prompt(update: Update, context):
    text = update.message.text
    response = send_prompt(text)

    sent_message = await context.bot.edit_message_text(
        text=f"**Prompt:**\n{text}\n\n**Response:**\n{response}",
        chat_id=context.user_data[ContextParams.CHAT_ID.value],
        message_id=context.user_data[ContextParams.MESSAGE_ID.value],
        reply_markup=create_back_menu(),
        parse_mode=ParseMode.MARKUP,
    )

    context.user_data[ContextParams.MESSAGE_ID.value] = sent_message.message_id


async def on_unknown_message(update: Update, context):
    await update.message.reply_text("Please use the menu above")


async def handle_message(update: Update, context):
    if context.user_data.get(ContextParams.PROMPT_EXPECTED.value):
        await on_prompt(update, context)
    else:
        await on_unknown_message(update, context)
