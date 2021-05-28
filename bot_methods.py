import logging
from nlp import nlp

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hi!')


def help(update, context):
    update.message.reply_text('Help!')


def echo(update, context):
    update.message.reply_text(update.message.text)

def voice(update, context):
    bot = context.bot;
    file = bot.getFile(update.message.voice.file_id)
    update.message.reply_text("Processing...")

    result = nlp(file)
    update.message.reply_text(result)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)