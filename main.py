from bot.config import TOKEN
import bot.buttons as btn

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher

bot = Bot(TOKEN)
disp = Dispatcher(bot)

@disp.message_handler(commands = ['start'])
async def init_menu(message: types.Message):
    await message.reply("Выберите действие", reply_markup = btn.markup_menu)


'''
@disp.callback_query_handler(func=lambda  call: True)
def event_buttons(call):
    if call.data = 'categ':
'''


##
if __name__ == '__main__':
    executor.start_polling(disp)