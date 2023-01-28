from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5593501461:AAEsF9GTIn60ZP-pZj6e9MW4AVkaY7WaOeQ").build()

app.add_handler(CommandHandler("hello", hello))
print('Bot is activated!')
app.run_polling()