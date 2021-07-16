import os
token = open(os.environ["HOME"] + "/.local/secret/telegram_token","r").read().strip()

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Ciao " + update.effective_user.name + " e benvenuto!!!")


updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
