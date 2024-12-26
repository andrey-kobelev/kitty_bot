# Kitty Bot

> **Kitty Bot** - это не просто бот, а радость для души! Ведь ни что так не радует, как картинки с котиками! Среди котиков может затеряться одинокая собачка, пожалуйста, не оставляйте ее без внимания =))

### Как развернуть проект локально и запустить

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/andrey-kobelev/kitty_bot.git
```

```
cd kitty_bot
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env  
```

```
source env/bin/activate  
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip  
```

```
pip install -r requirements.txt  
```

Файл .env должен содержать одну переменную TOKEN_TG_BOT - разместите этот файл в корне проекта. Создайте бота и получите токен через BotFather в telegram, полученный токен присвойте переменной TOKEN_TG_BOT.

Далее запустить бот: 

```
python main.py 
```

### Автор проекта:  
* [Kobelev Andrey](https://github.com/andrey-kobelev)

### Стек

[ Python 3.9](https://www.python.org/downloads/release/python-390/)

[python-telegram-bot](https://docs.python-telegram-bot.org/en/v21.9/)