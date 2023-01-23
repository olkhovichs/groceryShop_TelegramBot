from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
#import utils.sql_utils as db
from utils.config import about_path as gh_rm


# 1 level: menu
def main_menu():
    btn_products = InlineKeyboardButton(text='Товары', callback_data='products') 
    global btn_cart
    btn_cart = InlineKeyboardButton(text='Корзина', callback_data='cart') 
    btn_about = InlineKeyboardButton(text='Информация', url=gh_rm, callback_data='about') 
    btn_exit = InlineKeyboardButton(text='Выход', callback_data='exit')

    markup_menu = InlineKeyboardMarkup()
    markup_menu.row(btn_products).row(btn_cart) # add categories and cart
    markup_menu.row(btn_about, btn_exit) # add about and exit bot ?

    return markup_menu

# 2 level: all products
def products_menu():
    markup_categ = InlineKeyboardMarkup(row_width=1)
    btn_incr = InlineKeyboardButton('+', callback_data='incr')
    btn_decr = InlineKeyboardButton('-', callback_data='decr')
    for product in db.show_products():
        #markup_categ.add(InlineKeyboardButton(product[1], callback_data='product_id' + str(product[0])))
        markup_categ.row(btn_decr, btn_incr)
    markup_categ.add(InlineKeyboardButton('Назад', callback_data='back_product'))

    return markup_categ

'''pr_cb = CallbackData('product', 'id', 'action')
def test_out(idx = '', price = 0):
    global pr_cb
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(f'add to cart - {price}rub', callback_data=pr_cb.new(id = idx, action = 'add')))
    return markup'''


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