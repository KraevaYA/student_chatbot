from telegram import Update
from telegram.ext import ContextTypes
from transliterate import translit

from utils import *
from config import *


def generate_tutors_info_response(query: str | None) -> str:
    """
    Формирует текстовый ответ на пользовательский запрос,
    инициированный вводом команды /tutors_info в чат-боте.
    При генерации учитывается входной параметр,
    которому задается фамилия куратора.
    
    Если вводится фамилия преподавателя, который не является куратором,
    тогда формируется сообщение о некорректном входном параметре.
    Для случая когда пользователь вводит команду без параметра,
    ему сообщается, что параметр не был введен.
    
    Parameters
    ----------
    query : str | None
        Параметр команды.
    
    Returns
    -------
    response : str
        Текст ответа, готовый для отправки пользователю.
    """

    response = ""
    
    # INSERT YOUR CODE

    return response


async def tutors_info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    query = context.args[0].capitalize() if context.args else None
    response = generate_tutors_info_response(query)
    
    await update.message.reply_text(response, parse_mode='HTML')
