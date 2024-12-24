import logging
from logging.handlers import RotatingFileHandler

from telegram.ext import (
    Updater,
    Filters,
    MessageHandler,
    CommandHandler
)
from telegram import ReplyKeyboardMarkup
import requests

import constants as consts

logging.basicConfig(
    format=consts.LOGGING_FORMAT,
    level=logging.INFO,
    filename=consts.LOG_FILE_NAME,
    filemode=consts.FILE_MODE
)

logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    consts.LOGGING_FORMAT
)
handler = RotatingFileHandler(
    consts.LOG_FILE_NAME,
    maxBytes=consts.MAX_BYTES,
    backupCount=consts.BACKUP_COUNT
)
logger.addHandler(handler)
handler.setFormatter(formatter)


def get_new_image():
    try:
        response = requests.get(consts.API_CAT_IMAGES_URL)
    except Exception as err:
        logger.error(consts.API_ERROR.format(error=err))
        response = requests.get(consts.API_DOGS_IMAGES_URL)
    response = response.json()
    random_image = response[0].get('url')
    return random_image


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def start_bot(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup(
        [[f'/{consts.NEW_CAT_BUTTON}']],
        resize_keyboard=True
    )
    logger.info(update)
    context.bot.send_message(
        chat_id=chat.id,
        text=consts.TEXT_FOR_START.format(name=name),
        reply_markup=button
    )
    context.bot.send_photo(chat.id, consts.URL_TO_IMAGE_FOR_START)


def say_hi(update, context):
    chat = update.effective_chat
    logger.info(update)
    context.bot.send_message(
        chat_id=chat.id,
        text=consts.ANSWER_TEXT_FOR_EVERYTHING
    )


def main():
    updater = Updater(token=consts.TOKEN)
    updater.dispatcher.add_handler(
        CommandHandler(consts.START_BUTTON, start_bot)
    )
    updater.dispatcher.add_handler(
        CommandHandler(consts.NEW_CAT_BUTTON, new_cat)
    )
    updater.dispatcher.add_handler(
        MessageHandler(Filters.text, say_hi)
    )
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
