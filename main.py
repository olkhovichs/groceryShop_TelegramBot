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
'''
# categories
@dp.callback_query_handler(lambda call: call.data == 'categ')
async def categ_menu(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Категории:', reply_markup=btn.categ_menu())
'''
# exit
dp.callback_query_handler(lambda call: call.data == 'exit')
async def exit_bot(callback_query: types.CallbackQuery):
    await bot.delete_message(message.chat_id)




##
if __name__ == '__main__':
    executor.start_polling(dp)