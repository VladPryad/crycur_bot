import logging
from nlp import nlp
from query_builder import queryBuilder

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Just send voice!')


def help(update, context):
    update.message.reply_text('Help me!')


def echo(update, context):
    result = queryBuilder(update.message.text)

    update.message.reply_text(result, parse_mode='MarkdownV2')

def voice(update, context):
    bot = context.bot;
    file = bot.getFile(update.message.voice.file_id)
    result = nlp(file)
    update.message.reply_text(result, parse_mode='MarkdownV2')


def error(update, context):
    logger.warning('Update object caused error "%s"', context.error)