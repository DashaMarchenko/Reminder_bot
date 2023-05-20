import logging
from functools import wraps

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from cachetools import TTLCache

from config import load_config
from database.sqlite_db import SQLiteDB

storage = MemoryStorage()
logger = logging.getLogger(__name__)

config = load_config(r'C:\Users\HP\PycharmProjects\reminder_bot\config\config.ini')

TOKEN = config.tg_bot.BOT_TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

DB = SQLiteDB()


def antispam(rate: int, interval: int, mess: str = 'Слишком много запросов'):
    """Антиспам декоратор

    :param rate: лимит сообщений
    :param interval: промежуток времени
    :param mess: сообщение которое будет отправлено при превышении заданного лимита
    :return:
    """
    cache = TTLCache(maxsize=rate, ttl=interval)

    def decorator(func):
        @wraps(func)
        async def wrapped(message: types.Message, state: FSMContext, *args, **kwargs):
            user_id = message.from_user.id

            if user_id in cache:
                if cache[user_id] >= rate:
                    await message.reply(mess)
                    return
                cache[user_id] += 1
            else:
                cache[user_id] = 1

            return await func(message, state, *args, **kwargs)

        return wrapped

    return decorator