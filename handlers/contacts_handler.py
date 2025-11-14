from telegram import Update
from telegram.ext import ContextTypes

from utils import *
from config import *


def generate_contacts_response(query: str | None) -> str:
    """
    Формирует текстовый ответ на пользовательский запрос,
    инициированный вводом команды /contacts в чат-боте.
    При генерации учитывается входной параметр,
    который обозначает некоторую службу университета,
    контактную информацию о которой запрашивает пользователь.
    
    Если запрашиваемая служба присутствует в справочнике,
    тогда пользователю выводится вся информация о ней.
    В противном случае, генерируется сообщение о том,
    что был введен пользователем неизвестный параметр
    и приводится список допустимых параметров.
    Для случая когда пользователь вводит команду без параметра,
    ему сообщается, что параметр не был введен
    и приводится также список допустимых параметров.
    
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


async def contacts_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    query = context.args[0].capitalize() if context.args else None
    response = generate_contacts_response(query)

    await update.message.reply_text(response, parse_mode='HTML')
