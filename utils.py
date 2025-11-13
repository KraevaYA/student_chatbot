from telegram import Update 
from telegram.ext import ContextTypes
import json


def get_username(update: Update) -> str:
    user = update.effective_user
    username = user.username

    if (username == None):
        if (user.last_name != None):
            username = user.first_name + " " + user.last_name
        else:
            username = user.first_name

    return username


async def get_botname(context: ContextTypes.DEFAULT_TYPE) -> str:
    
    botname = context.application.bot_data.get("username", "неизвестное имя")
    
    return botname


def load_json_file(file_path: str) -> dict:
    """Загружает данные из json файла."""
    
    # INSERT YOUR CODE
