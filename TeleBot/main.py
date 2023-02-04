from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import token
from commands import *


app = ApplicationBuilder().token(token).build()
print('Server start')

app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("calc", calc))
app.add_handler(CommandHandler("game", game))

app.run_polling()
print('end.')