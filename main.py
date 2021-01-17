from bot.config import TOKEN
import bot.buttons as btn
import bot.sql.sql_utils as db

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
        await bot.send_message(call.from_user.id, 'Категории:', reply_markup=btn.categ_menu())
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.answer_callback_query(call.id)
    # cart
    elif call.data == 'cart':
        await bot.send_message(call.from_user.id, 'Корзина:', reply_markup=btn.cart_menu()) 
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.answer_callback_query(call.id)
    elif call.data == 'exit':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.answer_callback_query(call.id)
    # 2 level
    elif call.data == 'back_categ':
        await bot.send_message(call.from_user.id, 'Категории:', reply_markup=btn.main_menu())
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.answer_callback_query(call.id)

# 3 level
@dp.callback_query_handler(lambda call: call.data.startswitch('product_id'))
async def print_products(call: types.CallbackQuery):
    product = db.print_products(product_id)

    product_name = '<b> Название: </b>'
    product_price = '<b> Цена: </b>'
    product_text = '{product_name_f} {name}\n{product_price_f} <code>{price}</code>'.format(product_name_f = product_name,
                            name = product[2], product_price_f = product_price, price = product[3])
    await bot.send_message(call.from_user.id, product_text, reply_markup=btn.products_buttons(), parse_mode='HTML')
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.answer_callback_query(call.id)
    
###
if __name__ == '__main__':
    executor.start_polling(dp)