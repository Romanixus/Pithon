from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import game

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hello\n/calc')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    calc = eval(update.message.text.split()[1])
    await update.message.reply_text(f'{update.message.text.split()[1]}={calc}')

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(game.print_field())