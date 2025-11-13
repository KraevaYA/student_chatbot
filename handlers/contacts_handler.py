from telegram import Update
from telegram.ext import ContextTypes

from utils import *
from config import *


def generate_contacts_response(query: str | None) -> str:

    # INSERT YOUR CODE
    
    return response


async def contacts_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    query = context.args[0].capitalize() if context.args else None
    response = generate_contacts_response(query)

    await update.message.reply_text(response, parse_mode='HTML')
