from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from handlers import utils_handler, timetable_handler, tutors_info_handler, contacts_handler
from config import *


async def post_init(application: Application) -> None:
    
    bot_info = await application.bot.get_me()
   
    application.bot_data["first_name"] = bot_info.first_name
    application.bot_data["username"] = bot_info.username


def main():
    """Run bot."""
    
    # Создание Application и передача токена бота
    application = Application.builder().token(TOKEN).post_init(post_init).build()
    
    # Регистрация обработчиков команд через CommandHandler
    # Простые утилиты
    application.add_handler(CommandHandler("start", utils_handler.start_command))
    # Реализуйте добавление обработчиков остальных команд по аналогии. Вставьте свой код вместо 'INSERT YOUR CODE'
    # INSERT YOUR CODE
    
    # Команды на основе контекста
    # INSERT YOUR CODE
    
    # Обработчик неизвестных команд (должен быть последним!)
    # INSERT YOUR cODE
    
    # Запуск бота до тех пор, пока пользователь не нажмет Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

