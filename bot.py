from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import API_TOKEN
from bot_methods import start, help, echo, error, voice

def bot():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_handler(MessageHandler(Filters.voice, voice, run_async=True))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()