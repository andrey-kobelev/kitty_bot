import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN_TG_BOT')

# Images links
API_CAT_IMAGES_URL = 'https://api.thecatapi.com/v1/images/search'
URL_TO_IMAGE_FOR_START = (
    'https://downloader.disk.yandex.ru/preview/'
    'f6c5976bb2cbbadeb3bd959e0f55ef4355aa35f1b11a5752616b2834a2465332/'
    '656f8cba/WrnA3nTrZYGB0rhdh1HOW56bU1nmDqCwGSVHYHoSLrXgQzZs6SWqV_fgB'
    'UCoPPMB4PEo10Ny1ZNVhviOqfP--w%3D%3D?uid=0&filename=photo_2023-12-0'
    '5_19-44-43.jpg&disposition=inline&hash=&limit=0&content_type=image'
    '%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048'
)
API_DOGS_IMAGES_URL = 'https://api.thedogapi.com/v1/images/search'

# Block for send texts
ANSWER_TEXT_FOR_EVERYTHING = (
    'МЯУ! (Таков ответ на каждое ваше '
    'сообщение - мы же котики!)'
)
TEXT_FOR_START = (
    'Привет, {name}! Мы веселые котята! '
    'Рады видеть Вас! Мяу!!!'
)

# Buttons
SHOW_CAT_PHOTO_BUTTON = 'Показать фото котика!'
SHOW_HOUR_BUTTON = 'Который час?'
IP_DEFINE_BUTTON = 'Определи мой IP'
RANDOM_DIGIT_BUTTON = '/random_digit'
START_BUTTON = 'start'
NEW_CAT_BUTTON = 'newcat'

# For logging
LOG_FILE_NAME = 'main.log'
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
MAX_BYTES = 50000000
BACKUP_COUNT = 5
API_ERROR = 'Ошибка при запросе к основному API: {error}'
FILE_MODE = 'a'
