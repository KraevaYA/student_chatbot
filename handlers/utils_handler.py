from telegram import Update
from telegram.ext import ContextTypes

from utils import *


def generate_start_response(username: str, botname: str) -> str:

    # INSERT YOUR CODE
    
    return response


def generate_help_response(botname: str) -> str:

    # INSERT YOUR CODE
                
    return response


def generate_about_response(botname: str) -> str:

    # INSERT YOUR CODE
                
    return response


def generate_unknown_command_response(command: str) -> str:

    # INSERT YOUR CODE
    
    return response


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    username = get_username(update)
    botname = await get_botname(context)
    response = generate_start_response(username, botname)

    await update.message.reply_text(response)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    botname = await get_botname(context)
    response = generate_help_response(botname)
                 
    await update.message.reply_text(response, parse_mode='HTML')


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    botname = await get_botname(context)
    response = generate_about_response(botname)
                  
    await update.message.reply_text(response, parse_mode='Markdown')


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    response = generate_unknown_command_response(update.message.text)
    
    await update.message.reply_text(response)
