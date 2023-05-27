# Reminder Bot

Этот проект помогает сохранять напоминания в базе данных при помощи телеграмм бота, 
Также предоставляет простой REST API для обращений к базе данных и извлечения или добавления напоминаний.



## Установка

1. Клонировать репозиторий:
    ```shell
   git clone https://github.com/DashaMarchenko/reminder_bot
   
2. Установка библиотек и модулей:
    ```shell
   pip install -r requirements.txt

3. Создание и активация виртуального окружения (Windows):
    ```shell
   python -m venv venv
   cd venv/Scripts
   activate.bat
   
4. Изменения в config/config.ini:
* **BOT_TOKEN** - Токен бота полученный у @BotFather
* **HOST_URL** - ссылка на домен
* **ADMIN_ID** - ID администратора бота telegram
* **TIMEDELTA** - Отклонение локального времени от северного (в часах)

## Запуск проекта

Запуск app/main.py:
```shell
uvicorn app.main: app --reload
```

