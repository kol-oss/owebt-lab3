from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    filters,
)
from dotenv import load_dotenv
import os

from app.handlers.start import handle_start
from app.handlers.menu import handle_menu
from app.handlers.message import handle_message

load_dotenv()

app = Application.builder().token(os.getenv("TG_BOT_TOKEN")).build()

app.add_handler(CommandHandler("start", handle_start))
app.add_handler(CallbackQueryHandler(handle_menu))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

app.run_polling()
