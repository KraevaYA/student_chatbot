from telegram import Update
from telegram.ext import ContextTypes
from datetime import date, timedelta

from utils import *
from config import *


def generate_timetable_response(query: str | None) -> str:

    # INSERT YOUR CODE

    return response


async def timetable_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Выдает расписание на указанный день или на текущую неделю."""
    
    if context.args:
        query = context.args[0].lower()
    else:
        query = "today" # параметр по умолчанию
    
    response = generate_timetable_response(query)

    await update.message.reply_text(response, parse_mode='Markdown')
