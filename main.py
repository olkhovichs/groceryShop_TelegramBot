from bot.config import TOKEN
import bot.buttons as btn

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher

bot = Bot(TOKEN)
dp = Dispatcher(bot)

# main
@dp.message_handler(commands = ['start'])
async def main_menu(message: types.Message):
    await message.reply("Выберите действие:", reply_markup = btn.init_menu())

# nested menu
@dp.callback_query_handler(lambda call: True)
async def event_buttons(call):
    if call.data == 'exit':
        await bot.answer_callback_query(call.id)
        await bot.delete_message(call.from_user.id, call.message.message_id)


##
if __name__ == '__main__':
    executor.start_polling(dp)