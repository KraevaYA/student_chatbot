from telegram import Update
from telegram.ext import ContextTypes
from datetime import date, timedelta

from utils import *
from config import *


def generate_timetable_response(query: str) -> str:
    """
    Формирует текстовый ответ на пользовательский запрос,
    инициированный вводом команды /timetable в чат-боте.
    При генерации учитывается входной параметр, который определяет,
    на какой день (today или tomorrow) или неделю (week и nextweek)
    необходимо вывести расписание учебных занятий студенту.
    По умолчанию значение параметра равно today.
    
    Если вводится допустимый параметр, тогда формируется расписание для заданного периода.
    Иначе выводится сообщение о том, что расписание отсутствует на указанный период,
    или введен неверный параметр.
    
    Parameters
    ----------
    query : str
        Параметр команды.
    
    Returns
    -------
    response : str
        Текст ответа, готовый для отправки пользователю.
    """

    response = ""
    
    # INSERT YOUR CODE

    return response


async def timetable_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    if context.args:
        query = context.args[0].lower()
    else:
        query = "today" # параметр по умолчанию
    
    response = generate_timetable_response(query)

    await update.message.reply_text(response, parse_mode='Markdown')
