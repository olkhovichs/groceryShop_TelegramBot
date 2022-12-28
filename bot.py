from aiogram import types

from loader import dp, db, bot, start
import keyboards.buttons as btn

# main
@dp.message_handler(commands=['start'])
async def main_menu(message: types.Message):
    await message.reply("Выберите действие:", reply_markup=btn.main_menu())

# buttons
@dp.callback_query_handler(lambda call: True)
async def event_buttons(call: types.CallbackQuery):
    # 1 level and cart
    if call.data == 'products' or call.data == 'back_cart':
        await bot.send_message(call.from_user.id, 'Товары:', reply_markup=btn.products_menu())
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
    elif call.data == 'back_products':
        await bot.send_message(call.from_user.id, 'Товары:', reply_markup=btn.main_menu())
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.answer_callback_query(call.id)
    

###
if __name__ == '__main__':
    start(dp)