from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Ciao " + update.effective_user.name + " e benvenuto!!!")


updater = Updater('1723752355:AAHolWxexkvvnujPJjzk0hgwG8c4a6l_yHo')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()