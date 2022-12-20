from aiogram import Bot
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher

import utils.config as config
import utils.sql_utils as db


TOKEN = config.hide_token('token.txt')
bot = Bot(TOKEN)
dp = Dispatcher(bot)

def start(dp):
    executor.start_polling(dp)