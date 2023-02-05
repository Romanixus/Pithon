from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import token
from commands import *


app = ApplicationBuilder().token(token).build()
print('Server start\nCtrl+C to end')

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))

app.add_handler(CommandHandler("calc", calc))
app.add_handler(CommandHandler("anekdot", anekdot))

app.run_polling()
print('end.')