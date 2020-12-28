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
    await message.reply("Выберите действие:", reply_markup = btn.main_menu())

# buttons
@dp.callback_query_handler(lambda call: True)
async def event_buttons(call: types.CallbackQuery):
    # 1 level and cart
    if call.data == 'categ' or call.data == 'back_cart':
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, 'Категории:', reply_markup=btn.categ_menu())
        await bot.delete_message(call.from_user.id, call.message.message_id)
    elif call.data == 'cart':
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, 'Корзина:', reply_markup=btn.cart_menu()) 
        await bot.delete_message(call.from_user.id, call.message.message_id)
    elif call.data == 'exit':
        await bot.answer_callback_query(call.id)
        await bot.delete_message(call.from_user.id, call.message.message_id)
    # 2 level
    elif call.data == 'back_categ':
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, 'Категории:', reply_markup=btn.main_menu())
        await bot.delete_message(call.from_user.id, call.message.message_id)
    elif call.data == 'sales': # ?
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, 'Скидки:', reply_markup=btn.product_menu()) # finish it !!!
        await bot.delete_message(call.from_user.id, call.message.message_id)


###
if __name__ == '__main__':
    executor.start_polling(dp)