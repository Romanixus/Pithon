from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(eval(update.message.text.split()[1]))

app = ApplicationBuilder().token("").build()
print('begin')
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("calc", calc))

app.run_polling()
print('end.')