from typing import Union

from aiogram import types

from loader import dp, db, bot, start
import keyboards.inline.products_btn as products_btn


@dp.callback_query_handler(lambda call: True)
async def event_buttons(call: types.CallbackQuery):
    # 1 level
    await bot.send_message(call.from_user.id, 'Товары:', reply_markup=products_btn.products_menu())
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.answer_callback_query(call.id)
    # cart
    '''elif call.data == 'cart':
        await bot.send_message(call.from_user.id, 'Корзина:', reply_markup=cart.cart_menu()) 
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.answer_callback_query(call.id)
    elif call.data == 'exit':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.answer_callback_query(call.id)
    # 2 level
    elif call.data == 'back_products':
        await bot.send_message(call.from_user.id, 'Товары:', reply_markup=menu.main_menu())
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.answer_callback_query(call.id)'''