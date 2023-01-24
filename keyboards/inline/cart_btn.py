from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

import utils.sql_utils as db


# cart
def cart_menu():
    btn_place = InlineKeyboardButton('Оформить заказ на', callback_data='place_order') # + srt (sum)
    '''
    btn_left = InlineKeyboardButton('<', callback_data='left') # flipping
    btn_quantity = InlineKeyboardButton('', callback_data='quantity') # to add pages
    btn_right = InlineKeyboardButton('>', callback_data='right')
    '''
    btn_empty_cart = InlineKeyboardButton('Очистить', callback_data='empty')
    btn_back_cart = InlineKeyboardButton('К товарам', callback_data='back_cart')

    markup_cart = InlineKeyboardMarkup(row_width=1)
    markup_cart.add(btn_place, btn_empty_cart, btn_back_cart)

    return markup_cart