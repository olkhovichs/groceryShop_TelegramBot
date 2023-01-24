from types import Union

from aiogram import types

from loader import dp, db, bot, start
import keyboards.inline.products_btn as products_btn
import keyboards.inline.cart_btn as cart_btn


@dp.callback_query_handler(lambda call: True)
async def event_buttons(call: 'cart_btn'):
    # cart
    await bot.send_message(call.from_user.id, 'Корзина:', reply_markup=cart_btn.cart_menu()) 
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.answer_callback_query(call.id)