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

# Глобальные настройки логгера.
logging.basicConfig(
    format=consts.LOGGING_FORMAT,
    level=logging.INFO,
    filename=consts.LOG_FILE_NAME,
    filemode=consts.FILE_MODE
)

# Логгер модуля (?).
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
    # В ответ на команду /start
    # будет отправлено сообщение 'Спасибо, что включили меня'
    chat = update.effective_chat
    name = update.message.chat.first_name
    # Каждый вложенный список определяет
    # новый ряд кнопок в интерфейсе бота.
    # Здесь описаны две кнопки в первом ряду и одна - во втором.
    # buttons = ReplyKeyboardMarkup([
    #     [consts.SHOW_CAT_PHOTO_BUTTON],
    #     [consts.SHOW_HOUR_BUTTON],
    #     [consts.IP_DEFINE_BUTTON],
    #     [consts.RANDOM_DIGIT_BUTTON]
    # ])

    # За счёт параметра resize_keyboard=True
    # сделаем кнопки поменьше
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
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    logger.info(update)
    # В ответ на любое текстовое сообщение
    # будет отправлено 'Привет, я KittyBot!'
    context.bot.send_message(
        chat_id=chat.id,
        text=consts.ANSWER_TEXT_FOR_EVERYTHING
    )


def main():
    updater = Updater(token=consts.TOKEN)
    # Чтобы всё работало,
    # как задумано — CommandHandler должен
    # стоять в коде выше,
    # чем обработчик для текстовых сообщений
    updater.dispatcher.add_handler(
        CommandHandler(consts.START_BUTTON, start_bot)
    )
    updater.dispatcher.add_handler(
        CommandHandler(consts.NEW_CAT_BUTTON, new_cat)
    )

    # Регистрируется обработчик MessageHandler;
    # из всех полученных сообщений он будет
    # выбирать только текстовые сообщения
    # и передавать их в функцию say_hi()
    updater.dispatcher.add_handler(
        MessageHandler(Filters.text, say_hi)
    )

    # Метод start_polling() запускает процесс polling,
    # приложение начнёт отправлять регулярные
    # запросы для получения обновлений.
    updater.start_polling()

    # Бот будет работать до тех пор, пока не нажмете Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
