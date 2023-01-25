from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

#import utils.sql_utils as db
from utils.config import about_path as gh_rm


menu_cd = CallbackData('show_menu', 'level')

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