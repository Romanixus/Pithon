from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bs4 import BeautifulSoup as bs
import requests

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name} \n/help')    

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/calc (выражение)\n/anekdot (количество)')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    calc = eval(update.message.text.split()[1])
    await update.message.reply_text(f'{update.message.text.split()[1]}={calc}')

async def anekdot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    r = requests.get("https://www.anekdot.ru/random/anekdot/")
    soup = bs(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    text_anekdots = [c.text for c in anekdots]
    await update.message.reply_text(f'{text_anekdots[0]}')
    number = int(update.message.text.split()[1])
    for i in range(1, number):
        await update.message.reply_text(f'{text_anekdots[i]}')